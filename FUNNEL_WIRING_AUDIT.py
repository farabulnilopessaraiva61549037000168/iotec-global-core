import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# FUNNEL_WIRING_AUDIT.py
# Auditoria de IntegraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o Comercial do NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo

import os
import sqlite3
from pathlib import Path

ROOT = r"C:\IOTEC"

REPORT = r"C:\IOTEC\FUNNEL_WIRING_REPORT.txt"

ALVOS = {

    "LEAD":[
        "lead"
    ],

    "SCORE":[
        "score"
    ],

    "PIPELINE":[
        "pipeline",
        "opportunity"
    ],

    "PROPOSTA":[
        "proposal",
        "proposta"
    ],

    "NEGOCIACAO":[
        "negotiation",
        "approve"
    ],

    "PAGAMENTO":[
        "payment",
        "paypal",
        "billing"
    ],

    "RECEITA":[
        "revenue",
        "monetization"
    ],

    "DASHBOARD":[
        "dashboard",
        "tower"
    ]

}

resultado = {}

for etapa in ALVOS:
    pass

    resultado[etapa] = []

for raiz, dirs, files in os.walk(ROOT):
    pass

    for arq in files:
        pass

        if not arq.endswith(".py"):
            continue

        caminho = os.path.join(
            raiz,
            arq
        )

        nome = arq.lower()

        try:
            pass

            with open(
                caminho,
                "r",
                encoding="utf-8",
                errors="ignore"
            ) as f:

                conteudo = f.read().lower()

        except:
            continue

        for etapa, palavras in ALVOS.items():
            pass

            score = 0

            for p in palavras:
                pass

                score += conteudo.count(p)
                score += nome.count(p) * 10

            if score > 0:
                pass

                resultado[etapa].append(

                    (
                        score,
                        caminho
                    )

                )

with open(
    REPORT,
    "w",
    encoding="utf-8"
) as r:

    r.write("\n")
    r.write("="*70 + "\n")
    r.write("FUNNEL WIRING AUDIT\n")
    r.write("="*70 + "\n\n")

    for etapa in resultado:
        pass

        r.write(
            f"\n[{etapa}]\n"
        )

        r.write(
            "-"*60 + "\n"
        )

        resultado[etapa].sort(
            reverse=True
        )

        for score, caminho in resultado[etapa][:30]:
            pass

            r.write(
                f"{score:04} | {caminho}\n"
            )

    r.write("\n")
    r.write("="*70 + "\n")

# ---------------------------------------------------
# BANCOS
# ---------------------------------------------------

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

with open(
    REPORT,
    "a",
    encoding="utf-8"
) as r:

    r.write("\nDATABASES\n")
    r.write("-"*60 + "\n")

    for banco in dbs:
        pass

        r.write(
            banco + "\n"
        )

        try:
            pass

            c = sqlite3.connect(banco)

            tabelas = c.execute(

                """
                SELECT name
                FROM sqlite_master
                WHERE type='table'
                """

            ).fetchall()

            for t in tabelas:
                pass

                r.write(
                    f"   TABLE: {t[0]}\n"
                )

            c.close()

        except Exception as e:
            pass

            r.write(
                f"   ERRO: {e}\n"
            )

print("")
print("="*60)
print("FUNNEL WIRING AUDIT CONCLUIDO")
print("="*60)
print(REPORT)
print("")




