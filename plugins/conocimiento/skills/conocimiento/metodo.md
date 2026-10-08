# Método para estructurar conocimiento

Cómo se parte, se nombra, se relaciona, se escribe y se mantiene una base de conocimiento: un
vault de Obsidian o los docs de un repo. Las fuentes de cada regla están al final.

La idea entera en cinco reglas:

1. **Una nota, una pregunta.** Cada nota responde una sola pregunta y se entiende sola.
2. **Lo estable separado de lo volátil.** El concepto se escribe una vez; los comandos, valores y
   nombres de tablas van aparte o se enlazan a su fuente.
3. **Una sola fuente de verdad.** Cada cosa se explica en un lugar y el resto enlaza.
4. **La estructura es una red con Mapas encima.** Las notas se relacionan entre sí; los Mapas y los
   Recorridos ordenan la red por Tema.
5. **Toda nota tiene dueño y fecha de revisión.** Lo que nadie revisa se marca o se borra.

## La nota

- **Tamaño**: una idea entera, de 150 a 400 palabras de cuerpo (sin frontmatter ni bloques de
  código; `revisar.py` avisa pasando 450). Se empieza con una nota amplia y se parte
  cuando acumula prerrequisitos propios o cuando una parte se enlaza sola desde otras notas. Si
  para escribirla hace falta un segundo `##` de otro asunto, son dos notas. Lo que no llega a unas
  80 palabras propias se suma a la nota vecina.
- **Prueba de la nota**: ¿se puede enlazar desde otro lado sin arrastrar contexto que no hace
  falta? Si no, se parte.
- **Primera línea**: después del H1, una definición de una o dos oraciones que se entiende sola.
  Es la misma que `resumen`, a propósito: el frontmatter la sirve a los agentes y la primera línea
  a quien lee. Se cambian juntas.
- **Autocontenida**: nombra su sujeto, su período y su unidad, y enlaza a la nota que explica lo
  que da por sabido.
- **Título**: el H1 es el término que la gente usa al hablar y al buscar, en singular
  ("Cohorte", no "Cohortes"). Si el término en inglés es el de uso corriente, va en inglés
  ("Churn"); si no, en el idioma de la nota. Un título mezcla idiomas solo si así se dice
  ("Tasa de churn"). El otro idioma y los sinónimos van a `aliases`. Si dos cosas se llaman igual,
  se distinguen con un calificador: "Partición (Spark)".
- **Archivo**: el nombre es el ID, en kebab-case con letras ASCII: `analisis-de-cohortes.md`. Es
  único en toda la base. El título se puede cambiar; el archivo casi nunca,
  porque rompería los enlaces.
- **Idioma**: español o inglés, a elección de quien escribe; si no dice, el de las notas que ya
  hay en el Tema, y si no hay, español. Un Tema entero va en un idioma; un material que se usa tal
  cual con otra audiencia (un cuestionario, una rúbrica) puede quedar en su idioma original como
  `ficha`. Las claves y valores del frontmatter quedan siempre como están acá (son el esquema que
  lee `revisar.py`); en inglés se traducen los títulos de sección de la plantilla.

## Prosa

Cada regla sale de una guía de estilo; ver Fuentes.

1. **Lo principal primero**: la oración arranca con su palabra clave y el párrafo con su
   afirmación (Microsoft, Google).
2. **Una idea por oración**, unas 20 palabras de promedio; **una idea por párrafo**, de dos a
   cuatro oraciones (plainlanguage.gov, guías de lenguaje claro).
3. **Voz activa con sujeto visible**; lo impersonal, con "se" ("se calcula") (Google, FundéuRAE).
4. **La condición antes de la instrucción**: "Si la cohorte es semanal, agrupá por semana" (Google).
5. **Verbos concretos**: "decidir" en lugar de "tomar la decisión de", "usar" en lugar de
   "utilizar", "es" en lugar de "sirve como" (Google).
6. **Cifras, nombres y ejemplos** en lugar de adjetivos de importancia: en vez de "clave",
   "crucial" o "robusto", el dato que lo demuestra.
7. **Afirmar lo verificado y atribuir lo demás**: "según Amplitude…"; lo que es inferencia propia
   se dice como inferencia.
8. **Empezar y terminar en el contenido**: la nota abre con la definición y cierra con su última
   idea o sus relaciones.
9. **Formato según la forma del contenido**: lista numerada para pasos, viñetas para elementos
   paralelos, tabla cuando una estructura se repite tres o más veces, negrita para el término que
   se define y para las etiquetas de la plantilla (Google).
10. **Un término por concepto** en todo el Tema; los sinónimos viven en `aliases` (Google,
    Microsoft).
