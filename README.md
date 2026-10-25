# javidesignlabs — portfolio v2

Sitio estático (HTML/CSS/JS vanilla, cero dependencias, cero build) — rediseño
completo tipo estudio sobre la identidad lime/dark original.

## Sistema de diseño

- **Display**: Syne 700/800 (mayúsculas, titulares gigantes)
- **Body**: Instrument Sans
- **Datos/labels**: Space Mono (eyebrows, años, métricas)
- **Paleta**: void `#0B0B09` · cream `#EFEDE3` · lime `#C8FF4D`

## Interacciones

- Secuencia de carga del hero (líneas que entran por máscara)
- Reveals al hacer scroll (IntersectionObserver)
- **Preview flotante que sigue al cursor** en la lista de proyectos (desktop);
  en móvil se muestra la miniatura inline
- Cursor dot con mix-blend-mode difference (solo desktop, respeta reduced-motion)
- Header con blur al hacer scroll, menú móvil fullscreen
- Acordeón de carrera accesible por teclado (Enter/Espacio)
- Marquee de clientes reales (MotoGP, Bolttech, BASF, Desigual…)
- Sección "Results with receipts": métricas reales extraídas de tus case
  studies con su fuente (45% Bolttech, 23% Desigual, 17% MotoGP, 15% portals)
- Navegación secuencial entre case studies ("Next case study →")

## Estructura

Igual que antes: `index.html`, `projects.html`, `about.html`, `404.html`,
`projects/*.html` (los casos publicados; el número lo decide `_ORDER` en `build/data.py`),
`assets/`, y el generador en `build/`.

## Editar contenido

Edita `build/data.py` (textos, métricas PROOF, clientes CLIENTS, capacidades
CAPABILITIES) o `build/templates.py` (header/footer) y ejecuta:

```bash
cd build && python3 generate.py
```

## Imágenes

Enlazadas en vivo desde tu CDN de Framer (framerusercontent.com) y el CV desde
tu Dropbox. Si algún día cierras Framer, descarga esas imágenes a `assets/img/`
y actualiza los `cover_img` en `build/data.py` + los avatares en `PROFILE`.

## Deploy

Push a `main` → GitHub Pages redeploya solo. Nada más que hacer.

## Curaduría del portfolio (revisión 10/2026)

Decisiones tomadas tras la revisión y por qué, para no deshacerlas sin querer:

- **Las cifras son contrato.** Cada métrica de la home aparece idéntica en su caso,
  con una línea de cómo se midió. Si cambias un número en `PROOF` (en `build/data.py`),
  cámbialo también en el `impact` del caso y en el timeline de `CAREER`. El titular
  "Measured, not claimed" depende de eso.
  Cifras vigentes: Supply Chain **40%**, Desigual **23%**, renovaciones MotoGP **17%**,
  partner portals **15%**.
- **Orden y recorte** viven al final de `build/data.py`, en `_ORDER` y `_RETIRED`.
  La home muestra `HOME_FEATURED = 4` casos. Primero va trabajo de design system
  profesional, no el proyecto personal.
- **Casos retirados** (email marketing, landing pages, store locator de 2014): siguen
  en `data.py` pero fuera de `_ORDER`, así que no se publican ni entran en el sitemap.
  Para recuperar uno, basta con añadirlo a `_ORDER` y quitarlo de `_RETIRED`.
- **Autoría**: cada caso tiene `role` concreto y una línea `authorship` que separa lo
  tuyo de lo del equipo. El caso de BASF además lleva `nda` con la nota de confidencialidad.
- **Visuales de BASF y Bolttech** son diagramas SVG propios en `assets/img/<slug>/`,
  redibujados de forma genérica: no hay interfaz real de cliente. Si algún día puedes
  enseñar material real, sustituye el `gallery` del caso.
- **El hero** no ocupa la pantalla completa a propósito: `heroCap()` en `assets/js/main.js`
  limita el titular por altura disponible para que el primer caso asome. Si cambias el
  tamaño del hero, revisa esa constante `RESERVE`.

## Segunda pasada de revisión (23/10/2026, noche)

