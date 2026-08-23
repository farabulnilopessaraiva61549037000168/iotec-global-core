import json
import os
from datetime import datetime

EVENT_FILE = "IOTEC_EVENTS.json"

# ==========================================================
# CARREGAR EVENTOS
# ==========================================================

if not os.path.exists(EVENT_FILE):

    print("Arquivo de eventos nÃƒÂ£o encontrado.")
    raise SystemExit()

with open(EVENT_FILE, "r", encoding="utf-8") as f:

    events = json.load(f)

processed = 0

# ==========================================================
# ROTEAMENTO
# ==========================================================

for event in events:

    if event["status"] != "NOVO":
        continue

    event_type = event["event_type"]

    destinations = []

    if event_type == "WEBSITE_DISCOVERED":

        destinations = [
            "CRM",
            "CONTROL TOWER",
            "EXECUTIVE CENTER"
        ]

    elif event_type == "EMAIL_DISCOVERED":

        destinations = [
            "CRM",
            "COMMERCIAL CENTER"
        ]

    elif event_type == "PHONE_DISCOVERED":

        destinations = [
            "CRM",
            "COMMERCIAL CENTER"
        ]

    elif event_type == "LINKEDIN_DISCOVERED":

        destinations = [
            "CRM",
            "COMMERCIAL CENTER"
        ]

    elif event_type == "NEW_COMPANIES":

        destinations = [
            "COMPANY DATABASE",
            "OPPORTUNITY ENGINE",
            "CRM",
            "COMMERCIAL CENTER"
        ]

    elif event_type == "NEW_KNOWLEDGE":

        destinations = [
            "CORPORATE MEMORY",
            "SCIENTIFIC CENTER",
            "EXECUTIVE CENTER"
        ]

    else:

        destinations = [
            "CONTROL TOWER"
        ]

    event["destinations"] = destinations

    event["status"] = "PROCESSADO"

    event["processed_at"] = datetime.now().isoformat()

    processed += 1

# ==========================================================
# SALVAR
# ==========================================================

with open(EVENT_FILE, "w", encoding="utf-8") as f:

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
print("IOTEC KERNEL EVENT DISPATCHER")
print("="*90)
print()

print("EVENTOS PROCESSADOS :", processed)
print()

print("="*90)
print("ROTEAMENTO")
print("="*90)
print()

for event in events:

    print(event["event_type"])

    print("Destino :", ", ".join(event["destinations"]))

    print("Status..:", event["status"])

    print()

print("="*90)
print("MISSÃƒÆ'O")
print("="*90)
print()

print("Distribuir")
print("automaticamente")
print("cada evento")
print("para")
print("os Centros")
print("responsÃƒÂ¡veis.")

print()

print("="*90)
print("CHEFE DE GABINETE")
print("="*90)
print()

print()

print("Boa noite, Presidente.")

print()

print("O Kernel")

print("passa agora")

print("a distribuir")

print("os resultados")

print("entre")

print("todos os")

print("Centros")

print("da IOTEC.")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("Eventos Processados :", processed)

print("Data :", datetime.now())

print()

print("KERNEL EVENT DISPATCHER OPERACIONAL.")

