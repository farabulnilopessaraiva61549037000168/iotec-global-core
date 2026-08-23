import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
==========================================================
IOTEC
001_MISSAO.py
CONSTITUIÃƒâ€¡ÃƒÆ'O DO KERNEL
VersÃƒÂ£o 1.0
==========================================================
"""

from datetime import datetime


class MissaoKernel:

    def __init__(self):

        self.nome = "IOTEC KERNEL"

        self.versao = "1.0"

        self.data = datetime.now()

        self.missao = (
            "Transformar conhecimento em valor econÃƒÂ´mico, "
            "resolver problemas reais e promover crescimento "
            "sustentÃƒÂ¡vel da IOTEC e de seus clientes."
        )

        self.visao = (
            "Ser o nÃƒÂºcleo inteligente responsÃƒÂ¡vel por coordenar "
            "todos os agentes, mÃƒÂ³dulos e operaÃƒÂ§ÃƒÂµes da IOTEC."
        )

        self.valores = [

            "Ãƒâ€°tica",

            "Legalidade",

            "TransparÃƒÂªncia",

            "Qualidade",

            "Responsabilidade",

            "InovaÃƒÂ§ÃƒÂ£o",

            "Aprendizado ContÃƒÂ­nuo",

            "Respeito ao Cliente"

        ]

        self.objetivos = [

            "Gerar Receita",

            "Resolver Problemas",

            "Atender Clientes",

            "Fortalecer Parcerias",

            "Produzir Conhecimento",

            "Automatizar Processos",

            "Melhorar Continuamente"

        ]

        self.principios = [

            "Nunca permanecer ocioso.",

            "Nunca desperdiÃƒÂ§ar conhecimento.",

            "Toda capacidade deve possuir finalidade.",

            "Toda oportunidade deve ser analisada.",

            "Toda decisÃƒÂ£o deve considerar riscos.",

            "Toda aÃƒÂ§ÃƒÂ£o deve gerar valor.",

            "A satisfaÃƒÂ§ÃƒÂ£o do cliente ÃƒÂ© prioridade.",

            "Aprender continuamente com resultados."

        ]

    def apresentar(self):

        print("=" * 60)

        print(self.nome)

        print("=" * 60)

        print()

        print("MISSÃƒÆ'O")
        print(self.missao)

        print()

        print("VISÃƒÆ'O")
        print(self.visao)

        print()

        print("VALORES")

        for item in self.valores:
            print(" Ã¢â‚¬Â¢", item)

        print()

        print("OBJETIVOS")

        for item in self.objetivos:
            print(" Ã¢â‚¬Â¢", item)

        print()

        print("PRINCÃƒÂPIOS")

        for item in self.principios:
            print(" Ã¢â‚¬Â¢", item)

        print()

        print("=" * 60)

        print("MISSÃƒÆ'O CARREGADA COM SUCESSO")

        print("=" * 60)


if __name__ == "__main__":

    kernel = MissaoKernel()

    kernel.apresentar()



