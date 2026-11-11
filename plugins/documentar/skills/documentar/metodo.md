# Método

Cómo se parte un tema, qué tipos de nota hay, cómo se enlazan, cómo se escribe y cómo se mantiene. El porqué de cada regla está en el research (`docs/research/skill-documentar.md` del repo `the-software-co/skills`).

## Principios

1. **El tema se parte en áreas; el modo va adentro.** Cada nota está en un solo modo: explica, guía, decide o se consulta.
2. **Una nota, un concepto entero.** Se entiende sola, nombra su contexto y enlaza lo que da por sabido. Su título es el término que la gente usa.
3. **El núcleo no nombra productos.** Un concepto estable no cita versiones, marcas, precios ni pantallas: eso va a una `ficha` fechada que enlaza al concepto que implementa.
4. **Puente antes que copia.** Si afuera hay una explicación canónica, la nota da su propia definición y modelo mental cortos y manda al recurso: cuál, qué parte y en qué fijarse.
5. **Relaciones con tipo**, declaradas en el frontmatter y con su porqué en el cuerpo.
6. **Lo disputado se escribe como disputa**, con las dos posiciones y su evidencia.
7. **Las preguntas mandan.** El alcance es la lista de preguntas aprobada; una nota que no responde ninguna sobra.
8. **Completa, no rellena.** Un área sin contenido sustantivo no se crea; un hueco sin fuente queda visible.
9. **Umbral y errores primero.** De 3 a 7 conceptos umbral por tema, con sus concepciones erróneas.
10. **Aprender exige hacer.** La ruta tiene práctica, no solo lectura.

## Áreas

Toda nota lleva un `area`. Las áreas son un punto de partida: un tema usa las que tienen contenido.

| `area` | Responde | Estabilidad típica |
|---|---|---|
| `que-es` | ¿Qué es, para qué existe, dónde termina y en qué se diferencia de sus vecinos? | estable |
| `como-funciona` | ¿Cuál es el modelo mental, el mecanismo, el principio? | estable |
| `anatomia` | ¿De qué partes está hecho y cómo se clasifica? | estable o semi |
| `procesos` | ¿Cómo transcurre, se desarrolla o cambia en el tiempo? | estable o semi |
| `como-se-hace` | ¿Cómo se usa, se hace o se observa? | semi o volátil |
| `como-se-decide` | ¿Qué criterios, trade-offs y debates hay para elegir? | semi |
| `como-falla` | ¿Cómo falla, cómo se diagnostica, qué se cree mal? | estable o semi |
| `historia` | ¿De dónde viene y por qué es así hoy? | estable |
| `ecosistema` | ¿Qué herramientas, versiones, actores y recursos hay hoy? | volátil |
| `referencia` | ¿Cuál es el dato, la tabla o el término exacto? | mixta |
| `ruta` | ¿En qué orden y con qué práctica se aprende? | semi |

- **Taxonomía propia**: si el dominio ya se clasifica a sí mismo (la filogenia en animales, los objetos de una API), `anatomia` sigue esa clasificación y no una inventada.
- **Historia como hilo**: además de su área, la historia abre el modelo mental de los conceptos umbral, en una o dos oraciones.
- **Sub-temas**: un tema grande se parte en sub-carpetas, cada una con su `README.md` (Mapa) y su `ALCANCE.md`. Cada sub-tema usa las mismas áreas.

## Tipos de nota

| `tipo` | Para qué | Plantilla |
|---|---|---|
| `mapa` | La entrada al tema: qué hay, por dónde entrar según a qué venís, los conceptos umbral | `mapa.md` (es el `README.md`) |
| `concepto` | Qué es algo, cómo funciona, por qué es así | `concepto.md` |
| `como-hacer` | Los pasos para lograr algo | `como-hacer.md` |
| `decision` | Cómo elegir entre alternativas, o un debate abierto | `decision.md` |
| `falla` | Un modo de falla, su diagnóstico, o una concepción errónea | `falla.md` |
| `ficha` | Lo volátil o tabular: versiones, herramientas, datos, glosario | `ficha.md` |
| `ruta` | La secuencia para aprender un área o el tema | `ruta.md` |

## Frontmatter

```yaml
---
tipo: concepto            # ver Tipos
area: como-funciona       # ver Áreas; el mapa no lleva
resumen: >-               # 1-2 oraciones que se entienden solas; es también la primera línea del cuerpo
  ...
estabilidad: estable      # estable | semi | volatil
estado: borrador          # borrador | vigente | obsoleto
umbral: false             # true en los 3 a 7 conceptos umbral del tema
responde: [P2, P7]        # ids de preguntas del ALCANCE.md
es_un: []                 # jerarquía genérica: todo X es un Y
parte_de: []              # jerarquía partitiva: X es una parte de Y
instancia_de: []          # jerarquía instancial: X es un caso particular de Y
requiere: []              # lo que hay que entender antes
relacionado: []           # vecinos fuera de la jerarquía; va en las dos notas
fuentes: []               # URLs o referencias
aliases: []               # sinónimos, siglas, el término en otro idioma
creado: 2026-11-11
revisado:                 # cuando una persona confirmó la nota; vacío en borrador
autoria: ia               # ia | mixta | humano
reemplazado_por:          # id, solo si estado es obsoleto
---
```

- **Ids**: el nombre del archivo sin `.md`, en kebab-case ASCII, único en todo el tema con sus sub-temas. Las relaciones van por id.
- **`revisado`** significa que una persona la confirmó. Lo que escribe un agente entra en `borrador`.

