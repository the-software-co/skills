# Una skill que documenta cualquier tema: qué dicen los libros, la Academia y el mercado

Research para alinear la definición de una skill que, dado un tema ("Excel", "Kubernetes", "lagartos"), produce una base de conocimiento en Markdown en git. Los requisitos son cuatro: que esté estructurada, que no quede obsoleta rápido, que sea de alto nivel pero cubra el tema entero por subcategorías, y que se pueda recorrer concepto a concepto por enlaces. Todavía no es un diseño. Fecha: 2026-11-11.

Va aparte de la skill `conocimiento` de este repo, a propósito. Se investigó sin partir de ella, y solo al final se compara (ver "Qué cambia respecto de `conocimiento`").

## Resumen

- **El hueco del mercado es exactamente lo que se pide.** De las 17 skills leídas, ninguna arma desde cero la taxonomía de un tema arbitrario con un chequeo de cobertura. Las wikis del patrón Karpathy necesitan que el usuario les traiga las fuentes, y las skills de aprendizaje arman un curso por días que caduca. Tampoco hay ninguna que aísle lo volátil en pocas páginas fechadas ni que valide por script un grafo de conceptos con enlaces tipados.
- **La estructura tiene dos ejes que no se mezclan: el tema y el modo.** El tema se parte en áreas y el modo (aprender, hacer, consultar, entender, decidir) va dentro de cada área, nunca como cuatro árboles paralelos. Lo sostienen Diátaxis, DITA, Software Engineering at Google, Mark Baker, 4C/ID y el expertise reversal effect de Kalyuga.
- **Hay una lista de categorías genéricas que sirve igual para Excel que para lagartos.** Cinco tradiciones independientes llegan a casi los mismos ejes: las cuatro causas de Aristóteles, las cuatro preguntas de Tinbergen, los siete tipos de información de Horn, la dimensión del conocimiento de Bloom revisada y las facetas de Ranganathan. Esos ejes son qué es, cómo funciona, de qué está hecho, cómo transcurre, cómo se usa, cómo se decide, cómo falla, de dónde viene, su ecosistema, la referencia y la ruta para aprenderlo. Cuando el dominio tiene una taxonomía propia, como la filogenia en los lagartos, esa taxonomía reemplaza a la genérica (Hjørland).
- **Contra la obsolescencia, la palanca es dónde se pone cada afirmación, más que la fecha que lleva.** La Academia ya lo resolvió con una regla: el enunciado de una Competencia nombra lo que dura, y las herramientas del momento van en la Unidad. Llevado a documentación: un núcleo de conceptos estables que nunca cita una versión, y una periferia volátil (versiones, precios, interfaces, estadísticas) en pocas notas fechadas que enlazan al principio que implementan. El ADR 0011 de la Academia agrega otra palanca: no reescribir lo que afuera ya está mejor explicado, sino tender un puente hacia ese recurso.
- **Para enlazar concepto a concepto hacen falta relaciones con tipo.** SKOS e ISO 25964 separan la jerarquía (es-un, parte-de, instancia-de) de la asociación, y prohíben que un mismo par tenga las dos. Knowledge Space Theory y el grafo de Competencias de la Academia agregan `requiere`, que no es jerarquía y es la relación de la que salen las rutas de aprendizaje. Novak pide que cada enlace diga qué relación expresa ("se calcula sobre", "es un caso de").
- **Para que sirva para aprender, la base tiene que devolverle trabajo al lector.** Matuschak avisa que entender exige esfuerzo, y que una base escrita por otro se lo ahorra. La secuencia de 7 pasos de la Academia (modelo mental, predecir, ejemplo resuelto, Parsons, modificar, hacerlo solo, cierre) es la forma probada de devolvérselo. También hay que señalar los conceptos umbral (Meyer y Land) y las concepciones erróneas (Posner; Sadler).
- **La verificación se diseña antes que el contenido.** Las competency questions de Noy y McGuinness y las essential questions de Wiggins y McTighe fijan el alcance antes de escribir, y sirven de test al final. Es el mismo principio que el ADR 0008 de la Academia, donde los checks se escriben antes que la Unidad. El mercado aporta la ejecución: el lector en frío de `doc-coauthoring`, el `check_evidence.py` de Astro-Han y el `validate` de learn-something.
- **Hay que decidir cinco cosas antes de diseñar** (ver "Preguntas para alinear"). La más importante es si esto es una skill nueva o un modo nuevo de `conocimiento`, porque la mitad del método ya existe ahí.

## Qué trae la Academia

La Academia (`personal/academia`) es un método de enseñanza, no de documentación. Cinco de sus decisiones se trasladan casi directo.

