import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
from datetime import datetime

DB = r"C:\IOTEC\IOTEC_MISSION_EXECUTION.db"

print("=" * 70)
print("X27 FIRST CLIENT MISSION")
print("=" * 70)
print()

print("DATA:", datetime.now())
print()

produto = "AUDITORIA OPERACIONAL INTELIGENTE"

meta_leads = 50
meta_reunioes = 10
meta_propostas = 5

receita_alvo = 15000.00

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

cur.execute("""
CREATE TABLE IF NOT EXISTS first_client_mission(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TEXT,
    produto TEXT,
    target_leads INTEGER,
    target_meetings INTEGER,
    target_proposals INTEGER,
    revenue_goal REAL,
    status TEXT
)
""")

cur.execute("""
INSERT INTO first_client_mission(
    created_at,
    produto,
    target_leads,
    target_meetings,
    target_proposals,
    revenue_goal,
    status
)
VALUES (?,?,?,?,?,?,?)
""",(
    str(datetime.now()),
    produto,
    meta_leads,
    meta_reunioes,
    meta_propostas,
    receita_alvo,
    "ATIVA"
))

conn.commit()

print("=" * 70)
print("MISSAO LIBERADA")
print("=" * 70)

print()

print("PRODUTO:")
print(produto)

print()

print("METAS")

print(f"LEADS............. {meta_leads}")
print(f"REUNIOES.......... {meta_reunioes}")
print(f"PROPOSTAS......... {meta_propostas}")

print()

print(f"RECEITA ALVO...... R$ {receita_alvo:,.2f}")

print()

print("PIPELINE ESPERADO")

print("50 LEADS")
print("Ã¢â€ â€œ")
print("10 REUNIOES")
print("Ã¢â€ â€œ")
print("5 PROPOSTAS")
print("Ã¢â€ â€œ")
print("1 CLIENTE")
print("Ã¢â€ â€œ")
print("RECEITA")

print()

print("=" * 70)
print("LISTA DE ATAQUE")
print("=" * 70)

segmentos = [
    "PREFEITURAS",
    "ESCOLAS PARTICULARES",
    "CLINICAS",
    "INDUSTRIAS",
    "ESCRITORIOS CONTABEIS"
]

for s in segmentos:
    print("[ ]", s)

print()

print("OBJETIVO:")
print("PRIMEIRO CLIENTE REAL PAGANTE")

conn.close()



