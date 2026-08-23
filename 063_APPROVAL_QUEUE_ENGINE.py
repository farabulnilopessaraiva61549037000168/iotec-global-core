import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC APPROVAL QUEUE ENGINE
FASE 08

VersÃƒÂ£o 9.0

Central de AprovaÃƒÂ§ÃƒÂ£o

======================================================================
"""

import sqlite3
from datetime import datetime

DB="iotec.db"


class ApprovalQueue:

    def conectar(self):
        return sqlite3.connect(DB, timeout=30)

    # ----------------------------------------------------

    def criar_tabela(self):

        conn=self.conectar()

        cursor=conn.cursor()

        cursor.execute("""

        CREATE TABLE IF NOT EXISTS approval_queue(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            tipo TEXT,

            titulo TEXT,

            canal TEXT,

            prioridade TEXT,

            status TEXT,

            criado_em TEXT

        )

        """)

        conn.commit()

        conn.close()

    # ----------------------------------------------------

    def inserir_exemplo(self):

        conn=self.conectar()

        cursor=conn.cursor()

        cursor.execute("""

        SELECT COUNT(*)

        FROM approval_queue

        """)

        total=cursor.fetchone()[0]

        if total==0:

            cursor.execute("""

            INSERT INTO approval_queue(

            tipo,

            titulo,

            canal,

            prioridade,

            status,

            criado_em

            )

            VALUES(?,?,?,?,?,?)

            """,(

            "Campanha",

            "Business Intelligence",

            "WhatsApp",

            "CRÃƒÂTICA",

            "AGUARDANDO APROVAÃƒâ€¡ÃƒÆ'O",

            str(datetime.now())

            ))

            conn.commit()

        conn.close()

    # ----------------------------------------------------

    def executar(self):

        self.criar_tabela()

        self.inserir_exemplo()

        conn=self.conectar()

        cursor=conn.cursor()

        cursor.execute("""

        SELECT

        id,

        tipo,

        titulo,

        canal,

        prioridade,

        status

        FROM approval_queue

        ORDER BY prioridade DESC

        """)

        filas=cursor.fetchall()

        conn.close()

        print()

        print("="*70)
        print("IOTEC APPROVAL QUEUE ENGINE")
        print("="*70)
        print(datetime.now())
        print("="*70)

        print()

        print("FILA DE APROVAÃƒâ€¡ÃƒÆ'O")

        print()

        for item in filas:

            print(f"[{item[0]:03}] {item[2]}")

            print("Tipo.........",item[1])

            print("Canal........",item[3])

            print("Prioridade...",item[4])

            print("Status.......",item[5])

            print()

        print("="*70)

        print("AÃƒâ€¡ÃƒÆ'O DO OPERADOR")

        print()

        print("1 - Aprovar")

        print("2 - Editar")

        print("3 - Rejeitar")

        print("4 - Adiar")

        print()

        print("="*70)

        print("FILOSOFIA")

        print()

        print("O Kernel prepara.")

        print("O operador decide.")

        print("A plataforma executa.")

        print()

        print("="*70)

        print("APPROVAL QUEUE ONLINE")

        print("="*70)


if __name__=="__main__":

    ApprovalQueue().executar()



