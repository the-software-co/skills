#!/usr/bin/env python3
"""Chequeos deterministas de una base de conocimiento (ver `metodo.md`). Solo stdlib.

    python3 revisar.py <carpeta> [--hoy AAAA-MM-DD] [--desde REF] [--json]

Revisa las notas de <carpeta>; los enlaces se resuelven contra toda la base (la carpeta más cercana
hacia arriba con `CONVENCIONES.md` o `.git`). `--desde` (p. ej. `origin/main`, en CI) avisa de las
notas vigentes cuyas `fuentes` cambiaron en el diff y que la nota no acompañó. Un `CONVENCIONES.md`
puede traer un bloque ```yaml revisar``` con `ignorar: [subcarpeta, …]` y `palabras_max: N`.

Sale con 1 si hay errores; los avisos no cambian la salida.
"""
import argparse
import datetime as dt
import json
import pathlib
import re
import subprocess
import sys
import urllib.parse

ESTADOS = {"borrador", "vigente", "obsoleto"}
ESTABILIDADES = {"estable", "semi", "volatil"}
REVISION_DIAS = {"estable": 365, "semi": 180, "volatil": 90}
OBLIGATORIOS = ("resumen", "estado", "estabilidad")
PALABRAS_MAX = 1500
NO_NOTAS = {"CONVENCIONES.md", "ALCANCE.md"}
# Sin frontmatter, estos archivos son puertas: no son notas, pero sus enlaces cuentan.
PUERTAS = {"README.md", "CONTEXT.md", "GLOSSARY.md", "GLOSARIO.md", "AGENTS.md", "CLAUDE.md"}
RAICES = {"conocimiento", "indice", "index"}
TIPOS_ENTRADA = {"mapa", "ruta", "recorrido"}  # bases anteriores
NOMBRE = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")
# Títulos de formulario: sirven en cualquier nota, así que no dicen nada de esta (ver "La nota").
TITULOS_PLANTILLA = {
    "por qué existe", "cómo funciona", "no confundir con", "para profundizar", "relaciones", "ejemplo",
    "qué es", "notas", "alternativas", "qué hacer", "cómo se reconoce", "por qué pasa", "si algo falla",
    "cómo saber que salió", "cuándo cada una", "debate abierto", "antes de empezar", "las piezas",
    "las notas de esta parte", "las notas", "por dónde entrar", "por dónde empezar", "sub-temas",
}
MULETILLAS = (
    "crucial", "robusto", "robusta", "cabe destacar", "cabe mencionar", "cabe señalar",
    "es importante destacar", "es importante señalar", "es importante tener en cuenta",
    "en resumen", "en conclusión", "sin lugar a dudas", "en el mundo actual", "juega un papel",
    "desempeña un papel", "aprovechar al máximo", "holístico", "sinergia", "de manera eficiente",
    "it's important to note", "in summary", "in conclusion", "crucial role", "robust", "seamless",
    "leverage", "delve",
)
WIKILINK = re.compile(r"\[\[([^\]|#^]+)(?:[#^][^\]|]*)?(?:\|[^\]]*)?\]\]")
MDLINK = re.compile(r"\]\(([^)\s#]+\.md)(?:#[^)]*)?\)")
CODIGO = re.compile(r"```.*?```|~~~.*?~~~|`[^`\n]*`", re.S)


def frontmatter(texto: str) -> tuple[dict | None, str]:
    """Un subconjunto de YAML: `clave: valor`, listas `[a, b]` o `- item`, y bloques `>-`."""
    if not texto.startswith("---\n"):
        return None, texto
    fin = texto.find("\n---", 4)
    if fin == -1:
        return None, texto
    datos: dict = {}
    clave = None
    for linea in texto[4:fin].splitlines():
        if not linea.strip() or linea.lstrip().startswith("#"):
            continue
        if linea.startswith((" ", "\t")) and clave:
            item = linea.strip()
            if item.startswith("- "):
                datos[clave] = (datos[clave] if isinstance(datos[clave], list) else []) + [item[2:].strip().strip("'\"")]
            elif isinstance(datos[clave], str):
                datos[clave] = (datos[clave] + " " + item).strip()
            continue
        clave, _, valor = linea.partition(":")
        clave, valor = clave.strip(), re.sub(r"\s+#.*$", "", valor).strip()
        if valor.startswith("[") and valor.endswith("]"):
            datos[clave] = [v.strip().strip("'\"") for v in valor[1:-1].split(",") if v.strip()]
        elif valor in (">", ">-", "|", "|-"):
            datos[clave] = ""
        else:
            datos[clave] = valor.strip("'\"")
    return datos, texto[fin + 4:]