11. **Gerundio solo para acciones simultáneas** (FundéuRAE).
12. **Títulos de sección con mayúscula solo inicial** y sin punto final (FundéuRAE).
13. **Registro**: impersonal en `concepto`, `metrica`, `ficha`, `decision`, `mapa` y `recorrido`;
    voseo en los pasos de `como-hacer` ("filtrá", "agrupá"). En inglés, impersonal y "you" en los
    pasos.
14. **Prueba del lector en frío**: antes de dar una nota por terminada, un subagente que recibe
    solo esa nota responde la pregunta de su título y dos o tres preguntas que un lector haría.
    Quien escribe la nota compara las respuestas con las fuentes; si alguna falla, se reescribe
    hasta que acierte (Anthropic, `doc-coauthoring`). La prueba no ve errores de hecho: una nota
    puede ser clara y estar equivocada. Por eso va después de cotejar la nota con sus fuentes
    (`SKILL.md`, Verificar).

## Tipos

Cada nota tiene un `tipo`. Hay una plantilla por tipo en `plantillas/`.

| `tipo` | Responde | Estabilidad típica |
|---|---|---|
| `concepto` | ¿Qué es X y por qué importa? | estable |
| `metrica` | ¿Cómo se define y se calcula X? | semi |
| `como-hacer` | ¿Cómo logro Y? (pasos) | semi |
| `ficha` | ¿Cuál es el dato, la tabla o el instrumento exacto de X? | volátil, o estable si no cambia |
| `decision` | ¿Por qué elegimos X? | estable, no se revisa |
| `mapa` | ¿Qué hay sobre este Tema? | semi |
| `recorrido` | ¿En qué orden aprendo este Tema? | semi |

- Un `concepto` guarda lo que no envejece; los detalles volátiles van a una `ficha` o a un enlace
  a donde viven (el código, el modelo de dbt, el dashboard).
- Una `ficha` idealmente es un enlace comentado a la fuente real. Si copia valores, va
  `estabilidad: volatil` con la fecha de la copia. Un instrumento fijo (un cuestionario, una
  rúbrica, una tabla de equivalencias de un libro) es `ficha` con `estabilidad: estable` y va
  entero, sin límite de tamaño.
- Una `decision` no se reescribe: si cambia, se escribe otra y la vieja pasa a `obsoleto` con
  `reemplazado_por`. Una que se propuso y no se adoptó queda en `borrador`.

## Frontmatter

```yaml
---
tipo: concepto            # obligatorio: ver Tipos
resumen: >-               # obligatorio: 1-2 oraciones autocontenidas, igual a la primera línea
  ...
estado: vigente           # obligatorio: borrador | vigente | obsoleto
estabilidad: estable      # obligatorio: estable | semi | volatil
dueno: ana                # obligatorio: persona o equipo responsable
revisado: 2026-10-03      # obligatorio si está vigente: cuándo una persona confirmó que está bien
creado: 2026-10-03
autoria: mixta            # humano | ia | mixta
idioma: es                # es | en; si falta, es
fuentes: []               # URLs o referencias de donde sale el contenido
aliases: []               # sinónimos, otros idiomas, siglas
parte_de: []              # IDs: solo si "todo X es, por definición, un Y" o X es parte de Y
requiere: []              # IDs: lo que hay que entender antes
relacionado: []           # IDs: vecinos que no están en la misma cadena de parte_de
reemplazado_por:          # ID: solo si estado es obsoleto
---
```

- Las relaciones van por ID (el nombre del archivo sin `.md`) para que funcionen en Obsidian y en
  GitHub, y se repiten en la sección Relaciones del cuerpo como enlaces clickeables.
- Lo que escribe un agente entra como `borrador`, sin `revisado`. Pasa a `vigente`, con
  `revisado` de ese día, cuando una persona lo lee y lo confirma. Así `revisado` siempre significa
  "una persona lo confirmó".
- `autoria: ia` cuando lo escribió un agente, aunque sea a partir de material propio o de
  otra IA; `mixta` cuando una persona lo editó; `humano` cuando lo escribió una persona.

## Relaciones

- **`parte_de`**: jerarquía. Pasa la prueba "todo X es, por definición, un Y" (es-un) o "X es una
  parte de Y". Una nota puede tener varios padres: la red no es un árbol, y no tiene ciclos.
- **`requiere`**: lo que hay que entender antes. Es la relación más valiosa: de ella salen los
  Recorridos. Un hijo `requiere` a su padre solo si de verdad hay que leerlo antes.
