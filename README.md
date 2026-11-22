# Skills de The Software Company

Marketplace de plugins de Claude Code.

## `documentar`

Arma y mantiene bases de conocimiento en Markdown en git: `mtsdlf/conocimiento`, los docs de un repo o un tema nuevo. Tiene cinco modos:

| Modo | Para qué |
|---|---|
| `nuevo` | Un tema desde cero. Lee el contexto, te propone el árbol del tema en un solo mensaje (con dos o tres preguntas como mucho), investiga por vertical y escribe |
| `ampliar` | Profundizar un tema o sumarle una vertical |
| `existente` | Ordenar documentación que ya existe según el árbol que debería tener |
| `volcar` | Guardar un concepto suelto o algo que aprendiste |
| `mantener` | Encontrar lo viejo, roto, huérfano o contradictorio |

Trae además la skill `consultar`, el modo de lectura: contesta desde la base con ruta, sección y estado de cada nota (`borrador` o `vigente`), dice qué falta y ofrece `volcar` si la respuesta vale como nota. Se dispara también cuando una tarea en otro repo (una propuesta, un precio, un canal, una decisión de producto o de diseño) puede apoyarse en lo que la base ya sabe, aunque no se la nombre. Está en [`skills/consultar/SKILL.md`](plugins/documentar/skills/consultar/SKILL.md).

Un tema se estructura como se analiza un sistema, en capas: el todo (qué es y cómo se componen sus partes), las verticales (una carpeta por cada gran parte del sujeto), los componentes de cada una y, abajo de todo, lo operativo (herramientas, valores, plataformas), que es lo que más cambia. Cada afirmación dice de dónde sale. El método está en [`metodo.md`](plugins/documentar/skills/documentar/metodo.md), y el porqué de cada decisión, en [`docs/research/`](docs/research/).

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

Si tu base tiene convenciones propias (el dueño por defecto, carpetas especiales, dónde se registra lo que se vuelca), escribilas en un `CONVENCIONES.md` en su raíz.

### Pruebas

```
python3 -m pytest tests   # o: uvx pytest tests
```

Los casos de disparo de `consultar` están en [`plugins/documentar/evals/`](plugins/documentar/evals/): 10 pedidos que tienen que cargarla (tareas de negocio que no nombran la base) y 10 parecidos que no (datos propios de un repo, tareas operativas, escribir notas, que es `documentar`). Corren con la CLI de Claude Code, que gasta tokens de tu cuenta (unos USD 6,5 con las tres corridas por caso, unos USD 2 con `--runs 1`):

```
claude plugin eval plugins/documentar --tag disparo-consultar --ablation none -j 5 --no-publish
```

Cada caso corre tres veces por defecto (`--runs 1` para una pasada rápida). Correlo cuando cambia la descripción de una skill del plugin.

## Historia

`conocimiento` (hasta la 0.4.0) se fundió en `documentar` 0.3.0. En la 0.4.0, `documentar` cambió las áreas genéricas y la entrevista de tres rondas por las capas del sujeto y un solo mensaje de alineación: el porqué está en [`docs/research/capas.md`](docs/research/capas.md). Las bases anteriores siguen pasando el lint; el aviso `titulos-de-plantilla` marca las notas para pasar por `existente`. En la 0.6.0 se sumó `consultar`, el modo de lectura, y la sección de tareas en la entrada de cada tema: el porqué está en [`docs/research/consultar.md`](docs/research/consultar.md).

## Licencia

MIT
