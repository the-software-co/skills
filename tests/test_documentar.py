"""`revisar.py`: cada regla en una base temporal."""
import datetime as dt
import importlib.util
import pathlib
import subprocess

DOCUMENTAR = pathlib.Path(__file__).resolve().parents[1] / "plugins" / "documentar" / "skills" / "documentar"
_spec = importlib.util.spec_from_file_location("revisar_documentar", DOCUMENTAR / "revisar.py")
revisar = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(revisar)

HOY = dt.date(2026, 11, 19)


def nota(resumen="Un reptil es un vertebrado.", cuerpo="", estado="borrador", estabilidad="estable",
         extra="", titulo="Reptil"):
    return (f"---\nresumen: >-\n  {resumen}\nestado: {estado}\nestabilidad: {estabilidad}\n"
            f"fuentes: [https://example.org]\ncreado: 2026-11-19\n{extra}---\n\n# {titulo}\n\n{resumen}\n\n{cuerpo}")


def base(tmp_path, archivos: dict[str, str]) -> pathlib.Path:
    (tmp_path / "CONVENCIONES.md").write_text("# Convenciones\n")
    for ruta, texto in archivos.items():
        p = tmp_path / ruta
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(texto)
    return tmp_path


def reglas(raiz, **kw):
    return sorted((h["regla"], h["nota"]) for h in revisar.revisar(raiz, HOY, **kw)
                  if h["regla"] != "pendiente-de-revision")


ARBOL = {
    "conocimiento.md": nota("La base.", "- [Reptiles](Reptiles/reptiles.md) — el tema.", titulo="Conocimiento"),
    "Reptiles/reptiles.md": nota("Los reptiles.", "## De qué está hecho un reptil\n\n"
                                 "- [Biología](Biologia/biologia.md) — el cuerpo.\n", titulo="Reptiles"),
    "Reptiles/Biologia/biologia.md": nota("El cuerpo.", "## Las piezas\n\n- [Escama](escama.md) — la piel.\n"
                                          "Se apoya en el [todo](../reptiles.md).", titulo="Biología"),
    "Reptiles/Biologia/escama.md": nota("La escama es queratina.", "## Cómo crece la escama\n\nCrece.", titulo="Escama"),
}


def test_un_arbol_bien_armado_no_tiene_hallazgos(tmp_path):
    assert reglas(base(tmp_path, ARBOL)) == []


def test_pendientes_es_un_solo_aviso_con_la_cuenta(tmp_path):
    h = [h for h in revisar.revisar(base(tmp_path, ARBOL), HOY) if h["regla"] == "pendiente-de-revision"]
    assert len(h) == 1 and h[0]["mensaje"].startswith("4 notas")


def test_huerfana_y_carpeta_sin_entrada(tmp_path):
    arbol = dict(ARBOL)
    arbol["Reptiles/Biologia/cola.md"] = nota("La cola.", titulo="Cola")
    arbol["Reptiles/Salud/muda.md"] = nota("La muda.", titulo="Muda")
    assert reglas(base(tmp_path, arbol)) == [
        ("carpeta-sin-entrada", "Reptiles/Salud"),
        ("huerfana", "Reptiles/Biologia/cola.md"),
        ("huerfana", "Reptiles/Salud/muda.md"),
    ]


def test_un_enlace_entre_hermanos_no_salva_de_huerfana(tmp_path):
    arbol = dict(ARBOL)
    arbol["Reptiles/Biologia/cola.md"] = nota("La cola.", titulo="Cola")
    arbol["Reptiles/Biologia/escama.md"] = nota("La escama.", "Cubre la [cola](cola.md).", titulo="Escama")
    assert ("huerfana", "Reptiles/Biologia/cola.md") in reglas(base(tmp_path, arbol))


def test_enlace_roto_markdown_y_wikilink(tmp_path):
    arbol = dict(ARBOL)
    arbol["Reptiles/Biologia/escama.md"] = nota("La escama.", "Ver [piel](piel.md) y [[hueso]].", titulo="Escama")
    assert reglas(base(tmp_path, arbol)) == [("enlace-roto", "Reptiles/Biologia/escama.md")] * 2


def test_enlaces_dentro_de_codigo_no_se_chequean(tmp_path):
    arbol = dict(ARBOL)
    arbol["Reptiles/Biologia/escama.md"] = nota("La escama.", "`[x](no.md)`\n\n```\n[y](tampoco.md)\n```",
                                                 titulo="Escama")
    assert reglas(base(tmp_path, arbol)) == []


def test_campos_y_valores(tmp_path):
    arbol = dict(ARBOL)
    arbol["Reptiles/Biologia/escama.md"] = "---\nestado: listo\nestabilidad: estable\n---\n\n# Escama\n"
    arbol["Reptiles/Biologia/Hueso.md"] = "# Hueso\n"
    r = reglas(base(tmp_path, arbol))
    assert ("campo-faltante", "Reptiles/Biologia/escama.md") in r
    assert ("valor-invalido", "Reptiles/Biologia/escama.md") in r
    assert ("sin-frontmatter", "Reptiles/Biologia/Hueso.md") in r


def test_titulos_de_plantilla(tmp_path):
    arbol = dict(ARBOL)
    arbol["Reptiles/Biologia/escama.md"] = nota("La escama.", "## Por qué existe\n\nx\n\n## Relaciones\n\ny",
                                                 titulo="Escama")
    assert reglas(base(tmp_path, arbol)) == [("titulos-de-plantilla", "Reptiles/Biologia/escama.md")]


