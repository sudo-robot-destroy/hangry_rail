# hangry_rail

A collection of 3D printed mounts and hangers for garage tools designed to mount to a horizontal 1x4 or 2x4 board.

## Live site

https://sudo-robot-destroy.github.io/hangry_rail/

## Repository purpose

- Store STL files and related print assets
- Host a Markdown-first project page via GitHub Pages + Jekyll theme

## Current starter structure

- `_config.yml`: Jekyll/GitHub Pages site config and theme selection
- `index.md`: Homepage written in Markdown
- `stl/index.md`: STL library page written in Markdown
- `stl/`: Folder for printable model files

## Adding STL files

1. Put STL files under `stl/` in subfolders by category.
2. Use clear, lowercase, hyphenated names (example: `socket-wrench-hook-v2.stl`).
3. Optionally include preview images and slicer profiles (`.3mf`).

See `stl/README.md` and `stl/index.md` for the current layout and site page.

## Theme customization (no CSS/JS needed)

Theme selection is controlled in `_config.yml`:

- Current theme: `minima`

To change theme:

1. Pick a GitHub Pages supported Jekyll theme.
2. Update `theme:` in `_config.yml`.
3. Push to `main` and Pages will rebuild.

Common built-in choices include `minima`, `jekyll-theme-cayman`, and `jekyll-theme-slate`.

## GitHub Pages notes

- If Pages is configured to deploy from `main` branch root, pushes update the site.
- This repo currently expects root-based publishing from `main`.

## Next ideas

- Add per-model Markdown pages with print settings and photos
- Add a changelog page for versioned model revisions
- Add category pages that link to STL files in each folder
