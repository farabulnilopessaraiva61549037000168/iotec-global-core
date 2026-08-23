import json
import os
from datetime import datetime
import uuid

MISSIONS_FILE = "IOTEC_MISSIONS.json"
EVENTS_FILE = "IOTEC_EVENTS.json"

# ==========================================================
# CARREGAR MISSÃƒâ€¢ES
# ==========================================================

if not os.path.exists(MISSIONS_FILE):

    print("Arquivo de missÃƒÂµes inexistente.")
    raise SystemExit()

with open(
    MISSIONS_FILE,
    "r",
    encoding="utf-8"
) as f:

    missions = json.load(f)

events = []

# ==========================================================
# GERAR EVENTOS
# ==========================================================

for mission in missions:

    if mission.get("status") != "CONCLUÃƒÂDA":
        continue

    objective = mission.get("objective","").lower()

    event_type = "MISSION_COMPLETED"

    if "website" in objective:
        event_type = "WEBSITE_DISCOVERED"

    elif "e-mail" in objective:
        event_type = "EMAIL_DISCOVERED"

    elif "telefone" in objective:
        event_type = "PHONE_DISCOVERED"

    elif "linkedin" in objective:
        event_type = "LINKEDIN_DISCOVERED"

    elif "empresa" in objective:
        event_type = "NEW_COMPANIES"

    elif "tendÃƒÂªncia" in objective:
        event_type = "NEW_KNOWLEDGE"

    events.append({

        "event_id": str(uuid.uuid4())[:8],

        "mission_id": mission["mission_id"],

        "event_type": event_type,

        "center": mission["center"],

        "agent": mission["agent"],

        "objective": mission["objective"],

        "result": mission.get("result",""),

        "status": "NOVO",

        "timestamp": datetime.now().isoformat()

    })

# ==========================================================
# SALVAR
# ==========================================================

with open(
    EVENTS_FILE,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        events,
        f,
        indent=4,
        ensure_ascii=False
    )

# ==========================================================
# RELATÃƒâ€œRIO
# ==========================================================

print("="*90)
print("IOTEC EVENT BUS ENGINE")
print("="*90)
print()

print("EVENTOS GERADOS :",len(events))
print()

print("="*90)
print("FILA DE EVENTOS")
print("="*90)
print()

for e in events:

    print(e["event_id"])

    print("Evento....:",e["event_type"])

    print("Centro....:",e["center"])

    print("Agente....:",e["agent"])

    print("Objetivo..:",e["objective"])

    print("Status....:",e["status"])

    print()

print("="*90)
print("DESTINOS")
print("="*90)
print()

print("Ã¢Å"â€œ CRM")
print("Ã¢Å"â€œ Corporate Memory")
print("Ã¢Å"â€œ Commercial Center")
print("Ã¢Å"â€œ Control Tower")
print("Ã¢Å"â€œ Executive Center")
print("Ã¢Å"â€œ Dashboard")
print()

print("="*90)
print("MISSÃƒÆ'O")
print("="*90)
print()

print("Transformar")
print("resultados")
print("em")
print("eventos")
print("compartilhados")
print("por")
print("toda")
print("a plataforma.")

print()

print("="*90)
print("CHEFE DE GABINETE")
print("="*90)
print()

print()

print("Boa noite, Presidente.")
print()

print("Os agentes")
print("nÃƒÂ£o trabalham")
print("mais")
print("isoladamente.")

print()

print("Cada missÃƒÂ£o")
print("concluÃƒÂ­da")
print("gera")
print("eventos")

print("que podem")
print("ser utilizados")

print("por qualquer")

print("Centro")

print("da IOTEC.")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("Eventos :",len(events))

print("Data :",datetime.now())

print()

print("EVENT BUS OPERACIONAL.")