def _lista(v) -> list[str]:
    if not v:
        return []
    return v if isinstance(v, list) else [v]


def configuracion(carpeta: pathlib.Path) -> dict:
    """El bloque ```yaml revisar``` del `CONVENCIONES.md` de la carpeta, si hay."""
    conv = carpeta / "CONVENCIONES.md"
    m = re.search(r"```yaml revisar\n(.*?)```", conv.read_text(), re.S) if conv.exists() else None
    if not m:
        return {}
    datos, _ = frontmatter("---\n" + m.group(1) + "---\n")
    return datos or {}


def _base(carpeta: pathlib.Path) -> pathlib.Path:
    for a in [carpeta, *carpeta.parents]:
        if (a / "CONVENCIONES.md").exists() or (a / ".git").exists():
            return a
    return carpeta


def _archivos(base: pathlib.Path, ignorar: list[pathlib.Path]) -> list[pathlib.Path]:
    salida = []
    for p in sorted(base.rglob("*.md")):
        rel = p.relative_to(base)
        if any(parte.startswith(".") for parte in rel.parts) or p.name in NO_NOTAS:
            continue
        if any(p.is_relative_to(i) for i in ignorar):
            continue
        salida.append(p)
    return salida


def _es_entrada(p: pathlib.Path, datos: dict, base: pathlib.Path) -> bool:
    """La entrada de una carpeta: se llama como ella (o como ella con un calificador, `fundamentos-de-x`),
    es su README o su índice, o es un Mapa de antes."""
    if datos.get("tipo") in TIPOS_ENTRADA:
        return True
    if p.name == "README.md" or p.stem in RAICES:
        return True
    carpeta = p.parent.name.lower()
    return p.stem == carpeta or p.stem.startswith(carpeta + "-")


