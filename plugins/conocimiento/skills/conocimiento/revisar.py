#!/usr/bin/env python3
"""Chequeos deterministas del Conocimiento de una carpeta (ver `metodo.md`). Solo stdlib.

    python3 revisar.py <carpeta> [--hoy AAAA-MM-DD] [--json]

Sale con 1 si hay errores; los avisos no cambian la salida.
"""
import argparse
import datetime as dt
import json
import pathlib
import re
import sys

TIPOS = {"concepto", "metrica", "como-hacer", "ficha", "decision", "mapa", "recorrido"}
ESTADOS = {"borrador", "vigente", "obsoleto"}
IDIOMAS = {"es", "en"}
REVISION_DIAS = {"estable": 365, "semi": 180, "volatil": 90}
OBLIGATORIOS = ("tipo", "resumen", "estado", "estabilidad", "dueno")
RELACIONES = ("parte_de", "requiere", "relacionado")
MAPAS = {"mapa", "recorrido"}
PALABRAS_MAX = 450
MAPAS_RAIZ = {"conocimiento", "indice"}
# Archivos de la base que no son notas: las convenciones locales y los README de un repo.
NO_NOTAS = {"CONVENCIONES.md", "README.md"}
NOMBRE = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")
# Muletillas de texto generado: cada una se reemplaza por el dato o se borra (Prosa, regla 6 y 8).
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
    return datos, texto[fin + 4 :]


def _escalar(v: str) -> str:
    v = v.strip().strip("'\"")
    m = re.fullmatch(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]", v)
    return m.group(1) if m else v


def _lista(v) -> list[str]:
    if not v:
        return []
    return v if isinstance(v, list) else [v]