## Relaciones

- **Jerarquía con subtipo**: `es_un` (lagarto → reptil), `parte_de` (escama → piel), `instancia_de` (Komodo → varánido). Sin ciclos.
- **`requiere`**: lo que hay que entender antes. Es la relación de la que sale la ruta. No es jerarquía: un hijo requiere a su padre solo si de verdad hay que leerlo antes. Sin ciclos, y sin aristas que ya se deducen por otro camino.
- **`relacionado`**: asociación entre notas que no están en la misma cadena jerárquica. Un par jerárquico no puede estar también relacionado. Va en las dos notas.
- **En el cuerpo**: enlaces Markdown relativos (`[cohorte](cohorte.md)`), y cada enlace dice qué relación expresa: "se calcula sobre una [cohorte](cohorte.md)", no "ver [cohorte](cohorte.md)".
- **Sección Relaciones** al final: una línea por relación del frontmatter, `Etiqueta: [nota](nota.md) — por qué`.

## Núcleo y periferia

- **Núcleo**: las notas `estable` de `que-es`, `como-funciona`, `anatomia`, `procesos`, `historia` y `como-falla`. Su título y su `resumen` no nombran nada de la lista `volatiles` del `ALCANCE.md`, ni números de versión ni precios. El lint lo chequea.
- **Periferia**: `ficha`, `ecosistema` y lo `volatil`. Cada ficha enlaza al concepto que implementa, para que si la herramienta muere el concepto quede.
- **Puente**: la sección "Para profundizar" de una nota recomienda un recurso, como mucho dos alternativas, y dice qué parte usar, en qué fijarse y en qué difiere de la nota. Un recurso entra si es exacto, se puede usar por partes, es estable (documentación oficial, un libro, un curso abierto mantenido) y, si hay, en el idioma de la base. Lo volátil se enlaza a su fuente viva en vez de copiarlo; si se copia un valor, va con la fecha de la copia.

## Obsoleto y disputado

- **Una afirmación que cambió** no se reescribe en silencio: si importa como historia, queda con un aviso debajo y la nueva al lado:

  ```markdown
  > [!WARNING]
  > Obsoleto desde 2026-11: <qué cambió y dónde está lo vigente>.
  ```

- **Una afirmación disputada** lleva las dos posiciones con su evidencia, bajo `> [!IMPORTANT]` con "Disputado:" al principio. Si el debate es central al tema, va a una nota `decision`.
- **Una nota que ya no sirve** pasa a `obsoleto` con `reemplazado_por`, y se borra cuando nada la enlaza.

## Frescura

| `estabilidad` | Se re-verifica cada |
|---|---|
| `estable` | 12 meses |
| `semi` | 6 meses |
| `volatil` | 3 meses |

Re-verificar es leer la nota contra sus `fuentes` y actualizar `revisado`. Cambiar una coma no es re-verificar.

## Fuentes

- **Puntaje**: 3·autoridad + 2·profundidad + 2·ejemplos + unicidad, y + 2·recencia solo en lo volátil (en lo estable, una fuente canónica vieja vale más que un blog nuevo).
- **Diversidad**: cinco textos que parafrasean el mismo documento son una fuente.
- **Afirmaciones de alto riesgo** (salud, dinero, seguridad, legal) llevan dos fuentes independientes.
- **Números, fechas y citas textuales** salen literales de una fuente que la nota cita.
- **Concepciones erróneas** salen de estudios, de la documentación de quien hace la cosa o de la persona; si no, se marcan como inferencia. No se inventan.
- **Lo que no tiene fuente** se omite o queda como hueco visible: `> [!NOTE] Sin fuente todavía: <qué falta>.`

## Ruta de aprendizaje

Va si la intención incluye aprender; si no, el Mapa da un orden de lectura y nada más. Cada paso de la ruta sigue esta secuencia, adaptada al tema:

1. **Modelo mental**: el concepto, abierto con su historia en una oración. Enlaza a la nota y a su puente.
2. **Predecir**: una pregunta de "qué pasa si" antes de ver la respuesta.
3. **Ejemplo resuelto**: un caso completo con los pasos rotulados.
4. **Ordenar**: los pasos del ejemplo desordenados, con un paso distractor que encarna un error común.
5. **Modificar**: el mismo caso con un cambio.
6. **Hacerlo solo**: un caso nuevo sin ayuda.
7. **Cierre**: qué se aprendió, en tres líneas, y qué sigue.

En un tema que no es un procedimiento (un animal, una disciplina), predecir y hacer se vuelven identificar, explicar o predecir un comportamiento. Las respuestas van en `<details>`.

## Visuales

Un diagrama entra si muestra un mecanismo, un flujo o una jerarquía, y si sin el texto la forma sola ya comunica algo. Lo categórico va en una tabla. Los diagramas van en Mermaid, cada flecha con un verbo y un diagrama por afirmación. El Mapa lleva el mapa de los conceptos umbral.

## Prosa

- Lo principal primero: la nota abre con su definición, el párrafo con su afirmación.
- Una idea por oración y por párrafo; voz activa.
- Cifras, nombres y ejemplos en vez de adjetivos de importancia.
- Un término por concepto en todo el tema; los sinónimos van a `aliases`.
- Registro impersonal en las notas; voseo en los pasos de `como-hacer` y de la ruta.
- La nota habla del tema, no de sí misma ("esta nota explica…" sobra).
