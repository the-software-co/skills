"""`revisar.py` sobre un tema hecho con el modo `nuevo` (con `ALCANCE.md`): cada regla en un directorio temporal."""
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
            f"estado: borrador\ndueno: matias\nfuentes: [https://example.org]\ncreado: 2026-11-11\nautoria: ia\n"
            f"{extra}---\n\n{cuerpo}")


MAPA = nota("mapa", resumen="Mapa de Reptiles.",
            cuerpo="# Reptiles\n\nMapa de Reptiles.\n\n- [Reptil](reptil.md) — qué es.\n"
                   "- [Termorregulación](termorregulacion.md) — cómo.\n"
                   "- [Ectotermia](ectotermia.md) — la idea.\n- [Lagarto](lagarto.md) — un caso.\n")

# Avisos que da cualquier tema recién escrito: borradores sin confirmar y un Mapa sin padre fuera del vault.
DE_BORRADOR = {"pendiente-de-revision", "mapa-sin-padre"}


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
    return {(h["regla"], h["nota"]) for h in revisar.revisar(carpeta, HOY) if h["regla"] not in DE_BORRADOR}


def test_un_tema_bien_armado_no_tiene_hallazgos(tmp_path):
    assert reglas(tema(tmp_path)) == set()


def test_sin_mapa_y_alcance_sin_aprobar(tmp_path):
    r = reglas(tema(tmp_path, {"ALCANCE.md": ALCANCE.replace("aprobado: 2026-11-10\n", ""),
                               "sub/hoja.md": nota(titulo="Hoja")}))
    assert ("alcance-sin-aprobar", "ALCANCE.md") in r
    assert ("tema-sin-mapa", "sub") in r


def test_campo_faltante_y_valor_invalido(tmp_path):
    r = reglas(tema(tmp_path, {
        "lagarto.md": nota(area="cualquiera", titulo="Lagarto", extra="es_un: [reptil]\n").replace("dueno: matias\n", ""),
        "reptil.md": "# Reptil\n\nSin frontmatter.\n",
    }))
    assert ("valor-invalido", "lagarto.md") in r
    assert ("campo-faltante", "lagarto.md") in r
    assert ("formato-anterior", "reptil.md") in r


def test_area_obligatoria_en_un_tema_con_alcance(tmp_path):
    sin_area = nota(titulo="Lagarto", extra="es_un: [reptil]\n").replace("area: que-es\n", "")
    assert ("campo-faltante", "lagarto.md") in reglas(tema(tmp_path, {"lagarto.md": sin_area}))


def test_enlace_y_relacion_rotos(tmp_path):
    r = reglas(tema(tmp_path, {
        "lagarto.md": nota(area="anatomia", titulo="Lagarto", resumen="Un lagarto es un reptil escamoso.",
                           extra="es_un: [reptil]\nrequiere: [no-existe]\n",
                           cuerpo="# Lagarto\n\nUn lagarto es un reptil escamoso.\n\nVer [escama](escama.md).\n"),
    }))
    assert ("enlace-roto", "lagarto.md") in r
    assert ("relacion-rota", "lagarto.md") in r


def test_ciclo_en_requiere(tmp_path):
    r = reglas(tema(tmp_path, {"reptil.md": nota(extra="umbral: true\nresponde: [P1]\nrequiere: [termorregulacion]\n")}))
    assert any(regla == "ciclo-requiere" for regla, _ in r)


def test_jerarquia_y_relacionado_a_la_vez(tmp_path):
    r = reglas(tema(tmp_path, {
        "lagarto.md": nota(area="anatomia", titulo="Lagarto", resumen="Un lagarto es un reptil escamoso.",
                           extra="es_un: [reptil]\nrelacionado: [reptil]\n"),
        "reptil.md": nota(extra="umbral: true\nresponde: [P1]\nrelacionado: [lagarto]\n"),
    }))
    assert ("relacionado-en-jerarquia", "lagarto.md") in r


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
    assert ("umbral", "ALCANCE.md") in reglas(tema(tmp_path, {"reptil.md": nota(extra="responde: [P1]\n")}))


def test_revision_vencida(tmp_path):
    vieja = nota(area="anatomia", titulo="Lagarto", resumen="Un lagarto es un reptil escamoso.",
                 estabilidad="volatil", extra="es_un: [reptil]\n")
    vieja = vieja.replace("estado: borrador", "estado: vigente\nrevisado: 2026-01-01")
    assert ("revision-vencida", "lagarto.md") in reglas(tema(tmp_path, {"lagarto.md": vieja}))


def test_subtema_con_su_mapa_y_alcance(tmp_path):
    sub_mapa = nota("mapa", resumen="Mapa de Escamas.", cuerpo="# Escamas\n\nMapa de Escamas.\n\n- [Escama](escama.md) — qué es.\n")
    r = reglas(tema(tmp_path, {
        "README.md": MAPA + "- [Escamas](escamas/README.md) — sub-tema.\n",
        "escamas/README.md": sub_mapa,
        "escamas/ALCANCE.md": ALCANCE.replace("P1", "P3").replace("P2", "P4"),
        "escamas/escama.md": nota(area="anatomia", titulo="Escama", resumen="Una escama es una placa.",
                                  extra="responde: [P3, P4]\nparte_de: [lagarto]\n"),
    }))
    assert ("umbral", "escamas/ALCANCE.md") in r  # el sub-tema no tiene conceptos umbral propios
    assert r - {("umbral", "escamas/ALCANCE.md")} == set()


