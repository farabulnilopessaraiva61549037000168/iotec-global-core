# ==========================================================
# 051_MISSION_DISPATCH_ENGINE.py
# IOTEC MISSION DISPATCH ENGINE
# ==========================================================

import sqlite3
from datetime import datetime

DB = "iotec_kernel.db"

db = sqlite3.connect(DB, timeout=30)
cursor = db.cursor()

print("=" * 70)
print("IOTEC MISSION DISPATCH ENGINE")
print("=" * 70)
print()

# ==========================================================
# TABELA DE MISSÃƒâ€¢ES
# ==========================================================

cursor.execute("""

CREATE TABLE IF NOT EXISTS missions(

id INTEGER PRIMARY KEY AUTOINCREMENT,

origem TEXT,

destino TEXT,

operacao TEXT,

prioridade TEXT,

status TEXT,

agente TEXT,

inicio TEXT,

fim TEXT,

resultado TEXT

)

""")

db.commit()

# ==========================================================
# CARREGA PROTOCOLOS
# ==========================================================

cursor.execute("""

SELECT

origem,
destino,
operacao,
prioridade

FROM ecosystem_protocol

ORDER BY

CASE prioridade

WHEN 'ALTA' THEN 1
WHEN 'MÃƒâ€°DIA' THEN 2
ELSE 3

END

""")

protocolos = cursor.fetchall()

despachadas = 0

print("ANALISANDO PROTOCOLOS")
print()

for origem, destino, operacao, prioridade in protocolos:

    # procura agente livre no ecossistema de origem

    cursor.execute("""

    SELECT

    codigo,
    nome

    FROM workforce

    WHERE ecossistema=?
    AND status='LIVRE'

    ORDER BY nivel DESC

    LIMIT 1

    """,(origem,))

    agente = cursor.fetchone()

    if agente is None:

        print(f"[SEM AGENTE] {origem}")
        continue

    codigo, nome = agente

    # reserva agente

    cursor.execute("""

    UPDATE workforce

    SET

    status='EM_EXECUÃƒâ€¡ÃƒÆ'O',

    missoes=missoes+1

    WHERE codigo=?

    """,(codigo,))

    # cria missÃƒÂ£o

    cursor.execute("""

    INSERT INTO missions(

    origem,

    destino,

    operacao,

    prioridade,

    status,

    agente,

    inicio

    )

    VALUES(?,?,?,?,?,?,?)

    """,(

    origem,

    destino,

    operacao,

    prioridade,

    "EM EXECUÃƒâ€¡ÃƒÆ'O",

    codigo,

    datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    ))

    despachadas += 1

    print(f"[OK] {codigo}")
    print("Agente :",nome)
    print("MissÃƒÂ£o :",operacao)
    print("Destino:",destino)
    print("-"*60)

db.commit()

print()
print("="*70)
print("INDICADORES")
print("="*70)
print()

print("MissÃƒÂµes despachadas :",despachadas)

cursor.execute("""

SELECT COUNT(*)

FROM workforce

WHERE status='LIVRE'

""")

print("Agentes livres..... :",cursor.fetchone()[0])

cursor.execute("""

SELECT COUNT(*)

FROM workforce

WHERE status='EM_EXECUÃƒâ€¡ÃƒÆ'O'

""")

print("Em execuÃƒÂ§ÃƒÂ£o........ :",cursor.fetchone()[0])

cursor.execute("""

SELECT COUNT(*)

FROM missions

""")

print("MissÃƒÂµes registradas :",cursor.fetchone()[0])

print()

print("="*70)
print("MISSÃƒÆ'O")
print("="*70)
print()

print("A Torre de Controle")
print("despachou automaticamente")
print("as primeiras missÃƒÂµes.")

print()

print("PrÃƒÂ³xima etapa:")

print()

print("Criar o 052_TASK_EXECUTION_ENGINE")
print("para executar as missÃƒÂµes")
print("e devolver o resultado.")
print()

db.close()


