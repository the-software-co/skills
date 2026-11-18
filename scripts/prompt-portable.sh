#!/bin/sh
# Imprime la skill `documentar` como un solo prompt, para pegar en un chat sin la skill.
set -e
d="$(dirname "$0")/../plugins/documentar/skills/documentar"
cat "$d/conversacion.md"; echo; cat "$d/metodo.md"; echo; echo "## Plantillas"
for p in "$d"/plantillas/*.md; do
  printf '\n### Plantilla `%s`\n\n````markdown\n' "$(basename "$p" .md)"; cat "$p"; printf '````\n'
done
