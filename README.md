# Skills de The Software Co

Marketplace de plugins de Claude Code.

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
