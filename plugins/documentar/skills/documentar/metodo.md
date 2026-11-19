# Método

Cómo se estructura, se escribe y se mantiene una base. Vale para un tema general, para los docs de un repo y para el saber de la organización. Para los docs de un repo con código, sumá [`sistemas.md`](sistemas.md).

## Capas

Un tema se documenta como se analiza un sistema: se lo descompone en capas de abstracción, de lo general a lo particular. La estructura sale del sujeto, no de una lista de tipos de pregunta.

| Capa | Qué es | Dónde vive | Cambia |
|---|---|---|---|
| **El todo** | Qué es el sujeto, qué problema resuelve, dónde termina y, sobre todo, cuáles son sus partes y cómo se conectan entre sí | La entrada del tema, `<Tema>/<tema>.md` | casi nunca |
| **Las verticales** | Las grandes partes en que el sujeto se divide | Una carpeta cada una, con su entrada `<Vertical>/<vertical>.md` | poco |
| **Los componentes** | Las piezas de cada vertical: conceptos, mecanismos, prácticas, decisiones | Una nota cada uno, dentro de su vertical | a veces |
| **Lo operativo** | Herramientas, plataformas, valores, cifras, comandos | Fichas fechadas en la carpeta de su vertical, enlazadas desde el componente que implementan | seguido |

Reglas para armar el árbol:

- **Las verticales son partes del sujeto, no temas de conversación.** Responden "¿de qué está hecho?" o "¿en qué etapas o subsistemas se divide?". Kubernetes se divide en plano de control, nodos, cargas de trabajo, red, almacenamiento y seguridad; un gecko leopardo, en biología, recinto, alimentación, salud, reproducción y conducta; el marketing, en mercado y cliente, propuesta, marca, canales, comunicación y medición. "Debates", "B2B" o "Escuelas" no son partes: son cortes transversales.
- **Usá la división del propio dominio.** Si el campo ya se clasifica a sí mismo (la filogenia, los objetos de una API, el índice canónico de un libro de texto), las verticales la siguen.
- **De cuatro a ocho verticales en un tema general.** Con menos, el todo no está descompuesto; con más, mezclaste niveles. Un sistema tiene las que tiene.
- **Un tema chico no se parte en carpetas.** Con menos de unas 12 notas, las verticales son secciones de la entrada del tema, cada una con sus componentes enlazados, y las notas quedan en la carpeta del tema. Cuando crece, cada sección pasa a ser una carpeta.
- **La profundidad la pone el sujeto.** Una vertical tiene subcarpetas solo si sus componentes tienen partes propias que se estudian por separado. No hay un número fijo de niveles, y dos verticales pueden tener profundidades distintas.
- **Lo transversal va a `Fundamentos/`**: historia, escuelas, fuentes y glosario del tema. No es una vertical, porque no es una parte del sujeto.
- **Cada cosa en un solo lugar.** Una nota vive en la vertical de la que es parte y se enlaza desde las otras. Si una nota parece de dos verticales, o es un concepto de arriba (va al todo) o el árbol está mal cortado.
- **Lo que cambia, abajo.** Los nombres de productos, versiones, precios y plataformas viven en la capa operativa. Las capas de arriba no los nombran: así la base no envejece cuando cambia una herramienta.

## Qué dice cada capa

Al escribir una nota de cualquier capa, estas son las preguntas que guían (no son títulos):

- ¿Qué es y para qué existe? ¿Dónde termina y en qué se diferencia de sus vecinos?
- ¿De qué está hecho? Eso enlaza a la capa de abajo.
- ¿Cómo funciona y cómo se conecta con sus hermanos? Eso enlaza a los lados.
- ¿Cómo se hace o se decide, y cómo falla?

Una nota contesta las que tienen contenido. La entrada de una vertical tiene que dejar entender la vertical sin abrir sus componentes; un componente tiene que poder leerse solo.

## La nota

