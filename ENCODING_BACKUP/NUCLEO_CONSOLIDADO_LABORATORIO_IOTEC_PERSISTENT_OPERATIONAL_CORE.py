import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC_PERSISTENT_OPERATIONAL_CORE.py
# ============================================================
# PERSISTÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â NCIA OPERACIONAL + WORKFLOW + RASTREAMENTO
# ============================================================
# EVOLUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O:
# ------------------------------------------------------------
# Este nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo adiciona:
#
# - persistÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia real
# - banco SQLite
# - armazenamento de projetos
# - rastreamento permanente
# - workflow persistente
# - recuperaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de sessÃƒÆ'Ã†â€™o
# - histÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rico operacional
# - continuidade do atendimento
#
# ============================================================

import sqlite3
import uuid
import time
from datetime import datetime

# ============================================================
# BANCO DE DADOS
# ============================================================

DATABASE = "iotec_operational.db"

# ============================================================
# CATÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂLOGO
# ============================================================

CATALOG = {

    "ERP Empresarial": 35000,
    "Sistema Industrial": 45000,
    "Dashboard Inteligente": 15000,
    "Sistema JurÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­dico": 28000,
    "Sistema Hospitalar": 55000
}

# ============================================================
# ENGINE
# ============================================================

class IOTECOperationalEngine:
    pass

    def __init__(self):
        pass

        self.conn = sqlite3.connect(DATABASE)

        self.cursor = self.conn.cursor()

        self.create_tables()

    # ========================================================
    # IA VISUAL
    # ========================================================

    def think(self, text):
        pass

        print(f"\n[IOTEC CORE] {text}")

        time.sleep(1)

    # ========================================================
    # TABELAS
    # ========================================================

    def create_tables(self):
        pass

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS clients (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT,

            email TEXT,

            company TEXT
        )

        """)

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS projects (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            project_id TEXT,

            client_id INTEGER,

            service TEXT,

            total_value REAL,

            entry_value REAL,

            remaining_value REAL,

            status TEXT,

            created_at TEXT
        )

        """)

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS workflow (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            project_id TEXT,

            step TEXT,

            created_at TEXT
        )

        """)

        self.conn.commit()

    # ========================================================
    # CLIENTE
    # ========================================================

    def create_client(self):
        pass

        print("\n================ CLIENTE ================")

        name = input("\nNome: ")

        email = input("\nE-mail: ")

        company = input("\nEmpresa: ")

        self.cursor.execute("""

        INSERT INTO clients (
            name,
            email,
            company
        )

        VALUES (?, ?, ?)

        """, (name, email, company))

        self.conn.commit()

        return self.cursor.lastrowid

    # ========================================================
    # CATÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂLOGO
    # ========================================================

    def show_catalog(self):
        pass

        print("\n================ CATÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂLOGO ================")

        services = list(CATALOG.keys())

        for index, item in enumerate(services, start=1):
            pass

            print(f"\n{index} - {item}")

        return services

    # ========================================================
    # APRESENTAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
    # ========================================================

    def presentation(self, service):
        pass

        value = CATALOG[service]

        self.think(
            f"Apresentando soluÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o {service}"
        )

        print("\n================ APRESENTAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O ================")

        print(f"\nSERVIÃƒÆ'Ã†â€™O:")
        print(service)

        print(f"\nVALOR:")
        print(f"R$ {value:,.2f}")

        print("\nBENEFÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂCIOS:")

        print("- AutomaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o operacional")
        print("- ReduÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de falhas")
        print("- Monitoramento inteligente")
        print("- Escalabilidade")
        print("- GestÃƒÆ'Ã†â€™o integrada")

    # ========================================================
    # INVESTIGAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
    # ========================================================

    def investigation(self):
        pass

        print("\n================ INVESTIGAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O ================")

        sector = input(
            "\nQual ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© o setor?\n\n>>> "
        )

        problem = input(
            "\nQuais gargalos existem?\n\n>>> "
        )

        objective = input(
            "\nQual ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© o objetivo principal?\n\n>>> "
        )

        users = input(
            "\nQuantos usuÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rios utilizarÃƒÆ'Ã†â€™o o sistema?\n\n>>> "
        )

        return {

            "sector": sector,
            "problem": problem,
            "objective": objective,
            "users": users
        }

    # ========================================================
    # CRIAR PROJETO
    # ========================================================

    def create_project(self, client_id, service):
        pass

        total = CATALOG[service]

        entry = total * 0.30

        remaining = total * 0.70

        project_id = f"IOTEC-{str(uuid.uuid4())[:8].upper()}"

        status = "AGUARDANDO PAGAMENTO"

        created_at = str(datetime.now())

        self.cursor.execute("""

        INSERT INTO projects (

            project_id,
            client_id,
            service,
            total_value,
            entry_value,
            remaining_value,
            status,
            created_at

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?)

        """, (

            project_id,
            client_id,
            service,
            total,
            entry,
            remaining,
            status,
            created_at
        ))

        self.conn.commit()

        self.add_workflow(
            project_id,
            "Projeto criado"
        )

        return project_id

    # ========================================================
    # WORKFLOW
    # ========================================================

    def add_workflow(self, project_id, step):
        pass

        created_at = str(datetime.now())

        self.cursor.execute("""

        INSERT INTO workflow (

            project_id,
            step,
            created_at

        )

        VALUES (?, ?, ?)

        """, (

            project_id,
            step,
            created_at
        ))

        self.conn.commit()

    # ========================================================
    # MOSTRAR PROPOSTA
    # ========================================================

    def show_proposal(self, project_id):
        pass

        self.cursor.execute("""

        SELECT
            service,
            total_value,
            entry_value,
            remaining_value,
            status

        FROM projects

        WHERE project_id = ?

        """, (project_id,))

        project = self.cursor.fetchone()

        print("\n================ PROPOSTA ================")

        print(f"\nPROJECT ID:")
        print(project_id)

        print(f"\nSERVIÃƒÆ'Ã†â€™O:")
        print(project[0])

        print(f"\nVALOR TOTAL:")
        print(f"R$ {project[1]:,.2f}")

        print(f"\nENTRADA:")
        print(f"R$ {project[2]:,.2f}")

        print(f"\nRESTANTE:")
        print(f"R$ {project[3]:,.2f}")

        print(f"\nSTATUS:")
        print(project[4])

    # ========================================================
    # PAGAMENTO
    # ========================================================

    def payment_phase(self, project_id):
        pass

        self.think(
            "Aguardando confirmaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o financeira..."
        )

        print("\n================ PAGAMENTO ================")

        print("\nMÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°TODOS:")

        print("- PIX")
        print("- Stripe")
        print("- PayPal")
        print("- TransferÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia")

        self.add_workflow(
            project_id,
            "Pagamento solicitado"
        )

    # ========================================================
    # LIBERAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
    # ========================================================

    def internal_release(self, project_id):
        pass

        print("\n================ FINANCEIRO ================")

        confirmation = input(
            "\nPagamento reconhecido?\n\n>>> "
        ).lower()

        if confirmation in ["sim", "s"]:
            pass

            self.cursor.execute("""

            UPDATE projects

            SET status = ?

            WHERE project_id = ?

            """, (

                "PRODUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O LIBERADA",
                project_id
            ))

            self.conn.commit()

            self.add_workflow(
                project_id,
                "Pagamento confirmado"
            )

            self.think(
                "Projeto liberado."
            )

            return True

        self.think(
            "Projeto pausado."
        )

        return False

    # ========================================================
    # PRODUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
    # ========================================================

    def production(self, project_id):
        pass

        stages = [

            "Criando arquitetura",
            "Gerando banco de dados",
            "Configurando backend",
            "Construindo frontend",
            "Configurando APIs",
            "Executando validaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes",
            "Preparando entrega"
        ]

        print("\n================ PRODUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O ================")

        for stage in stages:
            pass

            self.think(stage)

            self.add_workflow(
                project_id,
                stage
            )

        self.cursor.execute("""

        UPDATE projects

        SET status = ?

        WHERE project_id = ?

        """, (

            "PROJETO FINALIZADO",
            project_id
        ))

        self.conn.commit()

    # ========================================================
    # ENTREGA
    # ========================================================

    def delivery(self, project_id):
        pass

        self.add_workflow(
            project_id,
            "Projeto entregue"
        )

        print("\n================ ENTREGA ================")

        print("\nSTATUS:")
        print("PROJETO ENTREGUE")

        print("\nSUPORTE:")
        print("Monitoramento inteligente ativo.")

    # ========================================================
    # RASTREAMENTO
    # ========================================================

    def tracking(self, project_id):
        pass

        print("\n================ RASTREAMENTO ================")

        self.cursor.execute("""

        SELECT
            status

        FROM projects

        WHERE project_id = ?

        """, (project_id,))

        status = self.cursor.fetchone()

        print(f"\nPROJECT ID:")
        print(project_id)

        print(f"\nSTATUS:")
        print(status[0])

        print("\nFLUXO:")

        self.cursor.execute("""

        SELECT
            step,
            created_at

        FROM workflow

        WHERE project_id = ?

        """, (project_id,))

        steps = self.cursor.fetchall()

        for step in steps:
            pass

            print(f"- {step[0]} | {step[1]}")

    # ========================================================
    # RECUPERAR PROJETO
    # ========================================================

    def recover_project(self):
        pass

        print("\n================ RECUPERAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O ================")

        project_id = input(
            "\nDigite o PROJECT ID:\n\n>>> "
        )

        self.cursor.execute("""

        SELECT
            status

        FROM projects

        WHERE project_id = ?

        """, (project_id,))

        project = self.cursor.fetchone()

        if not project:
            pass

            self.think(
                "Projeto nÃƒÆ'Ã†â€™o encontrado."
            )

            return

        self.think(
            "Projeto recuperado."
        )

        self.tracking(project_id)

    # ========================================================
    # FLUXO PRINCIPAL
    # ========================================================

    def start(self):
        pass

        print("\n================================================")
        print("       IOTEC PERSISTENT OPERATIONAL CORE")
        print("================================================")

        print("\n1 - Novo projeto")
        print("2 - Recuperar projeto")

        option = input("\n>>> ")

        if option == "2":
            pass

            self.recover_project()

            return

        client_id = self.create_client()

        services = self.show_catalog()

        choice = int(
            input(
                "\nEscolha um serviÃƒÆ'Ã†â€™o:\n\n>>> "
            )
        )

        selected_service = services[choice - 1]

        self.presentation(selected_service)

        self.investigation()

        project_id = self.create_project(
            client_id,
            selected_service
        )

        self.show_proposal(project_id)

        self.payment_phase(project_id)

        released = self.internal_release(project_id)

        if not released:
            pass

            return

        self.production(project_id)

        self.delivery(project_id)

        self.tracking(project_id)

# ============================================================
# EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ============================================================

if __name__ == "__main__":
    pass

    engine = IOTECOperationalEngine()

    engine.start()


