import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================
IOTEC
017_MISSION_ENGINE.py
MISSION ENGINE V2.0
======================================================================
"""

import sqlite3
from datetime import datetime


class MissionEngine:

    def __init__(self):

        self.db = sqlite3.connect("iotec_kernel.db")
        self.cursor = self.db.cursor()

        self.criar_tabelas()

    # ===============================================================

    def criar_tabelas(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS missoes(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            codigo TEXT UNIQUE,

            data TEXT,

            titulo TEXT,

            solicitante TEXT,

            responsavel TEXT,

            prioridade TEXT,

            status TEXT,

            progresso INTEGER,

            observacao TEXT

        )

        """)

        self.db.commit()

    # ===============================================================

    def registrar_evento(self, codigo, descricao):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print()
        print("EVENTO:")
        print(f"[{horario}] {codigo} -> {descricao}")

    # ===============================================================

    def nova_missao(
        self,
        titulo,
        solicitante,
        responsavel,
        prioridade="NORMAL"
    ):

        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        self.cursor.execute("""

        INSERT INTO missoes(

            codigo,
            data,
            titulo,
            solicitante,
            responsavel,
            prioridade,
            status,
            progresso,
            observacao

        )

        VALUES(?,?,?,?,?,?,?,?,?)

        """,(

            "",
            data,
            titulo,
            solicitante,
            responsavel,
            prioridade,
            "ABERTA",
            0,
            ""

        ))

        self.db.commit()

        mission_id = self.cursor.lastrowid

        codigo = f"MIS-{mission_id:06d}"

        self.cursor.execute("""

        UPDATE missoes

        SET codigo=?

        WHERE id=?

        """,(codigo, mission_id))

        self.db.commit()

        self.registrar_evento(
            codigo,
            "MissÃƒÂ£o criada."
        )

        print()
        print("="*70)
        print("MISSÃƒÆ'O CRIADA")
        print("="*70)

        print("CÃƒÂ³digo.........", codigo)
        print("TÃƒÂ­tulo.........", titulo)
        print("Solicitante....", solicitante)
        print("ResponsÃƒÂ¡vel....", responsavel)
        print("Prioridade.....", prioridade)
        print("Status......... ABERTA")
        print()

    # ===============================================================

    def atualizar(self, codigo, progresso, status, observacao=""):

        self.cursor.execute("""

        UPDATE missoes

        SET

        progresso=?,
        status=?,
        observacao=?

        WHERE codigo=?

        """,(

            progresso,
            status,
            observacao,
            codigo

        ))

        self.db.commit()

        self.registrar_evento(

            codigo,

            f"Status alterado para {status} ({progresso}%)"

        )

    # ===============================================================

    def listar(self):

        print()
        print("="*70)
        print("MISSÃƒâ€¢ES")
        print("="*70)

        self.cursor.execute("""

        SELECT

        codigo,
        titulo,
        responsavel,
        prioridade,
        status,
        progresso

        FROM missoes

        ORDER BY id DESC

        """)

        registros = self.cursor.fetchall()

        if not registros:

            print()
            print("Nenhuma missÃƒÂ£o cadastrada.")
            return

        for r in registros:

            print()
            print("CÃƒÂ³digo........", r[0])
            print("TÃƒÂ­tulo........", r[1])
            print("ResponsÃƒÂ¡vel...", r[2])
            print("Prioridade....", r[3])
            print("Status........", r[4])
            print("Progresso.....", str(r[5]) + "%")
            print("-"*60)

    # ===============================================================

    def resumo(self):

        self.cursor.execute("SELECT COUNT(*) FROM missoes")
        total = self.cursor.fetchone()[0]

        self.cursor.execute("SELECT COUNT(*) FROM missoes WHERE status='ABERTA'")
        abertas = self.cursor.fetchone()[0]

        self.cursor.execute("SELECT COUNT(*) FROM missoes WHERE status='CONCLUÃƒÂDA'")
        concluidas = self.cursor.fetchone()[0]

        self.cursor.execute("SELECT COUNT(*) FROM missoes WHERE status='BLOQUEADA'")
        bloqueadas = self.cursor.fetchone()[0]

        print()
        print("="*70)
        print("PAINEL DE MISSÃƒâ€¢ES")
        print("="*70)

        print()

        print(f"Total.............. {total}")
        print(f"Abertas............ {abertas}")
        print(f"ConcluÃƒÂ­das......... {concluidas}")
        print(f"Bloqueadas......... {bloqueadas}")

        print()
        print("="*70)

    # ===============================================================

    def fechar(self):

        self.db.close()


# ======================================================================

if __name__ == "__main__":

    motor = MissionEngine()

    motor.nova_missao(

        titulo="Buscar Empresas de Contabilidade",

        solicitante="Comercial",

        responsavel="TRK-002",

        prioridade="ALTA"

    )

    motor.nova_missao(

        titulo="Revisar Projeto Executivo",

        solicitante="ProduÃƒÂ§ÃƒÂ£o",

        responsavel="AGENTE-04"

    )

    motor.listar()

    motor.resumo()

    motor.fechar()