- **Bolttech es una contribución, no un liderazgo.** El caso dice "Product Designer —
  contributor": componentes, tokens y documentación en Zeroheight; el sistema lo llevaba
  el equipo de diseño. Tiene que seguir coincidiendo con About, el CV y LinkedIn — si
  cambias uno, cambia los tres.
- **BASF no tiene permiso formal**, así que la nota dice "Described at a structural level",
  no "Shown with permission". No la cambies sin tener el permiso por escrito.
- **Los titulares no parten palabras a partir de 375px.** Eso depende de tres cosas:
  `overflow-wrap:normal` en h1/h2/h3, los `clamp()` de `.t-giant` / `.t-sect` y los topes
  por columna (`.process-side`, `.caps-copy`, `.page-hero h1`). Si agrandas un titular,
  vuelve a comprobar a 375px con una palabra larga.
- **Los artefactos de payment-renewal, partner-portals y desigual** son diagramas míos y
  genéricos, igual que los de BASF y Bolttech.

## Tercera pasada: separar el trabajo de BASF en dos casos (25/10/2026)

- **BASF son ahora dos casos, no uno.** `basf-design-system` es el sistema; el portal
  multi-mercado se separó en `basf-customer-portal` con su propio eje: **arquitectura
  multi-mercado**. El caso del sistema se limpió de todo lo que era del portal (el
  problema multi-mercado y su learning se movieron al caso nuevo) — si vuelves a mezclarlos,
  los dos casos pierden el foco.
- **El slug evita el nombre interno del producto a propósito.** Se llama
  `basf-customer-portal`, no el nombre en clave que aparece en el Figma. El nombre interno
  no sale en ningún sitio: ni en la URL, ni en el título, ni en el texto. No lo metas.
- **El caso nuevo lleva el mismo `nda`** que el otro: "Described at a structural level".
  BASF sigue sin permiso formal.
- **Los tres SVG de `assets/img/basf-customer-portal/`** (cover, entry, rules) son diagramas
  míos, redibujados de forma genérica, cada uno con su nota de "no production interface shown".
  Describen decisiones de estructura (país antes del login; reglas de mercado como datos),
  no pantallas reales.
- **`roku-tv-app` está retirado**: era el caso más antiguo y el único sin ningún dato.
  Como todos los retirados, su página pasa a ser un redirect `noindex` a `projects.html`.
- **Los títulos de caso se quedan entre ~25 y ~70 caracteres.** El del portal empezó en 90 y
  ocupaba siete líneas de display en desktop. Si escribes uno más largo, míralo renderizado
  antes de darlo por bueno.

## Imágenes de compartir (og:image)

El `og:image` apuntaba a un asset del CDN de Framer que **era la captura de una plantilla**
("Webstack", de otro diseñador). Al compartir cualquier página salía el portfolio de otro.
Estaba en las 14 páginas.

Ahora las tarjetas son propias y están autoalojadas en `assets/img/og/`:

- `site.png` para home, projects, about, privacy y 404
- una por caso publicado, con su título y su outcome

Se generan con:

```bash
cd build && python3 ogimages.py    # necesita playwright y las woff2 de assets/fonts
```

Reglas para no repetir el error:

- **El `og:image` siempre absoluto y siempre en tu dominio.** Nunca un CDN que no controles.
- **Si cambias el título o el `outcome` de un caso, vuelve a correr `ogimages.py`** — la
  tarjeta lleva el texto quemado en el PNG. `generate.py` avisa si falta alguna tarjeta,
  pero no detecta que una esté desactualizada.
- Los PNG van comprimidos a 128 colores (1,4 MB → 500 KB en total). Si regeneras, vuelve a
  comprimirlos o el repo engorda.
- Después de desplegar, pasa la URL por el validador de LinkedIn/X; los dos cachean el
  preview una temporada.

**Pendiente, del mismo problema:** las portadas de los casos antiguos y tus avatares siguen
servidos desde `framerusercontent.com`. Funcionan, pero el día que cierres Framer desaparecen.
Hay que descargarlas a `assets/img/` y actualizar los `cover_img` de `data.py` y los avatares
de `PROFILE`.
