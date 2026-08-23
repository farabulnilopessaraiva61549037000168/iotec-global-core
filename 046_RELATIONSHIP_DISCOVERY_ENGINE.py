# ==========================================================
# 046_RELATIONSHIP_DISCOVERY_ENGINE.py
# IOTEC RELATIONSHIP DISCOVERY ENGINE
# ==========================================================

import os
import ast
import sqlite3
from collections import defaultdict

DB="iotec_kernel.db"

db=sqlite3.connect(DB, timeout=30)
cursor=db.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS module_relationships(

id INTEGER PRIMARY KEY AUTOINCREMENT,

arquivo TEXT,

tipo TEXT,

destino TEXT

)

""")

db.commit()

print("="*70)
print("IOTEC RELATIONSHIP DISCOVERY ENGINE")
print("="*70)
print()

arquivos=[]

for raiz,pastas,files in os.walk("."):

    for f in files:

        if f.endswith(".py"):

            arquivos.append(os.path.join(raiz,f))

print("Arquivos encontrados :",len(arquivos))
print()

imports=0
classes=0
funcoes=0

dependencias=defaultdict(set)

# ----------------------------------------------------------

for arquivo in arquivos:

    try:

        codigo=open(
            arquivo,
            encoding="utf8",
            errors="ignore"
        ).read()

        arvore=ast.parse(codigo)

    except:

        continue

    for no in ast.walk(arvore):

        if isinstance(no,ast.Import):

            for nome in no.names:

                cursor.execute("""

                INSERT INTO module_relationships(

                arquivo,

                tipo,

                destino

                )

                VALUES(?,?,?)

                """,(

                arquivo,

                "IMPORT",

                nome.name

                ))

                dependencias[arquivo].add(nome.name)

                imports+=1

        elif isinstance(no,ast.ImportFrom):

            modulo=no.module or ""

            cursor.execute("""

            INSERT INTO module_relationships(

            arquivo,

            tipo,

            destino

            )

            VALUES(?,?,?)

            """,(

            arquivo,

            "FROM",

            modulo

            ))

            dependencias[arquivo].add(modulo)

            imports+=1

        elif isinstance(no,ast.ClassDef):

            cursor.execute("""

            INSERT INTO module_relationships(

            arquivo,

            tipo,

            destino

            )

            VALUES(?,?,?)

            """,(

            arquivo,

            "CLASS",

            no.name

            ))

            classes+=1

        elif isinstance(no,ast.FunctionDef):

            cursor.execute("""

            INSERT INTO module_relationships(

            arquivo,

            tipo,

            destino

            )

            VALUES(?,?,?)

            """,(

            arquivo,

            "FUNCTION",

            no.name

            ))

            funcoes+=1

db.commit()

print("="*70)
print("ESTATÃƒÂSTICAS")
print("="*70)
print()

print("Imports encontrados :",imports)
print("Classes............ :",classes)
print("FunÃƒÂ§ÃƒÂµes............ :",funcoes)

print()

print("="*70)
print("MÃƒâ€œDULOS MAIS CONECTADOS")
print("="*70)
print()

ranking=[]

for modulo in dependencias:

    ranking.append((len(dependencias[modulo]),modulo))

ranking.sort(reverse=True)

for total,arquivo in ranking[:25]:

    print(f"{total:4}  {arquivo}")

print()

print("="*70)
print("MISSÃƒÆ'O")
print("="*70)
print()

print("O Kernel comeÃƒÂ§ou")
print("a descobrir como")
print("os mÃƒÂ³dulos conversam.")

print()

print("PrÃƒÂ³xima etapa:")

print("Descobrir os ÃƒÂ³rgÃƒÂ£os")
print("da IOTEC.")

db.close()


