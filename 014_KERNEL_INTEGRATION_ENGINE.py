import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================
IOTEC
014_KERNEL_INTEGRATION_ENGINE.py
MOTOR DE INTEGRAÃƒâ€¡ÃƒÆ'O DO KERNEL
======================================================================
"""

import importlib
from datetime import datetime


class KernelIntegration:

    def __init__(self):

        self.data = datetime.now()

        self.modulos = {

            "MISSÃƒÆ'O": "001_MISSAO",

            "CONTROL CENTER": "IOTEC_CONTROL_CENTER",

            "PLANTÃƒÆ'O": "PLANTAO_DE_EVENTOS",

            "LOGÃƒÂSTICA": "011_DATA_LOGISTICS_ENGINE",

            "CAMINHÃƒâ€¢ES": "012_TRUCK_SIMULATOR",

            "KERNEL BRAIN": "013_KERNEL_BRAIN"

        }

        self.status = {}


    def verificar_modulos(self):

        print("=" * 70)
        print("VERIFICANDO MÃƒâ€œDULOS")
        print("=" * 70)
        print()

        for nome, modulo in self.modulos.items():

            try:

                importlib.import_module(modulo)

                self.status[nome] = "ONLINE"

            except Exception as erro:

                self.status[nome] = f"ERRO ({erro.__class__.__name__})"

            print(f"{nome:<20} {self.status[nome]}")

        print()


    def resumo(self):

        online = sum(
            1
            for s in self.status.values()
            if s == "ONLINE"
        )

        total = len(self.status)

        percentual = (online / total) * 100

        print("=" * 70)
        print("RESUMO DA INTEGRAÃƒâ€¡ÃƒÆ'O")
        print("=" * 70)
        print()

        print(f"MÃƒÂ³dulos Online....... {online}")

        print(f"MÃƒÂ³dulos Totais....... {total}")

        print(f"ÃƒÂndice............... {percentual:.1f}%")

        print()

        if percentual == 100:

            print("STATUS GERAL......... INTEGRAÃƒâ€¡ÃƒÆ'O COMPLETA")

        elif percentual >= 70:

            print("STATUS GERAL......... BOA")

        elif percentual >= 40:

            print("STATUS GERAL......... PARCIAL")

        else:

            print("STATUS GERAL......... INICIAL")


    def recomendacoes(self):

        print()
        print("=" * 70)
        print("RECOMENDAÃƒâ€¡Ãƒâ€¢ES DO KERNEL")
        print("=" * 70)
        print()

        for nome, situacao in self.status.items():

            if situacao != "ONLINE":

                print(f"Ã¢â‚¬Â¢ Integrar corretamente o mÃƒÂ³dulo {nome}")

        print()

        print("PrÃƒÂ³ximos objetivos:")

        print("Ã¢â‚¬Â¢ Criar banco de dados central.")

        print("Ã¢â‚¬Â¢ Integrar CRM.")

        print("Ã¢â‚¬Â¢ Integrar Comercial.")

        print("Ã¢â‚¬Â¢ Integrar Financeiro.")

        print("Ã¢â‚¬Â¢ Integrar Agentes.")

        print("Ã¢â‚¬Â¢ Integrar CaminhÃƒÂµes TecnolÃƒÂ³gicos.")

        print("Ã¢â‚¬Â¢ Integrar Torre de Controle.")

        print()

        print("=" * 70)

        print("MISSÃƒÆ'O DO KERNEL")

        print("=" * 70)

        print()

        print("Conectar todos os mÃƒÂ³dulos")

        print("para que trabalhem como")

        print("uma ÃƒÂºnica plataforma.")

        print()

        print("=" * 70)


if __name__ == "__main__":

    print("=" * 70)

    print("IOTEC KERNEL INTEGRATION ENGINE")

    print("=" * 70)

    print("Data:", datetime.now().strftime("%d/%m/%Y"))

    print("Hora:", datetime.now().strftime("%H:%M:%S"))

    print()

    engine = KernelIntegration()

    engine.verificar_modulos()

    engine.resumo()

    engine.recomendacoes()



