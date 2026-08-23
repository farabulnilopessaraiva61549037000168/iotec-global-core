import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================
IOTEC
018_DATABASE_CENTER.py

DATABASE CENTER
CENTRAL ADMINISTRATIVA DO BANCO DE DADOS

======================================================================
"""

import sqlite3
from datetime import datetime


class DatabaseCenter:

    def __init__(self):

        self.db = sqlite3.connect("iotec_kernel.db")
        self.cursor = self.db.cursor()

    # ================================================================

    def contar(self, tabela):

        try:

            self.cursor.execute(
                f"SELECT COUNT(*) FROM {tabela}"
            )

            return self.cursor.fetchone()[0]

        except:

            return 0

    # ================================================================

    def missoes_por_status(self, status):

        try:

            self.cursor.execute("""

            SELECT COUNT(*)

            FROM missoes

            WHERE status=?

            """, (status,))

            return self.cursor.fetchone()[0]

        except:

            return 0

    # ================================================================

    def painel(self):

        print("=" * 70)
        print("IOTEC DATABASE CENTER")
        print("=" * 70)
        print()

        print("Data :", datetime.now().strftime("%d/%m/%Y"))
        print("Hora :", datetime.now().strftime("%H:%M:%S"))

        print()
        print("=" * 70)
        print("BANCO DE DADOS")
        print("=" * 70)

        print()

        eventos = self.contar("eventos")
        missoes = self.contar("missoes")

        abertas = self.missoes_por_status("ABERTA")
        concluidas = self.missoes_por_status("CONCLUÃƒÂDA")
        bloqueadas = self.missoes_por_status("BLOQUEADA")

        print(f"Eventos................ {eventos}")
        print(f"MissÃƒÂµes................ {missoes}")
        print(f"Abertas................ {abertas}")
        print(f"ConcluÃƒÂ­das............. {concluidas}")
        print(f"Bloqueadas............. {bloqueadas}")

        print()

        print("=" * 70)
        print("SAÃƒÅ¡DE DO SISTEMA")
        print("=" * 70)

        print()

        if eventos > 0:
            print("Kernel................. ONLINE")
        else:
            print("Kernel................. SEM EVENTOS")

        if missoes > 0:
            print("Mission Engine......... ONLINE")
        else:
            print("Mission Engine......... SEM MISSÃƒâ€¢ES")

        print("SQLite................. ONLINE")
        print("Database Center........ ONLINE")

        print()

        print("=" * 70)
        print("RECOMENDAÃƒâ€¡Ãƒâ€¢ES")
        print("=" * 70)

        print()

        if abertas > 0:
            print(f"Ã¢â‚¬Â¢ Existem {abertas} missÃƒÂ£o(ÃƒÂµes) aguardando execuÃƒÂ§ÃƒÂ£o.")

        if bloqueadas > 0:
            print(f"Ã¢â‚¬Â¢ Existem {bloqueadas} missÃƒÂ£o(ÃƒÂµes) bloqueada(s).")

        if abertas == 0 and bloqueadas == 0:
            print("Ã¢â‚¬Â¢ Nenhuma pendÃƒÂªncia operacional encontrada.")

        print("Ã¢â‚¬Â¢ Continuar registrando eventos.")
        print("Ã¢â‚¬Â¢ Integrar novos mÃƒÂ³dulos ao Kernel.")
        print("Ã¢â‚¬Â¢ Utilizar o banco como fonte oficial dos dados.")

        print()

        print("=" * 70)

    # ================================================================

    def historico_eventos(self, limite=10):

        print()
        print("=" * 70)
        print("ÃƒÅ¡LTIMOS EVENTOS")
        print("=" * 70)
        print()

        try:

            self.cursor.execute("""

            SELECT

            data,
            categoria,
            origem,
            destino,
            status

            FROM eventos

            ORDER BY id DESC

            LIMIT ?

            """, (limite,))

            registros = self.cursor.fetchall()

            if not registros:

                print("Nenhum evento encontrado.")
                return

            for r in registros:

                print(
                    f"{r[0]} | {r[1]} | "
                    f"{r[2]} -> {r[3]} | {r[4]}"
                )

        except Exception as erro:

            print("Erro:", erro)

    # ================================================================

    def fechar(self):

        self.db.close()


# =====================================================================

if __name__ == "__main__":

    centro = DatabaseCenter()

    centro.painel()

    centro.historico_eventos()

    centro.fechar()



