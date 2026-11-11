# Entrevista previa a documentar un tema

Research para el paso de entrevista de la skill `documentar`. Fecha: 2026-11-11. Lo resume y lo enlaza [`skill-documentar.md`](skill-documentar.md).

## TL;DR

- **Lo que dicen las fuentes, en tres reglas.** (a) Preguntá por un caso real y reciente, no por preferencias en abstracto: lo dicen CDM, JTBD y la entrevista de referencia bibliotecaria. (b) No confíes en lo que la persona dice saber: medilo con una tarea corta y mirá su material. Ahí entran Dunning et al. 2004, Kalyuga y la omisión de expertos medida por Sullivan et al. 2014. (c) Las preguntas cerradas solo sirven si la lista de opciones es completa, y conviene que ofrezcan alternativas en competencia en vez de sí/no (Krosnick & Presser 2010).
- **Agregado al alcance.** Propongo sumar un campo, *inventario de fuentes y acceso*, que hoy el alcance no tiene. Cubre los dos hallazgos de la experiencia previa: el material propio fue lo que más sirvió y las fuentes pagas fueron el mayor hueco. Ninguna fuente clásica lo trata como pregunta propia. Es inferencia mía, apoyada en el filtro de Taylor sobre la relación entre la consulta y la colección.
- **Forma del paso.** 9 preguntas fijas en 3 rondas, más ≤3 dinámicas por ronda (≤5 en total). Las dinámicas salen de un vistazo al tema y de un escaneo del material de la persona, y se priorizan por cuánto cambian el plan. Se para cuando todos los campos tienen respuesta o un default aceptado y explícito, o cuando aparecen señales de fatiga.

---

## 1. Fuentes: qué aporta cada una y qué límite tiene

Leyenda: **[P]** = fuente primaria leída (texto completo o abstract oficial). **[S]** = sale de un resumen secundario o un índice, no leí el original. **[M]** = de memoria bibliográfica, sin verificar en esta sesión.

### 1.1 Elicitación de requisitos

