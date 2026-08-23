import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from pathlib import Path

class Validator:

    def validate(self):

        print()

        print("VALIDANDO PLATAFORMA")

        folders=[

            "builder",

            "database",

            "logs",

            "config",

            "reports"

        ]

        for folder in folders:

            if Path(folder).exists():

                print("[ OK ]",folder)

            else:

                print("[FAIL]",folder)


