#!/usr/bin/env python3
"""Chequeos deterministas de un tema de la biblioteca (ver `metodo.md`). Solo stdlib.

    python3 revisar.py <carpeta del tema> [--hoy AAAA-MM-DD] [--json]

Escribe una línea por hallazgo, `ERROR|AVISO <regla> <archivo>: <mensaje>`, y sale con 1 si hay
algún error. Revisa el tema y sus sub-temas (sub-carpetas con `README.md`).
"""
import argparse
import datetime as dt
import json
import pathlib
import re
import sys

TIPOS = {"mapa", "concepto", "como-hacer", "decision", "falla", "ficha", "ruta"}
AREAS = {"que-es", "como-funciona", "anatomia", "procesos", "como-se-hace", "como-se-decide",
         "como-falla", "historia", "ecosistema", "referencia", "ruta"}
NUCLEO = {"que-es", "como-funciona", "anatomia", "procesos", "historia", "como-falla"}
ESTABILIDADES = {"estable": 365, "semi": 180, "volatil": 90}
ESTADOS = {"borrador", "vigente", "obsoleto"}
AUTORIAS = {"ia", "mixta", "humano"}
JERARQUIA = ("es_un", "parte_de", "instancia_de")
RELACIONES = JERARQUIA + ("requiere", "relacionado")
OBLIGATORIOS = ("tipo", "resumen", "estabilidad", "estado", "autoria", "creado")
NO_NOTAS = {"ALCANCE.md"}
PALABRAS_MAX = 600
UMBRAL = (3, 7)

NOMBRE = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")
MDLINK = re.compile(r"\]\(([^)\s#]+?\.md)(?:#[^)]*)?\)")
PREGUNTA = re.compile(r"\*\*([PE]\d+)\*\*")
VERSION = re.compile(r"\bv?\d+\.\d+(?:\.\d+)?\b")
PRECIO = re.compile(r"(?:US\$|U\$S|USD|ARS|EUR|\$|€)\s?\d|\d\s?(?:USD|ARS|EUR|dólares|pesos|euros)\b")


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
                previo = datos[clave] if isinstance(datos[clave], list) else []
                datos[clave] = previo + [_escalar(item[2:])]
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
    return v.strip().strip("'\"")


def _lista(fm: dict, clave: str) -> list[str]:
    v = fm.get(clave) or []
    return v if isinstance(v, list) else [v]


def _h1(cuerpo: str) -> str:
    m = re.search(r"^# (.+)$", cuerpo, re.M)
    return m.group(1).strip() if m else ""


def _ciclo(grafo: dict[str, list[str]]) -> list[str] | None:
    """Un ciclo cualquiera del grafo, como lista de ids, o None."""
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
        if n in vistos:
            continue
        vistos.add(n)
        pendientes.extend(grafo.get(n, []))
    return vistos


