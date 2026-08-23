import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================
IOTEC
016_KERNEL_EVENT_ENGINE.py

KERNEL EVENT ENGINE
VERSÃƒÆ'O 1.0

Todo acontecimento da IOTEC deve ser registrado aqui.

Este mÃƒÂ³dulo funciona como a memÃƒÂ³ria permanente do Kernel.

======================================================================
"""

import sqlite3
from datetime import datetime
import os


class KernelEventEngine:

    def __init__(self):

        self.database = "iotec_kernel.db"

        self.conexao = sqlite3.connect(self.database)

        self.cursor = self.conexao.cursor()

        self.criar_tabelas()


    # ==========================================================

    def criar_tabelas(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS eventos(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            data TEXT,

            categoria TEXT,

            origem TEXT,

            destino TEXT,

            objeto TEXT,

            status TEXT,

            descricao TEXT

        )

        """)

        self.conexao.commit()


    # ==========================================================

    def registrar(

        self,

        categoria,

        origem,

        destino,

        objeto,

        status,

        descricao

    ):

        horario = datetime.now().strftime(

            "%d/%m/%Y %H:%M:%S"

        )

        self.cursor.execute("""

        INSERT INTO eventos(

            data,

            categoria,

            origem,

            destino,

            objeto,

            status,

            descricao

        )

        VALUES(?,?,?,?,?,?,?)

        """,

        (

            horario,

            categoria,

            origem,

            destino,

            objeto,

            status,

            descricao

        ))

        self.conexao.commit()

        print()

        print("="*70)

        print("EVENTO REGISTRADO")

        print("="*70)

        print()

        print("HorÃƒÂ¡rio :", horario)

        print("Categoria :", categoria)

        print("Origem :", origem)

        print("Destino :", destino)

        print("Objeto :", objeto)

        print("Status :", status)

        print()

        print(descricao)

        print()

        print("="*70)


    # ==========================================================

    def listar_eventos(self):

        print()

        print("="*70)

        print("HISTÃƒâ€œRICO DO KERNEL")

        print("="*70)

        print()

        self.cursor.execute("""

        SELECT

        id,

        data,

        categoria,

        origem,

        destino,

        objeto,

        status

        FROM eventos

        ORDER BY id DESC

        """)

        registros = self.cursor.fetchall()

        if len(registros) == 0:

            print("Nenhum evento registrado.")

            return

        for registro in registros:

            print(

                f"[{registro[0]}] "

                f"{registro[1]}"

            )

            print(

                f"{registro[2]} | "

                f"{registro[3]} -> "

                f"{registro[4]}"

            )

            print(

                f"{registro[5]}"

            )

            print(

                f"Status: {registro[6]}"

            )

            print("-"*60)


    # ==========================================================

    def fechar(self):

        self.conexao.close()


# ======================================================================

if __name__ == "__main__":

    kernel = KernelEventEngine()

    kernel.registrar(

        categoria="LOGÃƒÂSTICA",

        origem="TRK-002",

        destino="COMERCIAL",

        objeto="Leads Empresariais",

        status="ENTREGUE",

        descricao="Carga entregue ao setor Comercial."

    )

    kernel.registrar(

        categoria="PRODUÃƒâ€¡ÃƒÆ'O",

        origem="AGENTE 04",

        destino="LINHA DE PRODUÃƒâ€¡ÃƒÆ'O",

        objeto="Projeto Executivo",

        status="BLOQUEADO",

        descricao="Material incompleto. Kernel acionou a LogÃƒÂ­stica."

    )

    kernel.listar_eventos()

    kernel.fechar()



