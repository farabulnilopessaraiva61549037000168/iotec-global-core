# ==========================================================
# 059_ARCHITECTURE_GOVERNANCE_ENGINE.py
# PARTE 1
# IOTEC ARCHITECTURE GOVERNANCE
# ==========================================================

import os
import sqlite3
from datetime import datetime

ROOT = r"C:\IOTEC"
DB = "iotec_kernel.db"

IGNORAR = {

    "venv",
    "node_modules",
    "__pycache__",
    "BACKUP",
    "ENCODING_BACKUP"

}

conn = sqlite3.connect(DB, timeout=30)
cursor = conn.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS architecture_registry(

id INTEGER PRIMARY KEY AUTOINCREMENT,

arquivo TEXT,

caminho TEXT,

classe TEXT,

ecossistema TEXT,

responsavel TEXT,

status TEXT,

criticidade INTEGER,

flask INTEGER,

fastapi INTEGER,

app_run INTEGER,

ultima_analise TEXT

)

""")

conn.commit()

cursor.execute("DELETE FROM architecture_registry")
conn.commit()

print("="*70)
print("IOTEC ARCHITECTURE GOVERNANCE")
print("="*70)
print()

arquivos = 0

for pasta,dirs,files in os.walk(ROOT):

    dirs[:] = [d for d in dirs if d not in IGNORAR]

    for nome in files:

        if not nome.endswith(".py"):
            continue

        caminho = os.path.join(pasta,nome)

        arquivos += 1

        flask = 0
        fastapi = 0
        apprun = 0

        try:

            with open(caminho,
                      encoding="utf8",
                      errors="ignore") as f:

                texto = f.read().lower()

        except:

            continue

        if "flask" in texto:
            flask = 1

        if "fastapi" in texto:
            fastapi = 1

        if "app.run(" in texto:
            apprun = 1

        cursor.execute("""

        INSERT INTO architecture_registry(

        arquivo,
        caminho,
        classe,
        ecossistema,
        responsavel,
        status,
        criticidade,
        flask,
        fastapi,
        app_run,
        ultima_analise

        )

        VALUES(?,?,?,?,?,?,?,?,?,?,?)

        """,(

        nome,
        caminho,
        "NÃƒÆ'O_CLASSIFICADO",
        "",
        "",
        "PENDENTE",
        0,
        flask,
        fastapi,
        apprun,
        str(datetime.now())

        ))

conn.commit()

print("Arquivos registrados :",arquivos)
print()

print("="*70)
print("SERVIDORES ENCONTRADOS")
print("="*70)
print()

cursor.execute("""

SELECT

arquivo,
caminho

FROM architecture_registry

WHERE app_run=1

ORDER BY arquivo

""")

dados = cursor.fetchall()

for arq,caminho in dados:

    print(arq)
    print(caminho)
    print("-"*60)

print()

print("="*70)
print("MISSÃƒÆ'O")
print("="*70)
print()

print("Todos os arquivos")
print("foram cadastrados")
print("na GovernanÃƒÂ§a Oficial.")

print()

print("PrÃƒÂ³xima etapa:")
print("classificar automaticamente")
print("cada arquivo.")

conn.close()


