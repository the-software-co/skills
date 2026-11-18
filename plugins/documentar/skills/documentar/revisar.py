#!/usr/bin/env python3
"""Chequeos deterministas de una base de conocimiento (ver `metodo.md`). Solo stdlib.

    python3 revisar.py <carpeta> [--hoy AAAA-MM-DD] [--desde REF] [--json]

Sirve para un vault de Obsidian, para los docs de un repo y para un tema hecho con el modo `nuevo`.
Las reglas de preguntas, conceptos umbral y área corren solo en las carpetas que tienen `ALCANCE.md`.
`--desde` (p. ej. `origin/main`, en CI) avisa de las notas cuyas `fuentes` cambiaron en el diff y que
la nota misma no acompañó. Un `CONVENCIONES.md` en la carpeta puede traer un bloque ```yaml revisar```
con `ignorar: [subcarpeta, …]` y `palabras_max: N`.

Sale con 1 si hay errores; los avisos no cambian la salida.
"""
import argparse
import datetime as dt
import json
import pathlib
import re
import subprocess
import sys

TIPOS = {"concepto", "metrica", "como-hacer", "falla", "ficha", "decision", "mapa", "ruta", "recorrido"}
MAPAS = {"mapa", "ruta", "recorrido"}  # `recorrido` es el nombre anterior de `ruta`
AREAS = {"que-es", "como-funciona", "anatomia", "procesos", "como-se-hace", "como-se-decide",
         "como-falla", "historia", "ecosistema", "referencia", "ruta"}
NUCLEO = {"que-es", "como-funciona", "anatomia", "procesos", "historia", "como-falla"}
ESTADOS = {"borrador", "vigente", "obsoleto"}
IDIOMAS = {"es", "en"}
AUTORIAS = {"ia", "mixta", "humano"}
REVISION_DIAS = {"estable": 365, "semi": 180, "volatil": 90}
OBLIGATORIOS = ("tipo", "resumen", "estado", "estabilidad", "dueno")
JERARQUIA = ("parte_de", "es_un", "instancia_de")
RELACIONES = JERARQUIA + ("requiere", "relacionado")
PALABRAS_MAX = 450
UMBRAL = (3, 7)
MAPAS_RAIZ = {"conocimiento", "indice"}
NO_NOTAS = {"CONVENCIONES.md", "ALCANCE.md"}
NOMBRE = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")
# Muletillas de texto generado: cada una se reemplaza por el dato o se borra (Prosa).
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
PREGUNTA = re.compile(r"\*\*([PE]\d+)\*\*")
VERSION = re.compile(r"\bv?\d+\.\d+(?:\.\d+)?\b")
PRECIO = re.compile(r"(?:US\$|U\$S|USD|ARS|EUR|\$|€)\s?\d|\d\s?(?:USD|ARS|EUR|dólares|pesos|euros)\b")
# Un número que la nota afirma: con decimales, o con una unidad. Se busca en `.investigacion/`.
CIFRA = re.compile(r"(?<![\w.,])(\d+(?:[.,]\d+)?)\s?(%|°C|°F|nmol/L|µW/cm²|UI/kg|mm|cm|kg|g|W)(?!\w)"
                   r"|(?<![\w.,])(\d+[.,]\d+)(?![\w.,])")


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
                datos[clave] = (datos[clave] if isinstance(datos[clave], list) else []) + [_escalar(item[2:])]
            elif isinstance(datos[clave], str):
                datos[clave] = (datos[clave] + " " + item).strip()
            continue
        clave, _, valor = linea.partition(":")
        clave, valor = clave.strip(), re.sub(r"\s+#.*$", "", valor).strip()
        if valor.startswith("[") and valor.endswith("]"):
            datos[clave] = [_escalar(v) for v in valor[1:-1].split(",") if v.strip()]
        elif valor in (">", ">-", "|", "|-"):
            datos[clave] = ""
        else:
            datos[clave] = _escalar(valor)
    return datos, texto[fin + 4:]


