"""`revisar.py`: cada regla sobre un Vault mínimo en un directorio temporal."""
import datetime as dt
import importlib.util

import pathlib

CONOCIMIENTO = pathlib.Path(__file__).resolve().parents[1] / "plugins" / "conocimiento" / "skills" / "conocimiento"

_spec = importlib.util.spec_from_file_location("revisar", CONOCIMIENTO / "revisar.py")
revisar = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(revisar)

HOY = dt.date(2026, 10, 3)


def nota(tipo="concepto", resumen="Una cohorte es un grupo.", estado="vigente", extra="", cuerpo=None):
    cuerpo = cuerpo if cuerpo is not None else f"# Título\n\n{resumen}\n"
    return (f"---\ntipo: {tipo}\nresumen: >-\n  {resumen}\nestado: {estado}\nestabilidad: estable\n"
            f"dueno: matias\nrevisado: 2026-09-01\n{extra}---\n\n{cuerpo}")


def vault(tmp_path, notas: dict[str, str]):
    (tmp_path / ".obsidian").mkdir()
    tema = tmp_path / "Matias" / "Conocimiento" / "Datos"
    tema.mkdir(parents=True)
    for nombre, texto in notas.items():
        (tema / nombre).write_text(texto)
    return tema


def reglas(tema):
    return {(h["regla"], h["nota"]) for h in revisar.revisar(tema, HOY)}


def test_un_tema_bien_armado_no_tiene_hallazgos(tmp_path):
    tema = vault(tmp_path, {
        "datos.md": nota("mapa", "Mapa de Datos.", cuerpo="# Datos\n\nMapa de Datos.\n\n- [[cohorte]] — qué es.\n")
                    .replace("revisado", "parte_de: []\nrevisado"),
        "cohorte.md": nota(),
    })
    assert reglas(tema) == {("mapa-sin-padre", "datos.md")}


def test_huerfana_borrador_y_muletilla(tmp_path):
    tema = vault(tmp_path, {
        "datos.md": nota("mapa", "Mapa.", extra="parte_de: [conocimiento]\n", cuerpo="# Datos\n\nNada.\n"),
        "cohorte.md": nota(estado="borrador", cuerpo="# Cohorte\n\nUna cohorte es un grupo.\n\nEs crucial.\n"),
    })
    r = reglas(tema)
    assert ("huerfana", "cohorte.md") in r
    assert ("pendiente-de-revision", "cohorte.md") in r
    assert ("muletilla", "cohorte.md") in r
    assert ("relacion-rota", "datos.md") in r  # el Mapa raíz `conocimiento` no existe


def test_resumen_distinto_nombre_y_relacionado_en_jerarquia(tmp_path):
    tema = vault(tmp_path, {
        "datos.md": nota("mapa", "M.", cuerpo="# D\n\n[[Cohorte_Vieja]] [[hija]]\n"),
        "Cohorte_Vieja.md": nota(cuerpo="# C\n\nOtra cosa.\n"),
        "hija.md": nota(extra="parte_de: [Cohorte_Vieja]\nrelacionado: [Cohorte_Vieja]\n"),
    })
    r = reglas(tema)
    assert ("resumen-distinto", "Cohorte_Vieja.md") in r
    assert ("nombre-de-archivo", "Cohorte_Vieja.md") in r
    assert ("relacionado-en-jerarquia", "hija.md") in r


def test_id_duplicado_en_otra_carpeta_del_vault_y_enlace_roto(tmp_path):
    tema = vault(tmp_path, {"datos.md": nota("mapa", "M.", cuerpo="# D\n\n[[cohorte]] [[no-existe]]\n"),
                            "cohorte.md": nota()})
    (tmp_path / "Fer").mkdir()
    (tmp_path / "Fer" / "cohorte.md").write_text("hola")
    r = reglas(tema)
    assert ("id-duplicado", "cohorte.md") in r
    assert ("enlace-roto", "datos.md") in r


def test_revision_vencida_segun_estabilidad(tmp_path):
    tema = vault(tmp_path, {"datos.md": nota("mapa", "M.", cuerpo="# D\n\n[[vieja]]\n"),
                            "vieja.md": nota().replace("2026-09-01", "2025-01-01")})
    assert ("revision-vencida", "vieja.md") in reglas(tema)