def revisar(carpeta: pathlib.Path, hoy: dt.date, desde: str | None = None) -> list[dict]:
    carpeta = carpeta.resolve()
    base = _base(carpeta)
    conf = configuracion(carpeta) or configuracion(base)
    ignorar = [base / x for x in _lista(conf.get("ignorar"))] + [carpeta / x for x in _lista(conf.get("ignorar"))]
    palabras_max = int(conf.get("palabras_max") or PALABRAS_MAX)
    hallazgos: list[dict] = []

    def hallar(nivel: str, regla: str, p: pathlib.Path, mensaje: str) -> None:
        if p.is_relative_to(carpeta):
            nota = str(p.relative_to(carpeta)) if p != carpeta else "."
            hallazgos.append({"nivel": nivel, "regla": regla, "nota": nota, "mensaje": mensaje})

    notas: dict[pathlib.Path, dict] = {}
    por_nombre: dict[str, list[pathlib.Path]] = {}
    for p in _archivos(base, ignorar):
        texto = p.read_text()
        datos, cuerpo = frontmatter(texto)
        if datos is None and p.name in PUERTAS:
            datos = {}  # una puerta: no es nota, pero sus enlaces cuentan
            puerta = True
        else:
            puerta = False
        notas[p] = {"datos": datos, "cuerpo": cuerpo, "puerta": puerta, "enlaces": set()}
        por_nombre.setdefault(p.stem, []).append(p)

    for p, n in notas.items():
        sin_codigo = CODIGO.sub("", n["cuerpo"])
        for destino in MDLINK.findall(sin_codigo):
            if "://" in destino or destino.startswith("/"):
                continue
            objetivo = (p.parent / urllib.parse.unquote(destino)).resolve()
            if objetivo.exists():
                n["enlaces"].add(objetivo)
            elif not any(objetivo.is_relative_to(i) for i in ignorar):
                hallar("error", "enlace-roto", p, f"`{destino}` no existe")
        for destino in WIKILINK.findall(sin_codigo):
            candidatos = por_nombre.get(destino.strip(), [])
            if candidatos:
                n["enlaces"].update(candidatos)
            else:
                hallar("error", "enlace-roto", p, f"`[[{destino}]]` no existe")

    entradas = {p for p, n in notas.items() if not n["puerta"] and _es_entrada(p, n["datos"] or {}, base)}
    con_entrada = {p.parent for p in entradas} | {p.parent for p, n in notas.items() if n["puerta"] and p.name == "README.md"}
    enlazadas_desde_entrada = {e for p in entradas | {p for p, n in notas.items() if n["puerta"]}
                               for e in notas[p]["enlaces"] if e != p}
    pendientes = 0

    for p, n in notas.items():
        if n["puerta"]:
            continue
        d = n["datos"]
        if d is None:
            hallar("error", "sin-frontmatter", p, "falta el frontmatter")
            continue
        for campo in OBLIGATORIOS:
            if not d.get(campo):
                hallar("error", "campo-faltante", p, f"falta `{campo}`")
        if d.get("estado") and d["estado"] not in ESTADOS:
            hallar("error", "valor-invalido", p, f"`estado: {d['estado']}`")
        if d.get("estabilidad") and d["estabilidad"] not in ESTABILIDADES:
            hallar("error", "valor-invalido", p, f"`estabilidad: {d['estabilidad']}`")
        if p.name != "README.md" and not NOMBRE.fullmatch(p.stem):
            hallar("error", "nombre-de-archivo", p, "el nombre va en kebab-case ASCII")

        revisado = None
        if d.get("revisado"):
            try:
                revisado = dt.date.fromisoformat(str(d["revisado"]))
            except ValueError:
                hallar("error", "valor-invalido", p, f"`revisado: {d['revisado']}`")
        if d.get("estado") == "borrador":
            pendientes += p.is_relative_to(carpeta)
        if d.get("estado") == "vigente":
            if not d.get("revisado"):
                hallar("aviso", "vigente-sin-revisado", p, "vigente sin `revisado`: ¿quién la confirmó y cuándo?")
            elif revisado:
                dias = REVISION_DIAS.get(d.get("estabilidad"), 365)
                if (hoy - revisado).days > dias:
                    hallar("aviso", "revision-vencida", p, f"revisada el {revisado}; vence a los {dias} días")
        if d.get("reemplazado_por"):
            destino = (p.parent / str(d["reemplazado_por"])).resolve()
            if not destino.exists() and not por_nombre.get(pathlib.Path(str(d["reemplazado_por"])).stem):
                hallar("error", "enlace-roto", p, f"`reemplazado_por: {d['reemplazado_por']}` no existe")
        es_ruta = p.stem.startswith(("recorrido-", "ruta-")) or d.get("tipo") in TIPOS_ENTRADA
        if p not in entradas and not es_ruta and not _lista(d.get("fuentes")):
            hallar("aviso", "sin-fuentes", p, "sin `fuentes`: ¿de dónde sale lo que afirma?")
        if d.get("resumen") and "adr" not in {x.lower() for x in p.parts}:
            primera = _primera_linea(n["cuerpo"])
            if primera and _normal(primera) != _normal(str(d["resumen"])):
                hallar("aviso", "resumen-distinto", p, "la primera línea no es igual al `resumen`")

        es_raiz = p.parent == base and p in entradas
        if d.get("estado") != "obsoleto" and not es_raiz and p not in enlazadas_desde_entrada:
            hallar("aviso", "huerfana", p, "ninguna entrada la enlaza")

        cuerpo = CODIGO.sub("", n["cuerpo"])
        titulos = {t.strip().lower() for t in re.findall(r"^#{2,3} (.+)$", cuerpo, re.M)}
        genericos = sorted(titulos & TITULOS_PLANTILLA)
        if len(genericos) >= 2:
            hallar("aviso", "titulos-de-plantilla", p,
                   f"títulos que servirían en cualquier nota: {', '.join(genericos)}")
        palabras = len(re.findall(r"\w+", cuerpo))
        if d.get("estabilidad") != "volatil" and palabras > palabras_max:
            hallar("aviso", "larga", p, f"{palabras} palabras: ¿adentro hay otro sujeto que se enlaza solo?")
        bajo = cuerpo.lower()
        usadas = [m for m in MULETILLAS if re.search(rf"\b{re.escape(m)}\b", bajo)]
        if usadas:
            hallar("aviso", "muletilla", p, ", ".join(usadas))

    carpetas = {p.parent for p, n in notas.items() if not n["puerta"] and n["datos"] is not None}
    for c in sorted(carpetas):
        if c != base and c not in con_entrada:
            hallar("aviso", "carpeta-sin-entrada", c, f"falta `{c.name.lower()}.md` con lo que hay adentro")

    if pendientes:
        hallar("aviso", "pendiente-de-revision", carpeta, f"{pendientes} notas en borrador esperan que una persona las lea")

    for p, n in notas.items():
        d = n["datos"] or {}
        if d.get("estado") != "vigente" or not d.get("revisado"):
            continue
        for fuente in _lista(d.get("fuentes")):
            cambio = _ultimo_commit(base, fuente)
            if cambio and cambio > str(d["revisado"]):
                hallar("aviso", "fuente-cambiada", p, f"`{fuente}` cambió el {cambio}, después de `revisado`")

    if desde:
        cambiados = _cambiados(base, desde)
        top = _top(base)
        for p, n in notas.items():
            d = n["datos"] or {}
            propia = str(p.relative_to(top)) if top else None
            if d.get("estado") != "vigente" or propia in cambiados:
                continue
            tocadas = [f for f in _lista(d.get("fuentes")) if re.split(r"[:#]", f, maxsplit=1)[0] in cambiados]
            if tocadas:
                hallar("aviso", "doc-sin-actualizar", p, f"cambió {', '.join(tocadas)} y la nota no: ¿sigue bien?")
    return hallazgos


