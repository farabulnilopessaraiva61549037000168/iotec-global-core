
import sqlite3
from datetime import datetime

print("======================================================================")
print("IOTEC COMMERCIAL AUTOPILOT - BASE REAL (IOTEC.DB)")
print("======================================================================")
print(f"Data : {datetime.now().strftime('%d/%m/%Y')}")
print(f"Hora : {datetime.now().strftime('%H:%M:%S')}")
print("======================================================================")
print("CLIENTES EM PROSPECÇÃO REAL")
print("======================================================================")

conn = sqlite3.connect("iotec.db")
cur = conn.cursor()
try:
    cur.execute("SELECT id, protocol, company, status, priority FROM leads")
    rows = cur.fetchall()
    for r in rows:
        empresa = str(r[2]).replace("{'company_name': '", "").replace("'", "").strip()
        print(f"Cliente...... REAL-{r[0]:06d}")
        print(f"Protocolo.... {r[1]}")
        print(f"Empresa...... {empresa}")
        print(f"Status....... {r[3]}")
        print(f"Prioridade... {r[4]}")
        print("-" * 60)
except Exception as e:
    print(f"Erro ao carregar leads: {e}")
finally:
    conn.close()

print("======================================================================")
