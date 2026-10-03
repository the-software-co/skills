# Conocimiento: estructurar y volcar en una conversación

Vas a ayudar a la persona a estructurar conocimiento en notas atómicas enlazadas, siguiendo el
método y las plantillas que están más abajo. En esta conversación no podés escribir archivos: cada
nota la entregás como un bloque de Markdown completo (frontmatter incluido) con su ruta arriba,
para que la persona la pegue en Obsidian o en el repo.

1. **Entender el pedido**: un tema nuevo, una nota existente para reestructurar (que la persona
   te pega o que leés con las herramientas del vault, si las tenés), o un concepto suelto para
   volcar; y en qué idioma van las notas, español o inglés.
2. **Buscar lo que ya existe**: si tenés herramientas para buscar y leer en el vault, buscá el
   término y sus sinónimos, y leé el `CONVENCIONES.md` de la raíz de la base si existe. Si no,
   preguntale a la persona qué notas tiene sobre el tema. Lo que existe se amplía o se enlaza.
3. **Proponer el mapa antes de escribir**: cada nota con su archivo, `tipo`, `resumen` y pregunta;
   sus `parte_de` y `requiere`; en qué Mapa entra; y qué notas existentes se amplían. Esperá a que
   la persona lo apruebe.
4. **Escribir**: una nota por bloque, desde la plantilla de su tipo, con `estado: borrador`,
   `autoria: ia` y la fecha de hoy en `creado`. Si el destino es un vault de Obsidian, enlaces
   `[[id]]`; si es un repo, enlaces Markdown relativos. Al final, el bloque del Mapa con las
   líneas nuevas.
5. **Cerrar**: decile a la persona la ruta de cada nota, y que las pase a `vigente` con
   `revisado` de ese día cuando las haya leído.
