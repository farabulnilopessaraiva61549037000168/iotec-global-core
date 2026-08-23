import os
import sqlite3
from pathlib import Path
from dataclasses import dataclass

ROOT = Path(r"C:\IOTEC")

CRM_DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"
RUNTIME_DB = r"C:\IOTEC_OMEGA_X\CORE\runtime\iotec.db"

@dataclass
class DiagnosticResult:
    module: str
    status: str
    severity: str
    cause: str
    solution: str
    next_action: str

def title(text):
    print()
    print("=" * 70)
    print(text)
    print("=" * 70)

def ok(v):
    return "[OK]" if v else "[ERRO]"

def count(db, table):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")
        value = cur.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        conn.close()
        return value
    except Exception:
        return None

title("IOTEC DIAGNOSTIC ASSISTANT V2")

print()

for table in ["leads","opportunities","pipeline"]:

    value = count(CRM_DB, table)

    print(f"{table:<20}: {value}")

print()

orders = count(RUNTIME_DB,"orders")

print(f"orders               : {orders}")

print()

print("ROOT CAUSE")

if count(CRM_DB,"leads")==0:

    print("Nenhum lead encontrado.")

elif count(CRM_DB,"opportunities") < count(CRM_DB,"leads"):

    print("Existem leads sem opportunities.")

elif count(CRM_DB,"pipeline") < count(CRM_DB,"opportunities"):

    print("Pipeline desatualizado.")

else:

    print("Fluxo estrutural OK.")


