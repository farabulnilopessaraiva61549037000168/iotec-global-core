"""
===========================================================
IOTEC KNOWLEDGE INDEXER
VersÃ£o: 1.0
Objetivo:
Mapear toda a estrutura da IOTEC e criar um catÃ¡logo
de conhecimento para os demais agentes.
===========================================================
"""

from pathlib import Path
import hashlib
import sqlite3
from datetime import datetime

# ==========================================================
# CONFIGURAÃ‡ÃƒO
# ==========================================================

ROOT = Path.home() / "Documents" / "OMEGA_BASE"

DB = ROOT / "iotec_knowledge.db"

EXTENSOES = {
    ".py",
    ".txt",
    ".md",
    ".pdf",
    ".docx",
    ".xlsx",
    ".pptx",
    ".json",
    ".csv",
    ".yaml",
    ".yml"
}

# ==========================================================
# BANCO
# ==========================================================

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

cur.execute("""
CREATE TABLE IF NOT EXISTS arquivos (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    caminho TEXT UNIQUE,

    nome TEXT,

    extensao TEXT,

    tamanho INTEGER,

    hash TEXT,

    modificado TEXT,

    indexado TEXT

)
""")

conn.commit()

# ==========================================================
# HASH
# ==========================================================

def gerar_hash(arquivo):

    sha = hashlib.sha256()

    with open(arquivo, "rb") as f:

        while True:

            bloco = f.read(8192)

            if not bloco:
                break

            sha.update(bloco)

    return sha.hexdigest()

# ==========================================================
# INDEXAÃ‡ÃƒO
# ==========================================================

total = 0

for arquivo in ROOT.rglob("*"):

    if not arquivo.is_file():
        continue

    if arquivo.suffix.lower() not in EXTENSOES:
        continue

    try:

        tamanho = arquivo.stat().st_size

        modificado = datetime.fromtimestamp(
            arquivo.stat().st_mtime
        ).isoformat()

        h = gerar_hash(arquivo)

        cur.execute("""

        INSERT OR REPLACE INTO arquivos(

            caminho,
            nome,
            extensao,
            tamanho,
            hash,
            modificado,
            indexado

        )

        VALUES(?,?,?,?,?,?,?)

        """,

        (

            str(arquivo),
            arquivo.name,
            arquivo.suffix,
            tamanho,
            h,
            modificado,
            datetime.now().isoformat()

        ))

        total += 1

    except Exception as erro:

        print("ERRO:", arquivo)
        print(erro)

conn.commit()

print("=" * 60)
print("IOTEC KNOWLEDGE INDEXER")
print("=" * 60)
print(f"Arquivos indexados : {total}")
print(f"Banco criado em    : {DB}")

conn.close()

