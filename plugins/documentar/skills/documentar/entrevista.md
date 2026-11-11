# Entrevista

Cómo se entrevista a la persona antes de escribir el `ALCANCE.md`. Todo lo necesario para correrla está acá. El porqué de cada pregunta está en `docs/research/entrevista-previa.md` del repo `the-software-co/skills`.

La entrevista es un grilling acotado: se trabaja por **rondas** y en cada una van juntas las preguntas que ya se pueden responder. Después se espera la respuesta. Los hechos los buscás vos, con subagentes; a la persona le preguntás solo lo que ella sabe o decide.

Abrí diciendo que son tres rondas cortas.

## Reglas de toda la entrevista

- **Formato**: cada pregunta va numerada. Las fijas son F1 a F9 y las dinámicas D1, D2…; la primera vez que aparezca una D, aclará que es una pregunta sobre su caso. Los casos o las listas van como sub-ítems.

  ```
  ❓ **F6** - **<título>**: <pregunta; si es cerrada, con alternativas en competencia>

  ➡️ <propuesta y por qué, en una línea> (solo donde está permitido)
  ```

- **Alternativas en competencia**: "A, B, las dos o decidí vos". Nada de sí o no ni de "¿te parece bien?", porque invitan a decir que sí.
- **Cuándo proponer**:
  - En F1 a F5 no proponés nada: ahí la persona es la única fuente, y en F5 se la está midiendo.
  - En F6, F7, F8 y las dinámicas proponés solo con evidencia de sus respuestas, de su material o del vistazo, y decís cuál es.
  - Una propuesta se lee como lo que conviene y arrastra la respuesta. Por eso va con el motivo, para que la persona pueda discutirla.
- **Su vocabulario y su idioma**: usá las palabras de sus respuestas y de su material. Si el vistazo trae términos en otro idioma (nombres de funciones o comandos), usá los de la versión que ella usa.
- **Respuestas parciales**: lo que una respuesta deja sin contestar no se vuelve a preguntar. Pasa a supuesto y se muestra en F9.
- **Topes**:
  - tres rondas;
  - seis preguntas por mensaje;
  - 14 preguntas en total, contando las F y las D, sin contar sub-ítems.

  Si una ronda tiene más preguntas de las que entran, las de menos impacto pasan a supuesto. El ajuste que sigue a F9 no cuenta como ronda.

## Ronda 1: situación y uso

Antes de mandarla, despachá un subagente para el **vistazo al tema**: hasta cinco búsquedas. Tiene que traer:

- la taxonomía del dominio (el índice de la documentación oficial, el programa de una certificación o un curso de referencia);
- las decisiones típicas y las controversias conocidas;
- de 3 a 7 conceptos umbral candidatos, que son hipótesis hasta el paso de investigación.

Las preguntas son abiertas:

- **F1, el último caso**: "Contame la última vez que necesitaste algo de <tema>: qué estabas haciendo, qué buscaste, dónde y cómo terminó." Alimenta la intención, las preguntas y la audiencia.
- **F2, el uso**: "Cuando la base exista, ¿qué vas a poder hacer que hoy no podés?" Alimenta la intención.
- **F3, quién**: "¿La leés solo vos, o también otra persona? ¿Quién la va a mantener al día?" Alimenta la audiencia y el tamaño.
- **F4, lo que ya tenés**: "¿Qué tenés sobre <tema>? Pasame rutas o links: notas, docs, apuntes, libros, archivos de trabajo. Y si tenés acceso a algo que yo no (libros o cursos pagos, docs de tu trabajo), decime si podés dejarlo en una carpeta o pegarme las partes clave." Alimenta las fuentes y el nivel.

Con la respuesta, si F4 trajo material, despachá el **escaneo del material**. Tiene que traer:

- la versión o la fecha;
- qué subtemas trae y cuáles faltan frente a la taxonomía;
- las contradicciones con la fuente oficial;
- su vocabulario;
- su contexto concreto: herramienta, versión, plataforma, especie o país.

Cuenta como material cualquier cosa: fotos, capturas, mensajes o algo que tenga en el celular. Lo que no pueda pasar ahora queda como fuente pendiente en el alcance. Si F4 vino vacía, no hay escaneo, y el nivel sale solo de F5.

Si las respuestas acotan el tema (un subtema, una región, una plataforma, una versión), volvé a despachar el vistazo con ese foco antes de armar la ronda 2. Si el vistazo inicial muestra que el tema cambia mucho según un dato de contexto (dónde vive, qué versión usa), esa pregunta puede ir en la ronda 1 como D1.

## Ronda 2: nivel y bordes

Va con el vistazo y el escaneo ya en la mano, como mucho seis preguntas, ordenadas por cuánto cambian el plan.

