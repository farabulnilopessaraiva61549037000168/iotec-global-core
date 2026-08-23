import sqlite3

DB = "iotec_kernel.db"

conn = sqlite3.connect(DB, timeout=30)
cursor = conn.cursor()

print("="*60)
print("IOTEC DATABASE MIGRATION")
print("="*60)

cursor.execute("PRAGMA table_info(clientes)")
colunas = [c[1] for c in cursor.fetchall()]

novas_colunas = {

    "necessidade":"TEXT",

    "origem":"TEXT"

}

for coluna,tipo in novas_colunas.items():

    if coluna not in colunas:

        print(f"Criando coluna: {coluna}")

        cursor.execute(

            f"ALTER TABLE clientes ADD COLUMN {coluna} {tipo}"

        )

    else:

        print(f"{coluna} jÃƒÂ¡ existe.")

conn.commit()

print()

print("MigraÃƒÂ§ÃƒÂ£o concluÃƒÂ­da.")

conn.close()

print("="*60)


