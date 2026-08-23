# ==========================================================
# 049_CONTROL_TOWER_ENGINE.py
# IOTEC CONTROL TOWER
# ==========================================================

import sqlite3
from datetime import datetime

DB="iotec_kernel.db"

db=sqlite3.connect(DB, timeout=30)
cursor=db.cursor()

# ==========================================================
# FILA CENTRAL DE EVENTOS
# ==========================================================

cursor.execute("""

CREATE TABLE IF NOT EXISTS control_tower(

id INTEGER PRIMARY KEY AUTOINCREMENT,

protocolo_id INTEGER,

origem TEXT,

destino TEXT,

operacao TEXT,

prioridade TEXT,

status TEXT,

agente TEXT,

inicio TEXT,

fim TEXT,

observacao TEXT

)

""")

db.commit()

# ==========================================================

print("="*70)
print("IOTEC CONTROL TOWER")
print("="*70)
print()

cursor.execute("""

SELECT

id,

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

protocolos=cursor.fetchall()

print("Protocolos encontrados :",len(protocolos))
print()

contador=0

for protocolo in protocolos:

    pid,origem,destino,operacao,prioridade=protocolo

    agente=f"BORDER-{pid:03}"

    cursor.execute("""

    INSERT INTO control_tower(

    protocolo_id,

    origem,

    destino,

    operacao,

    prioridade,

    status,

    agente,

    inicio,

    observacao

    )

    VALUES(?,?,?,?,?,?,?,?,?)

    """,(

    pid,

    origem,

    destino,

    operacao,

    prioridade,

    "AGUARDANDO",

    agente,

    datetime.now().strftime("%d/%m/%Y %H:%M:%S"),

    "Registrado pela Torre"

    ))

    contador+=1

db.commit()

print("="*70)
print("FILA DA TORRE")
print("="*70)
print()

cursor.execute("""

SELECT

agente,

origem,

destino,

operacao,

status

FROM control_tower

ORDER BY id

""")

for agente,origem,destino,operacao,status in cursor.fetchall():

    print(f"{agente:<12} {origem:<15} -> {destino:<15}")

    print("OperaÃƒÂ§ÃƒÂ£o :",operacao)

    print("Status   :",status)

    print("-"*60)

print()

print("="*70)
print("INDICADORES")
print("="*70)
print()

print("Eventos registrados :",contador)

cursor.execute("""

SELECT COUNT(*)

FROM ecosystems

""")

print("Ecossistemas....... :",cursor.fetchone()[0])

cursor.execute("""

SELECT COUNT(*)

FROM ecosystem_protocol

""")

print("Protocolos......... :",cursor.fetchone()[0])

print()

print("="*70)
print("MISSÃƒÆ'O")
print("="*70)
print()

print("A Torre de Controle")
print("assumiu a coordenaÃƒÂ§ÃƒÂ£o")

print()

print("Nenhum ecossistema")
print("conversa diretamente")

print("Toda comunicaÃƒÂ§ÃƒÂ£o")

print("passa pela Torre.")

print()

print("PrÃƒÂ³xima etapa:")

print()

print("Criar os Border Agents")

print("que executarÃƒÂ£o")

print("as ordens da Torre.")

db.close()