def test_una_nota_que_se_llama_como_el_tema_no_choca_con_el_mapa(tmp_path):
    carpeta = tmp_path / "reptil"
    tema(carpeta)
    assert reglas(carpeta) == set()


def test_un_readme_sin_frontmatter_es_una_puerta_y_no_una_nota(tmp_path):
    (tmp_path / "docs").mkdir()
    tema(tmp_path / "docs")
    (tmp_path / "docs" / "guia").mkdir()
    (tmp_path / "docs" / "guia" / "README.md").write_text("# Guía\n\nVer el índice.\n")
    assert reglas(tmp_path / "docs") == set()


def test_cifra_sin_evidencia(tmp_path):
    t = tema(tmp_path, {
        "reptil.md": nota(extra="umbral: true\nresponde: [P1]\n",
                          cuerpo="# Reptil\n\nUn reptil es un vertebrado.\n\nSu zona preferida va de 25 a 30 °C, pesa 52,0 g y dura 12 %.\n"),
        ".investigacion/fisiologia.md": "La zona preferida es 30 °C según Merck (2012).\n",
    })
    hallazgo = next(h for h in revisar.revisar(t, HOY) if h["regla"] == "cifra-sin-evidencia")
    assert hallazgo["nota"] == "reptil.md" and "52.0" in hallazgo["mensaje"] and "12" in hallazgo["mensaje"]
    assert "30" not in hallazgo["mensaje"]


def test_el_enfasis_no_cuenta_al_comparar_resumen_y_primera_linea(tmp_path):
    t = tema(tmp_path, {"reptil.md": nota(extra="umbral: true\nresponde: [P1]\n",
                                          cuerpo="# Reptil\n\nUn *reptil* es un vertebrado.\n")})
    assert not any(h["regla"] == "resumen-distinto" for h in revisar.revisar(t, HOY))


def test_dos_temas_con_los_mismos_ids_de_pregunta_no_se_tapan(tmp_path):
    tema(tmp_path / "uno")
    tema(tmp_path / "dos", {"termorregulacion.md": nota(area="como-funciona", titulo="Termorregulación",
                                                       resumen="La termorregulación mantiene la temperatura.",
                                                       extra="umbral: true\nrequiere: [ectotermia]\n")})
    (tmp_path / "dos" / "reptil.md").rename(tmp_path / "dos" / "reptil-dos.md")
    (tmp_path / "dos" / "reptil-dos.md").write_text(nota(extra="umbral: true\nresponde: [P1]\n"))
    for f in ("lagarto", "ectotermia", "termorregulacion"):
        p = tmp_path / "dos" / f"{f}.md"
        p.rename(tmp_path / "dos" / f"{f}-dos.md")
    r = {(h["regla"], h["nota"]) for h in revisar.revisar(tmp_path, HOY)}
    assert ("pregunta-sin-nota", "dos/ALCANCE.md") in r
    assert ("pregunta-sin-nota", "uno/ALCANCE.md") not in r


def test_enlaces_dentro_de_codigo_no_se_chequean(tmp_path):
    t = tema(tmp_path, {"reptil.md": nota(extra="umbral: true\nresponde: [P1]\n",
                                          cuerpo="# Reptil\n\nUn reptil es un vertebrado.\n\n"
                                                 "Un enlace se escribe `[[x]]`:\n\n```\n[[no-existe]] y [a](b.md)\n```\n")})
    assert not any(h["regla"] == "enlace-roto" for h in revisar.revisar(t, HOY))


def test_un_decimal_no_es_una_version(tmp_path):
    t = tema(tmp_path, {"reptil.md": nota(resumen="Un reptil mantiene 28.5 grados.", extra="umbral: true\nresponde: [P1]\n")})
    assert not any(h["regla"] == "volatil-en-nucleo" for h in revisar.revisar(t, HOY))


def test_un_tema_dentro_de_una_base_ve_el_mapa_raiz_y_sus_convenciones(tmp_path):
    (tmp_path / "CONVENCIONES.md").write_text("```yaml revisar\npalabras_max: 2000\n```\n")
    (tmp_path / "indice.md").write_text(nota("mapa", resumen="Índice.", cuerpo="# Índice\n\nÍndice.\n\n- [Reptiles](reptiles/README.md)\n"))
    t = tema(tmp_path / "reptiles", {"README.md": MAPA.replace("estado: borrador", "estado: borrador\nparte_de: [indice]")})
    r = {(h["regla"], h["nota"]) for h in revisar.revisar(t, HOY)}
    assert not any(regla == "relacion-rota" for regla, _ in r)


def test_reemplazado_por_que_no_existe(tmp_path):
    vieja = nota(area="anatomia", titulo="Lagarto", resumen="Un lagarto es un reptil escamoso.",
                 extra="es_un: [reptil]\nreemplazado_por: nada\n").replace("estado: borrador", "estado: obsoleto")
    assert ("relacion-rota", "lagarto.md") in reglas(tema(tmp_path, {"lagarto.md": vieja}))