- **Una nota, un sujeto.** Cada nota trata una cosa (un componente, una vertical, el todo) y la explica entera. Se parte cuando adentro hay un sujeto que se va a enlazar desde otros lados; no se parte por tamaño.
- **Tamaño**: lo que pida el sujeto. Una nota de 1200 palabras sobre una vertical está bien; una de 120 sobre un concepto que nadie va a enlazar se suma a su vecina. El lint avisa arriba de 1500.
- **Primera línea**: después del H1, una definición de una o dos oraciones que se entiende sola, igual al `resumen` (el lint lo avisa). En un ADR que ya existía no hace falta.
- **Títulos de sección**: dicen lo que dice la sección, con las palabras del tema. "Los cinco componentes", "Por qué crece por penetración", "Dónde choca con Sharp". Nunca títulos de formulario como "Por qué existe", "Cómo funciona", "No confundir con", "Para profundizar" o "Relaciones". Si un título serviría en cualquier otra nota, está mal.
- **Título de la nota**: el término que la gente usa, en singular. Si lo corriente es en inglés, va en inglés ("Churn"); el otro idioma va en `aliases`.
- **Archivo**: kebab-case ASCII. Las carpetas, con mayúscula inicial y guiones (`Mercado-y-cliente/`). La entrada de una carpeta se llama como ella en minúscula (`Mercado-y-cliente/mercado-y-cliente.md`), salvo en los docs de un repo, donde es `README.md`. Como los nombres de archivo son únicos en la base, una carpeta que se repite entre temas lleva el calificador en la entrada y no en la carpeta: `Fundamentos/fundamentos-de-marketing.md`.
- **Idioma**: el de las notas del tema; si no hay, el de la persona. Un tema va en un idioma.

## Enlaces

- **Markdown relativo**: `[texto](../Marca/capital-de-marca.md)`. Se lee en GitHub y en cualquier editor.
- **El enlace dice la relación**: "se calcula sobre una [cohorte](cohorte.md)", no "ver [cohorte](cohorte.md)".
- **Hacia abajo**: cada entrada enlaza todo lo que tiene adentro, con media línea de qué es. Una nota que ninguna entrada enlaza es huérfana.
- **Hacia los lados**: un componente enlaza a sus hermanos y a otras verticales en el cuerpo, donde la relación importa. Al final puede ir una lista corta "Ver también" solo con lo que no quedó enlazado en el texto.
- **Hacia afuera**: si existe una explicación canónica (un libro, la documentación oficial, un curso abierto), la nota da su versión corta y manda al recurso diciendo qué parte leer y en qué fijarse.

## Frontmatter

```yaml
---
resumen: >-          # 1-2 oraciones que se entienden solas; es la primera línea del cuerpo
  ...
estado: borrador     # borrador | vigente | obsoleto
estabilidad: estable # estable | semi | volatil
fuentes: []          # URLs, libros con capítulo, rutas de código
aliases: []          # opcional: sinónimos, siglas, el término en otro idioma
dueno:               # opcional: solo si no es el de CONVENCIONES.md
reemplazado_por:     # opcional: la ruta de la nota nueva, si está obsoleto
creado: 2026-11-19
revisado:            # cuando una persona la confirmó; vacío en borrador
---
```

- Lo que escribe un agente entra como `borrador` y pasa a `vigente`, con `revisado` de ese día, cuando una persona lo lee y lo confirma. Nunca se marca `vigente` sin esa confirmación.
- Las notas de bases anteriores pueden traer más campos (`tipo`, `area`, `parte_de`, `requiere`…). Se dejan; al tocar la nota, se pueden borrar.

## Lo volátil y las fichas

Una **ficha** (`estabilidad: volatil`) guarda lo que cambia: una tabla de herramientas, los valores de referencia, una plataforma, un comando. Lleva la fecha de la copia y la fuente viva, y enlaza al componente que implementa: si la herramienta muere, el componente queda. Idealmente es un enlace comentado a la fuente, no una copia.

**Un valor, un lugar**: cada cifra de referencia vive en una nota con su fuente; las demás la enlazan o la repiten igual.

## Fuentes

