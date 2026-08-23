import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC DATABASE CORE
# ============================================================

import sqlite3

# ============================================================
# CONEXÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ============================================================

connection = sqlite3.connect(
    "iotec_operational.db"
)

cursor = connection.cursor()

# ============================================================
# TABELA DE CLIENTES
# ============================================================

cursor.execute("""

CREATE TABLE IF NOT EXISTS clients (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    client_id TEXT,

    company_name TEXT,

    contact_name TEXT,

    email TEXT,

    whatsapp TEXT,

    country TEXT,

    status TEXT,

    registered_at TEXT
)

""")

# ============================================================
# TABELA DE SOLICITAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™ES
# ============================================================

cursor.execute("""

CREATE TABLE IF NOT EXISTS requests (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    request_id TEXT,

    client_id TEXT,

    request_type TEXT,

    description TEXT,

    complexity TEXT,

    pipeline_state TEXT,

    production_status TEXT,

    estimated_price REAL,

    estimated_delivery_days INTEGER,

    created_at TEXT
)

""")

# ============================================================
# TABELA DE PAGAMENTOS
# ============================================================

cursor.execute("""

CREATE TABLE IF NOT EXISTS payments (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    payment_id TEXT,

    request_id TEXT,

    amount REAL,

    gateway TEXT,

    status TEXT,

    paid_at TEXT
)

""")

# ============================================================
# TABELA DE LOGS
# ============================================================

cursor.execute("""

CREATE TABLE IF NOT EXISTS logs (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    log_id TEXT,

    event_type TEXT,

    message TEXT,

    timestamp TEXT
)

""")

# ============================================================
# SALVAR ALTERAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™ES
# ============================================================

connection.commit()

print("=" * 60)
print("IOTEC DATABASE CORE")
print("=" * 60)

print("\n[+] Banco de dados criado")
print("[+] Estrutura operacional criada")
print("[+] Tabelas inicializadas")
print("[+] PersistÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia habilitada")

connection.close()

# ============================================================
# FIM
# ============================================================



