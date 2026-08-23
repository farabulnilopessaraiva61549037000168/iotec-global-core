import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC DATABASE FIX ENGINE

Corrige automaticamente a estrutura do banco.

======================================================================
"""

import sqlite3
from datetime import datetime

DB = "iotec.db"


def coluna_existe(cursor, tabela, coluna):

    cursor.execute(f"PRAGMA table_info({tabela})")

    colunas = [c[1] for c in cursor.fetchall()]

    return coluna in colunas


def adicionar(cursor, tabela, coluna, definicao):

    if not coluna_existe(cursor, tabela, coluna):

        cursor.execute(

            f"ALTER TABLE {tabela} ADD COLUMN {coluna} {definicao}"

        )

        print(f"Ã¢Å"â€œ {tabela}.{coluna}")

    else:

        print(f"OK {tabela}.{coluna}")


def main():

    conn = sqlite3.connect(DB, timeout=30)

    cursor = conn.cursor()

    print()
    print("="*70)
    print("IOTEC DATABASE FIX ENGINE")
    print("="*70)
    print(datetime.now())
    print("="*70)
    print()

    # --------------------------------------------------------

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS leads(

        id INTEGER PRIMARY KEY AUTOINCREMENT

    )

    """)

    adicionar(cursor,"leads","company","TEXT")
    adicionar(cursor,"leads","contact_name","TEXT")
    adicionar(cursor,"leads","channel","TEXT")
    adicionar(cursor,"leads","campaign","TEXT")
    adicionar(cursor,"leads","source_event","TEXT")
    adicionar(cursor,"leads","status","TEXT")
    adicionar(cursor,"leads","score","INTEGER")
    adicionar(cursor,"leads","priority","TEXT")
    adicionar(cursor,"leads","assigned_to","TEXT")
    adicionar(cursor,"leads","created_at","TEXT")

    conn.commit()

    print()
    print("="*70)
    print("BANCO ATUALIZADO COM SUCESSO")
    print("="*70)

    conn.close()


if __name__ == "__main__":

    main()



