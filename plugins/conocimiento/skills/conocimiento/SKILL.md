---
name: conocimiento
description: Estructura conocimiento en notas atómicas enlazadas, en un vault de Obsidian o en los docs de un repo. Usar para documentar un tema nuevo, reestructurar documentación existente, volcar un concepto suelto a su lugar, o revisar documentación desactualizada.
---

# Conocimiento

Antes de cualquier modo, leé [`metodo.md`](metodo.md): es la fuente de verdad de cómo se parte,
se nombra, se relaciona, se escribe y se mantiene una nota. Cada nota nueva sale de la plantilla
de su tipo en [`plantillas/`](plantillas/). Los términos Tema, Mapa, Recorrido y los tipos de nota
están definidos ahí.

Elegí el modo por lo que pide la persona:

| Pide | Modo |
|---|---|
| documentar un tema que no está | `nuevo` |
| ordenar o mejorar documentación que ya existe | `existente` |
| llevar un concepto suelto o una nota cruda a su lugar | `volcar` |
| ver qué está viejo, roto, huérfano o contradictorio | `mantener` |

## Antes de escribir: dónde, en qué idioma y qué ya existe

1. **Dónde**: la base de conocimiento es un vault de Obsidian o los docs de un repo. Si hay más
   de una posible, preguntá.
2. **Convenciones locales**: si la raíz de la base tiene un `CONVENCIONES.md`, leelo y seguilo.
   Dice lo propio de esa base: los dueños posibles, carpetas especiales y dónde se registra lo
   que se vuelca. Lo que diga ahí manda sobre los ejemplos de `metodo.md`.
3. **Destino**: si hay un `.obsidian/` en la carpeta o arriba, `obsidian`; si no, `ambos`. La
   persona puede pedir el otro.
4. **Idioma**: el que pida la persona; si no dice, el de las notas del Tema.
5. **Buscar** el término, sus sinónimos y su traducción en toda la base (grep, o la herramienta
   de búsqueda del vault si la hay). Lo que ya existe se amplía o se enlaza.
6. **Mapas**: ubicá el Mapa raíz y el Mapa del Tema. El que falte se crea primero, antes que las
   notas que lo nombran en `parte_de`.

Terminás cuando tenés la carpeta, el destino, el idioma, la lista de notas que tocan el tema y
los Mapas donde van a entrar.

## Investigar

Cuando falta material, investigá en fuentes primarias: documentación oficial, papers, libros y
textos de referencia. Despachá un subagente por subtema, que devuelva afirmaciones con su URL,
y verificá vos cada URL antes de ponerla en `fuentes`. Lo que dice una sola fuente secundaria se
atribuye en el texto; lo que es inferencia propia se dice como inferencia.

## `nuevo`

1. **Material**: el que trajo la persona; lo que falte, investigalo.
2. **Mapa propuesto**: antes de escribir una sola nota, mostrale a la persona:
   - cada nota: archivo, `tipo`, `resumen` y su pregunta;
   - sus relaciones `parte_de` y `requiere`;
   - el Mapa del Tema y, si es para aprender, el Recorrido en orden;
   - qué notas existentes se amplían en vez de crear.

   Terminás cuando la persona aprueba la propuesta o la corrige y la aprueba.
3. **Escribir**: una nota por archivo, desde su plantilla, siguiendo la Prosa de `metodo.md`, con
   `estado: borrador`, `creado` de hoy y `autoria: ia`. Después, el Mapa, el Recorrido y el enlace
   desde el Mapa padre.
4. **Verificar**:
   - `python3 revisar.py <carpeta del Tema>` (está al lado de este archivo) sin errores;
   - la prueba del lector en frío de `metodo.md` aprobada en cada nota, con un subagente por nota
     que solo ve esa nota.
5. **Entregar**: decile a la persona qué notas quedaron en `borrador` para que las lea. Las que
   confirme pasan a `vigente` con `revisado` de ese día.

## `existente`

1. **Auditar**: corré `revisar.py` sobre la carpeta y leé cada nota entera. Para cada sección de
   cada nota decidí una o varias:
   - **partir**: responde otra pregunta;
   - **fusionar**: explica lo mismo que otra;
   - **aislar lo volátil**: comandos, valores o nombres que van a una `ficha` o a un enlace;
   - **borrar**: no aporta (relleno, restos de un chat, ejercicios vacíos, consultas de plugins);
   - **conservar**: queda como está, con el frontmatter nuevo.

   Lo que la nota solo nombra se completa investigando, marcado en la propuesta.
2. **Mapa propuesto**: como en `nuevo`, con la columna de origen: de qué nota y sección vieja sale
   cada nota nueva. Sumá las preguntas que solo la persona puede responder (de dónde sale un
   material, si algo es de un empleador). Esperá la aprobación.
3. **Reestructurar**: escribí las notas nuevas como en `nuevo`, mové el contenido (se borra del
   origen), actualizá los enlaces que apuntaban a las notas viejas en toda la base y borrá las que
   quedaron vacías. Los originales que se traducen o se reemplazan enteros van a `Archivo/`.
4. **Verificar** como en `nuevo` y contale a la persona cuántas notas había, cuántas quedaron y
   qué se borró.

## `volcar`

Para un concepto suelto, una nota cruda o algo aprendido que la persona quiere guardar.

1. **Buscar** como en "Antes de escribir" y decidí uno:
   - **ampliar** una nota existente, si responde la misma pregunta;
   - **crear** una nota, si es una pregunta nueva;
   - **partir** una nota, si al sumarle esto respondería dos preguntas;
   - **solo enlazar**, si ya está explicado.
2. **Proponer**: decile a la persona qué decidiste, en qué Tema y con qué relaciones. Esperá el sí.
3. **Escribir** desde la plantilla, enlazar desde el Mapa del Tema y verificar como en `nuevo`.
4. **Cerrar el ciclo**: devolvé la ruta de la nota, y registrala donde diga `CONVENCIONES.md` si
   dice algo.

## `mantener`

1. Corré `python3 revisar.py <carpeta> --json`.
2. Leé las notas de cada Tema juntas y buscá afirmaciones incompatibles entre ellas (una
   definición, una fórmula o un umbral que no coinciden).
3. Agrupá los hallazgos y, para cada uno, proponé el arreglo:
   - `enlace-roto`, `relacion-rota`: el destino correcto o sacar el enlace;
   - `revision-vencida`: releer la nota contra sus `fuentes` y decir qué cambió, o confirmar que
     sigue bien;
   - `huerfana`, `mapa-sin-padre`, `tema-sin-mapa`: en qué Mapa va;
   - `candidata-a-partir`, `formato-anterior`: pasarla por `existente`;
   - `muletilla`, `resumen-distinto`, `nombre-de-archivo`, `relacionado-asimetrico`,
     `borrador-revisado`: el arreglo puntual;
   - `pendiente-de-revision`: recordarle a la persona qué borradores esperan su lectura;
   - `obsoleto-sin-reemplazo`: borrarla si nada la enlaza;
   - una contradicción: cuál es la fuente de verdad y cómo queda la otra.
4. Aplicá solo lo que la persona aprueba. Una revisión confirmada actualiza `revisado` a hoy.