def test_vigente_sin_revisado_y_revision_vencida(tmp_path):
    arbol = dict(ARBOL)
    arbol["Reptiles/Biologia/escama.md"] = nota("La escama.", estado="vigente", titulo="Escama")
    arbol["Reptiles/Biologia/biologia.md"] = nota("El cuerpo.", "- [Escama](escama.md)", estado="vigente",
                                                  estabilidad="volatil", extra="revisado: 2026-01-01\n",
                                                  titulo="Biología")
    assert reglas(base(tmp_path, arbol)) == [
        ("revision-vencida", "Reptiles/Biologia/biologia.md"),
        ("vigente-sin-revisado", "Reptiles/Biologia/escama.md"),
    ]


def test_larga_y_palabras_max_de_convenciones(tmp_path):
    arbol = dict(ARBOL)
    arbol["Reptiles/Biologia/escama.md"] = nota("La escama.", "palabra " * 60, titulo="Escama")
    raiz = base(tmp_path, arbol)
    assert reglas(raiz) == []
    (raiz / "CONVENCIONES.md").write_text("```yaml revisar\npalabras_max: 50\nignorar: [Archivo]\n```\n")
    (raiz / "Archivo").mkdir()
    (raiz / "Archivo" / "vieja.md").write_text("# sin frontmatter\n")
    assert reglas(raiz) == [("larga", "Reptiles/Biologia/escama.md")]


def test_una_subcarpeta_ve_los_enlaces_de_toda_la_base(tmp_path):
    raiz = base(tmp_path, ARBOL)
    assert reglas(raiz / "Reptiles" / "Biologia") == []


def test_mapas_y_readme_de_bases_anteriores_cuentan_como_entrada(tmp_path):
    arbol = {
        "README.md": "# Puerta\n\n[Índice](docs/indice.md)\n",
        "docs/indice.md": nota("El índice.", "- [Pagos](pagos/README.md)", titulo="Índice"),
        "docs/pagos/README.md": nota("Pagos.", "- [Cobro](cobro.md)\n- [Viejo](viejo-mapa.md)", titulo="Pagos"),
        "docs/pagos/cobro.md": nota("El cobro.", titulo="Cobro"),
        "docs/pagos/viejo-mapa.md": nota("Un mapa.", "- [Reintento](reintento.md)", extra="tipo: mapa\n",
                                         titulo="Viejo"),
        "docs/pagos/reintento.md": nota("El reintento.", titulo="Reintento"),
    }
    raiz = base(tmp_path, arbol)
    (raiz / "CONVENCIONES.md").unlink()
    (raiz / "docs" / "CONVENCIONES.md").write_text("# Convenciones\n")
    assert reglas(raiz / "docs") == []


def test_fuente_cambiada_y_desde(tmp_path):
    raiz = base(tmp_path, {})
    git = lambda *a: subprocess.run(["git", "-C", str(raiz), *a], check=True, capture_output=True)
    git("init", "-q", "-b", "main")
    git("config", "user.email", "t@t")
    git("config", "user.name", "t")
    (raiz / "src").mkdir()
    (raiz / "src" / "cobro.py").write_text("x = 1\n")
    (raiz / "indice.md").write_text(nota("El índice.", "- [Cobro](cobro.md)", titulo="Índice"))
    (raiz / "cobro.md").write_text(nota("El cobro.", estado="vigente", titulo="Cobro",
                                        extra="revisado: 2020-01-01\n").replace("[https://example.org]", "[src/cobro.py]"))
    git("add", ".")
    git("commit", "-q", "-m", "a")
    git("checkout", "-q", "-b", "rama")
    (raiz / "src" / "cobro.py").write_text("x = 2\n")
    git("commit", "-qam", "b")
    r = reglas(raiz, desde="main")
    assert ("fuente-cambiada", "cobro.md") in r and ("doc-sin-actualizar", "cobro.md") in r


def test_un_readme_sin_frontmatter_en_una_subcarpeta_es_su_entrada(tmp_path):
    arbol = {
        "indice.md": nota("El índice.", "- [Pagos](Pagos/README.md)", titulo="Índice"),
        "Pagos/README.md": "# Pagos\n\n- [Cobro](cobro.md)\n",
        "Pagos/cobro.md": nota("El cobro.", "~~~\n[x](no-existe.md)\n~~~\n", titulo="Cobro"),
        "Pagos/CONTEXT.md": "# Glosario del dominio\n",
    }
    assert reglas(base(tmp_path, arbol)) == []


def test_resumen_distinto_sin_fuentes_y_reemplazo_roto(tmp_path):
    arbol = dict(ARBOL)
    arbol["Reptiles/Biologia/escama.md"] = nota("La escama.", titulo="Escama").replace(
        "\n\nLa escama.\n", "\n\nOtra cosa.\n").replace("fuentes: [https://example.org]", "fuentes: []")
    arbol["Reptiles/Biologia/biologia.md"] = nota("El cuerpo.", "- [Escama](escama.md)", estado="obsoleto",
                                                  extra="reemplazado_por: cuerpo.md\n", titulo="Biología")
    assert reglas(base(tmp_path, arbol)) == [
        ("enlace-roto", "Reptiles/Biologia/biologia.md"),
        ("resumen-distinto", "Reptiles/Biologia/escama.md"),
        ("sin-fuentes", "Reptiles/Biologia/escama.md"),
    ]