def _escalar(v: str) -> str:
    v = v.strip().strip("'\"")
    m = re.fullmatch(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]", v)
    return m.group(1) if m else v


def _lista(v) -> list[str]:
    if not v:
        return []
    return v if isinstance(v, list) else [v]


def configuracion(raiz: pathlib.Path) -> dict:
    """El bloque ```yaml revisar``` del `CONVENCIONES.md` de la base, si hay."""
    conv = raiz / "CONVENCIONES.md"
    m = re.search(r"```yaml revisar\n(.*?)```", conv.read_text(), re.S) if conv.exists() else None
    if not m:
        return {}
    datos, _ = frontmatter("---\n" + m.group(1) + "---\n")
    return datos or {}


def _ciclo(grafo: dict[str, list[str]]) -> list[str] | None:
    estado: dict[str, int] = {}
    pila: list[str] = []

    def visitar(n: str) -> list[str] | None:
        estado[n] = 1
        pila.append(n)
        for m in grafo.get(n, []):
            if estado.get(m) == 1:
                return pila[pila.index(m):] + [m]
            if m not in estado and m in grafo:
                c = visitar(m)
                if c:
                    return c
        pila.pop()
        estado[n] = 2
        return None

    for n in sorted(grafo):
        if n not in estado:
            c = visitar(n)
            if c:
                return c
    return None


def _alcanzables(grafo: dict[str, list[str]], desde: str, saltando: str | None = None) -> set[str]:
    vistos: set[str] = set()
    pendientes = [m for m in grafo.get(desde, []) if m != saltando]
    while pendientes:
        n = pendientes.pop()
        if n not in vistos:
            vistos.add(n)
            pendientes.extend(grafo.get(n, []))
    return vistos


def _alcance_de(path: pathlib.Path, raiz: pathlib.Path) -> pathlib.Path | None:
    """El `ALCANCE.md` del tema de una nota: en su carpeta o en una de arriba, sin salir de la raíz."""
    for carpeta in [path.parent, *path.parent.parents]:
        if (carpeta / "ALCANCE.md").exists():
            return carpeta / "ALCANCE.md"
        if carpeta == raiz:
            break
    return None


