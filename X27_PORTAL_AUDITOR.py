import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# X27_PORTAL_AUDITOR.py

import sqlite3
from pathlib import Path
from datetime import datetime

BASE = Path("C:/IOTEC")

print("=" * 70)
print("X27 PORTAL AUDITOR")
print("=" * 70)
print()
print("DATA:", datetime.now())
print()

dbs = {
    "LEADS": "IOTEC_REAL_LEADS.db",
    "PROPOSTAS": "IOTEC_PROPOSALS.db",
    "CONTRATOS": "IOTEC_CONTRACTS.db",
    "OPERACIONAL": "iotec_operational.db"
}

status = {}

for nome, arquivo in dbs.items():

    caminho = BASE / arquivo

    print("=" * 70)
    print(nome)
    print("=" * 70)

    if not caminho.exists():
        print("BANCO NAO ENCONTRADO")
        status[nome] = 0
        continue

    try:

        conn = sqlite3.connect(caminho)
        cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

        cur.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        )

        tabelas = [x[0] for x in cur.fetchall()]

        total = 0

        for tabela in tabelas:

            try:
                cur.execute(f"SELECT COUNT(*) FROM {tabela}")
                qtd = cur.fetchone()[0]

                print(f"{tabela:30} {qtd}")

                total += qtd

            except:
                pass

        status[nome] = total

        conn.close()

    except Exception as erro:
        print("ERRO:", erro)
        status[nome] = 0

print()
print("=" * 70)
print("PAINEL COMERCIAL")
print("=" * 70)

print()
print("LEADS.............", status.get("LEADS", 0))
print("PROPOSTAS.........", status.get("PROPOSTAS", 0))
print("CONTRATOS.........", status.get("CONTRATOS", 0))
print("OPERACIONAL.......", status.get("OPERACIONAL", 0))

print()

if status.get("LEADS", 0) == 0:
    print("ALERTA: SEM LEADS REAIS")

if status.get("PROPOSTAS", 0) == 0:
    print("ALERTA: SEM PROPOSTAS")

if status.get("CONTRATOS", 0) == 0:
    print("ALERTA: SEM CONTRATOS")

print()

if (
    status.get("LEADS", 0) > 0
    and status.get("PROPOSTAS", 0) > 0
):
    print("FUNIL COMERCIAL ATIVO")
else:
    print("FUNIL COMERCIAL INCOMPLETO")

print()

print("=" * 70)
print("PROXIMO PASSO")
print("=" * 70)

print("""
1 - Portal recebe lead
2 - Lead entra em IOTEC_REAL_LEADS.db
3 - Proposta ÃƒÂ© criada
4 - Link PIX/PayPal ÃƒÂ© gerado
5 - Pagamento confirmado
6 - Contrato criado
7 - Entrega registrada
8 - Receita contabilizada
""")

print("=" * 70)
print("AUDITORIA FINALIZADA")
print("=" * 70)



