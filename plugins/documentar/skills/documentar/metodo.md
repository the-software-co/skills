# Método

Cómo se parte una base de conocimiento, qué tipos de nota tiene, cómo se enlazan, cómo se escribe y cómo se mantiene. Vale para un vault de Obsidian, para los docs de un repo y para un tema nuevo. El porqué de cada regla está en el research (`docs/research/` del repo `the-software-co/skills`). Para los docs de un repo con código, sumá [`sistemas.md`](sistemas.md).

## Principios

1. **Una nota, una pregunta.** Cada nota responde una sola pregunta, entera, y se entiende sola.
2. **El tema se parte en áreas; el modo va adentro.** Cada nota está en un solo modo: explica, guía, decide o se consulta.
3. **El núcleo no nombra productos.** Un concepto estable no cita versiones, marcas, precios ni pantallas. Eso va a una `ficha` fechada que enlaza al concepto que implementa.
4. **Una sola fuente de verdad.** Cada cosa se explica en un lugar y el resto enlaza. Cada valor vive en una sola nota.
5. **Puente antes que copia.** Si afuera hay una explicación canónica, la nota da su propia definición y su modelo mental cortos y manda al recurso: cuál, qué parte y en qué fijarse.
6. **Relaciones con tipo**, declaradas en el frontmatter y con su porqué en el cuerpo.
7. **Lo disputado se escribe como disputa**, con cada posición y su evidencia.
8. **Las preguntas mandan.** En un tema nuevo, el alcance es la lista de preguntas aprobada, y una nota que no responde ninguna sobra.
9. **Completa, no rellena.** Un área sin contenido sustantivo no se crea, y un hueco sin fuente queda visible.
10. **Toda nota tiene dueño y fecha de revisión.** Lo que nadie revisa se marca o se borra.

## La nota

- **Tamaño**: una idea entera, de 150 a 450 palabras de cuerpo, sin contar frontmatter ni bloques de código. `revisar.py` avisa cuando pasa de 450. Si hace falta un segundo `##` sobre otro asunto, son dos notas. Lo que no llega a unas 80 palabras propias se suma a la nota vecina. Las `ficha` y los Mapas no tienen tope.
- **Prueba de la nota**: tiene que poder enlazarse desde otro lado sin arrastrar contexto que no hace falta. Si no se puede, se parte.
- **Primera línea**: después del H1 va una definición de una o dos oraciones que se entiende sola, igual al `resumen`. El frontmatter la sirve a los agentes y la primera línea a quien lee. Se cambian juntas.
- **Título**: el término que la gente usa al hablar y al buscar, en singular. Si lo corriente es el término en inglés, va en inglés ("Churn"). El otro idioma y los sinónimos van a `aliases`. Si dos cosas se llaman igual, se distinguen con un calificador: "Partición (Spark)".
- **Archivo**: el nombre es el id, en kebab-case con letras ASCII, único en toda la base. Un id genérico ("cola", "glosario") lleva calificador ("cola-del-gecko"). El título se puede cambiar; el archivo casi nunca, porque rompería los enlaces.
- **Idioma**: español o inglés. Si la persona no dice, se usa el de las notas del tema; si no hay notas, español. Un tema entero va en un idioma. Las claves del frontmatter quedan siempre como están acá.

## Áreas

En un tema nuevo, toda nota lleva un `area`. Las notas de una base anterior pueden no tenerla. Las áreas son un punto de partida: un tema usa las que tienen contenido.

| `area` | Responde | Estabilidad típica |
|---|---|---|
| `que-es` | ¿Qué es, para qué existe, dónde termina y en qué se diferencia de sus vecinos? | estable |
| `como-funciona` | ¿Cuál es el modelo mental, el mecanismo, el principio? | estable |
| `anatomia` | ¿De qué partes está hecho y cómo se clasifica? | estable o semi |
| `procesos` | ¿Cómo transcurre, se desarrolla o cambia en el tiempo? | estable o semi |
| `como-se-hace` | ¿Cómo se usa, se hace o se observa? | semi o volátil |
| `como-se-decide` | ¿Qué criterios, trade-offs, debates y escuelas hay para elegir? | semi |
| `como-falla` | ¿Cómo falla, cómo se diagnostica, qué se cree mal? | estable o semi |
| `historia` | ¿De dónde viene y por qué es así hoy? | estable |
| `ecosistema` | ¿Qué herramientas, versiones, actores y recursos hay hoy? | volátil |
| `referencia` | ¿Cuál es el dato, la tabla o el término exacto? | mixta |
| `ruta` | ¿En qué orden y con qué práctica se aprende? | semi |