def revisar(raiz: pathlib.Path, hoy: dt.date, desde: str | None = None) -> list[dict]:
    raiz = raiz.resolve()
    hallazgos: list[dict] = []
    conf = configuracion(raiz)
    ignorar = [raiz / x for x in _lista(conf.get("ignorar"))]
    palabras_max = int(conf.get("palabras_max") or PALABRAS_MAX)

    def hallar(nivel: str, regla: str, ruta, mensaje: str) -> None:
        hallazgos.append({"nivel": nivel, "regla": regla, "nota": str(ruta), "mensaje": mensaje})

    archivos = sorted(p for p in raiz.rglob("*.md")
                      if not any(x.startswith(".") for x in p.relative_to(raiz).parts) and p.name not in NO_NOTAS
                      and not any(i == p or i in p.parents for i in ignorar))
    notas: dict[str, dict] = {}
    for p in archivos:
        rel = p.relative_to(raiz)
        datos, cuerpo = frontmatter(p.read_text(errors="replace"))
        if p.name == "README.md":
            # Un README es puerta de entrada salvo que sea el Mapa de su carpeta.
            if not datos or datos.get("tipo") != "mapa":
                continue
            id_ = f"mapa:{rel.parent}"
        else:
            id_ = p.stem
        if id_ in notas:
            hallar("error", "id-duplicado", rel, f"otra nota se llama igual: {notas[id_]['ruta']}")
            continue
        notas[id_] = {"ruta": rel, "datos": datos, "cuerpo": cuerpo, "path": p}

    # Un [[enlace]] de Obsidian resuelve contra todo el vault, no solo contra esta carpeta.
    vault = next((a for a in [raiz, *raiz.parents] if (a / ".obsidian").is_dir()), raiz)
    todos = [x for x in vault.rglob("*") if x.is_file() and not any(y.startswith(".") for y in x.relative_to(vault).parts)]
    existentes = {x.stem if x.suffix == ".md" else x.name for x in todos}
    fuera = {x.stem: x for x in todos if x.suffix == ".md" and x.name not in NO_NOTAS | {"README.md"}
             and raiz not in x.resolve().parents}
    for i, n in notas.items():
        if i in fuera:
            hallar("error", "id-duplicado", n["ruta"], f"otra nota del vault se llama igual: {fuera[i].relative_to(vault)}")

    por_ruta = {n["path"].resolve(): i for i, n in notas.items()}
    enlazadas_desde_mapa: set[str] = set()
    for id_, n in notas.items():
        d, rel = n["datos"], n["ruta"]
        wikis = {x.strip().rstrip("\\") for x in WIKILINK.findall(n["cuerpo"])}
        for w in wikis:
            if pathlib.Path(w).name not in existentes and pathlib.Path(w).stem not in existentes:
                hallar("error", "enlace-roto", rel, f"no existe [[{w}]]")
        enlaces = {pathlib.Path(w).stem for w in wikis if pathlib.Path(w).suffix in ("", ".md")}
        for destino in MDLINK.findall(n["cuerpo"]):
            if "://" in destino:
                continue
            objetivo = (n["path"].parent / destino).resolve()
            if not objetivo.exists():
                hallar("error", "enlace-roto", rel, f"no existe {destino}")
            enlaces.add(por_ruta.get(objetivo, pathlib.Path(destino).stem))
        n["enlaces"] = enlaces
        for ruta in sorted(set(re.findall(r"`([\w./-]+\.md)`", n["cuerpo"]))):
            if any(c.exists() for c in (n["path"].parent / ruta, raiz / ruta)):
                hallar("aviso", "ruta-sin-enlace", rel, f"`{ruta}` es una nota: va como enlace para que se chequee")

        sin_codigo = re.sub(r"```.*?```", "", n["cuerpo"], flags=re.S)
        palabras = len([w for w in sin_codigo.split() if re.search(r"\w", w)])
        tabla = (d or {}).get("tipo") == "ficha"
        if (d or {}).get("tipo") not in MAPAS and not tabla and palabras > palabras_max:
            hallar("aviso", "candidata-a-partir", rel, f"{palabras} palabras: ¿responde una sola pregunta?")
        if d is None or d.get("tipo") not in TIPOS and not d.get("resumen"):
            hallar("aviso", "formato-anterior", rel, "no sigue el método todavía (modo `existente`)")
            n["datos"] = None
            continue
        if not id_.startswith("mapa:") and not NOMBRE.fullmatch(id_):
            hallar("aviso", "nombre-de-archivo", rel, "el nombre va en kebab-case con letras ASCII")
        if d.get("estado") == "vigente" and d.get("tipo") != "decision" and not d.get("revisado"):
            hallar("error", "campo-faltante", rel, "falta `revisado` (obligatorio si está vigente)")
        if d.get("estado") == "borrador":
            hallar("aviso", "pendiente-de-revision", rel, "borrador: espera que una persona lo lea y lo confirme")
        if d.get("estado") == "borrador" and d.get("revisado"):
            hallar("aviso", "borrador-revisado", rel, "un borrador no tiene `revisado`: se pone al pasar a vigente")
        primera = _primera_linea(n["cuerpo"])
        if d.get("resumen") and d.get("tipo") != "decision" and _normal(primera) != _normal(d["resumen"]):
            hallar("aviso", "resumen-distinto", rel, "la primera línea no es igual a `resumen`")
        texto = n["cuerpo"].lower()
        halladas = sorted({m for m in MULETILLAS if re.search(rf"\b{re.escape(m)}\b", texto)})
        if halladas:
            hallar("aviso", "muletilla", rel, ", ".join(halladas))
        for campo in OBLIGATORIOS:
            if not d.get(campo):
                hallar("error", "campo-faltante", rel, f"falta `{campo}`")
        for campo, validos in (("tipo", TIPOS), ("estado", ESTADOS), ("idioma", IDIOMAS),
                               ("estabilidad", set(REVISION_DIAS)), ("autoria", AUTORIAS), ("area", AREAS)):
            if d.get(campo) and d[campo] not in validos:
                hallar("error", "valor-invalido", rel, f"`{campo}: {d[campo]}` no es uno de {sorted(validos)}")
        for rel_ in RELACIONES:
            for otro in _lista(d.get(rel_)):
                if otro not in notas and otro not in existentes:
                    hallar("error", "relacion-rota", rel, f"`{rel_}` apunta a `{otro}`, que no existe")
        if d.get("estado") == "obsoleto" and not d.get("reemplazado_por"):
            hallar("aviso", "obsoleto-sin-reemplazo", rel, "obsoleto sin `reemplazado_por`: ¿se puede borrar?")
        if d.get("tipo") in MAPAS:
            enlazadas_desde_mapa |= enlaces
        if d.get("tipo") in {"concepto", "falla", "ficha", "decision", "metrica"} and not _lista(d.get("fuentes")):
            hallar("aviso", "sin-fuentes", rel, "no cita fuentes")
        if d.get("tipo") != "decision" and d.get("estado") != "obsoleto" and d.get("revisado"):
            try:
                revisado = dt.date.fromisoformat(str(d["revisado"]))
            except ValueError:
                hallar("error", "valor-invalido", rel, f"`revisado: {d['revisado']}` no es AAAA-MM-DD")
            else:
                dias = REVISION_DIAS.get(d.get("estabilidad"), 180)
                if (hoy - revisado).days > dias:
                    hallar("aviso", "revision-vencida", rel, f"revisada hace {(hoy - revisado).days} días (cada {dias})")

    for i, n in notas.items():
        d = n["datos"] or {}
        if d.get("tipo") == "mapa" and not _lista(d.get("parte_de")) and i not in MAPAS_RAIZ \
                and not any(i in (o.get("enlaces") or set()) for j, o in notas.items()
                            if j != i and (o["datos"] or {}).get("tipo") in MAPAS):
            hallar("aviso", "mapa-sin-padre", n["ruta"], "ningún Mapa padre: no se llega desde el Mapa raíz")

    for i, n in notas.items():
        d = n["datos"] or {}
        if d.get("estado") != "vigente" or not d.get("revisado"):
            continue
        for fuente in _lista(d.get("fuentes")):
            cambio = _ultimo_commit(raiz, fuente)
            if cambio and cambio > str(d["revisado"]):
                hallar("aviso", "fuente-cambiada", n["ruta"], f"`{fuente}` cambió el {cambio}, después de `revisado`")

    if desde:
        cambiados = _cambiados(raiz, desde)
        top = _top(raiz)
        for i, n in notas.items():
            d = n["datos"] or {}
            propia = str(n["path"].resolve().relative_to(top)) if top else None
            if d.get("estado") != "vigente" or propia in cambiados:
                continue
            tocadas = [f for f in _lista(d.get("fuentes")) if re.split(r"[:#]", f, maxsplit=1)[0] in cambiados]
            if tocadas:
                hallar("aviso", "doc-sin-actualizar", n["ruta"], f"cambió {', '.join(tocadas)} y la nota no: ¿sigue bien?")

    # Relaciones: jerarquía sin ciclos, `requiere` sin ciclos ni redundancias, `relacionado` fuera de la jerarquía.
    jerarquia = {i: [p for r in JERARQUIA for p in _lista((n["datos"] or {}).get(r)) if p in notas]
                 for i, n in notas.items()}
    requiere = {i: [p for p in _lista((n["datos"] or {}).get("requiere")) if p in notas] for i, n in notas.items()}
    for regla, grafo, nombre in (("ciclo", jerarquia, "la jerarquía"), ("ciclo-requiere", requiere, "`requiere`")):
        c = _ciclo(grafo)
        if c:
            hallar("error", regla, notas[c[0]]["ruta"], f"{nombre} vuelve sobre sí misma: {' → '.join(c)}")
    ancestros = {i: _alcanzables(jerarquia, i) for i in notas}
    for i, n in notas.items():
        d = n["datos"] or {}
        for otro in _lista(d.get("relacionado")):
            if otro not in notas:
                continue
            if otro in ancestros[i] or i in ancestros[otro]:
                hallar("error", "relacionado-en-jerarquia", n["ruta"], f"`{otro}` ya está en su jerarquía")
            elif i not in _lista((notas[otro]["datos"] or {}).get("relacionado")):
                hallar("aviso", "relacionado-asimetrico", n["ruta"], f"`{otro}` no la tiene en su `relacionado`")
        for otro in requiere[i]:
            if otro in _alcanzables(requiere, i, saltando=otro):
                hallar("aviso", "requiere-redundante", n["ruta"], f"`{otro}` ya se requiere por otro camino")
        if d and d.get("estado") != "obsoleto" and d.get("tipo") not in MAPAS and i not in enlazadas_desde_mapa:
            hallar("aviso", "huerfana", n["ruta"], "ningún Mapa ni Ruta la enlaza")
    con_mapa = {n["path"].parent for n in notas.values() if (n["datos"] or {}).get("tipo") == "mapa"}
    for carpeta in sorted({n["path"].parent for n in notas.values() if n["datos"]} - con_mapa):
        hallar("aviso", "tema-sin-mapa", carpeta.relative_to(raiz) if carpeta != raiz else ".", "la carpeta no tiene Mapa")

    _revisar_temas(raiz, notas, hallar)
    return hallazgos


