# Documentar un sistema

Cuando la base son los docs de un repo con código, el método es el mismo de [`metodo.md`](metodo.md), con estas reglas más.

- **Las capas son las del sistema.** El todo es qué hace el sistema y cómo se componen sus partes; las verticales son sus módulos, servicios o flujos principales; los componentes, las piezas de cada uno; lo operativo, la configuración, los comandos y los valores.
- **La estructura que ya tiene el repo manda.** Si hay ADRs, una decisión es un ADR en su carpeta y con su numeración. Un ADR existente solo suma el frontmatter mínimo (`resumen`, `estado`, `estabilidad`) y conserva su forma: su primera línea no tiene que repetir el `resumen`. Si hay un glosario del dominio (`CONTEXT.md`, `GLOSSARY.md` o similar), los términos se definen ahí y las notas lo enlazan.
- **Puertas y base.** El README de la raíz enruta a quien llega. La entrada raíz es `docs/indice.md`, y el README la enlaza. La entrada de cada carpeta de `docs/` es su `README.md`. Los archivos fuera de `docs/` (el README de la raíz, el glosario) son puertas: no llevan frontmatter y enlazan a la base.
- **`CONVENCIONES.md` en la base** (`docs/CONVENCIONES.md`) dice lo propio del repo: los dueños, las carpetas, qué no es nota y los títulos que un test del repo parsea. `revisar.py` lee su bloque ```` ```yaml revisar ````, con `ignorar: [carpetas]` y `palabras_max: N`.
- **El tamaño es otro.** Un doc de sistema responde una pregunta grande ("¿cómo funciona?", "¿qué herramientas hay?"). Se parte por pregunta, no por palabras, y `palabras_max` ajusta el aviso.
- **El código es la fuente primaria.** `fuentes` cita rutas relativas a la raíz del repo (`src/pagos/cobro.py`, con `:línea` o el nombre de la función si ayuda). Solo van los archivos cuyo cambio obliga a releer la nota, de uno a tres. Una nota explica lo que el código no dice: qué problema resuelve, cómo se relacionan las partes y por qué es así.
- **Lo que sale del código se verifica con un test.** Las listas de endpoints, flags, campos, variables de entorno o subcomandos, y los valores que el lector necesita ver ("vence a los 15 minutos"), se escriben en el doc y un test del repo verifica que coincidan con el código. La otra opción es generarlos.
- **Enlaces, no rutas.** Un doc que nombra a otro lo enlaza (`[referencia](referencia.md)`). No lo escribe entre backticks, para que `revisar.py` lo pueda chequear.
- **El estado de una tarea va a su issue.** Lo pendiente o lo hecho con fecha no vive en un doc.
- **La doc cambia en el mismo PR que el código.** En CI corre `python3 <revisar.py> docs --desde origin/main`, con el `revisar.py` de esta skill copiado al repo o bajado de `the-software-co/skills` en un commit fijo, que avisa `doc-sin-actualizar` cuando cambió una fuente y la nota no. Además, `revisar.py` avisa `fuente-cambiada` cuando un archivo citado tuvo commits después del `revisado`.
- **Los agentes la encuentran.** El `CLAUDE.md` o el `AGENTS.md` del repo tiene una línea que apunta a `docs/indice.md`.

## Cómo cambian los modos en un sistema

- **`nuevo`**: el contexto es el repo mismo (su README, su código, sus issues). El mensaje de alineación propone el árbol a partir de los módulos y pregunta, si no se deduce, para quién es la doc (quien opera, quien entra al equipo, quien decide). El `ALCANCE.md` es opcional si `CONVENCIONES.md` ya fija la audiencia.
- **Investigar**: los ángulos son las verticales del sistema. Cada subagente explora el código y devuelve las afirmaciones con `ruta:línea`, además de lo que dicen las issues, los ADR y los PR que explican el porqué. La web entra solo para lo que el sistema usa de afuera (la documentación de una dependencia, una especificación).
- **Cotejo con fuentes**: la fuente es el código. Cada afirmación sobre lo que hace el sistema se coteja contra el archivo citado, en el commit actual.
- **`mantener`**: arrancá por `--desde origin/main` y por `fuente-cambiada`. El diff de cada fuente desde el `revisado` de la nota dice qué releer.
