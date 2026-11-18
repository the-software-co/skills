---
name: documentar
description: Arma y mantiene bases de conocimiento en Markdown (un vault de Obsidian, los docs de un repo o un tema nuevo) con notas atómicas enlazadas concepto a concepto. Usar cuando piden documentar un tema o un sistema, guardar algo aprendido o un concepto suelto, ordenar o mejorar documentación que ya existe, ampliar un tema, o revisar qué quedó viejo, roto o huérfano.
---

# Documentar

Las reglas de cómo se parte, se nombra, se enlaza, se escribe y se mantiene una nota están en [`metodo.md`](metodo.md): leelo antes de cualquier modo. Cada nota sale de su plantilla en [`plantillas/`](plantillas/). Si la base son los docs de un repo con código, sumá [`sistemas.md`](sistemas.md). El lint es `revisar.py`, en la carpeta de esta skill: se corre como `python3 <carpeta de esta skill>/revisar.py <carpeta>`.

| Pide | Modo |
|---|---|
| documentar un tema que no está, desde cero | `nuevo` |
| profundizar, sumar un sub-tema o una ruta de aprendizaje a un tema que está | `ampliar` |
| ordenar o mejorar documentación que ya existe | `existente` |
| guardar un concepto suelto, una nota cruda o algo que aprendió | `volcar` |
| ver qué está viejo, roto, huérfano, disputado o contradictorio | `mantener` |

## Antes de cualquier modo: dónde, cómo y qué ya existe

1. **La base.** Si la persona no la nombra:
   - lo general, de cualquier tema, va al vault `mtsdlf/conocimiento`;
   - cómo emprendemos, a `mtsdlf/fundar`;
   - lo de un sistema, a los docs de su repo;
   - lo de una empresa, a su repo.

   Esa es la convención de esta organización, y la skill `tsc-organizacion` la detalla. Si la persona trabaja con otras bases, o hay más de una posible, preguntá dónde va. Buscá el clon en `~/repos` y, si no está, clonalo.
2. **Las convenciones.** Si la raíz de la base tiene un `CONVENCIONES.md`, leelo y seguilo: manda sobre los ejemplos de `metodo.md`. Ahí está quién puede ser dueño, cuál es el Mapa raíz, qué carpetas son especiales y si es un vault de Obsidian.
3. **El destino y el idioma**, como dicen "Destino" y "La nota" en `metodo.md`.
4. **Lo que ya existe.** Buscá el término, sus sinónimos y su traducción en toda la base. Lo que ya existe se amplía o se enlaza.
5. **Los Mapas.** Ubicá el Mapa raíz y el Mapa del tema. El que falte se crea primero.

Trabajás en una rama (`tema/<tema>`, `docs/<asunto>`) y entregás un PR en el repo de la base.

## `nuevo`

### 1. Entrevista y alcance

Entrevistá a la persona como dice [`entrevista.md`](entrevista.md): tres rondas cortas, con preguntas fijas y dinámicas. Mientras tanto, dos subagentes hacen un vistazo al tema y escanean el material que ella te pase. Con las respuestas escribí `<tema>/ALCANCE.md` desde [`plantillas/alcance.md`](plantillas/alcance.md):

- **intención** (aprender, consultar, decidir, operar), **audiencia** y **nivel previo**;
- **fuera de alcance**: lo vecino que no entra;
- **escuela**: la que eligió, o neutral;
- **preguntas**: de 3 a 5 esenciales y de 10 a 20 de cobertura, cada una con el área que la responde. Son el test del paso 5;
- **tamaño**: cuántas notas va a llevar, según la taxonomía del vistazo y la dedicación que dijo la persona. Si pasa de unas 40 notas, o el tema tiene partes que se aprenden por separado, partilo en sub-temas y decí cuáles se documentan ahora;
- **fuentes y acceso**: su material, lo pago o interno a lo que ella llega y vos no, y el mapa de fuentes del campo;
- **volátiles**: productos, versiones, marcas y cifras del tema que el núcleo no puede nombrar. Salen del vistazo y del escaneo de su material, y se confirman en la devolución;
- **dueño**: el que responde F3, o el que dice `CONVENCIONES.md`;
- **supuestos**: lo que decidiste por defecto.

