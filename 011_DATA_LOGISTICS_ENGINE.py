import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================
IOTEC
011_DATA_LOGISTICS_ENGINE.py
CENTRAL LOGÃƒÂSTICA DE DADOS
======================================================================
"""

from datetime import datetime


class CaminhaoTecnologico:

    def __init__(self,
                 identificador,
                 nome,
                 setor,
                 carga):

        self.id = identificador
        self.nome = nome
        self.setor = setor
        self.carga = carga
        self.status = "DISPONÃƒÂVEL"

    def carregar(self):

        self.status = "EM COLETA"

    def descarregar(self):

        self.status = "ENTREGUE"

    def exibir(self):

        print(f"[{self.id}] {self.nome}")

        print(f"Setor.............. {self.setor}")

        print(f"Carga.............. {self.carga}")

        print(f"Status............. {self.status}")

        print("-" * 60)


class CentralLogistica:

    def __init__(self):

        self.data = datetime.now()

        self.frota = [

            CaminhaoTecnologico(
                "TRK-001",
                "DOCUMENTOS",
                "JurÃƒÂ­dico",
                "Contratos, PDFs e Documentos"
            ),

            CaminhaoTecnologico(
                "TRK-002",
                "LEADS",
                "Comercial",
                "Empresas e Oportunidades"
            ),

            CaminhaoTecnologico(
                "TRK-003",
                "CRM",
                "Relacionamento",
                "Clientes e Contatos"
            ),

            CaminhaoTecnologico(
                "TRK-004",
                "FINANCEIRO",
                "Financeiro",
                "Receitas e Custos"
            ),

            CaminhaoTecnologico(
                "TRK-005",
                "PORTFÃƒâ€œLIOS",
                "Marketing",
                "CatÃƒÂ¡logos e Produtos"
            ),

            CaminhaoTecnologico(
                "TRK-006",
                "LICITAÃƒâ€¡Ãƒâ€¢ES",
                "Comercial",
                "Editais PÃƒÂºblicos"
            ),

            CaminhaoTecnologico(
                "TRK-007",
                "LEGISLAÃƒâ€¡ÃƒÆ'O",
                "JurÃƒÂ­dico",
                "Normas e Leis"
            ),

            CaminhaoTecnologico(
                "TRK-008",
                "PROJETOS",
                "Engenharia",
                "Arquivos TÃƒÂ©cnicos"
            )

        ]


    def apresentar(self):

        print("=" * 70)

        print("IOTEC - CENTRAL LOGÃƒÂSTICA DE DADOS")

        print("=" * 70)

        print()

        print("MissÃƒÂ£o:")

        print(
            "Abastecer continuamente todos os setores da IOTEC "
            "com dados necessÃƒÂ¡rios para operaÃƒÂ§ÃƒÂ£o."
        )

        print()

        print("=" * 70)

        print("FROTA TECNOLÃƒâ€œGICA")

        print("=" * 70)

        for caminhao in self.frota:

            caminhao.exibir()

        print()

        print("=" * 70)

        print("FLUXO LOGÃƒÂSTICO")

        print("=" * 70)

        etapas = [

            "Receber SolicitaÃƒÂ§ÃƒÂ£o",

            "Planejar Coleta",

            "Enviar CaminhÃƒÂ£o",

            "Coletar Dados",

            "Validar ConteÃƒÂºdo",

            "Classificar Material",

            "Armazenar",

            "Distribuir ao Setor",

            "Registrar OperaÃƒÂ§ÃƒÂ£o"

        ]

        for numero, etapa in enumerate(etapas, start=1):

            print(f"{numero:02d} - {etapa}")

        print()

        print("=" * 70)

        print("DESTINOS")

        print("=" * 70)

        destinos = [

            "Kernel",

            "Control Center",

            "Comercial",

            "JurÃƒÂ­dico",

            "Financeiro",

            "Marketing",

            "Projetos",

            "Auditoria",

            "GovernanÃƒÂ§a",

            "Agentes"

        ]

        for destino in destinos:

            print("Ã¢â‚¬Â¢", destino)

        print()

        print("=" * 70)

        print("STATUS")

        print("=" * 70)

        print("Toda solicitaÃƒÂ§ÃƒÂ£o interna deve ser atendida")

        print("pela Central LogÃƒÂ­stica de Dados.")

        print()

        print("Nenhum agente procura dados manualmente.")

        print()

        print("Os caminhÃƒÂµes tecnolÃƒÂ³gicos realizam a coleta,")

        print("transportam o material e abastecem a plataforma.")

        print()

        print("=" * 70)

        print("CENTRAL LOGÃƒÂSTICA OPERACIONAL")

        print("=" * 70)


if __name__ == "__main__":

    central = CentralLogistica()

    central.apresentar()



