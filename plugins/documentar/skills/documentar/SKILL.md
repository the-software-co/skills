---
name: documentar
description: Documenta un tema cualquiera (una herramienta, una tecnología, un animal, un oficio) como una base de conocimiento en Markdown en git, con áreas, enlaces concepto a concepto y ruta de aprendizaje. Usar cuando piden documentar, armar la base o la guía de un tema, ampliar o profundizar un tema ya documentado, o revisar qué quedó viejo en una base hecha con esta skill.
---

# Documentar

Armás la base de conocimiento de un **tema** en la biblioteca: una carpeta con un Mapa (`README.md`), un `ALCANCE.md` y notas enlazadas. Las reglas de cómo se parte, se escribe y se enlaza están en [`metodo.md`](metodo.md); leelo antes del paso 1. Cada nota sale de su plantilla en [`plantillas/`](plantillas/).

**Dónde**: el clon de `the-software-co/biblioteca` (buscalo en `~/repos`; si no está, clonalo). Cada tema es una carpeta en kebab-case en la raíz; un sub-tema es una sub-carpeta con su propio Mapa. Trabajás en una rama `tema/<tema>` y entregás un PR.

| Pide | Modo |
|---|---|
| un tema que no está en la biblioteca | `nuevo` |
| profundizar, sumar un sub-tema o una ruta de aprendizaje a un tema que está | `ampliar` |
| ver qué quedó viejo, roto o disputado | `mantener` |

## `nuevo`

### 1. Entrevista y alcance

Entrevistá a la persona como dice [`entrevista.md`](entrevista.md): tres rondas cortas, con preguntas fijas y dinámicas, mientras dos subagentes hacen un vistazo al tema y escanean el material que ella te pase. Con las respuestas escribí `<tema>/ALCANCE.md` desde [`plantillas/alcance.md`](plantillas/alcance.md):

- **intención** (aprender, consultar, decidir, operar), **audiencia** y **nivel previo**;
- **fuera de alcance**: lo vecino que no entra;
- **preguntas**: de 3 a 5 esenciales y de 10 a 20 de cobertura, cada una con el área que la responde. Son el test del paso 5;
- **tamaño**: la cuenta de notas que va a llevar, según la taxonomía del vistazo y la dedicación que dijo la persona. Si pasa de unas 40 notas, o el tema tiene partes que se aprenden por separado, partilo en sub-temas y decí cuáles se documentan ahora;
- **fuentes y acceso**: su material, lo pago o interno a lo que ella llega y vos no, y las fuentes canónicas públicas;
- **volátiles**: productos, versiones, marcas y cifras del tema que el núcleo no puede nombrar;
- **supuestos**: lo que decidiste por defecto.

Terminás cuando la persona respondió la devolución de la ronda 3 sin objeciones pendientes y el `ALCANCE.md` refleja esa versión. Anotá la fecha en `aprobado`.

### 2. Investigar

Despachá un subagente por ángulo: uno por área con preguntas, uno para la taxonomía propia del dominio, uno para los recursos canónicos (los que van a ser puente) y uno que busque **la posición contraria** y las concepciones erróneas documentadas. Cada uno devuelve afirmaciones con su URL, y las fuentes se puntúan como dice "Fuentes" en `metodo.md`. Tope: tres rondas por ángulo; lo que no se encuentra se declara como hueco.

Terminás cuando cada pregunta del `ALCANCE.md` tiene al menos una fuente primaria o un hueco declarado, y cada concepto umbral candidato tiene fuente o queda marcado como hipótesis.

### 3. Mapa propuesto

Mostrale a la persona, antes de escribir una sola nota:

- cada nota: archivo, `tipo`, `area`, `resumen` y qué preguntas `responde`;
- sus relaciones `es_un`, `parte_de`, `instancia_de` y `requiere`;
- los conceptos umbral (de 3 a 7);
- qué notas son puente a un recurso de afuera y cuál es ese recurso;
- el orden de la ruta, si la intención incluye aprender;
- un `glosario` (ficha de `referencia`) si el tema tiene jerga.

Terminás cuando toda pregunta tiene al menos una nota que la responde, toda área sin notas está justificada como poda, y la persona aprobó.

### 4. Escribir

Primero el núcleo (áreas estables: qué es, cómo funciona, anatomía, procesos, historia, cómo falla), después la periferia (cómo se hace, cómo se decide, ecosistema, referencia) y al final la ruta y el Mapa. Cada nota desde su plantilla, con `estado: borrador`, `autoria: ia` y `creado` de hoy. Cada nota nueva entra al Mapa en el mismo cambio.

El Mapa `responde` las preguntas esenciales, cada una con su sección; las de cobertura, las notas.

Si escribís con subagentes, cada uno recibe el mapa aprobado entero (ids, relaciones, puentes) y los informes que le tocan. Al juntar, buscá los valores que dos notas dan distinto sin explicarlo.

Terminás cuando existe cada nota del mapa aprobado y el Mapa enlaza a todas.

### 5. Verificar

1. `python3 revisar.py <carpeta del tema>` (al lado de este archivo) sale con 0. Los avisos se leen y se arreglan o se justifican en el PR.
2. **Lector en frío**: un subagente que recibe solo la ruta del `README.md` del tema, sin este contexto, responde cada pregunta del `ALCANCE.md` navegando desde el Mapa y **citando el archivo y el párrafo** que la responde. Pedile también una lista de contradicciones entre notas, enlaces que faltan y términos sin definir. Una respuesta sin cita, o con una cita que no la sostiene, es un hueco: se arregla la nota y se repite con un subagente nuevo, enfocado en lo que falló. Una respuesta a medias cuenta como respondida solo si lo que falta es un hueco declarado en la nota.
3. Pasada de prosa: si la skill `humanizer` está disponible, sobre cada nota; si no, las reglas de "Prosa" de `metodo.md`. Ningún hecho, número, nombre ni fuente se pierde en la pasada.

Terminás cuando el lint da 0, el lector en frío cita una respuesta válida para cada pregunta y la pasada de prosa está hecha.

### 6. Entregar

Commit en la rama `tema/<tema>`, push y PR en `biblioteca`. El cuerpo del PR lleva el Mapa resumido, los huecos declarados, los supuestos del alcance y los avisos del lint que quedaron. Sumá el tema al `README.md` raíz de la biblioteca.

Decile a la persona que las notas están en `borrador`: pasan a `vigente`, con `revisado` de ese día, cuando ella las lee y las confirma.

## `ampliar`

Leé el `ALCANCE.md` y el Mapa del tema. Hacé una entrevista corta, con F1, F4, F7 y las dinámicas de [`entrevista.md`](entrevista.md), sobre lo nuevo. Sumá las preguntas nuevas al `ALCANCE.md` (con la ampliación como sub-tema si es grande) y cerrá con la devolución; después seguí los pasos 2 a 6 solo para lo nuevo, enlazándolo con lo que ya existe. Lo que ya estaba explicado se enlaza, no se repite.

## `mantener`

1. `python3 revisar.py <carpeta> --json`.
2. Re-verificá contra sus fuentes las notas `volatil` vencidas y los recursos puente (link caído o texto que cambió).
3. Para cada afirmación que cambió: si la vieja es historia, marcala como dice "Obsoleto y disputado" en `metodo.md` y actualizá en cascada toda nota que la repite o la usa (buscá también por `aliases`).
4. Proponé los arreglos agrupados y aplicá los que la persona aprueba, en un PR.
