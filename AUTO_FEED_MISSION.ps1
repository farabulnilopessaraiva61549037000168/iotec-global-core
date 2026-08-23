Write-Host ""
Write-Host "====================================="
Write-Host "IOTEC AUTO FEED MISSION"
Write-Host "====================================="
Write-Host ""

$temp = @'
import sqlite3
import json
from datetime import datetime

DB = r"C:\IOTEC\IOTEC_EVENT_BUS.db"

conn = sqlite3.connect(DB)
cur = conn.cursor()

leads = [

    {
        "company":"Escola Alfa",
        "sector":"EDUCACAO"
    },

    {
        "company":"Clinica Vida",
        "sector":"SAUDE"
    },

    {
        "company":"Prefeitura Modelo",
        "sector":"GOVTECH"
    }

]

for lead in leads:

    cur.execute("""

    INSERT INTO events (

        timestamp,
        source,
        event_type,
        payload,
        processed

    )

    VALUES (

        ?,?,?,?,?

    )

    """,

    (

        str(datetime.now()),
        "AUTO_FEED",
        "LEAD",
        json.dumps(lead),
        0

    ))

conn.commit()

print("")
print("LEADS INSERIDOS:", len(leads))

conn.close()
'@

$temp | Out-File C:\IOTEC\TEMP_EVENT_FEED.py -Encoding utf8

python C:\IOTEC\TEMP_EVENT_FEED.py

Write-Host ""
Write-Host "EXECUTANDO AUTOPILOT..."
Write-Host ""

python C:\IOTEC\IOTEC_AUTOPILOT_ENGINE.py

Write-Host ""
Write-Host "STATUS DA MISSAO..."
Write-Host ""

python C:\IOTEC\IOTEC_MISSION_STATUS.py

Remove-Item `
C:\IOTEC\TEMP_EVENT_FEED.py `
-Force `
-ErrorAction SilentlyContinue

Write-Host ""
Write-Host "FIM"