| Fuente | Qué aporta | Límite para este caso |
|---|---|---|
| **Gause & Weinberg, *Exploring Requirements: Quality Before Design*, Dorset House 1989, cap. 6 "Context-Free Questions"**. La estructura del capítulo (6.1 preguntas de proceso, 6.3 de producto, 6.4 *metaquestions*) está en el [índice de Dorset House](https://dcmpx.remotevs.com/com/dorsethouse/www/PL/books/ercontents.html) [S]. Las metapreguntas ("Am I asking you too many questions?", "Do my questions seem relevant?", "Are you the right person to answer these questions?") vienen en una adaptación de [UCI](https://ics.uci.edu/~alspaugh/cls/shr/quickStart.html) [S]. | Hay preguntas que sirven para cualquier dominio. Las metapreguntas son la mejor herramienta conocida para cerrar ("¿qué debí preguntarte?") y para detectar que estás preguntando de más. | Está pensado para un producto de software con varios interesados. No vi la redacción exacta del libro. |
| **Wiegers & Beatty, *Software Requirements*, 3.ª ed., Microsoft Press 2013, cap. 7 "Requirements elicitation"** ([Pearson](https://www.pearson.com/store/en-us/p/software-requirements/P200000000686/9780735679665)) [S] | Define la elicitación como identificar necesidades y restricciones de cada interesado. Mezcla preguntas abiertas para explorar con cerradas para fijar restricciones (esto último sale de un resumen secundario). | **No verifiqué** el contenido sobre preguntas de contexto: solo vi índice y ficha. No lo usaría como apoyo de ninguna pregunta concreta. |
| **IIBA BABOK v3**, técnica *Interviews* | Distingue entrevista estructurada y no estructurada, y abierta y cerrada. | **No verifiqué** el texto ni la numeración (10.25): todo salió de guías de examen ([ej.](https://open-exam-prep.com/study-guides/ccba/babok-techniques/elicitation-analysis-techniques)) [S]. Su aporte es genérico y ya está cubierto por Krosnick & Presser. |
| **Reynolds & Gutman 1988, "Laddering Theory, Method, Analysis, and Interpretation", *J. Advertising Research* 28(1):11–31** ([copia](https://is.muni.cz/el/1456/jaro2013/MPH_MVPS/39278324/LadderingTheoy_original.pdf)) [S] | El *laddering* sube de atributo a consecuencia y de ahí a valor con preguntas de "¿por qué te importa eso?". Sirve para pasar de "quiero saber Excel" a "para cerrar el mes sin depender de otro". | Cansa y se siente invasivo. Para documentación alcanza con llegar a la consecuencia, no hace falta subir hasta el valor (inferencia mía). |
| **Ohno, *Toyota Production System: Beyond Large-Scale Production*, Productivity Press 1988**, "repetir por qué cinco veces" ([resumen IHI](https://www.ihi.org/library/tools/5-whys-finding-root-cause)) [S] | Repreguntar el "para qué" hasta llegar al motivo real. | Es una herramienta de causa raíz, no de entrevista. El 5 es arbitrario (según Art Smalley salió de un caso puntual en la planta de Kamigo, [leanblog](https://www.leanblog.org/2026/04/ohno-5-whys-actually-seven/) [S]). Con una persona, más de 1–2 "¿para qué?" seguidos suena a interrogatorio (inferencia). |

### 1.2 Entrevista de referencia bibliotecaria

Es la fuente más cercana a este caso: alguien pide información y otro arma la respuesta.

- **Taylor, R. S. 1968, "Question-Negotiation and Information Seeking in Libraries", *College & Research Libraries* 29(3):178–194** ([reimpresión](https://distantreader.org/stacks/journals/crl/crl-12027.pdf); [resumen UWO](https://instruct.uwo.ca/mit/144f/week3/tayfit.html)) [S].
  - *Aporta:* distingue cuatro niveles de necesidad. Q1 es la necesidad visceral, que la persona no expresa. Q2 es la consciente. Q3 es la formalizada. Q4 es la "comprometida", o sea la pregunta tal como se la hace al sistema. "Kubernetes" es una pregunta Q4, y la entrevista tiene que volver hacia Q2.
  - En la entrevista previa a la búsqueda, el bibliotecario fija el tema, la motivación y las características de quien consulta [S]. Taylor suma otros dos filtros: la relación de la consulta con cómo está organizada la colección y qué respuesta se espera [M]. El de la colección es el antecedente del campo "inventario de fuentes" que propongo.
  - *Límite:* es de 1968, conceptual y sin datos experimentales.
- **Dervin & Dewdney 1986, "Neutral Questioning: A New Approach to the Reference Interview", *RQ* 25(4):506–513** ([ficha](https://bibbase.org/network/publication/dervin-dewdney-neutralquestioninganewapproachtothereferenceinterview-1986)) [S].
  - *Aporta:* preguntas neutrales sobre situación, hueco y uso ("¿qué estabas haciendo?", "¿qué te falta?", "¿qué vas a hacer con eso?"). Se apoyan en la teoría *sense-making*. Según una fuente secundaria en chino ([Lin, JILA](https://jila.lib.nccu.edu.tw/wp-content/uploads/2019/11/72_1_cprsd.pdf)), la tesis de Dewdney encontró que los bibliotecarios entrenados en el método encontraban información más útil.
  - *Límite:* no leí el original y la evidencia que cito es de segunda mano.
- **RUSA/ALA, *Guidelines for Behavioral Performance of Reference and Information Service Providers*, rev. 2023** ([índice ALA](https://www.ala.org/rusa/documents-topic-standards-guidelines-and-recommendations)) [S]. Aporta la secuencia *Listening/Inquiring → Searching → Closure & Follow-up*, con cierre explícito y seguimiento. No verifiqué la redacción de 2023.

### 1.3 Análisis cognitivo de tareas (CTA)

- **Klein, Calderwood & MacGregor 1989, "Critical Decision Method for Eliciting Knowledge", *IEEE Trans. SMC* 19(3):462–472, doi:10.1109/21.31053** ([ficha](https://scilit.com/publications/6de69610151a4f60caddf9c2781753bc)) [P-abstract]. Extiende la técnica de incidentes críticos de Flanagan (1954) con sondeos sobre aspectos de la pericia. Fue pensado para entornos con presión de tiempo, mucha información y condiciones cambiantes.
  - La estructura de varias pasadas sale de un resumen secundario ([globalcognition.org](https://www.globalcognition.org/cognitive-task-analysis/)) [S]:
    1. elegir un incidente;
    2. relatarlo entero sin interrupciones;
    3. volver varias veces sobre los puntos clave para sacar señales, metas y estrategias;
    4. preguntas "¿y si…?".
  - La referencia completa de esa estructura es Hoffman, Crandall & Shadbolt 1998, *Human Factors* 40(2):254–276 ([Oxford](https://cs.ox.ac.uk/publications/publication12872-abstract.html)) [S]. Crandall, Klein & Hoffman, *Working Minds*, MIT Press 2006, es la guía práctica; no la leí y no confirmé que use el nombre "sweeps".
  - *Aporta:* anclar la entrevista en **un incidente real** ("la última vez que…") rinde más que preguntar en abstracto.
  - *Límite:* está diseñado para expertos y decisiones de alto riesgo, con entrevistas de horas. Si la persona es novata, no tiene incidentes ricos. Acá se usa una versión mínima: una sola pasada más un "¿qué te faltó?".
- **Omisión del experto.** El "~70%" se suele citar como Feldon & Clark 2006, pero no encontré ese paper; aparece citado en [Yates & Clark / USU](https://digitalcommons.usu.edu/itls_facpub/454) [S].
  - El dato empírico verificable es **Sullivan et al. 2014, *Academic Medicine* 89(5):811–816** ([PubMed 24667500](https://pubmed.ncbi.nlm.nih.gov/24667500/)) [S, abstract vía buscador; PubMed bloqueó la descarga]. Tres cirujanos que enseñaban una cricotirotomía omitieron el 71% de los pasos de conocimiento clínico, el 51% de los pasos de acción y el 73% de los pasos de decisión. La entrevista CTA subió lo descrito de ~44% a ~66%.
  - El capítulo de Clark, Feldon, van Merriënboer, Yates & Early 2008, "Cognitive task analysis", *Handbook of Research on Educational Communications and Technology* 3.ª ed., pp. 577–593 ([USU](https://digitalcommons.usu.edu/itls_facpub/366)) [S] es la síntesis habitual.
  - *Límite:* el 70% es una cifra redondeada a partir de pocos estudios, todos de procedimientos médicos o técnicos con expertos. **Implicancia para la skill:** lo que la persona sabe se ve mejor en su material que en lo que cuenta. Por eso conviene escanear sus docs antes de preguntarle el nivel (inferencia).
- **Hoffman, Shadbolt, Burton & Klein 1995, "Eliciting knowledge from experts: A methodological analysis", *OBHDP* 62(2):129–158, doi:10.1006/obhd.1995.1039** ([RePEc](https://ideas.repec.org/a/eee/jobhdp/v62y1995i2p129-158.html)) [S]. Clasifica los métodos en tres familias: analizar tareas habituales, entrevistas y **tareas artificiales** que exponen el razonamiento. Esta última familia es la que justifica la tarea de diagnóstico de la pregunta F5.

### 1.4 Jobs to be Done

- **Christensen, Hall, Dillon & Duncan, "Know Your Customers' 'Jobs to Be Done'", *HBR* sept. 2016** ([hbr.org](https://hbr.org/2016/09/know-your-customers-jobs-to-be-done)) [S]. La gente "contrata" algo para progresar en una situación, y el trabajo tiene dimensiones funcional, social y emocional. Que el competidor más común sea "no consumir" aplica directo: la alternativa a la base es preguntarle a un colega o googlear cada vez.
- **Moesta, charla "Understanding Your Customer: JTBD", Business of Software** ([transcripción](https://businessofsoftware.org/talks/understanding-your-customer-jtbd/)) [P].
  - Línea de tiempo: *first thought → passive looking → active looking → deciding*.
  - Cuatro fuerzas: *push* y *pull* contra *anxiety* y *habit*. Según Moesta, ansiedad y hábito suelen pesar más.
  - Técnica: entrevistar a quien ya compró ("los que no compraron te van a mentir"), "reconstruct the timeline, ask what changed", pedir ejemplos, desarmar palabras vagas, "never have a hypothesis".
  - Libro: Moesta, *Demand-Side Sales 101*, Lioncrest 2020 [M].
- *Aporta:* preguntar **qué pasó que hizo que hoy pida esto** (el *first thought*) y qué usa hoy en su lugar (el hábito).
- *Límite:* la entrevista *switch* necesita un cambio que ya ocurrió. Acá la persona todavía no "compró" la base, así que se adapta al momento en que decidió pedirla y a la última vez que le faltó información (inferencia). Las fuerzas sirven para prever abandono: si el hábito de "le pregunto a Juan" es fuerte, la base tiene que ser más rápida que Juan.

### 1.5 Competency questions y essential questions

- **Grüninger & Fox 1995, "Methodology for the Design and Evaluation of Ontologies", IJCAI-95 Workshop on Basic Ontological Issues in Knowledge Sharing** ([ficha](https://bibsonomy.org/bibtex/26881473a37ed442cff66d02790a258c0/lysander07)) [S], y "The Role of Competency Questions in Enterprise Engineering" (1995, Springer, [doi:10.1007/978-0-387-34847-6_3](https://link.springer.com/doi/10.1007/978-0-387-34847-6_3)) [S]. Las CQ informales van primero y la ontología se valida contra ellas ([TOVE](https://eil.mie.utoronto.ca/theory/enterprise-modelling/entmethod)).
- **Noy & McGuinness 2001, "Ontology Development 101", Stanford KSL-01-05** ([texto](https://protege.stanford.edu/publications/ontology_development/ontology101-noy-mcguinness.html)) [P]. El paso 1 hace cuatro preguntas: dominio, para qué se usa, qué preguntas debe responder, quién la usa y la mantiene. Sobre las CQ dice que "will serve as the litmus test later", que son "just a sketch and do not need to be exhaustive", y que "the answers to these questions may change during the ontology-design process". Cada una de esas citas sostiene una regla: CQ como test, borrador corto, alcance revisable.
- **Monfardini, Salamon & Barcellos 2023, "Use of Competency Questions in Ontology Engineering: A Survey", Springer, doi:10.1007/978-3-031-47262-6_3** ([PDF](https://nemo.inf.ufes.br/wp-content/papercite-data/pdf/use_of_competency_questions_in_ontology_engineering__a_survey_2023.pdf)) [S]. Encuestaron a 63 ingenieros de ontologías: las CQ sirven sobre todo para fijar alcance y evaluar, **pero escribirlas cuesta**. *Implicancia:* que las redacte el agente y que la persona las edite (inferencia).
- **McTighe & Wiggins, *Essential Questions: Opening Doors to Student Understanding*, ASCD 2013, ISBN 9781416615057** ([B&N](https://www.barnesandnoble.com/w/essential-questions-jay-mctighe/1121342832)) [S]. Son preguntas abiertas, que provocan, que vuelven una y otra vez y no tienen una única respuesta correcta. No pude confirmar las 7 características completas.
  - *Aporta:* sirve para la intención **aprender**: elegir 1–2 preguntas esenciales le da columna vertebral a la base ("¿por qué Kubernetes es declarativo y qué cuesta eso?").
  - *Límite:* para **consultar** u **operar** estorban. Ahí mandan las CQ, que son cerradas y verificables.

### 1.6 Diagnóstico rápido del conocimiento previo

- **Kalyuga & Sweller 2004, "Measuring knowledge to optimize cognitive load factors during instruction", *J. Educ. Psychol.* 96(3):558–568, doi:10.1037/0022-0663.96.3.558** [S]. Ojo: el título no es "rapid dynamic assessment". Ese es Kalyuga & Sweller 2005, *ETR&D* 53:83–93.
- **Kalyuga 2005, "When Less Is More in Cognitive Diagnosis", *Proc. CogSci* 27** ([eScholarship](https://escholarship.org/uc/item/0899206c)) [P]. Describe dos métodos:
  - *Primer paso:* se presenta una tarea con tiempo limitado y se pide el primer paso hacia la solución. El experto da la respuesta final, el intermedio da el primer paso y el novato busca al azar. En el piloto de 2004 (álgebra, geometría de coordenadas, problemas aritméticos de secundaria) se obtuvieron **r = .72–.92 contra tests completos, con tiempos de 2,8 a 4,9 veces menores**.
  - *Verificación rápida:* se muestran pasos intermedios correctos e incorrectos y se pide marcar cuáles valen. El test duró 16,5 min, con α = .76.
- **Kalyuga, Ayres, Chandler & Sweller 2003, "The expertise reversal effect", *Educ. Psychologist* 38(1):23–31** ([UOW](https://ro.uow.edu.au/edupapers/136)) [S]. Explica por qué importa medir el nivel: lo que ayuda al novato estorba al experto.
- **Dunning, Heath & Suls 2004, "Flawed Self-Assessment", *Psychol. Sci. Public Interest* 5(3):69–106, doi:10.1111/j.1529-1006.2004.00018.x** ([APS](https://www.psychologicalscience.org/journals/pspi/j.1529-1006.2004.00018.x/)) [S-abstract]. La correlación entre la autoevaluación y el desempeño real va de "moderada a magra".
- *Límite:* la validación es con dominios procedimentales y bien estructurados (álgebra, cinemática). Para "lagartos" o "arquitectura" no hay un "primer paso" canónico, así que la tarea tiene que ser un caso con una decisión (inferencia). Además, un adulto que pidió ayuda tolera mal que lo examinen: hacelo con 1–2 ítems y encuadrado como "para calibrar", no como test (inferencia).

### 1.7 Diseño de cuestionarios

**Krosnick & Presser 2010, "Question and Questionnaire Design", cap. 9 en Marsden & Wright (eds.), *Handbook of Survey Research* 2.ª ed., Emerald, pp. 263–313** ([PDF Stanford](https://web.stanford.edu/dept/communication/faculty/krosnick/docs/2010/2010%20Handbook%20of%20Survey%20Research.pdf)) [P]. Es la fuente principal de esta sección:
- **Orden.**
  - Primero preguntas fáciles, ligadas al tema anunciado, que generen *rapport*.
  - Las de un mismo tema juntas y de lo general a lo específico.
  - Las difíciles o sensibles no van al principio.
  - Los efectos de contexto se dan casi solo entre ítems contiguos y del mismo tema.
  - Si una pregunta filtro dispara repreguntas, la gente aprende a contestar "no" para acortar. Conviene juntar los filtros y hacer las repreguntas después.
- **Abierta vs. cerrada.**
  - La gente se restringe a las opciones ofrecidas: agregar "otro" "is generally not effective".
  - Una cerrada solo sirve si su lista es exhaustiva; si no, es mejor preguntar abierto.
  - Para cantidades, mejor abierta, porque los rangos ofrecidos sesgan.
  - Agregar algunas abiertas como seguimiento de las cerradas le da riqueza a las respuestas.
- **Aquiescencia.** Con formatos acuerdo/desacuerdo, verdadero/falso o sí/no, el efecto promedio es de **~10%**. Crece con preguntas difíciles, fatiga y modalidad no presencial. La recomendación es **evitar esos formatos** y ofrecer puntos de vista en competencia.
- **"No sé".** Los filtros "no sé" no mejoran la confiabilidad. Muchos que dirían "no sé" tienen una opinión real si se les insiste (Gilljam & Granberg 1993, citado ahí). En preguntas de conocimiento, desalentar el "no sé" da medidas más válidas (Mondak 2001, citado ahí).
- **Fatiga y *satisficing*.** Los ítems tardíos muestran más respuestas faltantes, más acuerdo, menos detalle y menos diferenciación. Base teórica en **Krosnick 1991, *Applied Cognitive Psychology* 5(3):213–236** [S].

Complementos:
- **Galesic & Bosnjak 2009, *Public Opinion Quarterly* 73(2):349–360, doi:10.1093/poq/nfp031** [S]. Anunciar más duración baja el arranque (75% con 10 min contra 65% con 20 min, según una revisión). Las respuestas tardías son más cortas y uniformes.
- **Default effect.**
  - **Johnson & Goldstein 2003, "Do Defaults Save Lives?", *Science* 302(5649):1338–1339** [S]. Los defaults mueven mucho las decisiones e imponen costo cognitivo a quien quiere cambiarlos.
  - **McKenzie, Liersch & Finkelstein 2006, "Recommendations Implicit in Policy Defaults", *Psychol. Sci.* 17(5):414–420** ([APS](https://www.psychologicalscience.org/journals/psychological-science/j.1467-9280.2006.01721.x/)) [S]. **Las personas leen el default como una recomendación de quien lo eligió**, y esa inferencia causa parte del efecto.
  - **Tversky & Kahneman 1974, *Science* 185:1124–1131** ([PubMed](https://pubmed.ncbi.nlm.nih.gov/17835457/)) [S]: anclaje.
  - *Implicancia:* un default del agente es una recomendación con autoridad. Es útil para bajar la carga, pero contamina justo los campos donde la persona es la única fuente válida (intención, CQ).

### 1.8 Agentes que preguntan

- **Li, Tamkin, Goodman & Andreas 2023, "Eliciting Human Preferences with Language Models" (GATE), [arXiv:2310.11589](https://arxiv.org/abs/2310.11589)** [P-abstract]. En experimentos preregistrados, la elicitación conducida por el LM fue a menudo más informativa que los prompts o las etiquetas escritas por los propios usuarios. Apoya que el agente conduzca la entrevista y no espere un brief.
- **CLAMBER, Zhang et al. 2024, [arXiv:2405.12063](https://arxiv.org/abs/2405.12063)** [S]. Los LLM preguntan mal en parte porque no reconocen sus propios huecos.
- Hay benchmarks de 2026 que separan sub-clarificar (contestar antes de tiempo) de sobre-clarificar. Solo los vi en resúmenes ([ejemplo](https://www.themoonlight.io/review/clarifymt-bench-benchmarking-and-improving-multi-turn-clarification-for-conversational-large-language-models)) [S]; no los usaría como evidencia firme.

---

## 2. Propuesta

**Flujo del paso 0:**
1. Ronda 1, con preguntas fijas.
2. En paralelo, vistazo al tema (≤10 min) y escaneo del material que pasó la persona.
3. Ronda 2: preguntas fijas más dinámicas.
4. Ronda 3: devolución del alcance, más dinámicas residuales.
5. Escribir el alcance.

Agrego al alcance un campo **"Fuentes y acceso"**: material propio, fuentes pagas o internas y qué puede exportar la persona.

### 2.1 Banco de preguntas fijas (9)

**Ronda 1: situación y uso.** Preguntas abiertas y fáciles, sin defaults, antes de que el agente sepa nada del tema.

| # | Pregunta | Por qué existe | Campo que alimenta |
|---|---|---|---|
| F1 | "Contame la última vez que necesitaste algo de *X*: qué estabas haciendo, qué buscaste, dónde, y cómo terminó." | Incidente real en vez de abstracción: CDM (Klein et al. 1989), *first thought* y reconstrucción de la línea de tiempo (Moesta), pregunta neutral sobre situación (Dervin & Dewdney 1986). Lleva de Q4 a Q2 en términos de Taylor. | Intención; semilla de las CQ; audiencia; nivel (indirecto) |
| F2 | "Cuando la base exista, ¿qué vas a poder hacer que hoy no podés? ¿Quién más la va a leer y quién la va a mantener?" | "¿Para qué se usa?" y "¿quién la usa y mantiene?" de Noy & McGuinness 2001; progreso y competidor "no consumir" de JTBD; un escalón de *laddering*, hasta la consecuencia. | Intención; audiencia; tamaño (mantenimiento) |
| F3 | "¿Qué tenés ya sobre *X*? Pasame rutas o links: notas, docs, apuntes de curso, libros, scripts, configs." | El material propio fue lo que más sirvió en la experiencia previa. Además, el experto omite ~70% al relatar (Sullivan et al. 2014), y lo escrito muestra mejor lo que sabe. Filtro "relación con la colección" de Taylor [M]. | Fuentes y acceso; nivel previo (inferido del material) |
| F4 | "¿Tenés acceso a algo que yo no: libros o cursos pagos, docs de tu empresa, papers con suscripción? ¿Podés exportarlos o pegarme las partes clave?" | El mayor hueco de la experiencia previa fueron las fuentes pagas. Sin esta pregunta el agente no puede planificar fuentes. Es inferencia mía: ninguna fuente clásica la trae como pregunta propia. | Fuentes y acceso |

**Ronda 2: nivel y bordes.** Va después del vistazo y del escaneo, así que ya puede llevar opciones y defaults.

| # | Pregunta | Por qué existe | Campo |
|---|---|---|---|
| F5 | Diagnóstico rápido con 1–2 casos graduados según el vistazo: "¿Cuál sería tu primer paso?". Se aceptan respuestas cortas y "ni idea". Recién después: "¿Cómo te ubicarías: nunca lo usé / lo uso con receta / lo uso y lo depuro / lo enseño?" | Método del primer paso de Kalyuga (r = .72–.92 y 2,8–4,9 veces más rápido en dominios procedimentales). Dunning et al. 2004 muestra que la autoevaluación sola no alcanza, por eso va al final y como contraste. | Nivel previo |
| F6 | "De esta lista de subtemas [taxonomía del vistazo], marcá qué **no** querés, y qué querés solo mencionado." La respuesta es una lista de opciones, no sí/no. | Las cerradas solo funcionan con lista exhaustiva y el "otro" no rinde (Krosnick & Presser 2010). Por eso la lista sale de la taxonomía relevada. | Fuera de alcance |
| F7 | "Estas son 3–5 preguntas que creo que la base tiene que poder contestar [redactadas desde F1/F2]. ¿Cuáles sobran, cuáles cambiarías, cuál falta?" | CQ como prueba de aceptación (Grüninger & Fox 1995; Noy & McGuinness 2001). Las redacta el agente porque a la gente le cuesta escribirlas (Monfardini et al. 2023). Si la intención es *aprender*, se suman 1 o 2 preguntas esenciales (McTighe & Wiggins 2013). | Preguntas de cobertura |
| F8 | "¿Cuánto vas a dedicarle a leerla: una consulta puntual, una tarde, una semana, o la vas a mantener viva?" | Cantidad expresada en una unidad que la persona conoce. Krosnick & Presser prefieren abiertas para cantidades; acá uso categorías concretas porque el número de notas no le dice nada a la persona (inferencia). | Tamaño |

**Ronda 3: cierre.**

| # | Pregunta | Por qué existe | Campo |
|---|---|---|---|
| F9 | Devolución del alcance completo en 6–8 líneas, con los defaults marcados (*supuesto*). Luego: "¿Qué sobra, qué falta, y qué te tendría que haber preguntado y no pregunté?" | Metapreguntas de Gause & Weinberg; cierre y seguimiento de RUSA. Se evita el "¿está bien?" porque invita a la aquiescencia (Krosnick & Presser). | Todos |

### 2.2 Reglas para las preguntas dinámicas

**De dónde salen.** Todas son inferencia mía, armadas con las fuentes que se indican.
1. **Ambigüedad del término.** Taylor: Q4 ≠ Q2. Ejemplos: "Excel" puede ser fórmulas, Power Query o VBA; "lagartos" puede ser terrario, campo o biología.
2. **Taxonomía del dominio** relevada en el índice de la doc oficial, en programas de certificación o cursos, y en artículos de referencia. Sirve para que F6 tenga lista exhaustiva y para detectar ramas que el material de la persona no toca.
3. **Decisiones típicas y controversias del dominio**: dónde los practicantes eligen entre alternativas. Siguiendo a CDM, ahí está la pericia.
4. **Conceptos umbral candidatos**: conceptos transformadores, problemáticos e integradores (Meyer & Land 2003, "Threshold concepts and troublesome knowledge", Univ. Edinburgh ETL Occasional Report 4 [M]; características en [guía U. Calgary](https://taylorinstitute.ucalgary.ca/sites/default/files/TI%20Guides/Threshold_Concepts_Guide.pdf) [S]). Se usan como material para F5 y para preguntar si la persona ya los cruzó.
5. **Escaneo del material de la persona**:
   - versión o fecha de lo que tiene;
   - subtemas presentes y ausentes respecto de la taxonomía;
   - contradicciones con la fuente oficial;
   - vocabulario propio (usarlo en las preguntas);
   - herramientas o contextos concretos (cloud vs. self-hosted, especie concreta).

**Cuántas.** ≤3 por ronda y ≤5 en total, sumadas a las 9 fijas. El tope de 12–14 preguntas es inferencia mía, a partir de los datos de fatiga y duración (Krosnick & Presser; Galesic & Bosnjak). No encontré una fuente que fije un número para entrevistas con agentes.

**Cómo se priorizan.** Por valor de información (inferencia):
- La pregunta entra solo si su respuesta cambia el plan (qué fuentes, qué subtemas, qué profundidad, qué formato) **y** no se puede inferir del material ni del contexto.
- El orden es impacto en el plan × incertidumbre del agente.
- Si una pregunta se puede inferir, se convierte en un supuesto marcado en F9.

**Formato.**
- Alternativas en competencia (A / B / ambas / decidí vos), nunca sí/no, por la aquiescencia.
- Con una opción **recomendada y su motivo en una línea**, solo si el agente tiene evidencia del escaneo o del vistazo.
- Todas van agrupadas por tema y contiguas, para contener el efecto de contexto.

**Ejemplos para Kubernetes:**
- *(escaneo)* "Tus notas son de k3s y Helm, y no aparece ningún cloud gestionado. ¿La base cubre **solo self-hosted**, **self-hosted y una referencia a EKS/GKE**, o **los gestionados por igual**? Recomiendo la primera porque es lo que operás." → fuera de alcance, fuentes.
- *(decisión típica)* "Para el tráfico de entrada: ¿**Gateway API**, **Ingress**, o **comparar ambos**? Recomiendo comparar si vas a decidir, y solo lo que usás si vas a operar." → CQ, intención.
- *(concepto umbral, para F5)* "Un Deployment quedó con 0/3 Pods listos. ¿Qué mirás primero?" Si la respuesta es "los eventos y el estado deseado contra el real", la persona ya entendió el modelo de reconciliación; si es "reinicio", no.

**Ejemplos para lagartos:**
- *(ambigüedad)* "¿La base es para **tener uno como mascota**, para **identificar especies en el campo** o para **biología y evolución**? Por lo que contaste en F1 (te regalaron uno), recomiendo la primera." → intención, fuera de alcance.
- *(contexto que cambia las fuentes)* "¿Qué especie y en qué país? Cambian la dieta, los parámetros del terrario y la legislación de tenencia." → fuentes, alcance.
- *(concepto umbral)* "Está quieto y no come hace tres días. ¿Qué es lo primero que revisás?" Mencionar la temperatura o el gradiente térmico indica que entiende la ectotermia; "le cambio la comida" indica que no.

### 2.3 Cuándo parar de preguntar

Todas son inferencia mía, montadas sobre las fuentes que se indican:
1. **Cobertura.** Cada campo del alcance (intención, audiencia, nivel, fuera de alcance, CQ, tamaño, fuentes y acceso) tiene una respuesta explícita o un supuesto marcado que la persona no objetó en F9.
2. **Trazabilidad.** Cada CQ aceptada tiene al menos una fuente candidata accesible: propia, pública o exportada por la persona. Si una CQ depende de una fuente inaccesible, se pregunta una vez cómo conseguirla o se marca como hueco. No se insiste.
3. **Valor marginal.** Si la próxima pregunta no cambiaría ninguna decisión del plan, no se hace.
4. **Presupuesto.** Tres rondas y ≤14 preguntas. Lo que quede abierto pasa a supuesto.
5. **Fatiga.** Respuestas cada vez más cortas, dos "lo que vos digas" seguidos o aceptar todos los defaults son señales de *satisficing* (Krosnick & Presser). Ahí se cierra con F9 de inmediato.
6. **Cierre explícito.** F9 respondida. Noy & McGuinness: las respuestas pueden cambiar. Por eso el alcance se reabre después de la primera entrega, no se sigue preguntando ahora.

### 2.4 Riesgos y mitigación

| Riesgo | Evidencia | Mitigación |
|---|---|---|
| **Preguntar de más** | Fatiga y menor calidad en ítems tardíos (Krosnick & Presser); anunciar más largo baja la participación (Galesic & Bosnjak) | Topes de 2.3. Anunciar al inicio "son 3 rondas cortas". Antes de preguntar, inferir del material y convertir lo inferible en supuesto. |
| **Sesgo por el default sugerido** | El default se lee como recomendación (McKenzie et al. 2006); anclaje (Tversky & Kahneman 1974) | **Sin default** en F1, F2 y F3 ni en la primera versión de las CQ: la persona es la única fuente válida ahí. Defaults solo donde el agente tiene evidencia, y siempre con su motivo. Registrar qué campos quedaron por default y revisarlos después de la primera entrega. *(Inferencia.)* |
| **Aquiescencia** | ~10% de acuerdo espurio en formatos sí/no; crece con dificultad y fatiga (Krosnick & Presser) | Nada de "¿te parece bien?". Usar alternativas en competencia y preguntas del tipo "¿qué cambiarías?". |
| **La persona no sabe qué necesita** | Necesidad visceral no expresable (Taylor 1968) | Anclar en incidentes (F1), dar casos concretos (F5) y aceptar "decidí vos" como respuesta válida: queda supuesto marcado y se revisa con la primera entrega. |
| **La persona no sabe responder sobre su nivel** | Autoevaluación pobre (Dunning et al. 2004) | Medir con el método del primer paso y con el escaneo; la autoevaluación solo como contraste. |
| **"No sé" que no es real** | Muchos de los que dicen "no sé" tienen respuesta (Krosnick & Presser) | En F5 aceptar "no sé", pero pedir "¿qué harías si tuvieras que adivinar?". En preferencias, un "no sé" pasa a supuesto con default, no a pregunta repetida. *(Inferencia.)* |
| **Omisión del experto** | 51–73% de pasos omitidos (Sullivan et al. 2014) | Si la persona es experta, su material vale más que su relato. Preguntar "¿qué te costó aprender de esto?" y "¿qué le explicarías primero a alguien nuevo?" (inferencia a partir de CTA). |
| **Que el agente pregunte mal** | Los LLM no detectan sus propios huecos (CLAMBER 2024) | Derivar las dinámicas de reglas explícitas (2.2), no de "lo que se me ocurra". F9 incluye la metapregunta. |
| **Fuentes pagas inaccesibles** | Experiencia previa | F4 explícita. Plan B: que la persona pegue índices o capítulos clave, o elegir una alternativa pública marcada como sustituto. Nunca fingir que se leyó lo que no se leyó. |

---

## 3. Qué es consenso y qué es inferencia mía

**Consenso entre varias fuentes independientes:**
- Anclar la entrevista en casos reales y recientes en vez de preguntas hipotéticas: CDM, Moesta, Dervin & Dewdney.
- Lo que la persona pide en primera instancia no es lo que necesita: Taylor, JTBD.
- La autoevaluación no mide bien el conocimiento: Dunning et al.
- El experto omite gran parte de lo que sabe al relatarlo: Sullivan et al.; Clark et al.
- Orden de las preguntas (fácil y general primero), evitar los formatos sí/no, la fatiga degrada las respuestas: Krosnick & Presser; Galesic & Bosnjak.
- Las CQ fijan alcance y después sirven de test: Grüninger & Fox; Noy & McGuinness; Monfardini et al.
- Los defaults pesan y se leen como recomendación: Johnson & Goldstein; McKenzie et al.

**Inferencia mía, sin fuente directa:**
- El campo "Fuentes y acceso" y las preguntas F3 y F4.
- La cifra de 9 fijas más ≤5 dinámicas y el tope de 3 rondas.
- La regla de prioridad por valor de información.
- Prohibir defaults en intención y CQ.
- Usar el método del primer paso en dominios no procedimentales, como los lagartos.
- La adaptación de la entrevista *switch* a algo que la persona todavía no "compró".
- Que el agente redacte las CQ y la persona las edite: está apoyado en Monfardini, pero esa encuesta no lo prueba.

**No verificado:**
- Contenido de BABOK v3 y de Wiegers & Beatty sobre preguntas de contexto.
- El paper Feldon & Clark 2006 (solo citado por terceros).
- El nombre "sweeps" en *Working Minds*.
- Las 7 características de McTighe & Wiggins.
- La redacción RUSA 2023.
- La lista completa de filtros de Taylor (las tres primeras sí están verificadas en un resumen secundario).

Dos correcciones a la consigna: el "rapid dynamic assessment" es Kalyuga & Sweller 2005 en *ETR&D*, no el paper de 2004 en *JEP*. Y el "~70% de Clark et al." tiene como respaldo empírico verificable a Sullivan et al. 2014, no un estudio de Clark citable directamente.