Terminás cuando la persona respondió la devolución de la ronda 3 sin objeciones pendientes y el `ALCANCE.md` refleja esa versión. Anotá la fecha en `aprobado`.

### 2. Investigar

Seguí [`investigacion.md`](investigacion.md): el mapa de fuentes del campo, qué se busca según cada pregunta, la escuela, un subagente por ángulo con el brief fijo (uno de ellos busca la posición contraria), el plan B para las fuentes bloqueadas y los informes enteros en `<tema>/.investigacion/`.

Terminás cuando se cumple el criterio de "Cuándo termina" de `investigacion.md`.

### 3. Mapa propuesto

Mostrale a la persona, antes de escribir una sola nota:

- cada nota: archivo, `tipo`, `area`, `resumen` y qué preguntas `responde`;
- sus relaciones `es_un`, `parte_de`, `instancia_de` y `requiere`;
- los conceptos umbral, de 3 a 7;
- qué notas son puente a un recurso de afuera, y cuál es ese recurso;
- el orden de la ruta, si la intención incluye aprender;
- un glosario, si el tema tiene jerga;
- qué notas existentes de la base se amplían en vez de crearse.

Terminás cuando toda pregunta tiene al menos una nota que la responde, toda área sin notas está justificada como poda y la persona aprobó.

### 4. Escribir

Primero el núcleo (qué es, cómo funciona, anatomía, procesos, historia, cómo falla), después la periferia (cómo se hace, cómo se decide, ecosistema, referencia) y al final la ruta y el Mapa. Cada nota sale de su plantilla, con `estado: borrador`, `autoria: ia`, `creado` de hoy y el `dueno` que dice `CONVENCIONES.md`. Cada nota nueva entra al Mapa en el mismo cambio. El Mapa `responde` las preguntas esenciales, cada una con su sección; las preguntas de cobertura las responden las notas. El Mapa del tema entra al Mapa raíz.

Si escribís con subagentes, cada uno recibe el mapa aprobado entero (ids, relaciones, puentes) y los informes que le tocan. Al juntar, buscá los valores que dos notas dan distinto sin explicarlo.

Terminás cuando existe cada nota del mapa aprobado y el Mapa enlaza a todas.

### 5. Verificar

Seguí "Verificar", más abajo, con el lector en frío del tema: navega desde el Mapa y responde las preguntas del `ALCANCE.md`.

Terminás cuando se cumple el criterio de "Verificar".

### 6. Entregar

Commit en la rama, push y PR. El cuerpo del PR lleva el Mapa resumido, los huecos declarados, los supuestos del alcance, los contrastes con el material de la persona y los avisos del lint que quedaron, sin contar `pendiente-de-revision`: de esos va solo la cuenta.

Decile a la persona que las notas están en `borrador`. Pasan a `vigente`, con `revisado` de ese día, cuando ella las lee y las confirma. Para ayudarla, ofrecé resumir lo que afirma cada nota, empezando por las que más usa.

## `ampliar`

Leé el `ALCANCE.md` y el Mapa del tema. Hacé una entrevista corta sobre lo nuevo, con F1, F4, F6, F7, F8 y las dinámicas de `entrevista.md`. Un sub-tema hereda los bordes del tema salvo que F6 diga otra cosa. Sumá las preguntas nuevas al `ALCANCE.md` (como sub-tema, con su propio `ALCANCE.md`, si es grande) y cerrá con la devolución. Después seguí los pasos 2 a 6 solo para lo nuevo, enlazándolo con lo que ya existe. Lo que ya estaba explicado se enlaza, no se repite.

Terminás como en `nuevo`, solo para lo nuevo.

## `existente`

