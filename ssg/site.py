
import sys
from pathlib import Path

from ssg import extensions


class Site:
    def __init__(self, source, dest, parsers=None):
@@ -27,6 +29,7 @@ def run_parser(self, path):
            )

    def build(self):
        extensions.load_bundled()
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
            elif path.is_file():
                self.run_parser(path)
    @staticmethod
    def error(message):
        sys.stderr.write("\x1b[1;31m{}\n".format(message))
