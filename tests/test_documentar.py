"""`revisar.py` de documentar: cada regla sobre un tema mínimo en un directorio temporal."""
import datetime as dt
import importlib.util
import pathlib

DOCUMENTAR = pathlib.Path(__file__).resolve().parents[1] / "plugins" / "documentar" / "skills" / "documentar"

_spec = importlib.util.spec_from_file_location("revisar_documentar", DOCUMENTAR / "revisar.py")
revisar = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(revisar)

HOY = dt.date(2026, 11, 11)

ALCANCE = """---
tema: Reptiles
volatiles: [ReptiCalc]
aprobado: 2026-11-10
---

# Alcance: Reptiles

## Preguntas de cobertura

- **P1** (`que-es`): ¿Qué es un reptil?
- **P2** (`como-funciona`): ¿Cómo regula su temperatura?
"""


def nota(tipo="concepto", area="que-es", resumen="Un reptil es un vertebrado.", extra="", cuerpo=None,
         estabilidad="estable", titulo="Reptil"):
    cuerpo = cuerpo if cuerpo is not None else f"# {titulo}\n\n{resumen}\n"
    area_linea = "" if tipo == "mapa" else f"area: {area}\n"
    return (f"---\ntipo: {tipo}\n{area_linea}resumen: >-\n  {resumen}\nestabilidad: {estabilidad}\n"
            f"estado: borrador\nfuentes: [https://example.org]\ncreado: 2026-11-11\nautoria: ia\n{extra}---\n\n{cuerpo}")


MAPA = nota("mapa", resumen="Mapa de Reptiles.",
            cuerpo="# Reptiles\n\n- [Reptil](reptil.md) — qué es.\n- [Termorregulación](termorregulacion.md) — cómo.\n"
                   "- [Ectotermia](ectotermia.md) — la idea.\n- [Lagarto](lagarto.md) — un caso.\n")


def tema(tmp_path, cambios: dict[str, str | None] | None = None):
    archivos = {
        "ALCANCE.md": ALCANCE,
        "README.md": MAPA,
        "reptil.md": nota(extra="umbral: true\nresponde: [P1]\n"),
        "ectotermia.md": nota(area="como-funciona", resumen="La ectotermia es depender del calor externo.",
                              titulo="Ectotermia", extra="umbral: true\nrequiere: [reptil]\n"),
        "termorregulacion.md": nota(area="como-funciona", resumen="La termorregulación mantiene la temperatura.",
                                    titulo="Termorregulación",
                                    extra="umbral: true\nresponde: [P2]\nrequiere: [ectotermia]\n"),
        "lagarto.md": nota(area="anatomia", resumen="Un lagarto es un reptil escamoso.", titulo="Lagarto",
                           extra="es_un: [reptil]\n"),
    }
    archivos.update(cambios or {})
    for nombre, texto in archivos.items():
        if texto is not None:
            (tmp_path / nombre).parent.mkdir(parents=True, exist_ok=True)
            (tmp_path / nombre).write_text(texto, encoding="utf-8")
    return tmp_path


def reglas(carpeta):
    return {(h["regla"], h["archivo"]) for h in revisar.revisar(carpeta, HOY)}


def test_un_tema_bien_armado_no_tiene_hallazgos(tmp_path):
    assert reglas(tema(tmp_path)) == set()


def test_sin_alcance_y_sin_mapa(tmp_path):
    r = reglas(tema(tmp_path, {"ALCANCE.md": None, "sub/hoja.md": nota()}))
    assert ("sin-alcance", "ALCANCE.md") in r
    assert ("sin-mapa", "sub/README.md") in r


def test_frontmatter_invalido(tmp_path):
    r = reglas(tema(tmp_path, {
        "lagarto.md": nota(area="cualquiera", titulo="Lagarto", extra="es_un: [reptil]\n").replace("tipo: concepto", "tipo: nota"),
        "reptil.md": "# Reptil\n\nSin frontmatter.\n",
    }))
    assert ("frontmatter", "lagarto.md") in r
    assert ("frontmatter", "reptil.md") in r


def test_enlace_y_relacion_rotos(tmp_path):
    r = reglas(tema(tmp_path, {
        "lagarto.md": nota(area="anatomia", titulo="Lagarto", extra="es_un: [reptil]\nrequiere: [no-existe]\n",
                           cuerpo="# Lagarto\n\nVer [escama](escama.md).\n"),
    }))
    assert ("enlace-roto", "lagarto.md") in r
    assert ("relacion-rota", "lagarto.md") in r