- **F5, el nivel**: dos o tres casos cortos y graduados (fácil, medio y difícil, según el vistazo), con la consigna "¿cuál sería tu primer paso? Si no sabés, adiviná". Usá casos distintos del de F1, que ya lo contó. En la misma pregunta, al final: "¿Cómo te ubicarías: nunca lo usé, lo uso con receta, lo uso y lo depuro, o lo enseño?". La autoevaluación es solo un contraste: el nivel lo fijan los casos y su material.
- **F6, los bordes**: proponé un corte con lo que entra, lo que va solo mencionado y lo que queda afuera. Deducilo de F1 a F4, del vistazo y del escaneo (F5 viaja en el mismo mensaje), en grupos de la taxonomía (como mucho diez), y pedí solo la corrección. A alguien que no conoce un subtema no le pidas que decida sobre él: proponé y marcá el motivo. La lista completa va al `ALCANCE.md`.
- **F7, las preguntas**: un borrador de las preguntas esenciales y de cinco a ocho de cobertura, escritas con su caso y sus palabras. Pedí qué sobra, qué cambiaría y cuál falta. Si la intención incluye aprender, las esenciales son preguntas que el tema entero ayuda a responder.
- **F8, la dedicación**: "¿Cuánto le vas a dedicar: una consulta puntual, una tarde, una semana, o la vas a mantener viva y volver cada tanto?". Para el tamaño, como punto de partida:

  | Dedicación | Notas |
  |---|---|
  | una consulta puntual | 8 a 12 |
  | una tarde | 12 a 20 |
  | una semana | 20 a 35 |

  "Mantenerla viva" no cambia el tamaño: suma el modo `mantener`.
- **Dinámicas**, las que entren hasta llegar a seis (ver abajo).

## Ronda 3: la devolución

- **F9**: el alcance entero, en 6 a 8 líneas, con cada supuesto marcado como *supuesto*. Si en la ronda 2 aceptó todo sin discutir, marcá lo que propusiste como *aceptado sin discutir*: queda para revisar con la primera entrega. Termina con "¿Qué sobra, qué falta y qué te tendría que haber preguntado y no pregunté?".

La ronda 3 solo lleva F9. Una pregunta que no entró en la ronda 2 pasa a supuesto dentro de F9.

La respuesta a F9 es la aprobación del alcance. Si corrige algo, se ajusta y se devuelve solo lo que cambió.

## Preguntas dinámicas

Salen de seis lugares:

1. **Un término ambiguo**, si F6 no lo resuelve. Por ejemplo, "lagartos" puede ser terrario, campo o biología.
2. **La plataforma real**: con qué programa, versión o entorno trabaja, cuando cambia lo que funciona. Ejemplos: Excel o LibreOffice, k3s o un cloud gestionado.
3. **Una rama de la taxonomía** que su material no toca y que F6 no alcanza a cubrir.
4. **Una decisión o controversia** del dominio relacionada con su uso. Cada una puede ser una nota `decision`.
5. **El borde con otra disciplina**. Ejemplos: el cierre de mes toca la contabilidad; el terrario toca la veterinaria.
6. **Su material**: una contradicción con la fuente oficial, o un contexto que cambia las fuentes.

**Filtro**: una dinámica entra solo si su respuesta cambia el plan (las fuentes, los subtemas, la profundidad o el formato) y no se puede inferir de su material ni del contexto. Lo que se puede inferir pasa a supuesto. Se ordenan por cuánto cambian el plan y por cuánto no sabés.

Ejemplos:

- **Kubernetes, por la plataforma**: "Tus notas son de k3s y Helm, sin cloud gestionado. ¿La base cubre solo self-hosted, self-hosted con una referencia a los gestionados, o los dos por igual?" ➡️ Solo self-hosted: es lo que operás.
- **Kubernetes, por una decisión**: "Para el tráfico de entrada: ¿Gateway API, Ingress o comparar los dos?" ➡️ Comparar, si vas a decidir; solo el que usás, si vas a operar.
- **Lagartos, por el contexto**: "¿Qué especie y en qué país? Cambian la dieta, los parámetros del terrario y la legislación."

## Cuándo parar

Cerrá con F9 cuando pase cualquiera de estas cosas:

- Cada campo del alcance (intención, audiencia, nivel, fuera de alcance, preguntas, tamaño, fuentes y acceso) tiene una respuesta o un supuesto.
- La próxima pregunta no cambiaría el plan.
- Se llegó al tope de rondas o de preguntas.
- Hay **fatiga**: respuestas cada vez más cortas, dos "lo que vos digas" seguidos, o que acepte todas las propuestas.

Una fuente inaccesible se pregunta una sola vez. Si no hay forma de conseguirla, queda como hueco.

Las respuestas pueden cambiar después de la primera entrega. El alcance se reabre en `ampliar`; en la entrevista no se sigue preguntando.

## Si la persona vino con todo

Si el pedido ya trae el uso, el material, las fuentes, los casos y el corte, salteá lo que ya está respondido. La ronda 2 queda con F5, F7 y las dinámicas, y se cierra con F9.
