Clear-Host

Write-Host ""
Write-Host "========================================"
Write-Host "IOTEC DATABASE MIGRATION"
Write-Host "========================================"
Write-Host ""

$db = "C:\IOTEC\IOTEC_OPPORTUNITY.db"

if (!(Test-Path $db))
{
    Write-Host "Banco não encontrado."
    exit
}

python - << 'PY'

import sqlite3

db=r"C:\IOTEC\IOTEC_OPPORTUNITY.db"

conn=sqlite3.connect(db)

cur=conn.cursor()

cur.execute("PRAGMA table_info(opportunities)")

cols=[x[1] for x in cur.fetchall()]

novas_colunas=[

("updated_at","TEXT"),
("country","TEXT"),
("city","TEXT"),
("contact","TEXT"),
("email","TEXT"),
("phone","TEXT"),
("website","TEXT"),
("campaign","TEXT"),
("lead_source","TEXT"),
("budget","REAL"),
("market_score","INTEGER"),
("priority","TEXT"),
("urgency","TEXT"),
("decision_maker","TEXT"),
("assigned_operator","TEXT"),
("recommended_action","TEXT"),
("notes","TEXT")

]

for nome,tipo in novas_colunas:

    if nome not in cols:

        print(f"Criando coluna {nome}")

        cur.execute(f"ALTER TABLE opportunities ADD COLUMN {nome} {tipo}")

conn.commit()

print()

print("Migração concluída.")

conn.close()

PY

Write-Host ""
Write-Host "========================================"
Write-Host "BANCO ATUALIZADO"
Write-Host "========================================"