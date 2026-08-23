import sqlite3
from pathlib import Path
from dataclasses import dataclass

ROOT = Path(r"C:\IOTEC")
CRM_DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"
RUNTIME_DB = r"C:\IOTEC_OMEGA_X\CORE\runtime\iotec.db"


@dataclass
class Finding:
    severity: str
    module: str
    title: str
    cause: str
    action: str


class AutonomousEngineer:

    def __init__(self):
        self.findings = []

    def banner(self):
        print("=" * 70)
        print("IOTEC AUTONOMOUS ENGINEER")
        print("=" * 70)

    def database_count(self, db, table):
        try:
            conn = sqlite3.connect(db)
            cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")
            value = cur.execute(
                f"SELECT COUNT(*) FROM {table}"
            ).fetchone()[0]
            conn.close()
            return value
        except Exception:
            return None

    def analyze_crm(self):

        leads = self.database_count(CRM_DB, "leads")
        opp = self.database_count(CRM_DB, "opportunities")
        pipe = self.database_count(CRM_DB, "pipeline")

        print()
        print("CRM")
        print("-" * 40)
        print(f"Leads............... {leads}")
        print(f"Opportunities....... {opp}")
        print(f"Pipeline............ {pipe}")

        if leads == 0:
            self.findings.append(
                Finding(
                    "HIGH",
                    "CRM",
                    "Nenhum lead",
                    "Banco sem leads.",
                    "Cadastrar primeiro lead."
                )
            )

        elif opp < leads:
            self.findings.append(
                Finding(
                    "HIGH",
                    "CRM",
                    "Leads sem oportunidade",
                    "Existem leads ainda nÃ£o promovidos.",
                    "Executar AUTO_MONETIZATION_ENGINE.py"
                )
            )

    def analyze_runtime(self):

        orders = self.database_count(RUNTIME_DB, "orders")

        print()
        print("RUNTIME")
        print("-" * 40)
        print(f"Orders.............. {orders}")

    def report(self):

        print()
        print("=" * 70)
        print("ROOT CAUSE REPORT")
        print("=" * 70)

        if not self.findings:
            print("Nenhum gargalo estrutural encontrado.")
            return

        for i, f in enumerate(self.findings, 1):

            print()
            print(f"GARGALO {i}")
            print(f"Severidade : {f.severity}")
            print(f"MÃ³dulo     : {f.module}")
            print(f"TÃ­tulo     : {f.title}")
            print(f"Causa      : {f.cause}")
            print(f"AÃ§Ã£o       : {f.action}")

    def run(self):

        self.banner()

        self.analyze_crm()

        self.analyze_runtime()

        self.report()


if __name__ == "__main__":

    AutonomousEngineer().run()