Cómo se buscan está en [`investigacion.md`](investigacion.md). En la nota:

- Los números, las fechas y las citas salen literales de una fuente que la nota cita.
- Lo de alto riesgo (salud, dinero, seguridad, ley) lleva dos fuentes independientes, o dice que hay una sola. Lo de salud aclara que no reemplaza a un profesional.
- Lo que no se leyó entero se dice ("según su resumen"). La inferencia propia se dice como inferencia.
- Lo que no tiene fuente se omite o queda visible: `> [!NOTE] Sin fuente todavía: <qué falta>.`
- Un libro o un curso no tiene nota propia: sus ideas se reparten en los componentes y el libro va en `fuentes`. La bibliografía del tema va en `Fundamentos/`.
- **Material de la persona**: lo que ya hace o escribió se contrasta con las fuentes en una sección propia al final de la nota ("En <lugar>"), para que la nota siga sirviendo a otro lector.
- **Texto de otra IA o de un chat**: se queda solo el contenido; las preguntas del asistente y los enlaces que no se pueden verificar se borran, y el resto se verifica como cualquier material.
- El material de un empleador se queda en sus herramientas; a la base va solo el concepto general. Los secretos nunca.

## Obsoleto y disputado

- **Disputado**: cada posición con su evidencia, bajo `> [!IMPORTANT]`. Si el debate es central a una vertical, tiene su propia nota dentro de esa vertical (no en una carpeta de debates).
- **Una afirmación que cambió** no se reescribe en silencio si importa como historia: `> [!WARNING] Obsoleto desde 2026-11: <qué cambió y dónde está lo vigente>.`
- **Una nota que ya no sirve** pasa a `obsoleto`, con `reemplazado_por` si hay otra, y se borra cuando nada la enlaza.
- **Una decisión** se escribe con la plantilla de nota, en este orden: el contexto, las alternativas con su evidencia, lo que se eligió (o que está abierta) y sus consecuencias. En los docs de un repo es un ADR. Una decisión tomada no se reescribe: se escribe otra y la vieja queda `obsoleto` con `reemplazado_por`. Si ninguna fuente registra el porqué, la nota lo dice.

## Frescura

| `estabilidad` | Se re-verifica cada | Típicamente |
|---|---|---|
| `estable` | 12 meses | el todo, las verticales, los conceptos |
| `semi` | 6 meses | prácticas, métricas, decisiones abiertas |
| `volatil` | 3 meses | fichas |

Re-verificar es leer la nota contra sus fuentes y actualizar `revisado`.

## Aprender

Si la base es para aprender, la entrada del tema lleva un orden de lectura: de arriba hacia abajo, y dentro de cada vertical, lo que hay que entender antes primero. Si hace falta más (ejercicios, práctica), va una nota `Fundamentos/ruta-de-<tema>.md` con pasos: el modelo mental, una predicción antes de ver la respuesta, un ejemplo resuelto, un caso modificado y uno para hacer solo, con las respuestas en `<details>`.

## Visuales

La entrada del tema lleva un diagrama Mermaid del todo: las verticales y cómo se conectan, con un verbo en cada flecha. Fuera de eso, un diagrama entra si muestra un mecanismo o un flujo que el texto solo no deja ver. Lo categórico va en una tabla.

## Prosa

1. **Lo principal primero**: el párrafo abre con su afirmación.
2. **Una idea por oración**, de unas 20 palabras; párrafos de dos a cuatro oraciones.
3. **Voz activa con sujeto visible**; lo impersonal, con "se".
4. **Verbos concretos** y **cifras, nombres y ejemplos** en lugar de adjetivos de importancia.
5. **Afirmar lo verificado y atribuir lo demás**: "según Sharp…".
6. **La nota habla del tema, no de sí misma**: "esta nota explica…" sobra.
7. **Formato según el contenido**: lista numerada para pasos, tabla cuando una estructura se repite tres o más veces. No conviertas cada párrafo en viñetas.
8. **Un término por concepto** en todo el tema.
9. **Registro**: impersonal en las notas, voseo en los pasos.
