import json
import os
from datetime import datetime

MISSION_FILE = "IOTEC_MISSIONS.json"
OUTPUT_FILE = "IOTEC_MISSIONS.json"

# ==========================================================
# AGENTES DISPONÃƒÂVEIS
# ==========================================================

AGENTS = {

    "CONTACT DISCOVERY ENGINE": "COMMERCIAL CENTER",

    "COMPANY DISCOVERY ENGINE": "MARKET CENTER",

    "MARKET SCIENTIST": "SCIENTIFIC CENTER"

}

# ==========================================================

if not os.path.exists(MISSION_FILE):

    print("Fila de missÃƒÂµes inexistente.")
    raise SystemExit()

with open(MISSION_FILE, "r", encoding="utf-8") as f:

    missions = json.load(f)

executadas = 0

for mission in missions:

    if mission["status"] != "PENDENTE":
        continue

    mission["status"] = "EM EXECUÃƒâ€¡ÃƒÆ'O"

    mission["started_at"] = datetime.now().isoformat()

    mission["progress"] = 25

    agent = mission["agent"]

    if agent in AGENTS:

        mission["assigned_center"] = AGENTS[agent]

        mission["last_message"] = "MissÃƒÂ£o recebida pelo agente."

    else:

        mission["assigned_center"] = "NÃƒÆ'O DEFINIDO"

        mission["last_message"] = "Agente nÃƒÂ£o encontrado."

    executadas += 1

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        missions,
        f,
        indent=4,
        ensure_ascii=False
    )

# ==========================================================

print("="*90)
print("IOTEC AGENT EXECUTION ENGINE")
print("="*90)
print()

print("MISSÃƒâ€¢ES ENVIADAS AOS AGENTES")
print("-"*90)
print()

for mission in missions:

    print(mission["mission_id"])

    print("Centro.....:", mission.get("assigned_center",""))

    print("Agente.....:", mission["agent"])

    print("Objetivo...:", mission["objective"])

    print("Status.....:", mission["status"])

    print("Progresso..:", str(mission["progress"])+"%")

    print()

print("="*90)
print("RESUMO")
print("="*90)
print()

print("MissÃƒÂµes Ativadas :", executadas)

print()

print("="*90)
print("CHEFE DE GABINETE")
print("="*90)
print()

print()

print("Boa noite, Presidente.")
print()

print("As missÃƒÂµes")
print("foram distribuÃƒÂ­das")
print("aos agentes")
print("especializados.")

print()

print("Cada agente")
print("passa a executar")
print("sua fila")
print("de trabalho.")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("Data :", datetime.now())

print()

print("AGENT EXECUTION ENGINE OPERACIONAL.")

