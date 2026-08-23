import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from datetime import datetime

class Report:

    def generate(self):

        print()

        print("="*60)

        print("RELATORIO")

        print("="*60)

        print("Gerado:",datetime.now())


