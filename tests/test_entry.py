#!/usr/bin/env python3
"""Tests for the news-image-20261125 entry.

Run: python3 -m unittest discover -s tests -v
Checks the graded artifact (entry.png + main.py) only: size, format,
determinism of main.py's two runs, stdlib-only imports, and that the
renderer's own clearance test passes.
"""
import ast
import hashlib
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ENTRY = os.path.join(ROOT, "entry.png")
MAIN = os.path.join(ROOT, "main.py")

ALLOWED_STDLIB = {
    "hashlib", "os", "shutil", "sys",
}


class TestEntryImage(unittest.TestCase):
    def test_entry_exists_and_small(self):
        self.assertTrue(os.path.isfile(ENTRY), "entry.png missing")
        size = os.path.getsize(ENTRY)
        self.assertLessEqual(size, 1048576, "entry.png over 1 MiB: %d" % size)
        self.assertGreater(size, 100000, "entry.png suspiciously small")

    def test_png_header_and_dimensions(self):
        with open(ENTRY, "rb") as f:
            head = f.read(33)
        self.assertEqual(head[:8], b"\x89PNG\r\n\x1a\n", "not a PNG")
        width = int.from_bytes(head[16:20], "big")
        height = int.from_bytes(head[20:24], "big")
        self.assertEqual((width, height), (1024, 1024))

    def test_main_runs_twice_byte_identical(self):
        hashes = []
        for _ in range(2):
            with tempfile.TemporaryDirectory() as tmp:
                env = dict(os.environ, MAKEFUN_OUTPUT_DIR=tmp)
                r = subprocess.run([sys.executable, MAIN], env=env,
                                   capture_output=True, text=True,
                                   cwd=tmp)
                self.assertEqual(r.returncode, 0, r.stderr)
                out = os.path.join(tmp, "entry.png")
                self.assertTrue(os.path.isfile(out))
                self.assertEqual(oct(os.stat(out).st_mode & 0o777), "0o644")
                with open(out, "rb") as f:
                    hashes.append(hashlib.sha256(f.read()).hexdigest())
        self.assertEqual(hashes[0], hashes[1], "two runs differ")
        with open(ENTRY, "rb") as f:
            self.assertEqual(hashes[0],
                             hashlib.sha256(f.read()).hexdigest(),
                             "main.py output differs from bundled entry.png")

    def test_main_stdlib_only(self):
        with open(MAIN) as f:
            tree = ast.parse(f.read())
        imports = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.update(a.name.split(".")[0] for a in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imports.add(node.module.split(".")[0])
        self.assertTrue(imports <= ALLOWED_STDLIB,
                        "non-stdlib imports: %s" % (imports - ALLOWED_STDLIB))

    def test_no_network_in_main(self):
        with open(MAIN) as f:
            src = f.read()
        for banned in ("socket", "urllib", "http.client", "requests",
                       "subprocess", "eval(", "exec("):
            self.assertNotIn(banned, src, "main.py contains %r" % banned)


class TestRenderer(unittest.TestCase):
    def test_render_clearance(self):
        r = subprocess.run([sys.executable, "render_poster.py"],
                           capture_output=True, text=True, cwd=ROOT)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("clearance violations: 0", r.stdout)


if __name__ == "__main__":
    unittest.main()
