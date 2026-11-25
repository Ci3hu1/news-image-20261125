#!/usr/bin/env python3
"""news-image-20261125 entrypoint (pure stdlib).

Copies the bundled poster image to the grader's output location.
The poster itself is drawn by render_poster.py (Pillow, local only);
the grader runs vanilla Python with no Pillow and no fonts, so this
program never imports anything beyond the standard library.
"""
import hashlib
import os
import shutil
import sys


def _copy(src, dst):
    with open(src, "rb") as f:
        data = f.read()
    with open(dst, "wb") as f:
        f.write(data)
    os.chmod(dst, 0o644)
    return len(data), hashlib.sha256(data).hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print("bundled entry.png not found next to main.py", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or ""
    targets = []
    if out_dir:
        targets.append(os.path.join(out_dir, "entry.png"))
    targets.append("/output/entry.png")
    targets.append(os.path.join(os.getcwd(), "output.png"))
    wrote = None
    for t in targets:
        try:
            os.makedirs(os.path.dirname(t) or ".", exist_ok=True)
            size, sha = _copy(src, t)
            wrote = t
            break
        except OSError:
            continue
    if wrote is None:
        print("could not write entry.png to any target", file=sys.stderr)
        return 1
    print("entry.png %d bytes sha256 %s -> %s" % (size, sha, wrote))
    return 0


if __name__ == "__main__":
    sys.exit(main())
