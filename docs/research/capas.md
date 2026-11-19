# Capas del sujeto en lugar de áreas genéricas (documentar 0.4.0)

## Qué pasó

La primera corrida real de `ampliar` (Marketing, `mtsdlf/conocimiento#11`) produjo 34 notas correctas en contenido y malas en forma. El dueño de la base lo resumió así: la entrevista hizo preguntas que el contexto ya respondía (quién es el dueño, "contame la última vez que lo usaste", aunque había dado Lind y TSC como contexto), y la estructura de carpetas, la profundidad y los títulos de sección no eran los que quería.

## Por qué salió así

1. **La entrevista venía de la investigación de usuarios.** F1 a F4 (último caso, uso, quién, material) son preguntas de descubrimiento de producto. Sirven cuando no se sabe nada de la persona; en una organización con repos que describen el uso, cada una es una pregunta evitable. La regla de saltear lo respondido solo se activaba si el pedido "traía todo".
2. **La estructura venía del tipo de pregunta, no del sujeto.** Las 11 áreas (`que-es`, `como-funciona`, `como-se-decide`…) son ejes de documentación al estilo Diátaxis: valen para cualquier tema y por eso no dicen nada de ninguno. Las carpetas terminaron agrupando por tipo de discusión ("Escuelas y fuentes", "Persuasión", "B2B y salida al mercado") en lugar de por las partes del marketing.
3. **Los títulos venían de la plantilla.** Cada tipo de nota tenía secciones fijas ("Por qué existe", "No confundir con", "Para profundizar", "Relaciones"); "Relaciones" aparecía 62 veces y repetía el frontmatter.
4. **El tope de 450 palabras atomizaba.** Una idea suelta por nota, y una red de relaciones con tipo (`es_un`, `parte_de`, `instancia_de`, `requiere`, `relacionado`) para recomponerla.

## Qué cambia

- **Capas de abstracción**: el todo, las verticales (las partes en que el sujeto se divide, una carpeta cada una), los componentes y lo operativo abajo. Es la descomposición que se usa para analizar un sistema, y el mismo criterio que siguen los buenos libros de texto: el índice es el sujeto partido en sus partes. Lo transversal (historia, escuelas, fuentes, glosario) va a `Fundamentos/`.
- **Lo volátil abajo**: la regla de núcleo y periferia sale sola de las capas, sin listas de volátiles ni lint de nombres de productos.
- **Alinear en un mensaje**: leer el contexto primero, proponer el árbol y hacer como mucho tres preguntas sobre el tema. Nada sobre la persona que el contexto ya diga.
- **Títulos con las palabras del tema** y una sola plantilla de nota sin secciones fijas.
- **Frontmatter de seis campos**; las relaciones son enlaces en el cuerpo, y la jerarquía la dan las carpetas.
- **Lint chico**: enlaces, campos, huérfanas, carpetas sin entrada, vencimientos, títulos de plantilla, largo y muletillas; más `fuente-cambiada` y `--desde` para los repos con código.

## Qué se conserva

La investigación por ángulos con el brief fijo, el mapa de fuentes por tipo de pregunta, la escuela, la posición contraria, el plan B para fuentes bloqueadas, `.investigacion/`, las cuatro pruebas de Verificar y la regla de borrador hasta que una persona confirma. Lo que funcionó en la corrida de Marketing (las fuentes, las correcciones de cifras, los huecos declarados) salió de ahí.

`entrevista-previa.md` y `skill-documentar.md` quedan como historia de la versión 0.3.
