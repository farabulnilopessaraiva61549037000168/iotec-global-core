import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
from pathlib import Path
from datetime import datetime

ROOT = Path(r"C:\IOTEC")

print("=" * 70)
print("X27 CASH AUDITOR")
print("=" * 70)
print()
print("DATA:", datetime.now())
print()

receita_confirmada = 0.0
pagamentos_confirmados = []
contratos_encontrados = []
faturas_encontradas = []

# =====================================================
# FUNCAO
# =====================================================

def abrir_db(caminho):
    try:
        return sqlite3.connect(caminho)
    except:
        return None

# =====================================================
# VARREDURA
# =====================================================

for db in ROOT.glob("*.db"):

    print("=" * 70)
    print("ANALISANDO:", db.name)
    print("=" * 70)

    conn = abrir_db(db)

    if not conn:
        continue

    cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

    try:

        cur.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        """)

        tabelas = [x[0] for x in cur.fetchall()]

        # -----------------------------------------
        # PAYMENTS
        # -----------------------------------------

        if "payments" in tabelas:

            try:

                cur.execute("""
                SELECT *
                FROM payments
                """)

                registros = cur.fetchall()

                for r in registros:

                    status = str(r[5]).upper()

                    if "CONFIRMED" in status:
                        valor = float(r[3])

                        receita_confirmada += valor

                        pagamentos_confirmados.append({
                            "db": db.name,
                            "payment_id": r[1],
                            "valor": valor,
                            "gateway": r[4],
                            "data": r[6]
                        })

            except:
                pass

        # -----------------------------------------
        # CONTRACTS
        # -----------------------------------------

        if "contracts" in tabelas:

            try:

                cur.execute("""
                SELECT *
                FROM contracts
                """)

                registros = cur.fetchall()

                for r in registros:

                    contratos_encontrados.append({
                        "db": db.name,
                        "cliente": r[2],
                        "produto": r[3],
                        "valor": r[4],
                        "status": r[5]
                    })

            except:
                pass

        # -----------------------------------------
        # INVOICES
        # -----------------------------------------

        if "invoices" in tabelas:

            try:

                cur.execute("""
                SELECT *
                FROM invoices
                """)

                registros = cur.fetchall()

                for r in registros:

                    faturas_encontradas.append({
                        "db": db.name,
                        "invoice": r[1],
                        "valor": r[4],
                        "status": r[5]
                    })

            except:
                pass

    except:
        pass

    conn.close()

# =====================================================
# RELATORIO
# =====================================================

print()
print("=" * 70)
print("RECEITA CONFIRMADA")
print("=" * 70)

print(f"TOTAL : R$ {receita_confirmada:,.2f}")

print()

if pagamentos_confirmados:

    print("PAGAMENTOS CONFIRMADOS")
    print()

    for p in pagamentos_confirmados:

        print(
            p["payment_id"],
            "|",
            f'R$ {p["valor"]:,.2f}',
            "|",
            p["gateway"],
            "|",
            p["data"]
        )

else:

    print("NENHUM PAGAMENTO CONFIRMADO")

# =====================================================

print()
print("=" * 70)
print("CONTRATOS")
print("=" * 70)

for c in contratos_encontrados:

    print(
        c["cliente"],
        "|",
        c["produto"],
        "|",
        f'R$ {float(c["valor"]):,.2f}',
        "|",
        c["status"]
    )

# =====================================================

print()
print("=" * 70)
print("FATURAS")
print("=" * 70)

if not faturas_encontradas:

    print("NENHUMA FATURA ENCONTRADA")

else:

    for f in faturas_encontradas:

        print(
            f["invoice"],
            "|",
            f'R$ {float(f["valor"]):,.2f}',
            "|",
            f["status"]
        )

# =====================================================

print()
print("=" * 70)

if receita_confirmada > 0:

    print("EXISTE RECEITA REGISTRADA")

else:

    print("NAO EXISTE RECEITA REAL CONFIRMADA")

print("=" * 70)



