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