- **`relacionado`**: vecinos útiles fuera de la cadena de `parte_de`. Va en las dos notas, y cada
  una dice en su cuerpo por qué.
- **Enlace en el cuerpo**: todo enlace dice por qué está ("se calcula sobre una [[cohorte]]").
- **Sección Relaciones**: una línea por enlace, `Etiqueta: enlace — por qué`. Parte de, Requiere y
  Relacionado repiten el frontmatter; para el sentido inverso se usa la etiqueta que lo diga
  ("Casos", "La usa", "Base de", "Se mide con", "Detalla"). Si el padre también se requiere, va una sola línea:
  "Parte de y requiere".
- **Entre personas**: si varias personas comparten la base, `dueno` dice quién mantiene cada
  nota; cualquiera la lee, la enlaza y propone cambios. Los apuntes personales (los de un curso)
  quedan aparte y se citan en `fuentes`.

## Temas, Mapas y Recorridos

- **Tema**: una carpeta dentro de la raíz de la base (en un vault, p. ej. `Conocimiento/`; en un
  repo, `docs/`). Cada
  nota vive en el Tema principal y se enlaza desde los Mapas de los otros. Las carpetas son por
  asunto, no por tipo. Un Tema grande se parte en sub-Temas: sub-carpetas con su propio Mapa.
- **Mapa** (`tipo: mapa`): `<Tema>/<tema>.md`, en kebab-case, curado por una persona o un agente.
  Agrupa las notas del Tema con una línea cada una que dice qué responde y cuándo leerla, y
  enlaza los sub-Mapas. Todo Tema tiene su Mapa desde la primera nota.
- **Mapa raíz**: `conocimiento.md` en la raíz de la base (en un repo, `docs/indice.md`). Enlaza el Mapa de
  cada Tema; cada Mapa de Tema tiene `parte_de` a su Mapa padre. Si no existe, se crea al crear el
  primer Tema.
- **Recorrido** (`tipo: recorrido`): `<Tema>/recorrido-<lo-que-enseña>.md` (p. ej.
  `recorrido-analisis-de-cohortes.md`), un orden de lectura para
  aprender el Tema. Cada paso dice por qué va ahí; el orden sale de seguir `requiere` hacia atrás,
  y lo que no tiene prerrequisitos va donde primero hace falta. Un Recorrido por audiencia, con la
  audiencia en el `resumen`. Las fichas van al final, como consulta.
- Toda nota vigente está enlazada desde al menos un Mapa: si no, es huérfana.
- Los Mapas son listas de enlaces comentadas, no consultas (Dataview y similares): una consulta
  no dice por qué cada nota está ni en qué orden leerla, y la base no depende de plugins.

## Material que llega

- **Un libro o un curso**: va en `fuentes` de cada nota que lo usa. Sus ideas se reparten en
  conceptos con nombre propio; el libro no tiene nota, salvo que el libro mismo sea el tema.
- **Texto de otra IA o pegado de un chat**: se queda solo el contenido. Las preguntas del
  asistente, los pedidos y los enlaces que no se pueden verificar se borran. Se verifica contra
  fuentes como cualquier material.
- **Diagramas**: en Mermaid. Uno en otro formato (Graphviz, imagen) se redibuja en Mermaid al
  nivel de detalle que necesita la nota, o se borra si repite el texto.
- **Material de un empleador**: se queda en las herramientas del empleador, con un enlace. Lo que
  se aprendió en general (el concepto, no el diseño del cliente) sí va a la base.

## Frescura

| `estabilidad` | Se revisa cada | Qué contiene |
|---|---|---|
| `estable` | 12 meses | conceptos, el porqué, instrumentos fijos |
| `semi` | 6 meses | métricas, pasos, Mapas |
| `volatil` | 3 meses | fichas con valores copiados |

- Las `decision` no se revisan: se reemplazan.
- Revisar es leer la nota contra sus `fuentes` y actualizar `revisado`. La fecha de modificación
  del archivo no cuenta: cambiar una coma no es revisar.
- Lo que ya no sirve se borra. Si todavía hay quien lo enlaza, pasa a `obsoleto` con
  `reemplazado_por` y un aviso arriba, y se borra cuando nadie lo enlace.
- Al mover contenido de una nota a otra, se borra del origen y queda un enlace. El original que
  se traduce o se reemplaza entero va a una carpeta `Archivo/` y se cita en `fuentes`.
- Dos notas que afirman cosas incompatibles se resuelven en una sola fuente de verdad.
- `revisar.py` encuentra lo vencido, lo roto y lo huérfano; ver el modo `mantener` en `SKILL.md`.

## Destino