def test_ciclo_en_requiere(tmp_path):
    r = reglas(tema(tmp_path, {
        "reptil.md": nota(extra="umbral: true\nresponde: [P1]\nrequiere: [termorregulacion]\n"),
    }))
    assert any(regla == "ciclo-requiere" for regla, _ in r)


def test_jerarquia_y_relacionado_a_la_vez(tmp_path):
    r = reglas(tema(tmp_path, {
        "lagarto.md": nota(area="anatomia", titulo="Lagarto", extra="es_un: [reptil]\nrelacionado: [reptil]\n"),
        "reptil.md": nota(extra="umbral: true\nresponde: [P1]\nrelacionado: [lagarto]\n"),
    }))
    assert ("jerarquia-y-relacionado", "lagarto.md") in r


def test_requiere_redundante(tmp_path):
    r = reglas(tema(tmp_path, {
        "termorregulacion.md": nota(area="como-funciona", titulo="Termorregulación",
                                    resumen="La termorregulación mantiene la temperatura.",
                                    extra="umbral: true\nresponde: [P2]\nrequiere: [ectotermia, reptil]\n"),
    }))
    assert ("requiere-redundante", "termorregulacion.md") in r


def test_huerfana(tmp_path):
    r = reglas(tema(tmp_path, {"escama.md": nota(area="anatomia", titulo="Escama", resumen="Una escama es una placa.")}))
    assert ("huerfana", "escama.md") in r


def test_pregunta_sin_nota_y_responde_inexistente(tmp_path):
    r = reglas(tema(tmp_path, {
        "termorregulacion.md": nota(area="como-funciona", titulo="Termorregulación",
                                    resumen="La termorregulación mantiene la temperatura.",
                                    extra="umbral: true\nresponde: [P9]\nrequiere: [ectotermia]\n"),
    }))
    assert ("pregunta-sin-nota", "ALCANCE.md") in r
    assert ("responde-inexistente", "termorregulacion.md") in r


def test_volatil_en_nucleo(tmp_path):
    r = reglas(tema(tmp_path, {
        "ectotermia.md": nota(area="como-funciona", titulo="Ectotermia según ReptiCalc",
                              resumen="La ectotermia es depender del calor externo.",
                              extra="umbral: true\nrequiere: [reptil]\n"),
        "lagarto.md": nota(area="anatomia", titulo="Lagarto", resumen="Un lagarto cuesta USD 40 en la v2.1.",
                           extra="es_un: [reptil]\n"),
    }))
    assert ("volatil-en-nucleo", "ectotermia.md") in r
    assert ("volatil-en-nucleo", "lagarto.md") in r


def test_volatil_fuera_del_nucleo_no_es_error(tmp_path):
    r = reglas(tema(tmp_path, {
        "lagarto.md": nota(tipo="ficha", area="ecosistema", titulo="ReptiCalc 2.1", estabilidad="volatil",
                           resumen="ReptiCalc 2.1 cuesta USD 40.", extra="es_un: [reptil]\n"),
    }))
    assert not any(regla == "volatil-en-nucleo" for regla, _ in r)


def test_umbral_fuera_de_rango(tmp_path):
    r = reglas(tema(tmp_path, {"reptil.md": nota(extra="responde: [P1]\n")}))
    assert ("umbral", "README.md") in r


def test_revision_vencida(tmp_path):
    vieja = nota(area="anatomia", titulo="Lagarto", estabilidad="volatil", extra="es_un: [reptil]\n")
    vieja = vieja.replace("estado: borrador", "estado: vigente\nrevisado: 2026-01-01")
    assert ("revision-vencida", "lagarto.md") in reglas(tema(tmp_path, {"lagarto.md": vieja}))


def test_subtema_con_su_mapa_y_alcance(tmp_path):
    sub_mapa = nota("mapa", resumen="Mapa de Escamas.", cuerpo="# Escamas\n\n- [Escama](escama.md) — qué es.\n")
    r = reglas(tema(tmp_path, {
        "README.md": MAPA + "- [Escamas](escamas/README.md) — sub-tema.\n",
        "escamas/README.md": sub_mapa,
        "escamas/ALCANCE.md": ALCANCE.replace("P1", "P3").replace("P2", "P4"),
        "escamas/escama.md": nota(area="anatomia", titulo="Escama", resumen="Una escama es una placa.",
                                  extra="responde: [P3, P4]\nparte_de: [lagarto]\n"),
    }))
    assert r == set()


def test_una_nota_que_se_llama_como_el_tema_no_choca_con_el_mapa(tmp_path):
    carpeta = tmp_path / "reptil"
    tema(carpeta)
    assert reglas(carpeta) == set()
