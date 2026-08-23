import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# X27_COMMERCIAL_XRAY.py

import sqlite3

DATABASES = {
    "LEADS": [
        r"C:\IOTEC\enterprise.db",
        r"C:\IOTEC\IOTEC_ACCOUNT_REGISTRY.db",
        r"C:\IOTEC\iotec_global.db",
        r"C:\IOTEC\tower.db"
    ],
    "OPORTUNIDADES": [
        r"C:\IOTEC\IOTEC_OPPORTUNITY.db",
        r"C:\IOTEC\opportunity_radar.db"
    ],
    "PROPOSTAS": [
        r"C:\IOTEC\IOTEC_PROPOSALS.db"
    ],
    "CONTRATOS": [
        r"C:\IOTEC\IOTEC_CONTRACTS.db"
    ],
    "OPERACIONAL": [
        r"C:\IOTEC\iotec_operational.db"
    ]
}

print("="*70)
print("X27 COMMERCIAL XRAY")
print("="*70)

for categoria, bancos in DATABASES.items():

    print("\n")
    print("="*70)
    print(categoria)
    print("="*70)

    for banco in bancos:

        try:

            conn = sqlite3.connect(banco)
            cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

            cur.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
            )

            tabelas = cur.fetchall()

            print("\nBANCO:", banco)

            for tabela in tabelas:

                nome = tabela[0]

                try:

                    cur.execute(
                        f"SELECT * FROM [{nome}] LIMIT 5"
                    )

                    registros = cur.fetchall()

                    print("\nTABELA:", nome)

                    for r in registros:
                        print(r)

                except Exception:
                    pass

            conn.close()

        except Exception as erro:
            print("ERRO:", erro)

print("\nXRAY FINALIZADO")



