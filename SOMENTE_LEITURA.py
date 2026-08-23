# ============================================================
# IOTEC - MÃƒâ€œDULO 001
# INDUSTRIAL CORE AUDITOR
# VersÃƒÂ£o: 2026.1
# Modo: SOMENTE LEITURA
# ============================================================

from pathlib import Path
import os
import sys
import platform
import sqlite3
import json
from datetime import datetime

ROOT = Path.cwd()

relatorio = {
    "data": datetime.now().isoformat(),
    "sistema": {},
    "arquivos_python": [],
    "bancos_sqlite": [],
    "variaveis_ambiente": [],
    "pastas": [],
    "estatisticas": {}
}

# ------------------------------------------------------------
# SISTEMA
# ------------------------------------------------------------

relatorio["sistema"] = {
    "python": sys.version,
    "plataforma": platform.platform(),
    "processador": platform.processor(),
    "diretorio": str(ROOT)
}

# ------------------------------------------------------------
# PASTAS
# ------------------------------------------------------------

for pasta in ROOT.iterdir():
    if pasta.is_dir():
        relatorio["pastas"].append(str(pasta))

# ------------------------------------------------------------
# PYTHON
# ------------------------------------------------------------

for py in ROOT.rglob("*.py"):

    try:
        tamanho = py.stat().st_size

        relatorio["arquivos_python"].append({
            "arquivo": str(py),
            "kb": round(tamanho / 1024, 2)
        })

    except Exception:
        pass

# ------------------------------------------------------------
# SQLITE
# ------------------------------------------------------------

for banco in ROOT.rglob("*.db"):

    try:

        conn = sqlite3.connect(banco)
        cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

        cur.execute(
            "SELECT name FROM sqlite_master "
            "WHERE type='table'"
        )

        tabelas = [x[0] for x in cur.fetchall()]

        conn.close()

        relatorio["bancos_sqlite"].append({
            "arquivo": str(banco),
            "tabelas": tabelas
        })

    except Exception as erro:

        relatorio["bancos_sqlite"].append({
            "arquivo": str(banco),
            "erro": str(erro)
        })

# ------------------------------------------------------------
# AMBIENTE
# ------------------------------------------------------------

for nome in sorted(os.environ):

    relatorio["variaveis_ambiente"].append(nome)

# ------------------------------------------------------------
# ESTATÃƒÂSTICAS
# ------------------------------------------------------------

relatorio["estatisticas"] = {

    "total_python":
        len(relatorio["arquivos_python"]),

    "total_bancos":
        len(relatorio["bancos_sqlite"]),

    "total_pastas":
        len(relatorio["pastas"])
}

# ------------------------------------------------------------
# RELATÃƒâ€œRIO
# ------------------------------------------------------------

saida = ROOT / "IOTEC_CORE_AUDIT_REPORT.json"

with open(saida, "w", encoding="utf-8") as f:
    json.dump(relatorio, f, indent=4, ensure_ascii=False)

print("=" * 60)
print("IOTEC INDUSTRIAL CORE AUDITOR")
print("=" * 60)
print()

print("Python........:", relatorio["estatisticas"]["total_python"])
print("Bancos........:", relatorio["estatisticas"]["total_bancos"])
print("Pastas........:", relatorio["estatisticas"]["total_pastas"])

print()
print("RelatÃƒÂ³rio salvo em:")
print(saida)

print()
print("STATUS: AUDITORIA CONCLUÃƒÂDA")

