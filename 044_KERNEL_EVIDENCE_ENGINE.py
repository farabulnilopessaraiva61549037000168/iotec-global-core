# ==========================================================
# 044_KERNEL_EVIDENCE_ENGINE.py
# IOTEC KERNEL EVIDENCE ENGINE
# ==========================================================

import sqlite3
import os
from datetime import datetime

DB = "iotec_kernel.db"

db = sqlite3.connect(DB, timeout=30)
cursor = db.cursor()

# ==========================================================
# TABELA DE EVIDÃƒÅ NCIAS
# ==========================================================

cursor.execute("""

CREATE TABLE IF NOT EXISTS executive_evidence(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    pergunta_id INTEGER,

    pergunta TEXT,

    arquivo TEXT,

    evidencia TEXT,

    coletado_em TEXT

)

""")

db.commit()

# ==========================================================

cursor.execute("""

SELECT id,pergunta

FROM executive_questions

ORDER BY id

""")

perguntas = cursor.fetchall()

print("="*70)
print("IOTEC KERNEL EVIDENCE ENGINE")
print("="*70)
print()

print("Perguntas encontradas :",len(perguntas))
print()

# ==========================================================

arquivos=[]

for raiz,pastas,files in os.walk("."):

    for f in files:

        if f.endswith(".py"):

            arquivos.append(os.path.join(raiz,f))

print("Arquivos Python :",len(arquivos))
print()

# ==========================================================

total=0

for pergunta_id,pergunta in perguntas:

    palavras=[]

    for p in pergunta.lower().replace("?","").split():

        if len(p)>=4:

            palavras.append(p)

    encontrados=0

    for arquivo in arquivos:

        try:

            texto=open(
                arquivo,
                encoding="utf8",
                errors="ignore"
            ).read().lower()

        except:

            continue

        score=0

        for palavra in palavras:

            if palavra in texto:

                score+=1

        if score>0:

            cursor.execute("""

            INSERT INTO executive_evidence(

                pergunta_id,

                pergunta,

                arquivo,

                evidencia,

                coletado_em

            )

            VALUES(?,?,?,?,?)

            """,(

                pergunta_id,

                pergunta,

                arquivo,

                f"{score} palavra(s) relacionada(s)",

                datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            ))

            encontrados+=1
            total+=1

    print(f"[OK] {pergunta}")
    print(f"     EvidÃƒÂªncias encontradas : {encontrados}")
    print()

db.commit()

print("="*70)
print("MISSÃƒÆ'O")
print("="*70)
print()

print("Total de evidÃƒÂªncias :",total)
print()

print("As evidÃƒÂªncias foram registradas no banco.")
print()

print("PrÃƒÂ³xima missÃƒÂ£o:")

print("Interpretar essas evidÃƒÂªncias")
print("e produzir um parecer executivo.")

db.close()


