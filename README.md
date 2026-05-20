# svg-icon-forge

Generate monochrome SVG icon themes for KDE/FreeDesktop-compatible desktops.  
No dependencies beyond Python 3.10+.

## Quick start

```bash
python3 icongen.py examples/music_icons.py --theme MusicMono
# → output/  contains index.theme + scalable/apps/*.svg

python3 icongen.py my_icons.py --install
# → installs to ~/.local/share/icons/MyIcons/
```

---

## For AI: how to generate icons

> Copy this section into your prompt. That's all the context needed.

**1. Download the runner (one line):**
```bash
curl -O https://raw.githubusercontent.com/St3llArS33R/svg-icon-forge/main/icongen.py
```

**2. Write an icons file — zero imports needed, all helpers are pre-injected:**

```python
# my_icons.py

build_theme(name="MyTheme")       # creates index.theme

# write(icon_name, svg_body)
write("org.kde.konsole", f"""
  <rect x="2" y="3" width="20" height="16" rx="2"
        fill="none" stroke="{C}" stroke-width="{SW}"/>
  <path d="M5 9 L9 12 L5 15"
        fill="none" stroke="{C}" stroke-width="{SWB}" {CAP}/>
  <line x1="11" y1="15" x2="15" y2="15"
        stroke="{C}" stroke-width="{SWB}" stroke-linecap="round"/>
""")

# link(source, *aliases) — same icon, multiple .desktop Icon= names
link("org.kde.konsole", "konsole", "terminal", "utilities-terminal")
```

**3. Run:**
```bash
python3 icongen.py my_icons.py --theme MyTheme --install
```

### Constants available in every icons file

| Name  | Value    | Use for                        |
|-------|----------|--------------------------------|
| `C`   | `white`  | fill/stroke color              |
| `SW`  | `1.8`    | normal stroke-width            |
| `SWS` | `1.4`    | thin stroke-width              |
| `SWB` | `2.2`    | bold stroke-width              |
| `CAP` | `stroke-linecap="round" stroke-linejoin="round"` | line caps |
| `FILL`   | `fill="white"` | solid white fill shorthand |
| `STROKE` | `fill="none" stroke="white"` | outline shorthand |

### SVG coordinate system

All icons use `viewBox="0 0 24 24"`.  
Center = (12, 12). Usable area ≈ 2–22 on both axes.

### How to find an app's icon name

```bash
grep "^Icon=" /usr/share/applications/APP.desktop
grep "^Icon=" /var/lib/flatpak/exports/share/applications/APP.desktop
```

---

## Full API

```python
setup(out_dir="output", theme_name="MyIcons")
    # Configure output path. Call once at the top of your icons file.

write(name, body, size=24)
    # Write one SVG icon.
    # name: FreeDesktop icon name (e.g. "firefox", "org.kde.konsole")
    # body: string of SVG elements
    # size: viewBox dimension (default 24)

link(src, *aliases)
    # Copy src icon to alias filenames.
    # Use when multiple .desktop files reference the same icon under different names.

build_theme(name=None, inherits="breeze-dark,hicolor,Adwaita", comment="")
    # Write index.theme. Call after all write() calls.
    # inherits: fallback chain for icons not in this theme.

install(dest_base=None)
    # Copy output/ to ~/.local/share/icons/<theme_name>/
```

---

## Examples

- [`examples/music_icons.py`](examples/music_icons.py) — 20 music app icons
- More examples welcome via PR.

## License

Apache 2.0