def _revisar_temas(raiz: pathlib.Path, notas: dict, hallar) -> None:
    """Lo propio de los temas hechos con el modo `nuevo`: los que tienen `ALCANCE.md`."""
    alcances = sorted(p for p in raiz.rglob("ALCANCE.md") if not any(x.startswith(".") for x in p.relative_to(raiz).parts))
    if not alcances:
        return
    preguntas: dict[str, pathlib.Path] = {}
    volatiles: dict[pathlib.Path, list[str]] = {}
    for a in alcances:
        fm, cuerpo = frontmatter(a.read_text(errors="replace"))
        if fm is None:
            hallar("error", "campo-faltante", a.relative_to(raiz), "el ALCANCE.md no tiene frontmatter")
            fm = {}
        if not fm.get("aprobado"):
            hallar("aviso", "alcance-sin-aprobar", a.relative_to(raiz), "falta `aprobado`: la persona no aprobó el alcance")
        volatiles[a] = [v for v in _lista(fm.get("volatiles")) if v]
        for p in PREGUNTA.findall(cuerpo):
            preguntas[p] = a
    respondidas: set[str] = set()
    umbral: dict[pathlib.Path, int] = {a: 0 for a in alcances}
    for n in notas.values():
        d = n["datos"]
        a = _alcance_de(n["path"], raiz)
        if not d or not a:
            continue
        for p in _lista(d.get("responde")):
            if p not in preguntas:
                hallar("error", "responde-inexistente", n["ruta"], f"{p} no está en ningún ALCANCE.md")
            respondidas.add(p)
        if d.get("tipo") not in (None, "mapa") and not d.get("area"):
            hallar("error", "campo-faltante", n["ruta"], "falta `area` (el tema tiene ALCANCE.md)")
        if str(d.get("umbral", "")).lower() == "true":
            umbral[a] = umbral.get(a, 0) + 1
        if d.get("area") in NUCLEO and d.get("estabilidad") == "estable":
            texto = f"{_h1(n['cuerpo'])} {d.get('resumen', '')}"
            for v in volatiles.get(a, []):
                if re.search(rf"(?<!\w){re.escape(v)}(?!\w)", texto, re.I):
                    hallar("error", "volatil-en-nucleo", n["ruta"], f"el título o el resumen nombran «{v}»")
            for patron, que in ((VERSION, "una versión"), (PRECIO, "un precio")):
                m = patron.search(texto)
                if m:
                    hallar("error", "volatil-en-nucleo", n["ruta"], f"el título o el resumen nombran {que}: «{m.group(0)}»")
        investigacion = a.parent / ".investigacion"
        if investigacion.is_dir():
            crudo = _normal_cifras(" ".join(f.read_text(errors="replace") for f in investigacion.rglob("*.md")))
            faltan = sorted({c for c in _cifras(n["cuerpo"]) if c not in crudo})
            if faltan:
                hallar("aviso", "cifra-sin-evidencia", n["ruta"],
                       f"no aparecen en .investigacion/: {', '.join(faltan[:8])}{' …' if len(faltan) > 8 else ''}")
    for p, a in sorted(preguntas.items(), key=lambda x: (x[0][0], int(x[0][1:]))):
        if p not in respondidas:
            hallar("error", "pregunta-sin-nota", a.relative_to(raiz), f"ninguna nota responde {p}")
    for a, cuantos in umbral.items():
        if not (UMBRAL[0] <= cuantos <= UMBRAL[1]):
            hallar("aviso", "umbral", a.relative_to(raiz), f"hay {cuantos} conceptos umbral; van de {UMBRAL[0]} a {UMBRAL[1]}")


