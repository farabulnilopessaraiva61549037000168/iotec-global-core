import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC APPROVAL MANAGER
FASE 08
REVENUE ACTIVATION

VersÃƒÂ£o 9.0

Gerenciador de AprovaÃƒÂ§ÃƒÂ£o

======================================================================
"""

import sqlite3
from datetime import datetime

DB = "iotec.db"


class ApprovalManager:

    def conectar(self):
        return sqlite3.connect(DB, timeout=30)

    # =====================================================

    def listar(self):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        SELECT
            id,
            titulo,
            canal,
            prioridade,
            status

        FROM approval_queue

        ORDER BY id

        """)

        dados = cursor.fetchall()

        conn.close()

        return dados

    # =====================================================

    def atualizar(self, campanha_id, novo_status):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        UPDATE approval_queue

        SET status=?

        WHERE id=?

        """, (novo_status, campanha_id))

        conn.commit()

        alteradas = cursor.rowcount

        conn.close()

        return alteradas

    # =====================================================

    def executar(self):

        while True:

            campanhas = self.listar()

            print()
            print("=" * 70)
            print("IOTEC APPROVAL MANAGER")
            print("=" * 70)
            print(datetime.now())
            print("=" * 70)

            if not campanhas:

                print()
                print("Nenhuma campanha encontrada.")
                print()
                return

            print()

            for c in campanhas:

                print(f"[{c[0]:03}] {c[1]}")
                print("Canal........", c[2])
                print("Prioridade...", c[3])
                print("Status.......", c[4])
                print()

            print("=" * 70)
            print("MENU")
            print("=" * 70)
            print("1 - Aprovar")
            print("2 - Rejeitar")
            print("3 - Adiar")
            print("4 - Atualizar Lista")
            print("0 - Sair")
            print()

            opcao = input("Escolha: ").strip()

            if opcao == "0":
                break

            if opcao == "4":
                continue

            if opcao not in ("1", "2", "3"):
                continue

            try:

                campanha = int(input("ID da campanha: "))

            except ValueError:

                print("ID invÃƒÂ¡lido.")
                continue

            if opcao == "1":
                status = "APROVADA"

            elif opcao == "2":
                status = "REJEITADA"

            else:
                status = "ADIADA"

            alteradas = self.atualizar(campanha, status)

            print()

            if alteradas:

                print("Ã¢Å"â€œ Campanha atualizada com sucesso.")
                print("Novo status:", status)

                if status == "APROVADA":

                    print()
                    print("Kernel notificado.")
                    print("Dispatcher poderÃƒÂ¡ processar esta campanha.")

            else:

                print("Campanha nÃƒÂ£o encontrada.")

            input("\nPressione ENTER para continuar...")


# ==========================================================

if __name__ == "__main__":

    ApprovalManager().executar()