- **Taxonomía propia**: si el dominio ya se clasifica a sí mismo (la filogenia en los animales, los objetos de una API), `anatomia` sigue esa clasificación y no una inventada.
- **Escuela**: si la persona eligió una escuela o un enfoque del campo, la base se escribe desde esa escuela, y lo que otras sostienen distinto va como disputa. Si no eligió, la base queda neutral y una nota de `como-se-decide` mapea las escuelas.
- **Historia como hilo**: además de su área, la historia abre el modelo mental de los conceptos umbral, en una o dos oraciones.

## Tipos de nota

| `tipo` | Para qué | Plantilla |
|---|---|---|
| `mapa` | La entrada a un tema: qué hay, por dónde entrar según a qué venís, los conceptos umbral | `mapa.md` |
| `concepto` | Qué es algo, cómo funciona, por qué es así | `concepto.md` |
| `metrica` | Cómo se define y se calcula algo | `metrica.md` |
| `como-hacer` | Los pasos para lograr algo | `como-hacer.md` |
| `decision` | Cómo elegir entre alternativas, un debate abierto, o por qué se eligió algo | `decision.md` |
| `falla` | Un modo de falla, su diagnóstico, o una concepción errónea | `falla.md` |
| `ficha` | Lo volátil o tabular: versiones, herramientas, datos, glosario, un instrumento fijo | `ficha.md` |
| `ruta` | La secuencia para aprender un área o el tema. Las bases anteriores la llaman `recorrido` | `ruta.md` |

- Una `ficha` idealmente es un enlace comentado a la fuente real. Si copia valores, va `estabilidad: volatil` con la fecha de la copia. Un instrumento fijo (un cuestionario, una rúbrica) es `ficha` estable y va entero.
- Una `decision` sobre algo que se eligió no se reescribe: si cambia, se escribe otra y la vieja pasa a `obsoleto` con `reemplazado_por`. Una que se propuso y no se adoptó queda en `borrador`. Si ninguna fuente registra el porqué, la nota lo dice; no se deduce.

## Frontmatter

```yaml
---
tipo: concepto            # obligatorio: ver Tipos
area: como-funciona       # obligatorio en un tema con ALCANCE.md; el mapa no lleva
resumen: >-               # obligatorio: 1-2 oraciones que se entienden solas; es la primera línea del cuerpo
  ...
estado: borrador          # obligatorio: borrador | vigente | obsoleto
estabilidad: estable      # obligatorio: estable | semi | volatil
dueno: matias             # obligatorio: persona o equipo que la mantiene (ver CONVENCIONES.md)
umbral: false             # true en los 3 a 7 conceptos umbral de un tema
responde: [P2, P7]        # ids de preguntas del ALCANCE.md
es_un: []                 # jerarquía genérica: todo X es un Y
parte_de: []              # jerarquía partitiva: X es una parte de Y
instancia_de: []          # jerarquía instancial: X es un caso particular de Y
requiere: []              # lo que hay que entender antes
relacionado: []           # vecinos fuera de la jerarquía; va en las dos notas
fuentes: []               # URLs, referencias o rutas de código
aliases: []               # sinónimos, siglas, el término en otro idioma
creado: 2026-11-18
revisado:                 # cuando una persona confirmó la nota; vacío en borrador
autoria: ia               # ia | mixta | humano
idioma: es                # es | en; si falta, es
reemplazado_por:          # id, solo si estado es obsoleto
---
```

- **Ids**: las relaciones van por id. Un `README.md` con `tipo: mapa` es el Mapa de su carpeta. Un `README.md` sin frontmatter es una puerta de entrada y no es nota.
- **`revisado`** significa que una persona la confirmó. Lo que escribe un agente entra como `borrador` y pasa a `vigente`, con `revisado` de ese día, cuando una persona lo lee y lo confirma.
- **`autoria`**: `ia` si la escribió un agente, aunque sea a partir de material propio; `mixta` si una persona la editó; `humano` si la escribió una persona. Confirmar no es editar.
- **`parte_de` en las bases anteriores**: antes cubría también "es un". Al tocar una nota vieja, se pasa a `es_un` lo que corresponde.

## Relaciones

- **Jerarquía con subtipo**: `es_un` (lagarto → reptil), `parte_de` (escama → piel), `instancia_de` (Komodo → varánido). Una nota puede tener varios padres; la red no tiene ciclos.
- **`requiere`**: lo que hay que entender antes. Es la relación más valiosa: de ella salen las rutas. No es jerarquía: un hijo requiere a su padre solo si de verdad hay que leerlo antes. Sin ciclos, y sin aristas que ya se deducen por otro camino.
- **`relacionado`**: asociación entre notas que no están en la misma cadena jerárquica. Un par jerárquico no puede estar también relacionado. Va en las dos notas, y cada una dice en su cuerpo por qué.
- **En el cuerpo**: cada enlace dice qué relación expresa: "se calcula sobre una [[cohorte]]", no "ver [[cohorte]]".
- **Sección Relaciones** al final: una línea por relación del frontmatter, con la forma `Etiqueta: enlace — por qué`. Para el sentido inverso se usa la etiqueta que lo diga: "Casos", "La usa", "Base de", "Se mide con", "Implementa".

