"""Las skills y sus casos de disparo: lo que `claude plugin eval` no chequea antes de correr."""
import pathlib
import re

PLUGIN = pathlib.Path(__file__).resolve().parents[1] / "plugins" / "documentar"


def frontmatter(p: pathlib.Path) -> dict[str, str]:
    cabeza = p.read_text().split("---")[1]
    return dict(re.findall(r"^(\w+): (.*)$", cabeza, re.M))


def test_cada_skill_se_llama_como_su_carpeta_y_su_descripcion_entra():
    skills = sorted(PLUGIN.glob("skills/*/SKILL.md"))
    assert {p.parent.name for p in skills} >= {"documentar", "consultar"}
    for p in skills:
        fm = frontmatter(p)
        assert fm["name"] == p.parent.name
        assert len(fm["description"]) <= 1024


def test_disparo_de_consultar_tiene_diez_y_diez():
    casos = [frontmatter(p) for p in PLUGIN.glob("evals/*/prompt.md")]
    tags = [c["tags"] for c in casos if "disparo-consultar" in c["tags"]]
    assert sum("near-miss" not in t for t in tags) == 10
    assert sum("near-miss" in t for t in tags) == 10