def revisar(raiz: pathlib.Path, hoy: dt.date) -> list[dict]:
    hallazgos: list[dict] = []

    def h(nivel: str, regla: str, archivo: pathlib.Path | str, mensaje: str) -> None:
        rel = archivo if isinstance(archivo, str) else str(archivo.relative_to(raiz))
        hallazgos.append({"nivel": nivel, "regla": regla, "archivo": rel, "mensaje": mensaje})

    # Notas y alcances.
    notas: dict[str, dict] = {}
    alcances: list[tuple[pathlib.Path, dict, str]] = []
    for ruta in sorted(raiz.rglob("*.md")):
        if any(p.startswith(".") for p in ruta.relative_to(raiz).parts):
            continue
        texto = ruta.read_text(encoding="utf-8")
        fm, cuerpo = frontmatter(texto)
        if ruta.name in NO_NOTAS:
            if fm is None:
                h("ERROR", "frontmatter", ruta, "el ALCANCE.md no tiene frontmatter")
            else:
                alcances.append((ruta, fm, cuerpo))
            continue
        if fm is None:
            h("ERROR", "frontmatter", ruta, "no tiene frontmatter")
            continue
        # Un Mapa no es destino de relaciones: su id no compite con la nota que se llama como el tema.
        nid = f"mapa:{ruta.parent.relative_to(raiz)}" if ruta.name == "README.md" else ruta.stem
        if ruta.name != "README.md" and not NOMBRE.fullmatch(ruta.stem):
            h("ERROR", "nombre", ruta, "el nombre no es kebab-case ASCII")
        if nid in notas:
            h("ERROR", "id-duplicado", ruta, f"el id {nid} ya es de {notas[nid]['archivo']}")
            continue
        notas[nid] = {"ruta": ruta, "archivo": str(ruta.relative_to(raiz)), "fm": fm, "cuerpo": cuerpo}

    carpetas = [raiz, *(p for p in raiz.rglob("*") if p.is_dir())]
    for carpeta in sorted(c for c in carpetas if not any(x.startswith(".") for x in c.relative_to(raiz).parts)):
        if any(carpeta.glob("*.md")) and not (carpeta / "README.md").exists():
            h("ERROR", "sin-mapa", carpeta / "README.md", "la carpeta tiene notas y no tiene Mapa")
        if (carpeta / "README.md").exists() and not (carpeta / "ALCANCE.md").exists():
            h("ERROR", "sin-alcance", carpeta / "ALCANCE.md", "el tema no tiene ALCANCE.md")

    # Frontmatter de cada nota.
    for nid, n in notas.items():
        fm, ruta = n["fm"], n["ruta"]
        for clave in OBLIGATORIOS:
            if not fm.get(clave):
                h("ERROR", "frontmatter", ruta, f"falta `{clave}`")
        if fm.get("tipo") and fm["tipo"] not in TIPOS:
            h("ERROR", "frontmatter", ruta, f"`tipo` inválido: {fm['tipo']}")
        if ruta.name == "README.md" and fm.get("tipo") != "mapa":
            h("ERROR", "frontmatter", ruta, "el README.md de un tema es su Mapa: `tipo: mapa`")
        if fm.get("tipo") not in (None, "mapa"):
            if not fm.get("area"):
                h("ERROR", "frontmatter", ruta, "falta `area`")
            elif fm["area"] not in AREAS:
                h("ERROR", "frontmatter", ruta, f"`area` inválida: {fm['area']}")
        if fm.get("estabilidad") and fm["estabilidad"] not in ESTABILIDADES:
            h("ERROR", "frontmatter", ruta, f"`estabilidad` inválida: {fm['estabilidad']}")
        if fm.get("estado") and fm["estado"] not in ESTADOS:
            h("ERROR", "frontmatter", ruta, f"`estado` inválido: {fm['estado']}")
        if fm.get("autoria") and fm["autoria"] not in AUTORIAS:
            h("ERROR", "frontmatter", ruta, f"`autoria` inválida: {fm['autoria']}")
        if fm.get("estado") == "vigente" and not fm.get("revisado"):
            h("ERROR", "frontmatter", ruta, "una nota vigente lleva `revisado`")
        if fm.get("estado") == "obsoleto" and fm.get("reemplazado_por") not in notas:
            h("ERROR", "frontmatter", ruta, "una nota obsoleta lleva `reemplazado_por` hacia una nota que existe")
        if fm.get("tipo") in {"concepto", "falla", "ficha", "decision"} and not _lista(fm, "fuentes"):
            h("AVISO", "sin-fuentes", ruta, "no cita fuentes")
        if fm.get("estado") == "vigente" and fm.get("revisado") and fm.get("estabilidad") in ESTABILIDADES:
            try:
                vence = dt.date.fromisoformat(fm["revisado"]) + dt.timedelta(days=ESTABILIDADES[fm["estabilidad"]])
                if vence < hoy:
                    h("AVISO", "revision-vencida", ruta, f"tocaba re-verificarla el {vence}")
            except ValueError:
                h("ERROR", "frontmatter", ruta, f"`revisado` no es una fecha: {fm['revisado']}")
        palabras = len(re.sub(r"```.*?```", "", n["cuerpo"], flags=re.S).split())
        if fm.get("tipo") not in {"mapa", "ficha", "ruta"} and palabras > PALABRAS_MAX:
            h("AVISO", "larga", ruta, f"{palabras} palabras: ¿responde más de una pregunta?")

    # Enlaces del cuerpo.
    for n in notas.values():
        for destino in MDLINK.findall(n["cuerpo"]):
            if destino.startswith(("http://", "https://")):
                continue
            if not (n["ruta"].parent / destino).resolve().exists():
                h("ERROR", "enlace-roto", n["ruta"], f"no existe {destino}")

    # Relaciones del frontmatter.
    grafos = {r: {} for r in RELACIONES}
    for nid, n in notas.items():
        for r in RELACIONES:
            destinos = _lista(n["fm"], r)
            for d in destinos:
                if d not in notas:
                    h("ERROR", "relacion-rota", n["ruta"], f"`{r}` apunta a {d}, que no existe")
            grafos[r][nid] = [d for d in destinos if d in notas]

    jerarquia = {nid: sum((grafos[r][nid] for r in JERARQUIA), []) for nid in notas}
    for nombre, grafo in (("ciclo-requiere", grafos["requiere"]), ("ciclo-jerarquia", jerarquia)):
        ciclo = _ciclo(grafo)
        if ciclo:
            h("ERROR", nombre, notas[ciclo[0]]["ruta"], " → ".join(ciclo))

    ancestros = {nid: _alcanzables(jerarquia, nid) for nid in notas}
    for nid, n in notas.items():
        for d in grafos["relacionado"][nid]:
            if d in ancestros[nid] or nid in ancestros[d]:
                h("ERROR", "jerarquia-y-relacionado", n["ruta"],
                  f"{d} está en su jerarquía: la relación es jerárquica, no `relacionado`")
            elif nid not in grafos["relacionado"].get(d, []):
                h("AVISO", "relacionado-asimetrico", n["ruta"], f"{d} no la tiene en `relacionado`")
        for d in grafos["requiere"][nid]:
            if d in _alcanzables(grafos["requiere"], nid, saltando=d):
                h("AVISO", "requiere-redundante", n["ruta"], f"{d} ya se requiere por otro camino")

    # Huérfanas: toda nota está enlazada desde algún Mapa.
    enlazadas: set[pathlib.Path] = set()
    for n in notas.values():
        if n["fm"].get("tipo") == "mapa":
            for destino in MDLINK.findall(n["cuerpo"]):
                enlazadas.add((n["ruta"].parent / destino).resolve())
    for n in notas.values():
        if n["ruta"] != raiz / "README.md" and n["ruta"].resolve() not in enlazadas:
            h("AVISO", "huerfana", n["ruta"], "ningún Mapa la enlaza")

    # Alcance: preguntas y volátiles.
    volatiles: list[str] = []
    preguntas: dict[str, pathlib.Path] = {}
    for ruta, fm, cuerpo in alcances:
        if not fm.get("aprobado"):
            h("AVISO", "alcance-sin-aprobar", ruta, "falta `aprobado`: la persona no aprobó el alcance")
        volatiles += [v for v in _lista(fm, "volatiles") if v]
        for p in PREGUNTA.findall(cuerpo):
            preguntas[p] = ruta
    respondidas: set[str] = set()
    for n in notas.values():
        for p in _lista(n["fm"], "responde"):
            if p not in preguntas:
                h("ERROR", "responde-inexistente", n["ruta"], f"{p} no está en ningún ALCANCE.md")
            respondidas.add(p)
    for p, ruta in sorted(preguntas.items(), key=lambda x: (x[0][0], int(x[0][1:]))):
        if p not in respondidas:
            h("ERROR", "pregunta-sin-nota", ruta, f"ninguna nota responde {p}")

    for n in notas.values():
        fm = n["fm"]
        if fm.get("area") in NUCLEO and fm.get("estabilidad") == "estable":
            texto = f"{_h1(n['cuerpo'])} {fm.get('resumen', '')}"
            for v in volatiles:
                if re.search(rf"(?<!\w){re.escape(v)}(?!\w)", texto, re.I):
                    h("ERROR", "volatil-en-nucleo", n["ruta"], f"el título o el resumen nombran «{v}»")
            for patron, que in ((VERSION, "una versión"), (PRECIO, "un precio")):
                m = patron.search(texto)
                if m:
                    h("ERROR", "volatil-en-nucleo", n["ruta"], f"el título o el resumen nombran {que}: «{m.group(0)}»")

    umbral = [nid for nid, n in notas.items() if str(n["fm"].get("umbral", "")).lower() == "true"]
    if notas and not (UMBRAL[0] <= len(umbral) <= UMBRAL[1]):
        h("AVISO", "umbral", "README.md", f"hay {len(umbral)} conceptos umbral; van de {UMBRAL[0]} a {UMBRAL[1]}")

    return hallazgos


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("carpeta", type=pathlib.Path)
    ap.add_argument("--hoy", type=dt.date.fromisoformat, default=dt.date.today())
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    if not args.carpeta.is_dir():
        print(f"no es una carpeta: {args.carpeta}", file=sys.stderr)
        return 2
    hallazgos = revisar(args.carpeta.resolve(), args.hoy)
    if args.json:
        print(json.dumps(hallazgos, ensure_ascii=False, indent=2))
    else:
        for x in hallazgos:
            print(f"{x['nivel']} {x['regla']} {x['archivo']}: {x['mensaje']}")
    return 1 if any(x["nivel"] == "ERROR" for x in hallazgos) else 0


if __name__ == "__main__":
    sys.exit(main())
