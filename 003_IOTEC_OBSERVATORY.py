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

003_IOTEC_OBSERVATORY.py

MISSÃƒÆ'O

Observar continuamente toda a plataforma.

Este mÃƒÂ³dulo NÃƒÆ'O corrige problemas.

Ele apenas detecta.

Tudo que for encontrado serÃƒÂ¡ enviado ao Event Bus.

===============================================================================
"""

from pathlib import Path
from datetime import datetime
import sqlite3
import hashlib

ROOT = Path(r"C:\IOTEC")

DATABASE = ROOT / "kernel.db"

# =====================================================================


class Observatory:

    def __init__(self):

        self.conn = sqlite3.connect(DATABASE)

        self.cursor = self.conn.cursor()

    # ===============================================================

    def now(self):

        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # ===============================================================

    def publish(

        self,

        categoria,

        titulo,

        descricao,

        impacto="NORMAL"

    ):

        self.cursor.execute("""

        INSERT INTO events(

            agent,

            type,

            description,

            timestamp

        )

        VALUES(?,?,?,?)

        """,

        (

            "OBSERVATORY",

            categoria,

            titulo + " | " + descricao,

            self.now()

        )

        )

        self.conn.commit()

        print()

        print("="*70)

        print("OBSERVATÃƒâ€œRIO")

        print("="*70)

        print("Categoria :",categoria)

        print("Evento    :",titulo)

        print("DescriÃƒÂ§ÃƒÂ£o :",descricao)

        print("Impacto   :",impacto)

    # ===============================================================

    def scan_python(self):

        total = len(list(ROOT.rglob("*.py")))

        self.publish(

            "ARQUITETURA",

            "Arquivos Python",

            f"Foram encontrados {total} arquivos Python."

        )

    # ===============================================================

    def scan_html(self):

        total = len(list(ROOT.rglob("*.html")))

        self.publish(

            "ARQUITETURA",

            "Interfaces",

            f"Foram encontradas {total} interfaces HTML."

        )

    # ===============================================================

    def scan_payment(self):

        palavras = [

            "paypal",

            "payment",

            "checkout",

            "pix",

            "mercadopago"

        ]

        encontrados=[]

        for arquivo in ROOT.rglob("*"):

            if not arquivo.is_file():

                continue

            nome = arquivo.name.lower()

            for palavra in palavras:

                if palavra in nome:

                    encontrados.append(arquivo)

                    break

        self.publish(

            "FINANCEIRO",

            "Sistema de Pagamentos",

            f"{len(encontrados)} componentes encontrados."

        )

    # ===============================================================

    def scan_forms(self):

        encontrados=[]

        palavras=[

            "form",

            "lead",

            "register"

        ]

        for arquivo in ROOT.rglob("*"):

            if not arquivo.is_file():

                continue

            nome=arquivo.name.lower()

            for p in palavras:

                if p in nome:

                    encontrados.append(arquivo)

                    break

        self.publish(

            "COMERCIAL",

            "FormulÃƒÂ¡rios",

            f"{len(encontrados)} componentes localizados."

        )

    # ===============================================================

    def scan_database(self):

        bancos=[]

        palavras=[

            "database",

            "sqlite",

            "postgres",

            ".db"

        ]

        for arquivo in ROOT.rglob("*"):

            if not arquivo.is_file():

                continue

            nome=arquivo.name.lower()

            for p in palavras:

                if p in nome:

                    bancos.append(arquivo)

                    break

        self.publish(

            "BANCO",

            "Estruturas de Banco",

            f"{len(bancos)} componentes encontrados."

        )

    # ===============================================================

    def architecture_signature(self):

        h = hashlib.sha256()

        total = 0

        for arq in ROOT.rglob("*.py"):

            h.update(arq.name.encode())

            total += 1

        assinatura = h.hexdigest()[:20]

        self.publish(

            "IDENTIDADE",

            "Assinatura da Arquitetura",

            assinatura

        )

    # ===============================================================

    def start(self):

        print()

        print("="*70)

        print("IOTEC OBSERVATORY")

        print("="*70)

        self.scan_python()

        self.scan_html()

        self.scan_forms()

        self.scan_payment()

        self.scan_database()

        self.architecture_signature()

        print()

        print("="*70)

        print("OBSERVAÃƒâ€¡ÃƒÆ'O FINALIZADA")

        print("="*70)


# =====================================================================

if __name__ == "__main__":

    observatory = Observatory()

    observatory.start()



