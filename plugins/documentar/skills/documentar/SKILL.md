---
name: documentar
description: Arma y mantiene bases de conocimiento en Markdown en git (un tema general, los docs de un repo o el saber de la organización), descomponiendo el sujeto en capas (el todo, sus verticales, sus componentes, lo operativo) con notas enlazadas. Usar cuando piden documentar un tema o un sistema, guardar algo aprendido, ordenar o ampliar documentación que ya existe, o revisar qué quedó viejo, roto o huérfano.
---

# Documentar

Cómo se estructura y se escribe una base está en [`metodo.md`](metodo.md): leelo antes de cualquier modo. Si la base son los docs de un repo con código, sumá [`sistemas.md`](sistemas.md). Las plantillas están en [`plantillas/`](plantillas/) y el lint es `python3 <carpeta de esta skill>/revisar.py <carpeta>`. Si la base documenta cómo trabaja una organización (procesos, runbooks), mirá "Procesos y runbooks" en `metodo.md`.

| Pide | Modo |
|---|---|
| documentar un tema que no está | `nuevo` |
| profundizar o sumar una vertical a un tema que está | `ampliar` |
| ordenar o mejorar documentación que ya existe | `existente` |
| guardar un concepto suelto o algo que aprendió | `volcar` |
| ver qué está viejo, roto o huérfano | `mantener` |
| leer o contestar desde la base, o usarla en una tarea | skill [`consultar`](../consultar/SKILL.md) |

## Antes de cualquier modo: leer el contexto

Antes de preguntar nada, averiguá solo todo lo que se puede averiguar. La persona no tiene que contarte lo que ya está escrito.

1. **La base, por lo que es el contenido y no por dónde está la sesión.** Lo que la persona escribe en el pedido (una empresa, un repo, un producto) es contexto de uso: dice para quién es, no a dónde va. Un tema general va a la base de conocimiento de la organización (`mtsdlf/conocimiento`) aunque la sesión esté abierta en otro repo; lo de un sistema va a los docs de su repo, y lo de una empresa, a su repo. Si el `AGENTS.md` o el `CLAUDE.md` del repo tiene una sección de dónde va cada cosa, manda. Buscá el clon en `~/repos`; si no está, clonalo. Si la sesión está en otro repo, el destino va en el mensaje de alinear («lo escribo en `conocimiento/<Tema>/`»).
2. **Las convenciones.** El `CONVENCIONES.md` de la base dice el dueño por defecto, la entrada raíz y lo propio de esa base. Manda sobre los ejemplos de `metodo.md`.
3. **Para qué y para quién.** Salen de la conversación, de los repos que la persona nombró o en los que está trabajando (sus `AGENTS.md`, `CLAUDE.md`, README) y de las skills de la organización. Si menciona una empresa de la organización, el uso está en su repo: leelo.
4. **Lo que ya existe.** Buscá el tema, sus sinónimos y su traducción en toda la base. Lo que existe se amplía, se reordena o se enlaza.

Trabajás en una rama (`tema/<tema>`, `docs/<asunto>`) y entregás un PR en el repo de la base.

## `nuevo`

### 1. Vistazo y árbol

Un subagente hace un vistazo al tema (hasta cinco búsquedas) y trae:

- cómo se divide el dominio a sí mismo: el índice de un libro de texto de referencia, el programa de una certificación o la documentación oficial;
- las escuelas o enfoques que compiten, si hay, con una línea cada uno;
- dónde se produce el conocimiento confiable del campo (ver [`investigacion.md`](investigacion.md)).

Si la persona adjuntó o nombró material propio (notas, apuntes, libros, docs de trabajo), otro subagente lo escanea en paralelo: qué partes del tema cubre, su vocabulario, su contexto concreto y dónde contradice a las fuentes.

Con eso y con el contexto armá el **árbol** como dice "Capas" en `metodo.md`: el todo, las verticales, los componentes de cada una y lo que va a la capa operativa o a `Fundamentos/`.

### 2. Alinear: un solo mensaje

Mandale a la persona **un solo mensaje** con:

- **lo que entendiste**, en tres o cuatro líneas: para qué es la base, para quién y qué nivel asumís, diciendo de dónde lo sacaste, y **dónde lo vas a escribir** (repo y carpeta);
- **el árbol propuesto**, como un bloque con carpetas y notas, cada una con media línea;
- **las preguntas que la base tiene que poder responder**, de tres a seis, con sus palabras y su caso: son la prueba del lector en frío;
- **como mucho tres preguntas** sobre el tema, solo las que cambian el árbol y no se pueden deducir: qué queda afuera, qué vertical va más hondo, desde qué escuela se escribe si el campo tiene varias. Cada una con alternativas concretas y tu recomendación con su motivo.

Nunca se pregunta por el dueño, la audiencia, la dedicación ni "la última vez que lo usaste" si el contexto lo dice o se puede suponer, y nunca se repregunta lo que la persona puso en el pedido: si nombró una empresa o un uso, eso es el para qué y el para quién. Lo que supusiste va en el mensaje, marcado, para que lo corrija. Si la persona contesta corto o "dale", seguí con lo propuesto.

Con la respuesta escribí `<Tema>/ALCANCE.md` desde [`plantillas/alcance.md`](plantillas/alcance.md). Terminás cuando la persona respondió y el árbol quedó corregido.

### 3. Investigar