1. **Auditar**: corré `revisar.py` sobre la carpeta y leé cada nota entera. Para cada sección de cada nota decidí una o varias de estas:
   - **partir**: responde otra pregunta;
   - **fusionar**: explica lo mismo que otra;
   - **aislar lo volátil**: comandos, valores o nombres que van a una `ficha` o a un enlace;
   - **borrar**: no aporta (relleno, restos de un chat, ejercicios vacíos);
   - **conservar**: queda como está, con el frontmatter nuevo.

   Lo que la nota solo nombra se completa investigando, y se marca en la propuesta.
2. **Mapa propuesto**: como en `nuevo`, con una columna más que dice de qué nota y sección vieja sale cada nota nueva. Sumá las preguntas que solo la persona puede responder (de dónde sale un material, si algo es de un empleador). Esperá la aprobación.
3. **Reestructurar**:
   - escribí las notas nuevas como en `nuevo`;
   - mové el contenido y borralo del origen;
   - actualizá en toda la base los enlaces que apuntaban a las notas viejas;
   - borrá las notas que quedaron vacías.

   Los originales que se traducen o se reemplazan enteros van a `Archivo/`.
4. **Verificar** como dice "Verificar", con el lector en frío por nota. Contale a la persona cuántas notas había, cuántas quedaron y qué se borró.

Terminás cuando cada sección vieja tiene su destino aplicado (partida, fusionada, aislada, borrada o conservada), no quedan enlaces a notas borradas y se cumple el criterio de "Verificar".

## `volcar`

Para un concepto suelto, una nota cruda o algo aprendido que la persona quiere guardar.

1. **Buscar** como en "Antes de cualquier modo", y decidir una de estas:
   - **ampliar** una nota existente, si responde la misma pregunta;
   - **crear** una nota, si es una pregunta nueva;
   - **partir** una nota, si al sumarle esto respondería dos preguntas;
   - **solo enlazar**, si ya está explicado.
2. **Proponer**: decile a la persona qué decidiste, en qué tema y con qué relaciones. Si lo que trae necesita respaldo (un dato, una cifra), decí qué vas a verificar. Esperá el sí.
3. **Escribir** desde la plantilla, enlazar desde el Mapa del tema y verificar como dice "Verificar", con el lector en frío por nota.
4. **Cerrar el ciclo**: devolvé la ruta de la nota, y registrala donde diga `CONVENCIONES.md`, si dice algo.

Terminás cuando la nota está enlazada desde su Mapa, pasó "Verificar" y la persona tiene su ruta.

## `mantener`

1. Corré el lint con `--json` sobre la base. En un repo con código, agregá `--desde origin/main`.
2. Leé juntas las notas de cada tema y buscá afirmaciones incompatibles: una definición, una fórmula, un valor o un umbral que no coinciden.
3. Re-verificá contra sus fuentes las notas vencidas, las `volatil` primero, y los recursos puente (link caído o texto que cambió). Si el tema tiene `.investigacion/`, partí de ahí. Una nota queda re-verificada cuando cada afirmación con fuente se cotejó contra esa fuente.
4. Para cada afirmación que cambió: si la vieja importa como historia, marcala como dice "Obsoleto y disputado" en `metodo.md`. Actualizá en cascada toda nota que la repite o la usa, buscando también por `aliases`.
5. Agrupá los hallazgos y proponé un arreglo para cada uno:
   - `enlace-roto`, `relacion-rota`: el destino correcto, o sacar el enlace;
   - `revision-vencida`, `fuente-cambiada`, `doc-sin-actualizar`: releer contra las fuentes (el diff desde `revisado`, si es código) y decir qué cambió, o confirmar que sigue bien;
   - `huerfana`, `mapa-sin-padre`, `tema-sin-mapa`: en qué Mapa va;
   - `candidata-a-partir`, `formato-anterior`: pasarla por `existente`;
   - `ciclo`, `ciclo-requiere`, `requiere-redundante`, `relacionado-en-jerarquia`, `relacionado-asimetrico`: cuál relación sobra o falta;
   - `volatil-en-nucleo`: mover el nombre a una `ficha` y dejar el concepto;
   - `cifra-sin-evidencia`: buscar la fuente, quitar la cifra, o decir en la nota que es una cuenta propia;
   - `pregunta-sin-nota`, `responde-inexistente`, `umbral`, `alcance-sin-aprobar`: ajustar el `ALCANCE.md` o las notas con la persona;
   - `sin-fuentes`: buscar la fuente o marcar el hueco;
   - `obsoleto-sin-reemplazo`, `reemplazo-sin-obsoleto`: borrarla si nada la enlaza, o corregir el estado;
   - `id-duplicado`, `nombre-de-archivo`, `campo-faltante`, `valor-invalido`, `resumen-distinto`, `muletilla`, `ruta-sin-enlace`, `borrador-revisado`: el arreglo puntual;
   - `pendiente-de-revision`: recordarle a la persona qué borradores esperan su lectura;
   - una contradicción: cuál es la fuente de verdad y cómo queda la otra.
