# ==========================================================
# 058_STRATEGIC_CODE_FORENSICS_ENGINE.py
# ==========================================================

import os
import sqlite3

ROOT = r"C:\IOTEC"
DB = "iotec_kernel.db"

ALVOS = [

"IOTEC_BL_PORTAL_PAGAMENTOS_AUTOMATICO.py",
"iotec_nucleus.py",
"IOTEC_GLOBAL_OPERATIONAL_CORE.py",
"visible_core_router.py"

]

PALAVRAS = [

"paypal",
"payment",
"checkout",
"capture",
"webhook",
"requests",
"sqlite",
"cursor.execute",
"subprocess",
"os.system",
"webbrowser",
"flask",
"fastapi",
"route",
"post",
"mission",
"control",
"tower",
"dispatch",
"production",
"delivery"

]

conn=sqlite3.connect(DB, timeout=30)
cur=conn.cursor()

cur.execute("""

CREATE TABLE IF NOT EXISTS strategic_forensics(

arquivo TEXT,
linha INTEGER,
palavra TEXT,
conteudo TEXT

)

""")

cur.execute("DELETE FROM strategic_forensics")

conn.commit()

print("="*70)
print("IOTEC STRATEGIC CODE FORENSICS")
print("="*70)
print()

for pasta,dirs,files in os.walk(ROOT):

    for nome in files:

        if nome not in ALVOS:
            continue

        caminho=os.path.join(pasta,nome)

        print(nome)

        try:

            with open(caminho,
                      encoding="utf8",
                      errors="ignore") as f:

                linhas=f.readlines()

        except:

            continue

        encontrados=0

        for numero,linha in enumerate(linhas,1):

            baixo=linha.lower()

            for palavra in PALAVRAS:

                if palavra in baixo:

                    encontrados+=1

                    cur.execute("""

                    INSERT INTO strategic_forensics
                    VALUES(?,?,?,?)

                    """,(

                    nome,
                    numero,
                    palavra,
                    linha.strip()

                    ))

        print("EvidÃƒÂªncias :",encontrados)
        print("-"*60)

conn.commit()

print()

print("="*70)
print("RESUMO")
print("="*70)
print()

for palavra in PALAVRAS:

    cur.execute("""

    SELECT COUNT(*)

    FROM strategic_forensics

    WHERE palavra=?

    """,(palavra,))

    total=cur.fetchone()[0]

    if total:

        print(f"{palavra:<20}{total}")

print()

print("="*70)
print("TOP EVIDÃƒÅ NCIAS")
print("="*70)
print()

cur.execute("""

SELECT

arquivo,
linha,
palavra

FROM strategic_forensics

LIMIT 100

""")

for arq,linha,p in cur.fetchall():

    print(f"{arq:<45} L{linha:<5} {p}")

print()

print("="*70)
print("MISSÃƒÆ'O")
print("="*70)
print()

print("A PresidÃƒÂªncia agora")
print("estÃƒÂ¡ investigando")
print("os arquivos")
print("mais estratÃƒÂ©gicos")
print("da plataforma.")

conn.close()


