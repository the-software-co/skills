# Un modo de lectura: la skill `consultar` y las tareas en la entrada del tema (documentar 0.6.0)

## Qué pasó

Un diagnóstico del 2026-11-22 sobre cómo entran los agentes a `mtsdlf/conocimiento` desde los repos de la organización encontró que la base solo se usa cuando la sesión está abierta en ella y el pedido es explícito («¿qué sabemos de…?»). En los repos de trabajo (`lind-negocio`, `tsc-negocio`, `marketing`) la base aparece como destino de escritura y no como fuente: un agente que arma una propuesta comercial no abre la nota de posicionamiento, que es justo lo que serviría.

## Por qué salió así

1. **El modo Entender no existía.** Los `CLAUDE.md` de la organización y la skill `tsc-organizacion` nombran un modo Entender («contestar desde las notas, con enlaces, y decir lo que falta») y remiten a `documentar`, pero los cinco modos de `documentar` escriben. Sin procedimiento, el agente improvisa un `grep` que anda con el término exacto y falla cuando la pregunta usa otras palabras.
2. **La descripción de `documentar` habla de escribir.** Claude elige una skill por su descripción, y nada en el listado decía «usá la base para trabajar». Ampliar esa descripción para lectura la vuelve difusa en los dos casos.
3. **Las notas dicen qué son, no para qué sirven.** El `resumen` define el concepto; nada lleva de una tarea («tengo que poner un precio») a las notas que la resuelven, ni deja a la vista que una tarea no tiene nota.

## Qué cambia

- **Skill hermana `consultar`** en el plugin: ubicar el clon, leer la entrada raíz y la del tema, buscar por término, `aliases` y glosario en los dos idiomas, bajar por los enlaces, contestar con ruta, sección y estado (`borrador` o `vigente`), decir qué falta y ofrecer `volcar`. Si delega en un subagente, le pasa la ruta de la entrada, porque el subagente arranca sin el `CLAUDE.md` de la base.
- **Descripción con el caso de uso primero y «pushy»**, como recomienda Anthropic: el listado de Claude Code corta la descripción a 1536 caracteres y la carga en todos los turnos, y las skills tienden a dispararse de menos ([skills](https://code.claude.com/docs/en/skills), [skill-creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md)). Nombra las tareas de otros repos que la base puede apoyar y excluye los datos propios del repo y la escritura.
- **Sección de tareas en la entrada del tema** (`metodo.md`, «Para qué tarea», y `plantillas/tema.md`): tareas genéricas en voseo que apuntan a sus notas, sin nombres de empresas, con `estabilidad: semi`. El lector en frío prueba también una pregunta con forma de tarea.
- **Casos de disparo** en `plugins/documentar/evals/`: 10 pedidos que deben cargar `consultar` y 10 near-misses, el diseño de la skill-creator (los mejores negativos comparten palabras pero piden otra cosa), corridos con `claude plugin eval`.

## Lo que no se hizo

- **Un campo `sirve_para` en cada nota**: más de 400 notas que mantener sin evidencia de que ayude; la sección por tema logra lo mismo.
- **Embeddings o un servidor MCP de búsqueda**: con `aliases`, glosarios y entradas por capas, grep alcanza para una base de este tamaño. Se reconsidera si la evaluación muestra fallas por sinónimos.
- **La sección «Qué leer de la base» en el `AGENTS.md` de cada repo de trabajo** va en esos repos, no en la skill.