def _top(carpeta: pathlib.Path) -> pathlib.Path | None:
    try:
        return pathlib.Path(subprocess.run(["git", "-C", str(carpeta), "rev-parse", "--show-toplevel"],
                                           capture_output=True, text=True, check=True).stdout.strip())
    except (OSError, subprocess.CalledProcessError):
        return None


def _cambiados(carpeta: pathlib.Path, desde: str) -> set[str]:
    """Los archivos que cambiaron desde la base común con `desde`, relativos a la raíz del repo."""
    r = subprocess.run(["git", "-C", str(carpeta), "diff", "--name-only", f"{desde}...HEAD"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(f"revisar.py: --desde {desde}: {r.stderr.strip() or 'git diff falló'}")
    return set(r.stdout.split())


def _ultimo_commit(carpeta: pathlib.Path, fuente: str) -> str | None:
    """La fecha (AAAA-MM-DD) del último commit que tocó una fuente que es un archivo del repo."""
    if "://" in fuente:
        return None
    ruta = re.split(r"[:#]", fuente.strip(), maxsplit=1)[0]
    top = _top(carpeta)
    if not top or not ruta:
        return None
    try:
        existe = (top / ruta).exists()
    except OSError:  # una cita larga en texto no es una ruta (ENAMETOOLONG)
        return None
    if not existe:
        return None
    fecha = subprocess.run(["git", "-C", str(top), "log", "-1", "--format=%as", "--", ruta],
                           capture_output=True, text=True).stdout.strip()
    return fecha or None


def _primera_linea(cuerpo: str) -> str:
    """El primer párrafo después del H1."""
    tras_h1 = re.split(r"^# .*$", cuerpo, maxsplit=1, flags=re.M)[-1]
    return next((x for x in re.split(r"\n\s*\n", tras_h1.strip()) if x.strip()), "")


def _normal(texto: str) -> str:
    """Sin espacios repetidos ni marcas de énfasis, para comparar `resumen` con la primera línea."""
    return re.sub(r"\s+", " ", re.sub(r"[*_`]", "", texto)).strip()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("carpeta", type=pathlib.Path)
    ap.add_argument("--hoy", type=dt.date.fromisoformat, default=dt.date.today())
    ap.add_argument("--desde", help="ref de git contra la que se mira el diff (p. ej. origin/main)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if not a.carpeta.is_dir():
        print(f"no es una carpeta: {a.carpeta}", file=sys.stderr)
        return 2
    hallazgos = revisar(a.carpeta, a.hoy, a.desde)
    if a.json:
        print(json.dumps(hallazgos, ensure_ascii=False, indent=2))
    else:
        for h in sorted(hallazgos, key=lambda h: (h["nivel"], h["regla"], h["nota"])):
            print(f"{h['nivel']:5} {h['regla']:22} {h['nota']}: {h['mensaje']}")
        errores = sum(h["nivel"] == "error" for h in hallazgos)
        print(f"\n{errores} errores, {len(hallazgos) - errores} avisos", file=sys.stderr)
    return 1 if any(h["nivel"] == "error" for h in hallazgos) else 0


if __name__ == "__main__":
    sys.exit(main())