def _cifras(cuerpo: str) -> set[str]:
    """Las cifras que afirma el cuerpo, sin bloques de código ni URLs, normalizadas."""
    texto = re.sub(r"```.*?```|https?://\S+|\]\([^)]*\)", " ", cuerpo, flags=re.S)
    salida = set()
    for m in CIFRA.finditer(texto):
        salida.add(_normal_cifras(m.group(1) or m.group(3)))
    return salida


def _normal_cifras(texto: str) -> str:
    return re.sub(r"(\d),(\d)", r"\1.\2", texto)


def _h1(cuerpo: str) -> str:
    m = re.search(r"^# (.+)$", cuerpo, re.M)
    return m.group(1).strip() if m else ""


def _top(raiz: pathlib.Path) -> pathlib.Path | None:
    try:
        return pathlib.Path(subprocess.run(["git", "-C", str(raiz), "rev-parse", "--show-toplevel"],
                                           capture_output=True, text=True, check=True).stdout.strip())
    except (OSError, subprocess.CalledProcessError):
        return None


def _cambiados(raiz: pathlib.Path, desde: str) -> set[str]:
    """Los archivos que cambiaron desde la base común con `desde`, relativos a la raíz del repo."""
    r = subprocess.run(["git", "-C", str(raiz), "diff", "--name-only", f"{desde}...HEAD"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(f"revisar.py: --desde {desde}: {r.stderr.strip() or 'git diff falló'}")
    return set(r.stdout.split())


def _ultimo_commit(raiz: pathlib.Path, fuente: str) -> str | None:
    """La fecha (AAAA-MM-DD) del último commit que tocó una fuente que es un archivo del repo."""
    if "://" in fuente:
        return None
    ruta = re.split(r"[:#]", fuente.strip(), maxsplit=1)[0]
    top = _top(raiz)
    if not top or not ruta or not (top / ruta).exists():
        return None
    fecha = subprocess.run(["git", "-C", str(top), "log", "-1", "--format=%cs", "--", ruta],
                           capture_output=True, text=True).stdout.strip()
    return fecha or None


def _primera_linea(cuerpo: str) -> str:
    """El primer párrafo después del H1."""
    tras_h1 = re.split(r"^# .*$", cuerpo, maxsplit=1, flags=re.M)[-1]
    return next((p for p in re.split(r"\n\s*\n", tras_h1.strip()) if p.strip()), "")


def _normal(texto: str) -> str:
    return re.sub(r"\s+", " ", texto).strip()


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
            print(f"{h['nivel']:5} {h['regla']:24} {h['nota']}: {h['mensaje']}")
        errores = sum(h["nivel"] == "error" for h in hallazgos)
        print(f"\n{errores} errores, {len(hallazgos) - errores} avisos", file=sys.stderr)
    return 1 if any(h["nivel"] == "error" for h in hallazgos) else 0


if __name__ == "__main__":
    sys.exit(main())
