import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# UNIFY_COMMERCIAL_CORE.py
#
# Objetivo:
# Descobrir automaticamente quais bancos possuem
# leads, oportunidades, pagamentos, clientes e receita
# e consolidar tudo em uma visÃƒÆ'Ã†â€™o ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºnica.
#
# Resultado:
# C:\IOTEC\COMMERCIAL_UNIVERSE_REPORT.txt

import os
import sqlite3
from datetime import datetime

ROOT = r"C:\IOTEC"

REPORT = r"C:\IOTEC\COMMERCIAL_UNIVERSE_REPORT.txt"

dbs = []

for raiz, dirs, files in os.walk(ROOT):
    pass

    for arq in files:
        pass

        if arq.endswith(".db"):
            pass

            dbs.append(
                os.path.join(
                    raiz,
                    arq
                )
            )

resultado = []

for banco in dbs:
    pass

    try:
        pass

        conn = sqlite3.connect(banco)

        cur = conn.cursor()

        tabelas = cur.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type='table'
            """
        ).fetchall()

        tabelas = [t[0] for t in tabelas]

        info = {
            "db": banco,
            "tables": {},
            "score": 0
        }

        for tabela in tabelas:
            pass

            try:
                pass

                qtd = cur.execute(
                    f"SELECT COUNT(*) FROM {tabela}"
                ).fetchone()[0]

            except:
                pass

                qtd = "?"

            info["tables"][tabela] = qtd

            nome = tabela.lower()

            if "lead" in nome:
                info["score"] += 10

            if "opportun" in nome:
                info["score"] += 15

            if "payment" in nome:
                info["score"] += 20

            if "invoice" in nome:
                info["score"] += 20

            if "client" in nome:
                info["score"] += 15

            if "revenue" in nome:
                info["score"] += 25

        conn.close()

        resultado.append(info)

    except Exception as e:
        pass

        resultado.append({

            "db": banco,
            "erro": str(e),
            "score": 0

        })

resultado.sort(
    key=lambda x: x["score"],
    reverse=True
)

with open(
    REPORT,
    "w",
    encoding="utf-8"
) as r:

    r.write("\n")
    r.write("="*70 + "\n")
    r.write("IOTEC COMMERCIAL UNIVERSE AUDIT\n")
    r.write("="*70 + "\n\n")

    r.write(
        f"DATA: {datetime.now()}\n\n"
    )

    for item in resultado:
        pass

        r.write(
            "\n" + "="*60 + "\n"
        )

        r.write(
            item["db"] + "\n"
        )

        r.write(
            "="*60 + "\n"
        )

        r.write(
            f"SCORE COMERCIAL: {item['score']}\n\n"
        )

        if "erro" in item:
            pass

            r.write(
                "ERRO: " +
                item["erro"] +
                "\n"
            )

            continue

        for tabela, qtd in item["tables"].items():
            pass

            r.write(
                f"{tabela} -> {qtd}\n"
            )

    r.write("\n")
    r.write("="*70 + "\n")
    r.write("FIM DA AUDITORIA\n")
    r.write("="*70 + "\n")

print("")
print("="*60)
print("COMMERCIAL UNIVERSE AUDIT CONCLUIDO")
print("="*60)
print(REPORT)
print("")


