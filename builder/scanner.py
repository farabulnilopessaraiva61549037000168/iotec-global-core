import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from pathlib import Path

class Scanner:

    def scan(self,modules):

        print()

        print("ESCANEANDO...")

        ok=0

        for module in modules:

            if Path(module).exists():

                print("[ OK ]",module)

                ok+=1

            else:

                print("[FAIL]",module)

        print()

        print("LOCALIZADOS:",ok)


