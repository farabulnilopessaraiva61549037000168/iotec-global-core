import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
===============================================================================
 IOTEC OPERATING SYSTEM
===============================================================================

MÃƒâ€œDULO

012_IOTEC_CODE_FACTORY_ENGINE.py

MISSÃƒÆ'O

Receber especificaÃƒÂ§ÃƒÂµes tÃƒÂ©cnicas e transformÃƒÂ¡-las
em projetos de desenvolvimento.

O Code Factory NÃƒÆ'O programa diretamente.

Ele prepara todo o projeto que serÃƒÂ¡ desenvolvido
pela prÃƒÂ³pria plataforma.

===============================================================================
"""

import json
import sqlite3
from pathlib import Path
from datetime import datetime

ROOT = Path(r"C:\IOTEC")

DATABASE = ROOT / "kernel.db"

FACTORY = ROOT / "SOFTWARE_FACTORY"

SPECIFICATIONS = FACTORY / "SPECIFICATIONS"

PROJECTS = FACTORY / "PROJECTS"

LOGS = FACTORY / "LOGS"

for pasta in [FACTORY, SPECIFICATIONS, PROJECTS, LOGS]:
    pasta.mkdir(exist_ok=True)


class CodeFactory:

    def __init__(self):

        self.conn = sqlite3.connect(DATABASE)

        self.cursor = self.conn.cursor()

    # ===============================================================

    def now(self):

        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # ===============================================================

    def publish(self, texto):

        print(texto)

        self.cursor.execute(

            """
            INSERT INTO events(
                agent,
                type,
                description,
                timestamp
            )
            VALUES(?,?,?,?)
            """,

            (

                "CODE_FACTORY",

                "SOFTWARE_FACTORY",

                texto,

                self.now()

            )

        )

        self.conn.commit()

    # ===============================================================

    def create_specification(

            self,

            nome,

            missao,

            entradas,

            saidas,

            eventos,

            testes

    ):

        dados = {

            "nome": nome,

            "missao": missao,

            "entradas": entradas,

            "saidas": saidas,

            "eventos": eventos,

            "testes": testes,

            "criado_em": self.now()

        }

        arquivo = SPECIFICATIONS / f"{nome}.json"

        with open(

            arquivo,

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                dados,

                f,

                indent=4,

                ensure_ascii=False

            )

        self.publish(f"EspecificaÃƒÂ§ÃƒÂ£o criada: {nome}")

        return arquivo

    # ===============================================================

    def create_project(self, specification):

        with open(

            specification,

            encoding="utf-8"

        ) as f:

            dados = json.load(f)

        projeto = {

            "modulo": dados["nome"],

            "status": "PLANEJADO",

            "etapas": [

                "Arquitetura",

                "ImplementaÃƒÂ§ÃƒÂ£o",

                "Testes",

                "Auditoria",

                "IntegraÃƒÂ§ÃƒÂ£o",

                "PublicaÃƒÂ§ÃƒÂ£o"

            ],

            "progresso": 0,

            "responsavel": "SOFTWARE_FACTORY",

            "criado_em": self.now()

        }

        destino = PROJECTS / f"{dados['nome']}_PROJECT.json"

        with open(

            destino,

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                projeto,

                f,

                indent=4,

                ensure_ascii=False

            )

        self.publish(f"Projeto criado: {dados['nome']}")

        return destino

    # ===============================================================

    def executive_report(self):

        specs = len(list(SPECIFICATIONS.glob("*.json")))

        projetos = len(list(PROJECTS.glob("*.json")))

        print()

        print("="*70)

        print("SOFTWARE FACTORY")

        print("="*70)

        print()

        print("EspecificaÃƒÂ§ÃƒÂµes :", specs)

        print("Projetos       :", projetos)

        print()

        print("A fÃƒÂ¡brica estÃƒÂ¡ pronta para")

        print("transformar especificaÃƒÂ§ÃƒÂµes")

        print("em mÃƒÂ³dulos da plataforma.")

        print()

        print("="*70)


if __name__ == "__main__":

    factory = CodeFactory()

    spec = factory.create_specification(

        nome="COMMERCIAL_FLOW_ENGINE",

        missao="Construir fluxo comercial completo",

        entradas=[

            "Landing Page",

            "FormulÃƒÂ¡rio",

            "Produto",

            "Pagamento"

        ],

        saidas=[

            "Venda concluÃƒÂ­da"

        ],

        eventos=[

            "Pagamento",

            "Entrega",

            "Cliente"

        ],

        testes=[

            "Compra de teste",

            "Recebimento",

            "Entrega"

        ]

    )

    factory.create_project(spec)

    factory.executive_report()



