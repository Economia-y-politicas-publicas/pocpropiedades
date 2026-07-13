# Cartera de Propiedades — esquema tipo "carpeta por elemento"

Este proyecto toma el esquema de organización del repo
[MasielloGroupWebsite](https://github.com/MasielloGroup/MasielloGroupWebsite)
(un sitio Quarto donde cada persona y cada publicación vive en su propia
carpeta, y una página los lista automáticamente) y lo deja limpio y
simplificado para publicar inmuebles: sin R, sin `renv`, sin plantillas
EJS — solo Quarto + una carpeta por propiedad.

## Cómo funciona

Quarto tiene una función nativa llamada **listing**: le apuntás a una
carpeta (`propiedades/`), y arma solo la grilla, las páginas de detalle
y hasta los filtros — usando el `categories:` que pusiste en cada ficha.
No hace falta CSV ni scripts generando HTML.

## Estructura

```
inmuebles-listing/
├── _quarto.yml              ← configuración del sitio (navbar, tema)
├── index.qmd                ← listing: arma la grilla+filtros solo
├── contacto.qmd
├── propiedades/
│   ├── depto-providencia/
│   │   ├── index.qmd        ← título, precio, specs, galería, descripción
│   │   └── fotos/
│   ├── casa-penalolen/
│   │   ├── index.qmd
│   │   └── fotos/
│   └── oficina-lascondes/
│       ├── index.qmd
│       └── fotos/
├── scripts/
│   └── nueva_propiedad.py   ← crea la carpeta+archivo de una propiedad nueva
├── justfile                 ← atajo `just nueva-propiedad` (como el
│                                `just newperson` del repo original)
├── styles/
│   ├── custom.scss
│   └── styles.css
├── .github/workflows/publish.yml   ← deploy automático a GitHub Pages
└── docs/                    ← salida generada (no se edita a mano)
```

## 1. Agregar una propiedad nueva

Opción con el script (te va preguntando los datos):

```bash
python3 scripts/nueva_propiedad.py
# o, si tenés 'just' instalado:
just nueva-propiedad
```

Esto crea `propiedades/<slug>/index.qmd` con el formato correcto. Después
agregás las fotos reales en `propiedades/<slug>/fotos/` (la primera,
`foto1.jpg`, es la que se usa como portada del listado).

O a mano: copiá una carpeta existente de `propiedades/`, renombrala, y
editá el `index.qmd` — el encabezado (`title`, `date`, `image`,
`categories`, `description`) es lo que alimenta la grilla y los filtros.

## 2. Previsualizar

```bash
quarto preview
```

## 3. Publicar en GitHub Pages

```bash
git init
git add .
git commit -m "Sitio de propiedades"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/TU_REPO.git
git push -u origin main
```

El workflow `.github/workflows/publish.yml` (ya incluido) renderiza con
Quarto y publica en la rama `gh-pages` en cada push. En GitHub:
**Settings → Pages → Source → rama `gh-pages`**.

## Notas

- Las fotos en `propiedades/*/fotos/` son placeholders — reemplazalas.
- Los `categories:` de cada ficha (ej. `[Disponible, Arriendo,
  Providencia]`) son los que generan los filtros de la barra lateral —
  usá siempre las mismas palabras para que agrupen bien (por ejemplo,
  siempre "Disponible", nunca a veces "Disponible" y a veces "disponible").
- Si más adelante querés separar "Arriendo" de "Venta" en dos páginas
  distintas (como el repo original separa `people/` de `publications/`),
  se puede duplicar `index.qmd` con un filtro por `categories` distinto.
