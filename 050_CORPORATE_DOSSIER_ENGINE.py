import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC CORPORATE DOSSIER ENGINE
FASE 07
ETAPA 007

VersÃƒÂ£o 8.0

DossiÃƒÂª Executivo Corporativo

======================================================================
"""

from datetime import datetime


class CorporateDossierEngine:

    def __init__(self):

        self.empresa="Microsoft"

        self.segmento="Tecnologia"

        self.capital=6.4

        self.meta=95

        self.status="EM ENRIQUECIMENTO"

        self.prioridades=[

            "Produtos",

            "ServiÃƒÂ§os",

            "Mercados",

            "Tecnologias",

            "Website Oficial",

            "Telefone Comercial",

            "E-mail Comercial"

        ]

    # ======================================================

    def executar(self):

        print()

        print("="*70)

        print("IOTEC CORPORATE DOSSIER ENGINE")

        print("="*70)

        print(datetime.now())

        print("="*70)

        print()

        print("EMPRESA")

        print(self.empresa)

        print()

        print("SEGMENTO")

        print(self.segmento)

        print()

        print("="*70)

        print("STATUS DO DOSSIÃƒÅ ")

        print()

        print(self.status)

        print()

        print("="*70)

        print("CAPITAL INTELECTUAL")

        print()

        print(f"Atual............. {self.capital:.1f}%")

        print(f"Meta.............. {self.meta}%")

        print()

        print("="*70)

        print("PRIORIDADES")

        print()

        for numero,item in enumerate(self.prioridades,1):

            print(f"{numero}. {item}")

        print()

        print("="*70)

        print("DECISÃƒÆ'O DO KERNEL")

        print()

        if self.capital < 25:

            print("FASE ATUAL")

            print("Enriquecimento Corporativo")

            print()

            print("AÃƒâ€¡ÃƒÆ'O")

            print("Coletar informaÃƒÂ§ÃƒÂµes pÃƒÂºblicas.")

            print("Atualizar cadastro.")

            print("Validar fontes.")

            print("Recalcular Capital Intelectual.")

        elif self.capital < 70:

            print("FASE ATUAL")

            print("PreparaÃƒÂ§ÃƒÂ£o Comercial")

        else:

            print("FASE ATUAL")

            print("Abordagem Comercial")

        print()

        print("="*70)

        print("PRÃƒâ€œXIMA MISSÃƒÆ'O")

        print()

        print("Executar o Pipeline")

        print()

        print("Coleta")

        print("Ã¢â€ â€œ")

        print("ValidaÃƒÂ§ÃƒÂ£o")

        print("Ã¢â€ â€œ")

        print("NormalizaÃƒÂ§ÃƒÂ£o")

        print("Ã¢â€ â€œ")

        print("Enriquecimento")

        print("Ã¢â€ â€œ")

        print("Novo DossiÃƒÂª")

        print("Ã¢â€ â€œ")

        print("Nova PontuaÃƒÂ§ÃƒÂ£o")

        print()

        print("="*70)

        print("FILOSOFIA")

        print()

        print("O objetivo")

        print("nÃƒÂ£o ÃƒÂ© vender")

        print("rapidamente.")

        print()

        print("O objetivo")

        print("ÃƒÂ© conhecer")

        print("profundamente")

        print("cada organizaÃƒÂ§ÃƒÂ£o.")

        print()

        print("="*70)

        print("CORPORATE DOSSIER ONLINE")

        print("="*70)


if __name__=="__main__":

    CorporateDossierEngine().executar()



