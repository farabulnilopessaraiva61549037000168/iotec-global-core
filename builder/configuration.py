import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
from pathlib import Path

class ConfigurationManager:

    def __init__(self):

        self.file = Path("config/config.json")

        self.data = {}

    # --------------------------------------------------------

    def load(self):

        if not self.file.exists():

            raise FileNotFoundError(

                "config/config.json nao encontrado."

            )

        with open(

            self.file,

            "r",

            encoding="utf-8"

        ) as f:

            self.data = json.load(f)

        print("[CONFIG] CARREGADA")

        return self.data

    # --------------------------------------------------------

    def get(self,key,default=None):

        return self.data.get(

            key,

            default

        )

    # --------------------------------------------------------

    def show(self):

        print()

        print("="*70)

        print("CONFIGURACAO DA PLATAFORMA")

        print("="*70)

        for chave,valor in self.data.items():

            print(f"{chave:<15}: {valor}")

        print()



