import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC - OPERAÃƒâ€¡ÃƒÆ'O PRIMEIRA VENDA
# MissÃƒÂ£o EstratÃƒÂ©gica
# ==========================================================

from datetime import datetime
import json

class FirstSaleMission:

    def __init__(self):

        self.mission = {

            "id": "MISSION_0001",

            "name": "OPERAÃƒâ€¡ÃƒÆ'O PRIMEIRA VENDA",

            "priority": "CRÃƒÂTICA",

            "status": "AGUARDANDO",

            "created": datetime.now().isoformat(),

            "product": {

                "name": "DiagnÃƒÂ³stico Executivo",

                "price": 30.00,

                "currency": "BRL"

            },

            "steps":[

                {
                    "id":1,
                    "name":"LOCALIZAR_GATEWAY",
                    "status":"PENDENTE"
                },

                {
                    "id":2,
                    "name":"CRIAR_COBRANCA",
                    "status":"PENDENTE"
                },

                {
                    "id":3,
                    "name":"GERAR_LINK",
                    "status":"PENDENTE"
                },

                {
                    "id":4,
                    "name":"AGUARDAR_PAGAMENTO",
                    "status":"PENDENTE"
                },

                {
                    "id":5,
                    "name":"REGISTRAR_VENDA",
                    "status":"PENDENTE"
                },

                {
                    "id":6,
                    "name":"ENTREGAR_PRODUTO",
                    "status":"PENDENTE"
                }

            ]

        }

    # ------------------------------------------------------

    def show(self):

        print()

        print("="*70)

        print("MISSÃƒÆ'O EXECUTIVA")

        print("="*70)

        print()

        print("Nome :", self.mission["name"])

        print("Status :", self.mission["status"])

        print()

        print("Produto")

        print(self.mission["product"]["name"])

        print("Valor : R$ %.2f" % self.mission["product"]["price"])

        print()

        print("Plano Operacional")

        print()

        for step in self.mission["steps"]:

            print(

                "[ ]",

                step["id"],

                "-",

                step["name"]

            )

        print()

    # ------------------------------------------------------

    def export(self):

        with open(

            "MISSION_0001.json",

            "w",

            encoding="utf8"

        ) as f:

            json.dump(

                self.mission,

                f,

                indent=4,

                ensure_ascii=False

            )

        print()

        print("MissÃƒÂ£o exportada.")

        print("Arquivo : MISSION_0001.json")

# ==========================================================

if __name__ == "__main__":

    engine = FirstSaleMission()

    engine.show()

    engine.export()



