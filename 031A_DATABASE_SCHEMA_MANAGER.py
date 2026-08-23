import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC DATABASE SCHEMA MANAGER
FASE 05
ETAPA 001

VersÃƒÂ£o 6.0

ConstrÃƒÂ³i automaticamente toda a estrutura do banco.

======================================================================
"""

import sqlite3

from datetime import datetime


class DatabaseSchemaManager:

    VERSION = "6.0"

    def __init__(self):

        self.conn = sqlite3.connect("iotec.db")

        self.cur = self.conn.cursor()

    # =============================================================

    def criar_companies(self):

        self.cur.execute("""

        CREATE TABLE IF NOT EXISTS companies(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            created_at TEXT,

            company_name TEXT,

            segment TEXT,

            city TEXT,

            state TEXT,

            country TEXT,

            website TEXT,

            linkedin TEXT,

            phone TEXT,

            email TEXT,

            status TEXT,

            opportunity_score INTEGER,

            notes TEXT

        )

        """)

    # =============================================================

    def criar_leads(self):

        self.cur.execute("""

        CREATE TABLE IF NOT EXISTS leads(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            created_at TEXT,

            company_id INTEGER,

            contact_name TEXT,

            email TEXT,

            phone TEXT,

            stage TEXT,

            status TEXT,

            value REAL,

            notes TEXT

        )

        """)

    # =============================================================

    def criar_products(self):

        self.cur.execute("""

        CREATE TABLE IF NOT EXISTS products(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            created_at TEXT,

            name TEXT,

            category TEXT,

            description TEXT,

            price REAL,

            status TEXT

        )

        """)

    # =============================================================

    def criar_campaigns(self):

        self.cur.execute("""

        CREATE TABLE IF NOT EXISTS campaigns(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            created_at TEXT,

            name TEXT,

            channel TEXT,

            objective TEXT,

            budget REAL,

            status TEXT

        )

        """)

    # =============================================================

    def criar_proposals(self):

        self.cur.execute("""

        CREATE TABLE IF NOT EXISTS proposals(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            created_at TEXT,

            company_id INTEGER,

            value REAL,

            status TEXT,

            notes TEXT

        )

        """)

    # =============================================================

    def criar_contracts(self):

        self.cur.execute("""

        CREATE TABLE IF NOT EXISTS contracts(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            created_at TEXT,

            proposal_id INTEGER,

            company_id INTEGER,

            value REAL,

            status TEXT

        )

        """)

    # =============================================================

    def criar_payments(self):

        self.cur.execute("""

        CREATE TABLE IF NOT EXISTS payments(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            created_at TEXT,

            contract_id INTEGER,

            amount REAL,

            payment_method TEXT,

            status TEXT

        )

        """)

    # =============================================================

    def criar_tasks(self):

        self.cur.execute("""

        CREATE TABLE IF NOT EXISTS tasks(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            created_at TEXT,

            title TEXT,

            department TEXT,

            priority TEXT,

            status TEXT

        )

        """)

    # =============================================================

    def criar_missions(self):

        self.cur.execute("""

        CREATE TABLE IF NOT EXISTS missions(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            created_at TEXT,

            mission TEXT,

            priority TEXT,

            status TEXT

        )

        """)

    # =============================================================

    def criar_settings(self):

        self.cur.execute("""

        CREATE TABLE IF NOT EXISTS settings(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            setting_name TEXT,

            setting_value TEXT

        )

        """)

    # =============================================================

    def criar_audit_log(self):

        self.cur.execute("""

        CREATE TABLE IF NOT EXISTS audit_log(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            created_at TEXT,

            module TEXT,

            action TEXT,

            details TEXT

        )

        """)

    # =============================================================

    def executar(self):

        print()

        print("="*70)
        print("IOTEC DATABASE SCHEMA MANAGER")
        print("="*70)
        print(datetime.now())
        print("="*70)

        self.criar_companies()
        self.criar_leads()
        self.criar_products()
        self.criar_campaigns()
        self.criar_proposals()
        self.criar_contracts()
        self.criar_payments()
        self.criar_tasks()
        self.criar_missions()
        self.criar_settings()
        self.criar_audit_log()

        self.conn.commit()

        tabelas = [

            "companies",
            "leads",
            "products",
            "campaigns",
            "proposals",
            "contracts",
            "payments",
            "tasks",
            "missions",
            "settings",
            "audit_log"

        ]

        print()

        print("TABELAS CRIADAS")

        print()

        for tabela in tabelas:

            print("Ã¢Å"â€œ", tabela)

        print()

        print("="*70)
        print("DATABASE STRUCTURE READY")
        print("="*70)

        self.conn.close()


if __name__ == "__main__":

    DatabaseSchemaManager().executar()