## Temas, Mapas y Rutas

- **Tema**: una carpeta por asunto, no por tipo. Cada nota vive en su tema principal y se enlaza desde los Mapas de los otros. Un tema grande se parte en sub-temas: sub-carpetas con su propio Mapa.
- **Mapa** (`tipo: mapa`): uno por carpeta. Según la base, es `<Tema>/<tema>.md` (un vault) o `README.md` (los docs de un repo o un tema sin convención). Agrupa las notas con una línea cada una que dice qué responde y cuándo leerla, enlaza los sub-Mapas y tiene `parte_de` hacia su Mapa padre. Es una lista comentada, nunca una consulta automática (como Dataview).
- **Mapa raíz**: `conocimiento.md` en un vault, `docs/indice.md` en un repo. Enlaza el Mapa de cada tema.
- **Ruta** (`tipo: ruta`): un orden para aprender un tema, para una audiencia. Ver "Ruta de aprendizaje".
- Toda nota que no está `obsoleto` está enlazada desde al menos un Mapa o una Ruta; si no, es huérfana.

## Núcleo y periferia

- **Núcleo**: las notas `estable` de `que-es`, `como-funciona`, `anatomia`, `procesos`, `historia` y `como-falla`. Su título y su `resumen` no nombran nada de la lista `volatiles` del `ALCANCE.md`, ni versiones ni precios. El lint lo chequea.
- **Periferia**: `ficha`, `ecosistema` y lo `volatil`. Cada ficha enlaza al concepto que implementa: si la herramienta muere, el concepto queda.
- **Puente**: la sección "Para profundizar" recomienda un recurso, como mucho dos alternativas, y dice qué parte usar, en qué fijarse y en qué difiere de la nota. Un recurso entra si es exacto, se puede usar por partes, es estable (documentación oficial, un libro, un curso abierto mantenido) y, si existe, está en el idioma de la base. Lo volátil se enlaza a su fuente viva en vez de copiarlo.

## Valores, términos y material propio

- **Un valor, un lugar.** Los números de referencia (temperaturas, dosis, tamaños, frecuencias) viven en la ficha de `referencia`, con su fuente y sus desacuerdos. Una nota que necesita un valor lo enlaza o lo repite con la misma cifra y la misma fuente. Dos notas no dan valores distintos sin decir por qué.
- **Jerga en el glosario.** Si el tema tiene términos técnicos, un glosario (`ficha` de `referencia`) los define en una línea y enlaza la nota que los desarrolla. El Mapa enlaza el glosario.
- **Material de la persona.** Lo que la persona ya hace o escribió se contrasta con las fuentes en una sección propia al final de la nota ("En <lugar>"), separada del contenido general, para que la nota siga sirviendo a otro lector.

## Material que llega

- **Un libro o un curso**: va en `fuentes` de cada nota que lo usa. Sus ideas se reparten en conceptos con nombre propio. El libro no tiene nota propia, salvo que el libro mismo sea el tema.
- **Texto de otra IA o pegado de un chat**: se queda solo el contenido. Las preguntas del asistente, los pedidos y los enlaces que no se pueden verificar se borran. El resto se verifica contra fuentes, como cualquier material.
- **Diagramas**: en Mermaid. Uno en otro formato se redibuja en Mermaid o se borra si repite el texto.
- **Material de un empleador**: se queda en las herramientas del empleador, con un enlace. Lo que se aprendió en general (el concepto, no el diseño del cliente) sí va a la base.
- **Secretos**: nunca van en una nota. Van al gestor de contraseñas.

## Obsoleto y disputado

- **Una afirmación que cambió** no se reescribe en silencio. Si importa como historia, queda con un aviso debajo y la nueva al lado:

  ```markdown
  > [!WARNING]
  > Obsoleto desde 2026-11: <qué cambió y dónde está lo vigente>.
  ```

- **Una afirmación disputada** lleva cada posición con su evidencia, bajo `> [!IMPORTANT]` con "Disputado:" al principio. Si el debate es central al tema, va a una nota `decision`.
- **Una nota que ya no sirve** pasa a `obsoleto` con `reemplazado_por`, y se borra cuando nada la enlaza.
- **Dos notas que afirman cosas incompatibles** se resuelven en una sola fuente de verdad.

## Frescura

