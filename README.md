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
`projects/*.html` (10 case studies), `assets/`, y el generador en `build/`.

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
