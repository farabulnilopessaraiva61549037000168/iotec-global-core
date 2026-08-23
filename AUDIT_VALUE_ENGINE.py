import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# AUDIT_VALUE_ENGINE.py

import os
import sqlite3
from pathlib import Path
from datetime import datetime

ROOT = r"C:\IOTEC_OMEGA_X"

RELATORIO = os.path.join(
    ROOT,
    "REPORTS",
    "AUDITORIA_VALOR_ATIVOS.txt"
)

DB = os.path.join(
    ROOT,
    "backend",
    "iotec.db"
)

ARQUIVOS = 0
LINHAS = 0
TAMANHO = 0

EXTENSOES = {
    ".py": 5,
    ".html": 4,
    ".js": 4,
    ".json": 2,
    ".db": 8,
    ".css": 2
}

PONTOS = 0

for raiz, dirs, files in os.walk(ROOT):
    pass

    for nome in files:
        pass

        caminho = os.path.join(raiz, nome)

        try:
            pass

            tamanho = os.path.getsize(caminho)

            TAMANHO += tamanho

            ARQUIVOS += 1

            ext = Path(nome).suffix.lower()

            PONTOS += EXTENSOES.get(ext, 1)

            if ext in [".py", ".html", ".js", ".css"]:
                pass

                with open(
                    caminho,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as f:

                    qtd = len(f.readlines())

                    LINHAS += qtd

        except:
            pass

# =====================================================
# CRM
# =====================================================

LEADS = 0
OPPS = 0
CLIENTES = 0

if os.path.exists(DB):
    pass

    try:
        pass

        conn = sqlite3.connect(DB, timeout=30)

        cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

        try:
            LEADS = cur.execute(
                "SELECT COUNT(*) FROM leads"
            ).fetchone()[0]
        except:
            pass

        try:
            OPPS = cur.execute(
                "SELECT COUNT(*) FROM opportunities"
            ).fetchone()[0]
        except:
            pass

        try:
            CLIENTES = cur.execute(
                """
                SELECT COUNT(*)
                FROM pipeline
                WHERE status='CLIENTE_ATIVO'
                """
            ).fetchone()[0]
        except:
            pass

        conn.close()

    except:
        pass

# =====================================================
# ESTIMATIVA
# =====================================================

VALOR_REPOSICAO_USD = max(
    5000,
    int(
        (LINHAS * 0.5)
        +
        (ARQUIVOS * 25)
        +
        (PONTOS * 100)
    )
)

VALOR_REPOSICAO_BRL = VALOR_REPOSICAO_USD * 5.50

# =====================================================
# RELATORIO
# =====================================================

os.makedirs(
    os.path.dirname(RELATORIO),
    exist_ok=True
)

with open(
    RELATORIO,
    "w",
    encoding="utf-8"
) as f:

    f.write("\n")
    f.write("=====================================\n")
    f.write("IOTEC AUDITORIA DE VALOR\n")
    f.write("=====================================\n")
    f.write("\n")

    f.write(
        f"DATA: {datetime.now()}\n\n"
    )

    f.write(
        f"ARQUIVOS: {ARQUIVOS}\n"
    )

    f.write(
        f"LINHAS CODIGO: {LINHAS}\n"
    )

    f.write(
        f"TAMANHO TOTAL: {round(TAMANHO/1024/1024,2)} MB\n"
    )

    f.write(
        f"PONTUACAO TECNICA: {PONTOS}\n\n"
    )

    f.write(
        f"LEADS: {LEADS}\n"
    )

    f.write(
        f"OPPORTUNITIES: {OPPS}\n"
    )

    f.write(
        f"CLIENTES ATIVOS: {CLIENTES}\n\n"
    )

    f.write(
        f"VALOR REPOSICAO USD: ${VALOR_REPOSICAO_USD:,.2f}\n"
    )

    f.write(
        f"VALOR REPOSICAO BRL: R$ {VALOR_REPOSICAO_BRL:,.2f}\n"
    )

    f.write("\n")
    f.write("=====================================\n")
    f.write("FIM DA AUDITORIA\n")
    f.write("=====================================\n")

print("")
print("=====================================")
print("AUDITORIA CONCLUIDA")
print("=====================================")
print(RELATORIO)
print("")




