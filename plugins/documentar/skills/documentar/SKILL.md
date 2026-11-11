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

### 1. Alcance

Escribí `<tema>/ALCANCE.md` desde [`plantillas/alcance.md`](plantillas/alcance.md):

- **intención** (aprender, consultar, decidir, operar), **audiencia** y **nivel previo**: lo que la persona dijo; lo que no dijo, decidilo vos y marcalo como supuesto;
- **fuera de alcance**: lo vecino que no entra;
- **preguntas**: de 3 a 5 esenciales y de 10 a 20 de cobertura, cada una con el área que la responde. Son el test del paso 6;
- **tamaño**: un relevamiento rápido (una búsqueda, la taxonomía propia del dominio si la tiene) y la cuenta de notas que va a llevar. Si pasa de unas 40 notas, o el tema tiene partes que se aprenden por separado, partilo en sub-temas y decí cuáles se documentan ahora;
- **volátiles**: productos, versiones, marcas y cifras del tema que el núcleo no puede nombrar.

Si el tema es de la persona (su sistema, su colección, su oficio), entrevistala sobre dos o tres casos reales antes de escribir las preguntas: el experto no ve lo que omite.

Terminás cuando mostraste el `ALCANCE.md` completo y la persona lo aprobó o lo corrigió. Anotá la fecha en `aprobado`.

### 2. Investigar

Despachá un subagente por ángulo: uno por área con preguntas, uno para la taxonomía propia del dominio, uno para los recursos canónicos (los que van a ser puente) y uno que busque **la posición contraria** y las concepciones erróneas documentadas. Cada uno devuelve afirmaciones con su URL, y las fuentes se puntúan como dice "Fuentes" en `metodo.md`. Tope: tres rondas por ángulo; lo que no se encuentra se declara como hueco.

Terminás cuando cada pregunta del `ALCANCE.md` tiene al menos una fuente primaria o un hueco declarado, y cada concepto umbral candidato tiene fuente o queda marcado como hipótesis.

### 3. Mapa propuesto

Mostrale a la persona, antes de escribir una sola nota:

- cada nota: archivo, `tipo`, `area`, `resumen` y qué preguntas `responde`;
- sus relaciones `es_un`, `parte_de`, `instancia_de` y `requiere`;
- los conceptos umbral (de 3 a 7);
- qué notas son puente a un recurso de afuera y cuál es ese recurso;
- el orden de la ruta, si la intención incluye aprender.

Terminás cuando toda pregunta tiene al menos una nota que la responde, toda área sin notas está justificada como poda, y la persona aprobó.

### 4. Escribir

Primero el núcleo (áreas estables: qué es, cómo funciona, anatomía, procesos, historia, cómo falla), después la periferia (cómo se hace, cómo se decide, ecosistema, referencia) y al final la ruta y el Mapa. Cada nota desde su plantilla, con `estado: borrador`, `autoria: ia` y `creado` de hoy. Cada nota nueva entra al Mapa en el mismo cambio.

El Mapa `responde` las preguntas esenciales; las de cobertura, las notas.

Terminás cuando existe cada nota del mapa aprobado y el Mapa enlaza a todas.

### 5. Verificar

1. `python3 revisar.py <carpeta del tema>` (al lado de este archivo) sale con 0. Los avisos se leen y se arreglan o se justifican en el PR.
2. **Lector en frío**: un subagente que recibe solo la ruta del `README.md` del tema, sin este contexto, responde cada pregunta del `ALCANCE.md` navegando desde el Mapa y **citando el archivo y el párrafo** que la responde. Una respuesta sin cita, o con una cita que no la sostiene, es un hueco: se arregla la nota y se repite con un subagente nuevo.
3. Pasada de prosa: si la skill `humanizer` está disponible, sobre cada nota; si no, las reglas de "Prosa" de `metodo.md`. Ningún hecho, número, nombre ni fuente se pierde en la pasada.

Terminás cuando el lint da 0, el lector en frío cita una respuesta válida para cada pregunta y la pasada de prosa está hecha.

### 6. Entregar

Commit en la rama `tema/<tema>`, push y PR en `biblioteca`. El cuerpo del PR lleva el Mapa resumido, los huecos declarados, los supuestos del alcance y los avisos del lint que quedaron. Sumá el tema al `README.md` raíz de la biblioteca.

Decile a la persona que las notas están en `borrador`: pasan a `vigente`, con `revisado` de ese día, cuando ella las lee y las confirma.

## `ampliar`

Leé el `ALCANCE.md` y el Mapa del tema. Sumá las preguntas nuevas al `ALCANCE.md` (con la ampliación como sub-tema si es grande) y pedí la aprobación; después seguí los pasos 2 a 6 solo para lo nuevo, enlazándolo con lo que ya existe. Lo que ya estaba explicado se enlaza, no se repite.

## `mantener`

1. `python3 revisar.py <carpeta> --json`.
2. Re-verificá contra sus fuentes las notas `volatil` vencidas y los recursos puente (link caído o texto que cambió).
3. Para cada afirmación que cambió: si la vieja es historia, marcala como dice "Obsoleto y disputado" en `metodo.md` y actualizá en cascada toda nota que la repite o la usa (buscá también por `aliases`).
4. Proponé los arreglos agrupados y aplicá los que la persona aprueba, en un PR.