| En la Academia | Qué dice | Llevado a la skill |
|---|---|---|
| Competencia (`GLOSSARY.md`) | "Su enunciado nombra lo que dura; las herramientas del momento van en la Unidad." Un linter (`grafo estilo`, Vale) rechaza productos, versiones y precios en un enunciado (C20 de la Spec de #50). | El título y la definición de un concepto no nombran productos ni versiones. Lo volátil va a notas de ecosistema o de referencia, fechadas. Un lint lo puede chequear con una lista cerrada por tema. |
| Grafo con `requiere` y `abarca` (#26, #40) | `requiere` es lo que hay que saber antes. `abarca` dice que aprobar algo avanzado repasa lo que contiene. El validador rechaza ciclos y avisa aristas redundantes. | `requiere` como relación de primera clase, distinta de la jerarquía, sin ciclos y con aviso de redundancia. `abarca` sirve para el repaso, pero es opcional en una base de consulta. |
| Secuencia de 7 pasos (#26; ficha de `primer-proyecto` en la Spec de #50) | Modelo mental (abre con el Hilo de historia) → predecir → ejemplo resuelto con pasos rotulados → Parsons → modificar → hacerlo solo → cierre explícito. | Es la estructura de la ruta de aprendizaje de cada área. En un tema no procedimental, como los lagartos, "predecir" y "hacer" se vuelven identificar, explicar o predecir conductas. |
| Hilo | Un tema que recorre varias Unidades sin ser Competencia, como la historia de IT. | La historia de un tema funciona como hilo: aparece en el modelo mental de cada área y tiene además su propia área. |
| ADR 0011: la Teoría recorre Recursos de afuera | Cuando afuera ya hay una buena explicación, no se escribe otra. La Teoría propia es corta y dice qué recurso usar, qué parte, en qué fijarse y en qué difiere de la práctica. Si ningún recurso pasa los criterios, se escribe el modelo mental propio y se anota "sin Recurso". | Esto ataca la obsolescencia y el costo a la vez. Cuando existe una fuente canónica (documentación oficial, un libro, un curso abierto), la nota es un puente hacia ella. Con un chequeo de links caídos y de textos que cambiaron. |

Hay otras tres lecciones que vienen de los research de la Academia:

- **El experto no ve lo que omite.** En los expertos que nadie interroga, se omite cerca del 73% de las decisiones (research de #212). La instrucción basada en análisis cognitivo de tareas rinde g = 0,87 (Tofel-Grehl y Feldon 2013, citado en el research de libros y papers). Cuando el tema es del usuario (su homelab, su biblioteca de DJ), la skill tiene que entrevistarlo sobre casos reales y no conformarse con lo que cuenta solo.
- **Los errores comunes no se inventan.** Salen de estudios sobre principiantes, de las preguntas al experto o de datos reales (ADR 0011). Coincide con la advertencia del research de libros: un LLM inventa concepciones erróneas plausibles pero que nadie documentó.
- **Un subagente no es un novato.** Aunque se le pida, contesta como experto, así que el lector en frío puede aprobar una nota que un novato no entendería (research de #212). Por eso la prueba tiene que obligar a citar el párrafo que responde la pregunta, no solo a responderla.

## Qué dicen los libros y los papers

### Tipologías de documentación

- **Diátaxis** distingue cuatro formas (tutorial, how-to, referencia, explicación) sobre dos ejes: acción o cognición, adquirir o aplicar. Para jerarquías complejas propone poner primero lo que ordena al usuario (el tema) y adentro las cuatro formas. Avisa que no hay que crear estructuras vacías ("Don't do that. It's horrible.") y que la meta es una documentación "complete, not finished". **Límite:** no dice cómo partir un dominio en temas.
- **DITA** tipa los topics por la pregunta que responden y define las relaciones en una `reltable` aparte del contenido. Eso permite ver dónde falta información relacionada. **Límite:** es una arquitectura técnica para documentar productos.
- **Information Mapping** (Horn) define siete tipos de información: estructura, concepto, procedimiento, proceso, clasificación, principio y hecho. Propone una matriz tema × tipo cuyos huecos son huecos de conocimiento. Horn aclara que el método sirve para material estable; para lo disputado creó los mapas de argumentos, con afirmaciones, refutaciones y relaciones de apoyo.
- **Every Page is Page One** (Baker) critica que concepto, tarea y referencia se degradaron a "tabla, procedimiento y todo lo demás", y que partir sin una teoría de cómo se rearma produce "Frankenbooks". Cada página tiene que establecer su contexto y enlazar mucho. **Límite:** sirve para consultar, no para ordenar un aprendizaje.
- **The Good Docs Project** y *Docs for Developers* tratan como tipos estándar a la resolución de problemas (troubleshooting) y al glosario.

### Organización del conocimiento

- **SKOS** (W3C): `broader` y `narrower` son inversas. `related` es simétrica y no transitiva, y no puede coincidir con una relación jerárquica (regla S27). `prefLabel` es el nombre y `altLabel` los sinónimos. Las notas `historyNote` y `changeNote` son el lugar natural de lo que cambia.
- **ISO 25964** (tesauros) parte la jerarquía en genérica (lagarto → reptil), partitiva (escama → piel) e instancial (Komodo → varánido). Mezclarlas es la causa clásica de jerarquías incoherentes.
- **Facetas** (Ranganathan, vía Hjørland): un solo principio de división por nivel, con clases mutuamente excluyentes. La crítica de Hjørland es que las facetas a priori no tienen base empírica, y que el esquema real de un dominio sale de sus propias teorías.
- **Ontology Development 101** (Noy y McGuinness): no hay una sola forma correcta de modelar un dominio. El alcance se fija con *competency questions*, que la base tiene que poder responder.
- **Zettelkasten** (Luhmann): identificadores fijos que no dependen de la ubicación, para reordenar sin romper enlaces, y un registro de palabras clave aparte del árbol.
- **Evergreen notes** (Matuschak): una nota trata una sola cosa, pero entera. El título funciona como una API. Los enlaces densos valen más que los tags. El límite para este caso es que Matuschak escribe para sí mismo, y entender exige esfuerzo propio.
- **Maps of Content** (Milo): los nodos intermedios son mapas con prosa, no carpetas.

### Contra la obsolescencia

- ***Software Engineering at Google*, cap. 10**:
  - "Documents without owners become stale." Cada documento lleva dueño y fecha de revisión en metadatos, con recordatorios automáticos.
  - Hay un documento canónico por tema y los duplicados se deprecan.
  - Un documento no mezcla tipos.
  - Lo obsoleto se borra o se marca, y dice a dónde ir.
  - La mayoría de la documentación responde "cómo" y descuida "quién, qué, cuándo, dónde y por qué".
- **Docs-as-code** (Write the Docs): texto plano en git, review y tests automáticos.
- **Estable contra volátil.** Horn separa material estable de material disputado. Arbesman habla de *mesofacts*, hechos que cambian ni muy rápido ni muy lento. El par "durable vs perishable knowledge" no tiene una fuente primaria: es una heurística de quienes practican.
- **Efecto Lindy** (Ord 2023): lo que lleva más tiempo vigente tiende a durar más, pero solo en algunas categorías. Sirve para decidir qué entra en el núcleo, no para fechar notas.
- **Principios antes que herramientas.** Ninguna fuente lo dice sola, pero convergen las *enduring understandings* de Wiggins y McTighe, la distinción entre conocimiento conceptual y factual de Krathwohl y la regla de la Competencia de la Academia.

### Ciencia del aprendizaje aplicada a un documento

| Fuente | Idea | Qué pide a la base |
|---|---|---|
| Meyer y Land 2003, conceptos umbral | Conceptos transformadores, integradores, difíciles de volver atrás y que suelen marcar fronteras entre subáreas. | Entre 3 y 7 por tema, destacados en el mapa, con notas más largas. El LLM los propone como hipótesis. |
| Novak y Cañas 2008, mapas conceptuales | La unidad es la proposición: concepto, frase de enlace, concepto. Un mapa esqueleto hecho por un experto sirve de andamio. | Los enlaces dicen la relación. El mapa de cada área se dibuja en Mermaid. |
| Ausubel 1960, organizadores previos | Se aprende anclando lo nuevo en lo que ya se sabe. | Cada nota abre conectando con lo previo y nombrando qué requiere. |
| Sweller; Kalyuga et al. 2003 | El ejemplo resuelto rinde más que resolver en novatos, y deja de rendir, o daña, en expertos. | La ruta de aprendizaje va separada de la referencia. |
| 4C/ID (van Merriënboer) | Las tareas completas son la columna vertebral. La información de apoyo es "la teoría" y la procedimental llega justo a tiempo. | La ruta se arma con tareas que crecen en dificultad y enlazan a la teoría y a los procedimientos. |
| Wiggins y McTighe, *Understanding by Design* | Primero los resultados y las preguntas esenciales, después la evidencia y al final el plan. | La skill fija las preguntas antes de escribir. |
| Bloom revisada (Krathwohl 2002) | Conocimiento factual, conceptual, procedimental (incluido Cc, el criterio de cuándo usar cada procedimiento) y metacognitivo. | Cc justifica un área "cómo se decide". El metacognitivo justifica "cómo estudiar este tema". |
| Knowledge Space Theory (Doignon y Falmagne) | Estados de conocimiento sobre una relación de prerrequisitos. La "frontera externa" es lo que el lector está listo para aprender. | `requiere` permite contestar "si ya sé X e Y, ¿qué sigue?". |
| PRIMM (Sentance et al. 2019); Parsons y Haden 2006 | Predecir antes de ver el resultado; ordenar pasos con un distractor que encarna un error típico. | Son los pasos 2 y 4 de la Academia, y entran en la ruta. |
| Posner et al. 1982; Sadler et al. 2013 | El cambio conceptual exige insatisfacción con la idea previa. Los docentes que conocían la concepción errónea lograron más que los que solo sabían la respuesta. | Cada concepto umbral lleva su concepción errónea, con fuente o marcada como inferencia. |

### Cómo partir un tema desconocido

Cinco tradiciones independientes proponen preguntas canónicas casi iguales: Aristóteles (las cuatro causas), Tinbergen (mecanismo, función, desarrollo, filogenia), Horn (siete tipos), Krathwohl (cuatro tipos de conocimiento) y Ranganathan (PMEST). La documentación técnica agrega dos: cómo falla y cómo se decide. La prueba de que la lista es genérica:

| Área | Excel | Kubernetes | Lagartos |
|---|---|---|---|
| Cómo funciona | motor de recálculo | bucle de reconciliación | termorregulación |
| Para qué existe | modelar cálculos en tablas | operar cargas de forma declarativa | su nicho ecológico |
| Cómo transcurre | ciclo de vida de un libro | ciclo de vida de un pod | del huevo al adulto |
| De dónde viene | VisiCalc → Lotus → Excel | Borg → Kubernetes | filogenia de Squamata |
| Cómo falla | errores de referencia | CrashLoopBackOff | enfermedades, errores de identificación |

## Qué hace el mercado

Se leyó el `SKILL.md` original de cada una, no resúmenes de agregadores. Las estrellas son de la API de GitHub del 2026-11-11.

### Qué propósito cubre cada una

| Propósito | Las que lo cubren bien |
|---|---|
| Aprender | socratic-tutor (Jane Street), learn-anything, learn-something, `teach` (Matt Pocock), tutorial (iannbing) |
| Consultar | Diátaxis (barlevalon), agent-sh/learn (para agentes), `reference/` de `teach`, Mintlify |
| Incorporarse a algo (onboarding) | Mintlify (base interna con dueño y onboarding), `walkthrough` de iannbing ("You inherit…") |
| Decidir | doc-coauthoring, notion-knowledge-capture (OpenAI), `walkthrough` (alternativas → veredicto), claude-obsidian |
| Operar (pasos, runbooks) | Diátaxis how-to, Mintlify (help center por problema) |
| Ver (visual) | visual-explainer, excalidraw-diagram, learn-something (tabla o Mermaid), iannbing (mapa de conceptos) |
| Mantener vigente | karpathy-llm-wiki (Astro-Han), llm-wiki (nvk), claude-obsidian, learn-anything |

### Lo que conviene tomar, por skill

| Skill | Qué tomar | Qué evitar |
|---|---|---|
| [doc-coauthoring](https://github.com/anthropics/skills/blob/main/skills/doc-coauthoring/SKILL.md) (Anthropic) | El lector en frío: predice de 5 a 10 preguntas de lector y se las da a un subagente sin contexto, y el ciclo se repite hasta que no aparecen huecos nuevos. También el orden "lo más incierto primero, el resumen al final". | Depende de que el usuario aporte el contexto; no escala a un tema sin experto. |
| [socratic-tutor](https://github.com/janestreet/agent_skills) (Jane Street, 5,5k★) | El tema partido en 4 a 10 subhabilidades, con un árbol de dos niveles si es amplio. La escala de 0 a 5. Preguntar primero si quiere una respuesta rápida o aprender en serio. | No guarda nada. |
| [learn-anything](https://github.com/vesperchinn/learn-anything-skill) | El mapa del dominio con pares que se confunden ("confusion pairs"), lo mínimo para arrancar, qué no aprender todavía y la regla 20-60-20. El semáforo de volatilidad (🟢 12 meses o más, 🟡 de 3 a 6, 🔴 de 1 a 4 semanas). Un pie por página con fuentes, riesgo de frescura y última verificación. "No Source, No Claim". | Un SKILL.md de unos 35 KB que mezcla la base con un curso por días que caduca. |
| [learn-something](https://github.com/adamaiken89/learn-something) | Un glosario canónico con columna "Avoid" y un grep que tiene que dar cero, igual que el de la Academia. Los prerrequisitos en YAML como DAG. La regla de cuándo va tabla (contenido categórico) y cuándo Mermaid (flujo o jerarquía), con `mmdc` validando el Mermaid. `Predict`, `Think` y `Spot the Mistake` dentro del texto. | El foco en quizzes y repaso espaciado; reglas de finanzas presentadas como genéricas. |
| [agent-sh/learn](https://github.com/agent-sh/learn) | Puntaje de fuentes: 3·autoridad + 2·recencia + 2·profundidad + 2·ejemplos + unicidad, con la aclaración de que en temas estables la recencia pesa menos. "Cinco blogs que parafrasean el mismo doc son una fuente." Un tope de tres rondas de búsqueda, declarando el hueco si no alcanza. Un índice con frases que disparan cada tema. | Una sola página por tema, sin subcategorías ni enlaces. |
| [skills-for-learning](https://github.com/iannbing/skills-for-learning) (iannbing) | Las controversias como página propia, cada una con crítica, contraargumento y postura tomada. Un quiz para expertos calibrado: un senior saca 7 u 8, un principiante 2 o 3. Un mapa de conceptos en la página raíz. | Solo sirve para temas de software y tiene un tope de 5 a 8 conceptos. |
| [documentation-system-skill](https://cdn.jsdelivr.net/npm/@barlevalon/documentation-system-skill@1.1.0/SKILL.md) (Diátaxis) | La brújula como clasificador y su advertencia: Diátaxis no garantiza exactitud ni utilidad, que se validan aparte. | Su regla contra el andamiaje especulativo choca con "cubrir todo el tema". |
| [Karpathy, LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | Fuentes crudas, wiki y esquema en capas separadas. `index.md` con una línea por página y `log.md` con prefijo que se puede buscar con grep. El lint: afirmaciones viejas, huérfanas, conceptos mencionados sin página. Las buenas respuestas se archivan. | Supone que el usuario trae las fuentes; no tiene una fase de descubrimiento. |
| [karpathy-llm-wiki](https://github.com/Astro-Han/karpathy-llm-wiki) (Astro-Han, 2,7k★) | "Status: Outdated" y "Status: Disputed" debajo de la afirmación, sin reescribir la historia. Actualizar en cascada por entidad y por alias. "No material" como resultado válido. Buscar a propósito la posición contraria. `check_evidence.py`: todo número, fecha o cita aparece literal en la fuente. Un lint con tres niveles: arreglos seguros, mecánicos y de juicio. | Un solo nivel de carpetas. |
| [llm-wiki](https://github.com/nvk/llm-wiki) (nvk, 1,5k★) | En el frontmatter, `volatility` (hot, warm o cold), `verified` (solo lo avanza una persona) y `confidence`. Verbos de relación con tipo: `depends-on`, `contradicts`, `supersedes`. Un enlace doble que sirve a Obsidian y a GitHub a la vez: `[[slug\|Nombre]] ([Nombre](ruta.md))`. Las fuentes las califica otro agente, no el que las buscó. | Está sobredimensionada: sesiones, adaptadores, iCloud. |
| [claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) (16,3k★) | Toda página nueva actualiza un índice o mapa en el mismo cambio. Dos fuentes independientes para afirmaciones de alto riesgo. No parafrasear solo para tener más páginas. Un contrato de investigación con presupuesto y condición de parada. | Transacciones con hash: el PR de git ya cumple ese rol. |
| [teach](https://github.com/mattpocock/skills) (Matt Pocock) | **La lección es efímera y la referencia es duradera**: "lessons will rarely be revisited – reference documents will be". "Fuera de alcance" como frontera explícita. Una página con dónde se aprende la práctica en comunidades reales. "Never trust your parametric knowledge." | Produce HTML. |
| [notion-knowledge-capture](https://github.com/openai/skills) (OpenAI) | Decidir el tipo de página antes de escribir. La decisión como tipo propio, con alternativas, razones y resultado. | Atada a Notion. |
| [Mintlify](https://github.com/mintlify/mintlify-claude-plugin) | La skill no confía en lo que recuerda: trae la guía en vivo y, si contradice al SKILL.md, gana la guía. "No invented details": lo que no tiene fuente va como hueco visible. Primero la navegación entera, después cada página una sola vez. Un artículo responde una pregunta, en el primer párrafo. `broken-links`. | Supone un sitio de documentación de producto. |
| [visual-explainer](https://github.com/nicobailon/visual-explainer) (11k★) | Una afirmación por figura. Dibujar el mecanismo, no el nombre. Cada flecha lleva un verbo. Títulos que afirman ("La caché evita ir a Postgres"). | Produce HTML. |
| [excalidraw-diagram](https://github.com/coleam00/excalidraw-diagram-skill) (5,2k★) | El test de isomorfismo: sin texto, ¿la forma sola comunica? El test educativo. Varios niveles de zoom. | Produce JSON de Excalidraw. |
| [humanizer](https://github.com/blader/humanizer) (68k★) | Como pasada final: chequea que no se perdió ningún hecho, nombre, número ni cita, y caza el patrón de escribir sobre el documento en lugar de sobre el tema. | — |

### Huecos que ninguna cubre

1. Armar desde cero la taxonomía de un tema arbitrario, con un chequeo de cobertura.
2. Separar por estructura el núcleo estable de la periferia volátil, en vez de marcar la volatilidad página por página.
3. Validar por script un grafo de conceptos: enlaces tipados, `requiere` sin ciclos, cada concepto con enlaces que entran y salen.
4. Correr el lector en frío sobre la base entera, navegando desde el índice, en vez de sobre un documento suelto.
5. Temas que no son de software: solo learn-anything los contempla, y desde el curso.
6. Una entrada por propósito: "si venís a aprender, empezá acá; si venís a decidir, acá".
7. Decidir en Markdown cuándo un diagrama se gana su lugar y validarlo.
8. Confusiones y controversias enlazadas desde los conceptos que involucran.

## Propuesta de definición, para discutir

Esto es lo que sale de juntar las tres fuentes. Lo que es consenso está marcado arriba. Lo que sigue combina ese consenso con inferencia propia.

### Principios

1. **Primero el tema, adentro el modo.** Las áreas parten el tema. Cada nota está en un solo modo y no mezcla tipos.
2. **Una nota, un concepto entero.** Se entiende sola, establece su contexto y su título funciona como una API.
3. **El núcleo no nombra productos.** Los conceptos y los mecanismos no citan versiones, precios ni interfaces. Eso va a notas de ecosistema o de referencia, fechadas, que enlazan al principio que implementan. Es la regla de la Competencia, y un lint la chequea.
4. **Un puente antes que una copia.** Si afuera hay una explicación canónica, la nota la recomienda, dice qué parte leer y en qué fijarse. Solo se escribe el modelo propio cuando no hay recurso.
5. **Relaciones con tipo.** Jerarquía con subtipo, asociación y `requiere` por separado, sin ciclos en `requiere` y sin que un mismo par tenga relación jerárquica y asociativa. Cada enlace del cuerpo dice qué relación expresa.
6. **Lo disputado se escribe como disputa.** Se presentan la afirmación, la contraria y la evidencia, con el estado `disputado` y nunca como un hecho.
7. **Las preguntas antes que el contenido.** Entre 10 y 20 preguntas de cobertura y las preguntas esenciales del tema se fijan y se aprueban antes de escribir. La base está terminada cuando las responde.
8. **Completa, no rellena.** Cada área se evalúa con la matriz tema × tipo, pero un área sin contenido sustantivo no se crea, y un hueco sin fuente queda visible.
9. **Umbral y errores primero.** Entre 3 y 7 conceptos umbral por tema, cada uno con sus concepciones erróneas, que llevan fuente o se marcan como inferencia.
10. **Aprender exige hacer.** La ruta de aprendizaje sigue los 7 pasos y está separada de la referencia.
11. **Frescura medible.** Cada nota lleva estabilidad, fuentes, fecha de revisión y quién la confirmó. Lo viejo se marca y redirige. Un lint encuentra lo vencido, lo roto, lo huérfano y lo contradictorio.
12. **Un visual tiene que ganarse su lugar.** Va si pasa el test de isomorfismo y si es un mecanismo, un flujo o una jerarquía. Si el contenido es categórico, va una tabla.

### Áreas genéricas de un tema

| # | Área | Pregunta | Estabilidad típica |
|---|---|---|---|
| 00 | Mapa | ¿Qué hay acá, por dónde entro según a qué vengo y cuáles son los conceptos umbral? | estable |
| 01 | Qué es y para qué existe | Definición, límites, el problema que resuelve, en qué se diferencia de sus vecinos | estable |
| 02 | Cómo funciona | Modelo mental, mecanismos, principios | estable |
| 03 | Anatomía y clasificación | Partes, tipos, la taxonomía propia del dominio | estable o semi |
| 04 | Procesos y ciclo de vida | Cómo transcurre, se desarrolla o cambia | estable o semi |
| 05 | Cómo se hace | Procedimientos, técnicas, cómo se observa o se usa | semi o volátil |
| 06 | Cómo se decide | Criterios, trade-offs, cuándo usar qué, debates abiertos | semi |
| 07 | Cómo falla | Fallas, diagnóstico, concepciones erróneas, pares que se confunden | estable o semi |
| 08 | Historia | De dónde viene y por qué es así hoy; también es el hilo de las otras áreas | estable |
| 09 | Ecosistema | Herramientas, versiones, actores, recursos recomendados | **volátil** |
| 10 | Referencia y glosario | Datos, tablas, términos y términos a evitar | mixta, fechada |
| 11 | Ruta de aprendizaje | Los 7 pasos por área, autoevaluación, cómo estudiar este tema | semi |

Las áreas son un punto de partida, no un molde fijo:
- Si el dominio tiene una taxonomía propia, la 03 la usa: los lagartos se parten por filogenia, no por facetas.
- Un área que no tiene contenido no se crea. En los lagartos, la 06 puede quedar en "cómo elegir una especie para terrario" o no existir.
- Un tema grande se parte en sub-temas, cada uno con las mismas áreas. Kubernetes, por ejemplo, tendría redes, almacenamiento y planificación.

### Proceso de la skill (borrador)

1. **Intención y alcance.** Para qué es (aprender, consultar, decidir, operar), para quién, qué queda fuera y qué profundidad. Preguntar solo lo que no se puede decidir por defecto.
2. **Preguntas.** De 10 a 20 preguntas de cobertura y las esenciales. Se aprueban antes de seguir.
3. **Investigación.** Un subagente por ángulo, que incluya la posición contraria. Fuentes puntuadas, y calificadas por otro agente distinto del que las buscó. Recursos canónicos para tender puentes. Tope de rondas, con el hueco declarado si no alcanza.
4. **Mapa propuesto.** Áreas, notas con su tipo, su pregunta y sus relaciones, conceptos umbral y la ruta. Se aprueba antes de escribir.
5. **Escritura.** Primero el núcleo estable, después la periferia. Cada nota nueva entra en su mapa en el mismo cambio.
6. **Verificación.**
   - Lint de estructura: enlaces, relaciones, ciclos, huérfanas y productos en el núcleo.
   - Lint de evidencia: los números, fechas y citas existen en la fuente.
   - Lector en frío sobre la base entera, que responda las preguntas del paso 2 navegando desde el mapa y citando el párrafo.
   - Pasada final de humanizer.
7. **Mantenimiento.** Re-verificar la periferia volátil, actualizar en cascada, marcar lo viejo y lo disputado, y revisar si cambiaron los recursos externos.

## Qué cambia respecto de `conocimiento`

La skill `conocimiento` de este repo ya resuelve más o menos la mitad: una nota por pregunta, la separación entre estable y volátil por tipo `ficha`, `requiere` y `parte_de`, los Mapas y Recorridos, la frescura por estabilidad, `revisar.py` y el lector en frío. Está pensada para ordenar o volcar conocimiento que ya tiene alguien, nota por nota.

Lo que este research agrega y `conocimiento` no tiene:

- Generar un tema entero desde cero, con las áreas genéricas, la poda y la taxonomía propia del dominio.
- Las preguntas de cobertura fijadas antes de escribir, y el lector en frío corrido sobre la base entera contra esas preguntas.
- La regla de que el núcleo no nombra productos, chequeada por un lint.
- Los puentes a recursos de afuera (ADR 0011) como forma de nota.
- La jerarquía con subtipo (es-un, parte-de, instancia-de) y la prohibición de que un par sea a la vez jerárquico y asociativo.
- Lo disputado y lo obsoleto marcados debajo de cada afirmación.
- La pedagogía: conceptos umbral, concepciones erróneas con fuente, la secuencia de 7 pasos y una entrada por propósito.
- Decidir cuándo un visual se gana su lugar.

## Preguntas para alinear

Son decisiones que cambian el diseño y que no se pueden resolver con un default.

1. **¿Skill nueva o modo nuevo de `conocimiento`?** Un modo `dominio` reusa el frontmatter, las plantillas, `revisar.py` y la prosa, y suma lo de arriba. Una skill nueva tiene un propósito más claro, pero duplica la mitad. Mi recomendación es el modo, salvo que quieras que se pueda instalar por separado.
2. **¿Cuánto produce por defecto?** Una base de 15 a 30 notas con todas las áreas en superficie y los conceptos umbral en profundidad, o algo más chico que crece a pedido.
3. **¿La ruta de aprendizaje va siempre o solo cuando se pide aprender?** Es la parte más cara de producir y la que más rápido caduca.
4. **¿Teoría propia o puente a recursos de afuera por defecto?** El ADR 0011 eligió el puente para la Academia. Para una base de consulta puede convenir lo contrario.
5. **¿Dónde vive cada base?** Una carpeta por tema en un repo "biblioteca", el vault de Obsidian, o los docs del repo al que pertenece el tema.

## Fuentes

### Academia (`the-software-co/academia`)

- `GLOSSARY.md`: Competencia, Unidad, Hilo, Entrevista al Mentor.
- ADR 0008 (los checks del Intento antes que la Unidad) y ADR 0011 (la Teoría recorre Recursos de afuera), en `docs/adr/`.
- Spec v3 de #50 (`docs/work-products/50/spec-v3.md`): reglas C14, C18 y C20, y la ficha de `primer-proyecto` con su `secuencia`.
- Issue #26: el modelo pedagógico y los 7 pasos.
- Research en ramas y en `main`: `investigacion-pedagogica` (#25), `skills-con-pedagogia` (#31), `libros-y-papers-educacion-computacion`, `evaluacion-de-entrada` (#32) y `camino-curado` (#212).

### Libros, papers y estándares

- Procida, D. *Diátaxis*. https://diataxis.fr/ ; "Diátaxis in complex hierarchies" (archivo, 2024-12): https://web.archive.org/web/20241227142758/https://diataxis.fr/complex-hierarchies/
- OASIS. *DITA 1.3*, "Information typing": https://docs.oasis-open.org/dita/dita/v1.3/os/part3-all-inclusive/archSpec/base/information-typing.html
- Horn, R. E. (2001). "What Kinds of Writing Have a Future?" https://faculty.washington.edu/farkas/TC510-Fall2011/Horn-DocsWithFuture.pdf
- Baker, M. (2013). *Every Page is Page One*. XML Press. "The Tyranny of the Terrible Troika": https://everypageispageone.com/2012/07/28/the-tyranny-of-the-terrible-troika-rethinking-concept-task-and-reference/
- The Good Docs Project, templates: https://www.thegooddocsproject.dev/template ; Bhatti et al. (2021). *Docs for Developers*. Apress.
- Miles, A. y Bechhofer, S. (2009). *SKOS Reference*. W3C. https://www.w3.org/TR/skos-reference/
- ISO 25964 (NISO): https://niso.org/schemas/iso25964 ; Dextre Clarke, "Thesaurus", *ISKO Encyclopedia*: https://www.isko.org/cyclo/thesaurus
- Hjørland, B. (2013). "Facet analysis". *IP&M* 49(2). https://www.isko.org/cyclo/facet_analysis
- Noy, N. y McGuinness, D. (2001). "Ontology Development 101". https://protege.stanford.edu/publications/ontology_development/ontology101-noy-mcguinness.html
- Luhmann, N. (1981). "Communicating with Slip Boxes". https://luhmann.surge.sh/communicating-with-slip-boxes
- Matuschak, A. "Evergreen notes". https://notes.andymatuschak.org/Evergreen_notes
- Milo, N. "MOCs Overview". https://blog.linkingyourthinking.com/notes/mocs-overview
- Winters, Manshreck y Wright (2020). *Software Engineering at Google*, cap. 10. https://abseil.io/resources/swe-book/html/ch10.html
- Write the Docs. "Docs as Code". https://www.writethedocs.org/guide/docs-as-code/
- Ord, T. (2023). "The Lindy Effect". arXiv:2308.09045. https://arxiv.org/abs/2308.09045
- Meyer, J. y Land, R. (2003). *Threshold Concepts and Troublesome Knowledge*. ETL Report 4. https://web.archive.org/web/2020/http://www.etl.tla.ed.ac.uk/docs/ETLreport4.pdf
- Novak, J. y Cañas, A. (2008). *The Theory Underlying Concept Maps*. IHMC. https://cmap.ihmc.us/docs/pdf/TheoryUnderlyingConceptMaps.pdf
- Ausubel, D. (1960). doi:10.1037/h0046669
- Kalyuga, S. et al. (2003). "The Expertise Reversal Effect". doi:10.1207/s15326985ep3801_4
- van Merriënboer, Kirschner y Frèrejean (2024). *Ten Steps to Complex Learning*. https://www.4cid.org/about/
- McTighe, J. y Wiggins, G. (2012). *Understanding by Design Framework*. ASCD. https://files.ascd.org/staticfiles/ascd/pdf/siteASCD/publications/UbD_WhitePaper0312.pdf
- Krathwohl, D. (2002). "A Revision of Bloom's Taxonomy". doi:10.1207/s15430421tip4104_2
- Doignon, J.-P. y Falmagne, J.-C. (1985). doi:10.1016/S0020-7373(85)80031-6
- Sentance, S. et al. (2019). PRIMM. doi:10.1080/08993408.2019.1608781
- Parsons, D. y Haden, P. (2006). ACE 2006, CRPIT 52.
- Posner, G. et al. (1982). doi:10.1002/sce.3730660207 ; Sadler, P. et al. (2013). doi:10.3102/0002831213477680
- Falcon, A. "Aristotle on Causality". *SEP*. https://plato.stanford.edu/entries/aristotle-causality/ ; Tinbergen (1963), reimpreso en doi:10.1163/157075605774840941

### Skills del mercado

Las URL están en la tabla de "Lo que conviene tomar". Hay además dos que no tienen fila propia:

- GitBook `write-docs`: https://github.com/GitbookIO/gitbook-skills
- Karpathy, "LLM Wiki": https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

## Límites de este research

- No se leyó el texto completo de ISO 25964, Sweller et al. 2019, Ausubel 1960, Tinbergen 1963, Arbesman 2012 ni *Docs for Developers*. Se citan por sus metadatos, su resumen o fuentes secundarias.
- La página de jerarquías complejas de Diátaxis da 404 en el sitio vivo y se leyó en el archivo de diciembre de 2024.
- No se encontró una fuente primaria para "durable vs perishable knowledge".
- Varias piezas tienen un solo respaldo fuerte: las áreas 06 y 09 como áreas propias, el orden por estabilidad y la adaptación de los 7 pasos a temas no procedimentales. Son inferencia.
- No se leyeron los scripts de evaluación de learn-anything ni el repo de origen de la skill de Diátaxis (solo su paquete de npm). Docusaurus no tiene una skill oficial.
- Nada se probó todavía sobre un tema real. El próximo paso natural es correr la propuesta a mano sobre un tema chico y ver dónde falla.
