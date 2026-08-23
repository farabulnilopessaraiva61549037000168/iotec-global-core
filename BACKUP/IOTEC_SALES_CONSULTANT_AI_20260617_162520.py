import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# IOTEC_SALES_CONSULTANT_AI.py
#
# CONSULTORA COMERCIAL VIRTUAL IOTEC
#
# OBJETIVO:
#
# - Receber visitantes
# - Entender necessidade
# - Identificar produto
# - Calcular oportunidade
# - Gerar lead
# - Gerar score
# - Encaminhar para pipeline
# - Registrar histÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rico
#
# VERSÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O 1.0

import sqlite3
from datetime import datetime

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

conn = sqlite3.connect(DB)
cur = conn.cursor()

# ==================================================
# TABELAS
# ==================================================

cur.execute("""

CREATE TABLE IF NOT EXISTS sales_consultant_sessions(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    created_at TEXT,

    company TEXT,

    contact_name TEXT,

    email TEXT,

    phone TEXT,

    sector TEXT,

    employees INTEGER,

    problem TEXT,

    recommendation TEXT,

    estimated_value REAL,

    lead_score INTEGER,

    status TEXT

)

""")

conn.commit()

# ==================================================
# CATALOGO
# ==================================================

CATALOGO = {

    "crm":
    {
        "produto":"PIPELINE COMERCIAL",
        "valor":2500
    },

    "vendas":
    {
        "produto":"PIPELINE COMERCIAL",
        "valor":2500
    },

    "dashboard":
    {
        "produto":"PAINEL EXECUTIVO",
        "valor":3500
    },

    "dados":
    {
        "produto":"ORGANIZACAO DE DADOS",
        "valor":3000
    },

    "automacao":
    {
        "produto":"AUTOMACAO EMPRESARIAL",
        "valor":5000
    },

    "industria":
    {
        "produto":"AUTOMACAO INDUSTRIAL",
        "valor":10000
    }

}

# ==================================================
# CONSULTORA
# ==================================================

print("")
print("===================================================")
print("IOTEC SALES CONSULTANT AI")
print("===================================================")
print("")

empresa = input("EMPRESA: ")
contato = input("CONTATO: ")
email = input("EMAIL: ")
telefone = input("TELEFONE: ")
setor = input("SETOR: ")

try:
    funcionarios = int(
        input("FUNCIONARIOS: ")
    )
except:
    funcionarios = 0

problema = input(
    "QUAL O PRINCIPAL PROBLEMA DA EMPRESA? "
)

texto = problema.lower()

produto = "DIAGNOSTICO EMPRESARIAL"
valor = 500
score = 1

for chave in CATALOGO:
    pass

    if chave in texto:
        pass

        produto = CATALOGO[chave]["produto"]

        valor = CATALOGO[chave]["valor"]

        score += 5

if funcionarios > 20:
    score += 2

if funcionarios > 100:
    score += 3

if funcionarios > 500:
    score += 5

cur.execute("""

INSERT INTO sales_consultant_sessions(

    created_at,

    company,

    contact_name,

    email,

    phone,

    sector,

    employees,

    problem,

    recommendation,

    estimated_value,

    lead_score,

    status

)

VALUES(

?,?,?,?,?,?,?,?,?,?,?,?

)

""",(

datetime.now().strftime(
"%d/%m/%Y %H:%M:%S"
),

empresa,
contato,
email,
telefone,
setor,
funcionarios,
problema,
produto,
valor,
score,
"NOVO_LEAD"

))

conn.commit()
conn.close()

print("")
print("===================================================")
print("ANALISE IOTEC")
print("===================================================")
print("")
print("EMPRESA:", empresa)
print("SETOR:", setor)
print("")
print("SOLUCAO RECOMENDADA:")
print(produto)
print("")
print("VALOR ESTIMADO:")
print(f"R$ {valor:,.2f}")
print("")
print("LEAD SCORE:")
print(score)
print("")
print("STATUS:")
print("ENCAMINHAR PARA PIPELINE")
print("")