def revisar(raiz: pathlib.Path, hoy: dt.date) -> list[dict]:
    hallazgos: list[dict] = []

    def hallar(nivel: str, regla: str, ruta, mensaje: str) -> None:
        hallazgos.append({"nivel": nivel, "regla": regla, "nota": str(ruta), "mensaje": mensaje})

    archivos = sorted(p for p in raiz.rglob("*.md")
                      if not any(x.startswith(".") for x in p.relative_to(raiz).parts) and p.name not in NO_NOTAS)
    notas: dict[str, dict] = {}
    for p in archivos:
        rel = p.relative_to(raiz)
        if p.stem in notas:
            hallar("error", "id-duplicado", rel, f"otra nota se llama igual: {notas[p.stem]['ruta']}")
            continue
        datos, cuerpo = frontmatter(p.read_text(errors="replace"))
        notas[p.stem] = {"ruta": rel, "datos": datos, "cuerpo": cuerpo, "path": p}

    # Un [[enlace]] de Obsidian resuelve contra todo el vault, no solo contra esta carpeta.
    vault = next((a for a in [raiz.resolve(), *raiz.resolve().parents] if (a / ".obsidian").is_dir()), raiz)
    todos = [x for x in vault.rglob("*") if x.is_file() and not any(y.startswith(".") for y in x.relative_to(vault).parts)]
    existentes = {x.stem if x.suffix == ".md" else x.name for x in todos}
    fuera = {x.stem: x for x in todos if x.suffix == ".md" and raiz.resolve() not in x.resolve().parents}
    for i, n in notas.items():
        if i in fuera:
            hallar("error", "id-duplicado", n["ruta"], f"otra nota del vault se llama igual: {fuera[i].relative_to(vault)}")

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
            if not (n["path"].parent / destino).resolve().exists():
                hallar("error", "enlace-roto", rel, f"no existe {destino}")
            enlaces.add(pathlib.Path(destino).stem)
        n["enlaces"] = enlaces

        sin_codigo = re.sub(r"```.*?```", "", n["cuerpo"], flags=re.S)
        palabras = len([w for w in sin_codigo.split() if re.search(r"\w", w)])
        instrumento = (d or {}).get("tipo") == "ficha" and (d or {}).get("estabilidad") == "estable"
        if (d or {}).get("tipo") not in MAPAS and not instrumento and palabras > PALABRAS_MAX:
            hallar("aviso", "candidata-a-partir", rel, f"{palabras} palabras: ¿responde una sola pregunta?")
        if d is None or d.get("tipo") not in TIPOS and not d.get("resumen"):
            hallar("aviso", "formato-anterior", rel, "no sigue el método todavía (modo `existente`)")
            n["datos"] = None
            continue
        if not NOMBRE.fullmatch(id_):
            hallar("aviso", "nombre-de-archivo", rel, "el nombre va en kebab-case con letras ASCII")
        if d.get("estado") == "vigente" and not d.get("revisado"):
            hallar("error", "campo-faltante", rel, "falta `revisado` (obligatorio si está vigente)")
        if d.get("estado") == "borrador":
            hallar("aviso", "pendiente-de-revision", rel, "borrador: espera que una persona lo lea y lo confirme")
        if d.get("estado") == "borrador" and d.get("revisado"):
            hallar("aviso", "borrador-revisado", rel, "un borrador no tiene `revisado`: se pone al pasar a vigente")
        primera = _primera_linea(n["cuerpo"])
        if d.get("resumen") and _normal(primera) != _normal(d["resumen"]):
            hallar("aviso", "resumen-distinto", rel, "la primera línea no es igual a `resumen`")
        texto = n["cuerpo"].lower()
        halladas = sorted({m for m in MULETILLAS if re.search(rf"\b{re.escape(m)}\b", texto)})
        if halladas:
            hallar("aviso", "muletilla", rel, ", ".join(halladas))
        for campo in OBLIGATORIOS:
            if not d.get(campo):
                hallar("error", "campo-faltante", rel, f"falta `{campo}`")
        if d.get("tipo") and d["tipo"] not in TIPOS:
            hallar("error", "valor-invalido", rel, f"`tipo: {d['tipo']}` no es uno de {sorted(TIPOS)}")
        if d.get("estado") and d["estado"] not in ESTADOS:
            hallar("error", "valor-invalido", rel, f"`estado: {d['estado']}` no es uno de {sorted(ESTADOS)}")
        if d.get("idioma") and d["idioma"] not in IDIOMAS:
            hallar("error", "valor-invalido", rel, f"`idioma: {d['idioma']}` no es uno de {sorted(IDIOMAS)}")
        if d.get("estabilidad") and d["estabilidad"] not in REVISION_DIAS:
            hallar("error", "valor-invalido", rel, f"`estabilidad: {d['estabilidad']}` no es una de {sorted(REVISION_DIAS)}")
        for rel_ in RELACIONES:
            for otro in _lista(d.get(rel_)):
                if otro not in notas and otro not in existentes:
                    hallar("error", "relacion-rota", rel, f"`{rel_}` apunta a `{otro}`, que no existe")
        if d.get("estado") == "obsoleto" and not d.get("reemplazado_por"):
            hallar("aviso", "obsoleto-sin-reemplazo", rel, "obsoleto sin `reemplazado_por`: ¿se puede borrar?")
        if d.get("tipo") in MAPAS:
            enlazadas_desde_mapa |= enlaces
        if d.get("tipo") != "decision" and d.get("estado") != "obsoleto" and d.get("revisado"):
            try:
                revisado = dt.date.fromisoformat(str(d["revisado"]))
            except ValueError:
                hallar("error", "valor-invalido", rel, f"`revisado: {d['revisado']}` no es AAAA-MM-DD")
            else:
                dias = REVISION_DIAS.get(d.get("estabilidad"), 180)
                if (hoy - revisado).days > dias:
                    hallar("aviso", "revision-vencida", rel, f"revisada hace {(hoy - revisado).days} días (cada {dias})")
        if d.get("tipo") == "mapa" and not _lista(d.get("parte_de")) and id_ not in MAPAS_RAIZ:
            hallar("aviso", "mapa-sin-padre", rel, "ningún Mapa padre: no se llega desde el Mapa raíz")

    padres = {i: [p for p in _lista((n["datos"] or {}).get("parte_de")) if p in notas] for i, n in notas.items()}

    def ancestros(i: str) -> set[str]:
        vistos, pila = set(), list(padres.get(i, []))
        while pila:
            a = pila.pop()
            if a not in vistos:
                vistos.add(a)
                pila.extend(padres.get(a, []))
        return vistos

    for i, n in notas.items():
        d = n["datos"] or {}
        if i in ancestros(i):
            hallar("error", "ciclo", n["ruta"], "`parte_de` vuelve sobre sí misma")
        for otro in _lista(d.get("relacionado")):
            if otro in notas and (otro in ancestros(i) or i in ancestros(otro)):
                hallar("error", "relacionado-en-jerarquia", n["ruta"], f"`{otro}` ya está en su cadena de `parte_de`")
        for otro in _lista(d.get("relacionado")):
            if otro in notas and i not in _lista((notas[otro]["datos"] or {}).get("relacionado")):
                hallar("aviso", "relacionado-asimetrico", n["ruta"], f"`{otro}` no la tiene en su `relacionado`")
        es_raiz = d.get("tipo") in MAPAS
        if d and d.get("estado") != "obsoleto" and not es_raiz and i not in enlazadas_desde_mapa:
            hallar("aviso", "huerfana", n["ruta"], "ningún Mapa ni Recorrido la enlaza")
    con_mapa = {n["path"].parent for n in notas.values() if (n["datos"] or {}).get("tipo") == "mapa"}
    for carpeta in sorted({n["path"].parent for n in notas.values() if n["datos"]} - con_mapa):
        hallar("aviso", "tema-sin-mapa", carpeta.relative_to(raiz) if carpeta != raiz else ".", "la carpeta no tiene Mapa")
    return hallazgos


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
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    hallazgos = revisar(a.carpeta, a.hoy)
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