| Dónde vive | `destino` | Enlaces | Avisos |
|---|---|---|---|
| Vault de Obsidian (carpeta con `.obsidian/` arriba) | `obsidian` | `[[id]]`, `[[id\|texto]]` | cualquier callout `> [!tipo]` |
| Docs de un repo | `ambos` | `[texto](ruta/relativa.md)` | solo `NOTE`, `TIP`, `IMPORTANT`, `WARNING`, `CAUTION` |

`ambos` se lee igual en GitHub y en Obsidian. Lo que documenta un sistema va a los docs de su
repo, junto a lo que lo usa. Los secretos van a un gestor de contraseñas, nunca a una nota.

## Documentar un sistema

Cuando la base son los docs de un repo con código, el método es el mismo, con estas reglas más.

- **La estructura que ya tiene el repo manda.** Si hay ADRs, una `decision` es un ADR en su
  carpeta y con su numeración; un ADR existente solo suma el frontmatter mínimo (`tipo`,
  `resumen`, `estado`, `estabilidad`, `dueno`) y conserva su forma: su primera línea no tiene que
  repetir el `resumen`. Si hay un glosario del dominio (`CONTEXT.md` o
  similar), los términos se definen ahí y las notas lo enlazan.
- **Puertas y base.** El README de la raíz enruta a quien llega; el Mapa raíz es
  `docs/indice.md`, y el README lo enlaza. Los archivos fuera de `docs/` (README, glosario,
  README de subcarpetas) son puertas: no llevan frontmatter y enlazan a la base.
- **`CONVENCIONES.md` en la base** (`docs/CONVENCIONES.md`) dice lo propio del repo: dueños,
  carpetas, qué no es nota y los títulos que un test del repo parsea. Su bloque
  ```` ```yaml revisar ```` lo lee `revisar.py`: `ignorar: [carpetas]` y `palabras_max: N`. El Mapa de
  una carpeta especial (p. ej. `adr/`) es cualquier nota `tipo: mapa` en ella.
- **El tamaño es otro.** Un doc de sistema responde una pregunta grande ("¿cómo funciona?",
  "¿qué herramientas hay?"); se parte por pregunta, no por palabras. `palabras_max` lo ajusta.
- **El código es la fuente primaria.** `fuentes` cita rutas relativas a la raíz del repo
  (`src/pagos/cobro.py`, con `:línea` o el nombre de la función si ayuda), y solo los archivos
  cuyo cambio obliga a releer la nota: uno a tres. Una nota explica lo que el código no dice solo:
  qué problema resuelve, cómo se relacionan las partes, por qué es así.
- **Lo que sale del código se verifica con un test.** Listas de endpoints, flags, campos,
  variables de entorno o subcomandos, y valores que el lector necesita ver ("vence a los 15
  minutos"): se escriben en el doc y un test del repo verifica que coincidan con el código, o se
  generan.
- **Enlaces, no rutas.** Un doc que nombra a otro lo enlaza (`[referencia](referencia.md)`), no
  lo escribe entre backticks, para que `revisar.py` lo chequee.
- **El estado de una tarea va a su issue.** Lo pendiente o lo hecho con fecha no vive en un doc.
- **La doc cambia en el mismo PR que el código.** En CI corre `revisar.py docs --desde
  origin/main`: avisa `doc-sin-actualizar` cuando cambió una fuente y la nota no. `revisar.py`
  también avisa `fuente-cambiada` cuando un archivo citado tuvo commits después del `revisado`.
- **Los agentes la encuentran.** El `CLAUDE.md` o `AGENTS.md` del repo tiene una línea que
  apunta a `docs/indice.md`.

## Fuentes

- Estructura: *Every Page is Page One* (Mark Baker), DITA (descripción corta), Information Mapping (definición, ejemplo, contraejemplo), Diátaxis (como chequeo), SKOS (relaciones), evergreen notes de Andy Matuschak y Maps of Content.
- Frescura: docs-as-code (Write the Docs), *Software Engineering at Google* cap. 10, ADRs (Michael Nygard).
- Prosa: [Google developer documentation style guide](https://developers.google.com/style/highlights), [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/top-10-tips-style-voice), [plainlanguage.gov](https://www.plainlanguage.gov/guidelines/), [guía de comunicación clara de Madrid](https://www.madrid.es/UnidadesDescentralizadas/Calidad/LenguajeClaro/ComunicacionClara/Documentos/GuiaPracticaCClara.pdf), [FundéuRAE](https://www.fundeu.es).
- Prueba del lector en frío: [`doc-coauthoring` de Anthropic](https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring).
- Muletillas: [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).
- Contradicciones en el mantenimiento: [LLM Wiki de Andrej Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).
