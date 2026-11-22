---
name: consultar
description: Contesta y trabaja desde una base de conocimiento hecha con `documentar` (como `mtsdlf/conocimiento`), entrando por la entrada del tema, sus aliases y su glosario, y citando ruta y estado. Usar siempre que preguntan qué se sabe de algo, y también cuando una tarea en cualquier repo (una propuesta, un precio, un canal, un análisis de competencia, una decisión de producto o de diseño) puede apoyarse en lo que la organización ya sabe, aunque no lo pidan. No para datos propios del repo (qué incluye un plan, qué se acordó con un cliente) ni para escribir notas, que es `documentar`.
---

# Consultar

El modo de lectura de una base hecha con [`documentar`](../documentar/SKILL.md). Es el modo **Entender** que nombran los `CLAUDE.md` y `AGENTS.md` de la organización.

## Cuándo

- **Una pregunta sobre la base**: «¿qué sabemos de X?», «¿dónde está lo de Y?».
- **Una tarea en otro repo que la base puede mejorar**, aunque nadie la nombre: armar una propuesta o un deck, poner o explicar un precio, elegir un canal, mirar a la competencia, decidir algo de producto o de diseño. Primero leés la base y después hacés la tarea con eso.
- **No** para lo que es del repo de la sesión: qué incluye un plan, qué se acordó con un cliente, una cifra de la empresa. Eso está en ese repo y manda. La base aporta el concepto general, no los datos de una empresa.
- **No** para escribir: guardar algo, ampliar o corregir una nota es `documentar`.

## Cómo

1. **Ubicar el clon.** Buscá el repo de la base en `~/repos`, en cualquier subcarpeta (`find ~/repos -maxdepth 3 -type d -name conocimiento`); si aparecen varios, es el que tiene `CONVENCIONES.md` en la raíz y el remoto de la base (`git -C <dir> remote -v`). Si no está, clonala; si no se puede, leela por GitHub (`gh api` o la URL `raw`). Una URL `github.com/<org>/<base>/blob/main/<ruta>` se lee en el clon, en `<ruta>`.
2. **Leer las entradas.** El `CONVENCIONES.md` dice cuál es la entrada raíz (en `mtsdlf/conocimiento`, `conocimiento.md`). Leela, elegí el tema que toca y leé su entrada (`<Tema>/<tema>.md`). Si la entrada tiene una sección de tareas («Para qué tarea», con un título propio del tema), empezá por ahí: dice qué notas sirven para qué trabajo.
3. **Buscar.** `grep -ril` del término, sus sinónimos y su traducción al inglés en toda la base; el frontmatter `aliases` tiene los sinónimos de cada nota. Mirá también el glosario del tema (`<Tema>/Fundamentos/glosario-*.md`), que lleva de un término a su nota.
4. **Bajar por los enlaces**: de la entrada del tema a la de la vertical y de ahí al componente. Leé la nota entera, no solo la línea que coincide; el `resumen` dice si es la que buscás.
5. **Contestar con ruta y sección**: `Marketing/Propuesta/posicionamiento.md`, «Los cinco componentes, en este orden». Decí qué notas están en `borrador` (escritas por un agente, sin confirmar) y cuáles en `vigente`; lo de `borrador` se usa, pero se dice. Si una nota está `obsoleto`, seguí su `reemplazado_por`.
6. **Decir qué falta.** Si la base no lo cubre, decilo y decí qué es lo más cercano («no hay nota de análisis de competencia; lo más cercano son las alternativas competitivas de…»). Si la respuesta que armaste vale como nota, ofrecé guardarla con `documentar` en modo `volcar`.

En una tarea, la base se cita donde se usa («posiciono contra las alternativas competitivas, como dice `posicionamiento.md`») y lo propio de la empresa sale de su repo.

## Con un subagente

Si delegás la búsqueda en un subagente (Explore u otro), pasale la ruta absoluta del clon y de la entrada del tema, y la pregunta. El subagente arranca sin el `CLAUDE.md` de la base: sin la ruta, busca a ciegas. Pedile que devuelva rutas, secciones y el `estado` de cada nota.
