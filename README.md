# hangry_rail

A collection of 3D printed mounts and hangers for garage tools designed to mount to a horizontal 1x4 or 2x4 board.

## Live site

https://sudo-robot-destroy.github.io/hangry_rail/

## Repository purpose

- Store STL files and related print assets
- Host a static project page via GitHub Pages

## Current starter structure

- `index.html`: Main GitHub Pages homepage
- `styles.css`: Site styling with theme variables
- `script.js`: Theme switching and small page behavior
- `stl/`: Folder for printable model files
- `.nojekyll`: Ensures plain static file handling on GitHub Pages

## Adding STL files

1. Put STL files under `stl/` in subfolders by category.
2. Use clear, lowercase, hyphenated names (example: `socket-wrench-hook-v2.stl`).
3. Optionally include preview images and slicer profiles (`.3mf`).

See `stl/README.md` for a suggested layout.

## Theme customization

Theme colors are controlled by CSS variables in `styles.css`:

- `:root` for default `workshop`
- `:root[data-theme="blueprint"]`
- `:root[data-theme="signal"]`

To add a new theme:

1. Add a new `:root[data-theme="your-theme-name"]` block in `styles.css`.
2. Add a matching `<option>` in `index.html` under the theme selector.

The selected theme is stored in browser local storage via `script.js`.

## GitHub Pages notes

- If Pages is configured to deploy from `main` branch root, pushes update the site.
- If Pages is configured to deploy from `/docs`, move site files into a `docs/` folder.

## Next ideas

- Add a gallery page with one card per model and preview image
- Add a printable BOM/instructions page
- Add release notes for design revisions
