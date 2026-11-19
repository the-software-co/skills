# Skills de The Software Company

Marketplace de plugins de Claude Code.

## `documentar`

Arma y mantiene bases de conocimiento en Markdown: el vault de Obsidian `mtsdlf/conocimiento`, los docs de un repo o un tema nuevo. Tiene cinco modos:

| Modo | Para qué |
|---|---|
| `nuevo` | Un tema desde cero. Te entrevista en tres rondas, investiga por ángulos (uno busca la posición contraria), propone el mapa de notas y escribe |
| `ampliar` | Profundizar un tema o sumarle un sub-tema |
| `existente` | Ordenar documentación que ya existe |
| `volcar` | Guardar un concepto suelto o algo que aprendiste |
| `mantener` | Encontrar lo viejo, roto, huérfano o contradictorio |

Las notas son atómicas, con relaciones con tipo (`es_un`, `parte_de`, `instancia_de`, `requiere`, `relacionado`). El núcleo estable va separado de lo volátil y cada afirmación dice de dónde sale. El método está en [`metodo.md`](plugins/documentar/skills/documentar/metodo.md), y el porqué de cada decisión, en [`docs/research/`](docs/research/).

### Instalar

En Claude Code:

```
/plugin marketplace add the-software-co/skills
/plugin install documentar@the-software-co
```

Para actualizar: `/plugin marketplace update the-software-co`.

En claude.ai: comprimí la carpeta [`plugins/documentar/skills/documentar`](plugins/documentar/skills/documentar) en un zip y subilo en Settings → Capabilities → Skills.

En cualquier otro chat: `./scripts/prompt-portable.sh` imprime el método y las plantillas como un solo prompt para pegar.

### Chequear una base a mano

```
python3 plugins/documentar/skills/documentar/revisar.py <carpeta> [--desde origin/main]
```

Si tu base tiene convenciones propias (quiénes son dueños, carpetas especiales, dónde se registra lo que se vuelca), escribilas en un `CONVENCIONES.md` en su raíz.

### Pruebas

```
python3 -m pytest tests
```

## Historia

`conocimiento` (hasta la 0.4.0) se fundió en `documentar` 0.3.0: sus modos, su método y su lint viven ahí, y las bases que la usaban siguen pasando el lint sin cambios.

## Licencia

MIT
