#!/usr/bin/env python3
"""
svg-icon-forge — monochrome SVG icon generator for FreeDesktop/KDE icon themes.

LIBRARY USAGE:
    from icongen import setup, write, link, build_theme
    from icongen import C, SW, SWS, SWB, CAP

CLI USAGE:
    python3 icongen.py my_icons.py
    python3 icongen.py my_icons.py --out ./output --theme MyTheme
    python3 icongen.py my_icons.py --install             # → ~/.local/share/icons/
"""

import os
import sys
import glob
import argparse
import textwrap

# ── Style constants (importable, usable directly in icon bodies) ──────────────
C   = "white"   # fill / stroke color
SW  = "1.8"     # stroke-width normal
SWS = "1.4"     # stroke-width slim
SWB = "2.2"     # stroke-width bold
CAP = 'stroke-linecap="round" stroke-linejoin="round"'
FILL   = f'fill="{C}"'
STROKE = f'fill="none" stroke="{C}"'

# ── Internal state ─────────────────────────────────────────────────────────────
_out_dir    = "output"
_theme_name = "MyIcons"

def setup(out_dir: str = "output", theme_name: str = "MyIcons") -> None:
    """Call once at the top of your icons file to configure output location."""
    global _out_dir, _theme_name
    _out_dir    = out_dir
    _theme_name = theme_name
    os.makedirs(os.path.join(_out_dir, "scalable", "apps"), exist_ok=True)

# ── Core helpers ───────────────────────────────────────────────────────────────
def write(name: str, body: str, size: int = 24) -> None:
    """Write one SVG icon file.

    Args:
        name: FreeDesktop icon name (e.g. "org.kde.konsole", "firefox").
        body: SVG element string — <circle>, <rect>, <path>, <line>, etc.
        size: viewBox size (default 24).
    """
    _ensure_setup()
    content = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}">\n'
        f'{textwrap.indent(body.strip(), "  ")}\n'
        f'</svg>\n'
    )
    path = os.path.join(_out_dir, "scalable", "apps", f"{name}.svg")
    with open(path, "w") as f:
        f.write(content)


def link(src: str, *aliases: str) -> None:
    """Copy src icon to one or more alias names.

    Use this when multiple .desktop files reference the same app under
    different Icon= values (e.g. "firefox", "firefox-esr", "org.mozilla.firefox").
    """
    _ensure_setup()
    src_path = os.path.join(_out_dir, "scalable", "apps", f"{src}.svg")
    if not os.path.exists(src_path):
        print(f"  [warn] link: source '{src}.svg' not found", file=sys.stderr)
        return
    with open(src_path) as f:
        content = f.read()
    for alias in aliases:
        dest = os.path.join(_out_dir, "scalable", "apps", f"{alias}.svg")
        with open(dest, "w") as f:
            f.write(content)


def build_theme(
    name: str | None = None,
    inherits: str = "breeze-dark,hicolor,Adwaita",
    comment: str = "Monochrome icon theme",
) -> None:
    """Write index.theme into the output directory.

    Args:
        name:     Display name of the theme (defaults to setup()'s theme_name).
        inherits: Comma-separated fallback chain for missing icons.
        comment:  Short description shown in icon pickers.
    """
    _ensure_setup()
    theme_name = name or _theme_name
    index = textwrap.dedent(f"""\
        [Icon Theme]
        Name={theme_name}
        Comment={comment}
        Inherits={inherits}
        Example=utilities-terminal

        Directories=scalable/apps

        [scalable/apps]
        Size=48
        MinSize=1
        MaxSize=512
        Type=Scalable
        Context=Applications
    """)
    path = os.path.join(_out_dir, "index.theme")
    with open(path, "w") as f:
        f.write(index)


def install(dest_base: str | None = None) -> None:
    """Install the generated theme to dest_base (default: ~/.local/share/icons/)."""
    import shutil
    _ensure_setup()
    base   = dest_base or os.path.expanduser("~/.local/share/icons")
    dest   = os.path.join(base, _theme_name)
    shutil.rmtree(dest, ignore_errors=True)
    shutil.copytree(_out_dir, dest)
    os.system(f"gtk-update-icon-cache -f -t '{dest}' 2>/dev/null || true")
    count = len(glob.glob(os.path.join(dest, "scalable", "apps", "*.svg")))
    print(f"  Installed '{_theme_name}' ({count} icons) → {dest}")


# ── CLI ────────────────────────────────────────────────────────────────────────
def _ensure_setup() -> None:
    os.makedirs(os.path.join(_out_dir, "scalable", "apps"), exist_ok=True)


def _run_file(icons_file: str, out_dir: str, theme: str, do_install: bool) -> None:
    """Execute an icons definition file with all helpers pre-injected."""
    setup(out_dir=out_dir, theme_name=theme)

    # Inject all public names so the icons file needs zero imports
    ns = {
        "setup": setup, "write": write, "link": link,
        "build_theme": build_theme, "install": install,
        "C": C, "SW": SW, "SWS": SWS, "SWB": SWB, "CAP": CAP,
        "FILL": FILL, "STROKE": STROKE,
    }
    with open(icons_file) as f:
        code = compile(f.read(), icons_file, "exec")
    exec(code, ns)

    if do_install:
        install()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="svg-icon-forge: generate monochrome SVG icon themes",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            Examples:
              python3 icongen.py examples/music_icons.py
              python3 icongen.py my_icons.py --out ./dist --theme CoolIcons
              python3 icongen.py my_icons.py --install
        """),
    )
    parser.add_argument("icons_file", help="Python file containing write()/link() calls")
    parser.add_argument("--out",     default="output",   help="Output directory (default: ./output)")
    parser.add_argument("--theme",   default="MyIcons",  help="Theme display name (default: MyIcons)")
    parser.add_argument("--install", action="store_true", help="Install to ~/.local/share/icons/ after generating")
    args = parser.parse_args()

    if not os.path.exists(args.icons_file):
        print(f"Error: '{args.icons_file}' not found", file=sys.stderr)
        sys.exit(1)

    print(f"Generating icons from '{args.icons_file}'...")
    _run_file(args.icons_file, args.out, args.theme, args.install)

    # Summary: unique designs vs aliases
    import hashlib
    files = glob.glob(os.path.join(args.out, "scalable", "apps", "*.svg"))
    hashes: dict[str, list[str]] = {}
    for f in files:
        h = hashlib.md5(open(f).read().encode()).hexdigest()
        hashes.setdefault(h, []).append(os.path.basename(f))
    unique = len(hashes)
    aliases = len(files) - unique
    print(f"  Done: {unique} unique icons, {aliases} aliases → {os.path.abspath(args.out)}/")


if __name__ == "__main__":
    main()
