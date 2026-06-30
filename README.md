# javidesignlabs — portfolio site

Sitio estático (HTML/CSS/JS vanilla, sin frameworks ni build tools) generado a partir
del diseño de javidesignlabs.com: home, listado de proyectos, 10 case studies, about y 404.

## Estructura

```
.
├── index.html              ← Home
├── projects.html            ← Listado "Selected work"
├── about.html               ← About & Contact
├── 404.html                  ← Página de error (GitHub Pages la usa automáticamente)
├── assets/
│   ├── css/style.css
│   ├── js/main.js            ← menú móvil, acordeón del timeline, nav activo
│   └── img/favicon.svg
├── projects/
│   ├── saas-supply-chain.html
│   ├── bolttech-design-system.html
│   ├── partner-portals.html
│   ├── saas-process-modeling.html
│   ├── payment-renewal.html
│   ├── landing-pages-dorna.html
│   ├── roku-tv-app.html
│   ├── email-marketing-dorna.html
│   ├── desigual-product-card.html
│   └── desigual-store-locator.html
└── build/                    ← Generador Python (opcional, solo para editar contenido)
    ├── data.py                ← Todo el copy de los 10 proyectos, timeline, testimonios
    ├── templates.py            ← Header / marquee / footer reutilizables
    ├── illustrations.py        ← Ilustraciones SVG abstractas por categoría de proyecto
    └── generate.py              ← Script que renderiza los 14 .html
```

## Cómo editar el contenido

Las páginas HTML están generadas, no las edites directamente si quieres volver a
generar después — edítalas en `build/data.py` (textos de cada proyecto) o
`build/templates.py` (header/footer) y vuelve a correr:

```bash
cd build
python3 generate.py
```

Esto regenera los 14 `.html` con los mismos estilos y estructura.

Si prefieres editar directamente el HTML final sin tocar el generador, también
puedes hacerlo — son archivos planos, sin build step para publicarlos.

## Imágenes y enlaces reales

Las fotos, capturas de cada proyecto, tu CV y los enlaces (LinkedIn, X, Cal.com,
"Visit website" de cada caso) están **enlazados directamente desde tu propia
web de Framer** (`framerusercontent.com` y tu Dropbox), no copiados al repo.
Es tu contenido real, simplemente referenciado por URL en vez de descargado —
así el sitio se ve igual que el original sin tener que subir archivos pesados
a GitHub.

**Importante**: esto depende de que esas URLs sigan activas. Si en algún
momento dejas de pagar Framer o borras esos assets, las imágenes y el link
del CV se romperán en este sitio también. Si quieres independencia total,
descarga esas imágenes tú mismo y súbelas a `assets/img/`, luego cambia los
`src="https://framerusercontent.com/..."` por rutas locales como
`assets/img/saas-supply-chain-cover.jpg` en `build/data.py` (campo
`cover_img` de cada proyecto) y en `build/templates.py` (avatares).

El avatar pequeño (header/hero), el de "About me" y el del footer son tres
fotos distintas — así estaban en el original — definidas en
`build/data.py` dentro de `PROFILE`.

## Publicar en GitHub Pages

1. Crea un repositorio nuevo en GitHub (puede ser público o privado con GitHub Pro).
2. Desde esta carpeta:

   ```bash
   git init
   git add .
   git commit -m "Initial portfolio site"
   git branch -M main
   git remote add origin https://github.com/TU_USUARIO/TU_REPO.git
   git push -u origin main
   ```

3. En GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch**,
   elige la rama `main` y la carpeta `/ (root)`. Guarda.
4. En uno o dos minutos tu sitio estará disponible en:
   `https://TU_USUARIO.github.io/TU_REPO/`

   Si el repo se llama `TU_USUARIO.github.io`, la web quedará en la raíz:
   `https://TU_USUARIO.github.io/`

### Dominio propio (opcional)

Si quieres usar `javidesignlabs.com`:
1. Crea un archivo `CNAME` en la raíz con el dominio dentro (una sola línea: `javidesignlabs.com`).
2. En tu proveedor DNS, añade un registro `A` apuntando a las IPs de GitHub Pages
   (185.199.108.153, .109.153, .110.153, .111.153) o un `CNAME` a `TU_USUARIO.github.io`
   si usas un subdominio.
3. En GitHub → Settings → Pages, escribe el dominio en "Custom domain" y activa
   "Enforce HTTPS" en cuanto esté disponible.

## Actualizar la web después de publicarla

Cada vez que quieras actualizar contenido:

```bash
# edita build/data.py o el HTML directamente
cd build && python3 generate.py   # si tocaste data.py
cd ..
git add .
git commit -m "Update content"
git push
```

GitHub Pages redeploya automáticamente con cada push a `main`.