6. Aplicá solo lo que la persona aprueba, en un PR. Una revisión confirmada actualiza `revisado` a hoy.

Terminás cuando cada hallazgo tiene un arreglo aplicado o la decisión de la persona de dejarlo.

## Verificar

Cuatro pruebas, en este orden. Cada una atrapa algo que las otras no ven.

1. **Prosa**: una pasada con la skill `humanizer` si está disponible; si no, con las reglas de "Prosa" de `metodo.md`. Antes de la pasada guardá una copia. Después extraé los números, las URLs y los enlaces de cada nota y compará contra la copia: tienen que ser los mismos. Si cambió una primera línea, cambiá el `resumen` igual.
2. **Lint**: sale con 0 errores. Los avisos se leen y se arreglan, o se justifican en el PR.
3. **Cotejo con fuentes**: un subagente por nota, o por grupo de notas que comparten fuentes, recibe la nota y sus `fuentes` (el informe de `.investigacion/`, el código, la página) y devuelve cada afirmación que la fuente no sostiene o contradice. El material que llega de otro doc se coteja igual, porque puede estar desactualizado. Si ninguna fuente registra el porqué de una decisión, no se deduce: la nota dice que no quedó registrado.
4. **Lector en frío**: atrapa lo que la nota da por sabido.
   - **Preguntas**: en un tema con `ALCANCE.md`, sus preguntas. Si no hay, quien escribe redacta por nota la pregunta del título y dos o tres preguntas que haría un lector.
   - **Lector**: un subagente sin este contexto, que recibe solo la ruta del Mapa del tema (o de la nota) y las preguntas. Navega por los enlaces, responde cada una **citando el archivo y el párrafo**, y lista las contradicciones entre notas, los enlaces que faltan y los términos sin definir.
   - **Juicio**: lo hace quien escribe, no el lector, porque el lector no conoce las respuestas correctas. Una respuesta sin cita, con una cita que no la sostiene o que no coincide con las fuentes, es un hueco. Una respuesta a medias cuenta como respondida solo si lo que falta es un hueco declarado en la nota.
   - **Arreglo**: se corrige la nota y se repite con un subagente nuevo, enfocado en lo que falló.
   - Los Mapas y las Rutas no pasan esta prueba por sí mismos: son listas, y su control es que cada línea diga qué responde la nota y cuándo leerla.

Terminás cuando la prosa no perdió nada, el lint da 0 errores, el cotejo no deja afirmaciones sin sostén y el lector cita una respuesta válida para cada pregunta.

Los subagentes de cotejo y de lector se lanzan de a varios en paralelo. Un orquestador de muchos agentes (un workflow) se usa solo si la persona lo pidió.

## Sin archivos

En un chat donde no podés escribir archivos (claude.ai sin acceso al repo), seguí [`conversacion.md`](conversacion.md).