Seguí [`investigacion.md`](investigacion.md): un subagente por vertical, más uno para la posición contraria. Los informes quedan enteros en `<Tema>/.investigacion/`.

### 4. Escribir

De arriba hacia abajo: primero la entrada del tema (el todo), después la entrada de cada vertical, después los componentes y al final lo operativo. Cada nota sale de su plantilla, con `estado: borrador` y `creado` de hoy. Cada entrada enlaza a todo lo que tiene adentro, en el mismo cambio.

Si escribís con subagentes, cada uno recibe el árbol entero, la entrada del tema ya escrita y los informes de su vertical. Al juntar, buscá valores que dos notas dan distinto sin explicarlo y términos que dos notas usan distinto.

### 5. Verificar

Seguí "Verificar", más abajo.

### 6. Entregar

Commit, push y PR. El cuerpo lleva el árbol, los huecos declarados, los supuestos y los avisos del lint que quedaron. Decile a la persona que todo está en `borrador` y pasa a `vigente` cuando lo lee y lo confirma; ofrecé un resumen de lo que afirma cada vertical para que la confirmación sea rápida.

## `ampliar`

Leé el `ALCANCE.md` y la entrada del tema. Proponé dónde entra lo nuevo en el árbol (una vertical nueva, un nivel más hondo en una que está, componentes nuevos) en un solo mensaje, como en el paso 2 de `nuevo`, con una o dos preguntas como mucho. Después seguí los pasos 3 a 6 solo para lo nuevo. Lo que ya estaba explicado se enlaza, no se repite. Si lo nuevo no entra en el árbol, el árbol está mal: proponé reordenarlo.

## `existente`

1. **Auditar**: corré `revisar.py` y leé todo. Armá el árbol que el tema debería tener según "Capas" y, para cada nota vieja, decí a dónde va: queda, se mueve, se fusiona con otra, se parte, se baja a la capa operativa o se borra (relleno, restos de un chat).
2. **Proponer**: el árbol nuevo con el origen de cada nota, en un solo mensaje. Sumá solo las preguntas que la persona puede responder (de dónde salió un material, si algo es de un empleador). Esperá el sí.
3. **Reestructurar**: mové con `git mv` (los originales que se reemplazan enteros van a `Archivo/`, si `CONVENCIONES.md` lo pide), reescribí los títulos de sección que vienen de una plantilla vieja, actualizá en toda la base (y en los repos que la enlazan) los enlaces a rutas viejas, y borrá lo que quedó vacío.
4. **Verificar** como dice "Verificar". Contale a la persona cuántas notas había, cuántas quedaron y qué se borró.

## `volcar`

1. **Ubicar** en el árbol: ¿qué vertical? ¿es un componente nuevo, amplía uno que está, o ya está explicado? Si no entra en ninguna vertical, puede ser una vertical que falta o un tema nuevo.
2. **Proponer** en una línea: dónde va, qué nota crea o amplía, y qué vas a verificar si trae un dato. Si la ubicación es obvia, escribí directo y decilo al entregar.
3. **Escribir** desde la plantilla, enlazar desde la entrada de su vertical y verificar. Si trae texto pegado de otra IA o de un chat, se queda solo el contenido y se verifica como cualquier material.
4. **Devolver** la ruta de la nota, y registrarla donde diga `CONVENCIONES.md`, si dice algo.

## `mantener`

1. Corré el lint con `--json` (en un repo con código, con `--desde origin/main`).
2. Leé juntas las notas de cada vertical y buscá afirmaciones incompatibles.
3. Re-verificá contra sus fuentes las notas vencidas, las `volatil` primero. Si el tema tiene `.investigacion/`, partí de ahí.
4. Lo que cambió se marca como dice "Obsoleto y disputado" en `metodo.md`, y se actualiza toda nota que lo repite.
5. Proponé un arreglo por hallazgo y aplicá solo lo aprobado, en un PR. Una revisión confirmada pone `revisado` de hoy.

## Verificar

1. **Prosa**: una pasada con la skill `humanizer` si está; si no, con "Prosa" de `metodo.md`. Guardá una copia antes y después compará los números, las URLs y los enlaces de cada nota contra la copia: tienen que ser los mismos.
2. **Lint**: 0 errores. Los avisos se arreglan o se justifican en el PR.
3. **Cotejo con fuentes**: un subagente por vertical recibe sus notas y sus fuentes (los informes de `.investigacion/`, el código, la página) y devuelve cada afirmación que la fuente no sostiene. Si ninguna fuente dice el porqué de algo, no se deduce: la nota dice que no quedó registrado.
4. **Lector en frío**: un subagente sin este contexto recibe solo la ruta de la entrada del tema y las preguntas del `ALCANCE.md` (sin `ALCANCE.md`, quien escribe redacta tres por nota). Navega por los enlaces como dice la skill `consultar`, responde citando archivo y párrafo, y lista los términos sin definir y los enlaces que faltan. Si el tema se usa para trabajar, recibe también una pregunta con forma de tarea («tengo que armar una propuesta comercial, ¿qué me sirve de acá?») y tiene que llegar a las notas correctas desde la entrada del tema. Quien escribe juzga las respuestas, corrige y repite solo lo que falló.

Terminás cuando la prosa no perdió nada, el lint da 0 errores, el cotejo no deja afirmaciones sin sostén y el lector responde todo con una cita válida.

## Sin archivos

En un chat donde no podés escribir archivos, seguí [`conversacion.md`](conversacion.md).
