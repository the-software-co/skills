# Documentar un sistema

Cuando la base son los docs de un repo con código, el método es el mismo de [`metodo.md`](metodo.md), con estas reglas más.

- **La estructura que ya tiene el repo manda.** Si hay ADRs, una `decision` es un ADR en su carpeta y con su numeración. Un ADR existente solo suma el frontmatter mínimo (`tipo`, `resumen`, `estado`, `estabilidad`, `dueno`) y conserva su forma: su primera línea no tiene que repetir el `resumen`. Si hay un glosario del dominio (`CONTEXT.md`, `GLOSSARY.md` o similar), los términos se definen ahí y las notas lo enlazan.
- **Puertas y base.** El README de la raíz enruta a quien llega. El Mapa raíz es `docs/indice.md`, y el README lo enlaza. Los archivos fuera de `docs/` (el README, el glosario, los README de subcarpetas) son puertas: no llevan frontmatter y enlazan a la base.
- **`CONVENCIONES.md` en la base** (`docs/CONVENCIONES.md`) dice lo propio del repo: los dueños, las carpetas, qué no es nota y los títulos que un test del repo parsea. `revisar.py` lee su bloque ```` ```yaml revisar ````, con `ignorar: [carpetas]` y `palabras_max: N`. El Mapa de una carpeta especial (por ejemplo `adr/`) es cualquier nota `tipo: mapa` que esté en ella.
- **El tamaño es otro.** Un doc de sistema responde una pregunta grande ("¿cómo funciona?", "¿qué herramientas hay?"). Se parte por pregunta, no por palabras, y `palabras_max` ajusta el tope.
- **El código es la fuente primaria.** `fuentes` cita rutas relativas a la raíz del repo (`src/pagos/cobro.py`, con `:línea` o el nombre de la función si ayuda). Solo van los archivos cuyo cambio obliga a releer la nota, de uno a tres. Una nota explica lo que el código no dice: qué problema resuelve, cómo se relacionan las partes y por qué es así.
- **Lo que sale del código se verifica con un test.** Las listas de endpoints, flags, campos, variables de entorno o subcomandos, y los valores que el lector necesita ver ("vence a los 15 minutos"), se escriben en el doc y un test del repo verifica que coincidan con el código. La otra opción es generarlos.
- **Enlaces, no rutas.** Un doc que nombra a otro lo enlaza (`[referencia](referencia.md)`). No lo escribe entre backticks, para que `revisar.py` lo pueda chequear.
- **El estado de una tarea va a su issue.** Lo pendiente o lo hecho con fecha no vive en un doc.
- **La doc cambia en el mismo PR que el código.** En CI corre `revisar.py docs --desde origin/main`, que avisa `doc-sin-actualizar` cuando cambió una fuente y la nota no. Además, `revisar.py` avisa `fuente-cambiada` cuando un archivo citado tuvo commits después del `revisado`.
- **Los agentes la encuentran.** El `CLAUDE.md` o el `AGENTS.md` del repo tiene una línea que apunta a `docs/indice.md`.
