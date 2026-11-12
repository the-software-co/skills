---
name: tsc-organizacion
description: El mapa de los repos de negocio y conocimiento (conocimiento, fundar, marketing, tsc-negocio, lind-negocio) en tres capas, y cómo pasa algo de una capa a otra. Usar cuando una sesión en cualquiera de esos repos tiene que decidir dónde va algo, llevar algo aprendido a otro repo, o cuando la persona pide el panorama de todo («¿qué hay pendiente en todo?», «¿dónde va esto?»).
---

# La organización: las capas

Los repos se ordenan en tres capas. Cada una sirve a la de abajo, y ninguna habla de la de arriba.

| Capa | Qué guarda | Repos |
|---|---|---|
| **1. Conocimiento** | Lo que es verdad para cualquiera: conceptos técnicos, de datos, de cualquier tema. Agnóstico a todo | `mtsdlf/conocimiento` (vault de Obsidian) |
| **2. Cómo lo hacemos** | Nuestros métodos, agnósticos a la empresa: cómo se emprende, cómo se hace marketing | `mtsdlf/fundar` (emprender, de libros y la práctica), `mtsdlf/marketing` (el método de marketing y su vertical) |
| **3. Las empresas** | Cada empresa aplicando los métodos: su modelo, sus precios, sus clientes, sus decisiones | `mtsdlf/tsc-negocio` (la consultora), `mtsdlf/lind-negocio` (Lind) |

Fuera de las capas están los sistemas: la plataforma que construye (`the-software-co/automated-software-building-platform`), el back-office común (`mtsdlf/emprendimientos`, su `bootstrap/`) y el producto de Lind (`the-software-co/nube-*`, `tiendanube-exploration`). Las empresas los leen como semilla o por su entrada, y no se le muestran a quien lleva el negocio.

## Cómo pasa algo de una capa a otra

- **Hacia abajo se cita, nunca se copia.** Una empresa enlaza la nota de `fundar` o el método de `marketing` que aplica. La única copia es la semilla: un sistema copiado en un commit fijo.
- **Hacia arriba sube lo que dejó de ser de una sola empresa.** Lo que una empresa probó y funcionó, y serviría a otra, se propone como método en la capa 2. Lo que es un concepto general, sin método nuestro, va a la capa 1. Se sube en el modo `volcar` de la skill `conocimiento`, sin nombres de empresas ni de clientes.
- **Cada repo decide lo suyo.** Lo que se necesita de otro repo se pide por su entrada (un issue), y lo decide quien lo lleva.

## Dónde va algo

1. **Habla de una empresa en particular** (su precio, un cliente, una decisión): capa 3, en el repo de esa empresa.
2. **Es cómo hacemos algo, y serviría a cualquiera de nuestras empresas:** capa 2, en `fundar` si es sobre emprender y en `marketing` si es marketing.
3. **Es un concepto general:** capa 1.

Ante la duda entre dos capas, va a la más baja (la más concreta) y sube cuando otra empresa lo necesite.

## El panorama

Si la persona pide el panorama de todo, juntá con `gh issue list -R mtsdlf/<repo>` los issues abiertos de `tsc-negocio`, `lind-negocio`, `marketing` y `fundar`. Primero los que tienen el label `dueño`, después los suyos y después el resto, por repo y en una línea cada uno. Cerrá con las fechas próximas que aparezcan en `el-taller/preguntas-abiertas.md` de cada empresa.
