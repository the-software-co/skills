# Skills de The Software Company

Marketplace de plugins de Claude Code.

## `documentar`

Documenta un tema cualquiera (Excel, Kubernetes, lagartos) como una base de conocimiento en Markdown
en [`the-software-co/biblioteca`](https://github.com/the-software-co/biblioteca): te entrevista en tres
rondas cortas, fija el alcance y las preguntas antes de escribir, parte el tema en áreas genéricas, separa el núcleo estable de lo volátil,
enlaza concepto a concepto con relaciones con tipo y, si es para aprender, arma una ruta de práctica.
El método está en
[`metodo.md`](plugins/documentar/skills/documentar/metodo.md) y su porqué en
[`docs/research/skill-documentar.md`](docs/research/skill-documentar.md).

```
/plugin install documentar@the-software-co
python3 plugins/documentar/skills/documentar/revisar.py <carpeta del tema>
```

## `tsc-organizacion`

El mapa de los repos de negocio y conocimiento en tres capas: lo general (`conocimiento`), cómo lo hacemos (`fundar`, `marketing`) y las empresas (`tsc-negocio`, `lind-negocio`), con cómo pasa algo de una capa a otra y el panorama de lo pendiente en todos.

```
/plugin install tsc-organizacion@the-software-co
```

## `conocimiento`

Estructura conocimiento en notas atómicas enlazadas, en un vault de Obsidian o en los docs de un
repo: una nota por pregunta, lo estable separado de lo volátil, Mapas y Recorridos curados,
reglas de prosa y chequeos de frescura. Tiene cuatro modos: `nuevo`, `existente`, `volcar` y
`mantener`. El método está en
[`metodo.md`](plugins/conocimiento/skills/conocimiento/metodo.md).

### Instalar

En Claude Code:

```
/plugin marketplace add the-software-co/skills
/plugin install conocimiento@the-software-co
```

Para actualizar: `/plugin marketplace update the-software-co`.

En claude.ai: comprimí la carpeta
[`plugins/conocimiento/skills/conocimiento`](plugins/conocimiento/skills/conocimiento) en un zip
y subilo en Settings → Capabilities → Skills.

En cualquier otro chat: `./scripts/prompt-portable.sh` imprime el método y las plantillas como un
solo prompt para pegar.

### Usar

Pedile a Claude que documente un tema, que ordene una carpeta de notas, que guarde un concepto o
que revise qué quedó viejo. Para chequear una carpeta a mano:

```
python3 plugins/conocimiento/skills/conocimiento/revisar.py <carpeta>
```

Si tu base tiene convenciones propias (quiénes son dueños, carpetas especiales, dónde se registra
lo volcado), escribilas en un `CONVENCIONES.md` en su raíz: el skill lo lee antes de escribir.

## Licencia

MIT
