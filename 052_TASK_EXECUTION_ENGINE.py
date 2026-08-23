# ==========================================================
# 052_TASK_EXECUTION_ENGINE.py
# IOTEC TASK EXECUTION ENGINE
# ==========================================================

import sqlite3
from datetime import datetime

DB="iotec_kernel.db"

db=sqlite3.connect(DB, timeout=30)
cursor=db.cursor()

print("="*70)
print("IOTEC TASK EXECUTION ENGINE")
print("="*70)
print()

cursor.execute("""

SELECT

id,
agente,
origem,
destino,
operacao

FROM missions

WHERE status='EM EXECUÃƒâ€¡ÃƒÆ'O'

ORDER BY id

""")

missoes=cursor.fetchall()

print("MissÃƒÂµes em execuÃƒÂ§ÃƒÂ£o :",len(missoes))
print()

concluidas=0

for missao in missoes:

    mid,agente,origem,destino,operacao=missao

    print(f"[EXECUTANDO] {agente}")
    print("OperaÃƒÂ§ÃƒÂ£o :",operacao)

    # ------------------------------------------------------

    cursor.execute("""

    UPDATE missions

    SET

    status='CONCLUÃƒÂDA',

    fim=?,

    resultado=?

    WHERE id=?

    """,(

    datetime.now().strftime("%d/%m/%Y %H:%M:%S"),

    "EXECUÃƒâ€¡ÃƒÆ'O REGISTRADA",

    mid

    ))

    # ------------------------------------------------------

    cursor.execute("""

    UPDATE workforce

    SET

    status='LIVRE'

    WHERE codigo=?

    """,(agente,))

    concluidas+=1

    print("Status : CONCLUÃƒÂDA")
    print("-"*60)

db.commit()

print()

print("="*70)
print("INDICADORES")
print("="*70)
print()

print("MissÃƒÂµes concluÃƒÂ­das :",concluidas)

cursor.execute("""

SELECT COUNT(*)

FROM workforce

WHERE status='LIVRE'

""")

print("Agentes livres..... :",cursor.fetchone()[0])

cursor.execute("""

SELECT COUNT(*)

FROM workforce

WHERE status='EM EXECUÃƒâ€¡ÃƒÆ'O'

""")

print("Agentes ocupados... :",cursor.fetchone()[0])

cursor.execute("""

SELECT COUNT(*)

FROM missions

WHERE status='CONCLUÃƒÂDA'

""")

print("MissÃƒÂµes concluÃƒÂ­das. :",cursor.fetchone()[0])

print()

print("="*70)
print("MISSÃƒÆ'O")
print("="*70)
print()

print("Todos os agentes")
print("retornaram para")
print("o estado LIVRE.")

print()

print("A Torre pode")
print("despachar novas")
print("missÃƒÂµes.")

db.close()