| `estabilidad` | Se re-verifica cada | Qué contiene |
|---|---|---|
| `estable` | 12 meses | conceptos, el porqué, instrumentos fijos |
| `semi` | 6 meses | métricas, pasos, Mapas |
| `volatil` | 3 meses | fichas con valores copiados |

Re-verificar es leer la nota contra sus `fuentes` y actualizar `revisado`. Cambiar una coma no es re-verificar. Las `decision` sobre algo elegido no se revisan: se reemplazan.

## Fuentes

Cómo se buscan está en [`investigacion.md`](investigacion.md). Cómo se usan en una nota:

- **Números, fechas y citas textuales** salen literales de una fuente que la nota cita. Si el tema tiene `.investigacion/`, el lint avisa las cifras que no aparecen ahí.
- **Afirmaciones de alto riesgo** (salud, dinero, seguridad, legal) llevan dos fuentes independientes, o dicen que hay una sola. Lo de salud aclara una vez que no reemplaza a un profesional.
- **Lo que no se leyó entero se dice**: "según su resumen", "una sola fuente", "según criadores".
- **Concepciones erróneas** salen de estudios, de la documentación de quien hace la cosa o de la persona; si no, se marcan como inferencia. No se inventan.
- **Lo que no tiene fuente** se omite o queda como hueco visible: `> [!NOTE] Sin fuente todavía: <qué falta>.`

## Ruta de aprendizaje

Va si la intención incluye aprender; si no, el Mapa da un orden de lectura y nada más. Cada paso de la ruta sigue esta secuencia, adaptada al tema:

1. **Modelo mental**: el concepto, abierto con su historia en una oración. Enlaza a la nota y a su puente.
2. **Predecir**: una pregunta de "qué pasa si", antes de ver la respuesta.
3. **Ejemplo resuelto**: un caso completo, con los pasos rotulados.
4. **Ordenar**: los pasos del ejemplo desordenados, con un paso distractor que encarna un error común.
5. **Modificar**: el mismo caso con un cambio.
6. **Hacerlo solo**: un caso nuevo, sin ayuda.
7. **Cierre**: qué se aprendió, en tres líneas, y qué sigue.

El orden de los pasos sale de seguir `requiere` hacia atrás. En un tema que no es un procedimiento (un animal, una disciplina), predecir y hacer se vuelven identificar, explicar o predecir un comportamiento. Las respuestas van en `<details>`.

## Visuales

Un diagrama entra si muestra un mecanismo, un flujo o una jerarquía, y si sin el texto la forma sola ya comunica algo. Lo categórico va en una tabla. Los diagramas van en Mermaid, con un verbo en cada flecha y una afirmación por diagrama. El Mapa de un tema nuevo lleva el mapa de los conceptos umbral.

## Destino

| Dónde vive | Enlaces | Avisos |
|---|---|---|
| Vault de Obsidian | `[[id]]`, `[[id\|texto]]` | cualquier callout `> [!tipo]` |
| Docs de un repo | `[texto](ruta/relativa.md)` | solo `NOTE`, `TIP`, `IMPORTANT`, `WARNING`, `CAUTION` |

Una base es un vault si tiene `.obsidian/` arriba o si su `CONVENCIONES.md` lo dice. Las plantillas traen enlaces Markdown relativos: en un vault, pasalos a `[[id]]` o `[[id|texto]]`. Los enlaces relativos de Markdown se leen igual en GitHub y en Obsidian.

## Prosa

1. **Lo principal primero**: la oración arranca con su palabra clave y el párrafo con su afirmación.
2. **Una idea por oración**, de unas 20 palabras en promedio. **Una idea por párrafo**, de dos a cuatro oraciones.
3. **Voz activa con sujeto visible.** Lo impersonal va con "se": "se calcula".
4. **La condición antes de la instrucción**: "Si la cohorte es semanal, agrupá por semana".
5. **Verbos concretos**: "decidir" y no "tomar la decisión de"; "usar" y no "utilizar".
6. **Cifras, nombres y ejemplos** en lugar de adjetivos de importancia. El lint avisa las muletillas.
7. **Afirmar lo verificado y atribuir lo demás**: "según Merck…". La inferencia propia se dice como inferencia.
8. **Empezar y terminar en el contenido.** La nota habla del tema, no de sí misma: "esta nota explica…" sobra.
9. **Formato según el contenido**: lista numerada para pasos, viñetas para elementos paralelos, tabla cuando una estructura se repite tres o más veces.
10. **Un término por concepto** en todo el tema. Los sinónimos viven en `aliases`.
11. **Títulos de sección** con mayúscula solo inicial y sin punto final.
12. **Registro**: impersonal en las notas, voseo en los pasos de `como-hacer` y de la ruta. En inglés, impersonal y "you" en los pasos.
