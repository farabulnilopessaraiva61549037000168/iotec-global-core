import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC REAL-TIME PROSPECTION ENGINE
# ============================================================

import json
import random
import time
from datetime import datetime

# ============================================================
# CONFIGURAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™ES
# ============================================================

SCAN_INTERVAL = 5

BASE_CONVERSION = 0.14

RECURRENCE_RATE = 0.38

SECTORS = {

    "educacao": [1000, 8000],

    "juridico": [3000, 25000],

    "corporativo": [5000, 50000],

    "automacao": [7000, 120000],

    "ia": [12000, 250000],

    "governo": [25000, 500000],

    "saude": [6000, 80000]

}

# ============================================================
# COMMAND TOWER
# ============================================================

tower = {

    "runtime": "ONLINE",

    "mode": "REAL_TIME_PROSPECTION",

    "started_at": str(datetime.now()),

    "leads": [],

    "revenue": 0,

    "recurring": 0,

    "clients": 0

}

# ============================================================
# LEAD GENERATOR
# ============================================================

def generate_lead():
    pass

    sector = random.choice(
        list(SECTORS.keys())
    )

    urgency = random.randint(1, 10)

    priority = random.randint(1, 10)

    financial = random.randint(1, 10)

    maturity = random.randint(1, 10)

    score = (
        urgency +
        priority +
        financial +
        maturity
    ) / 4

    conversion = (
        score / 10
    ) * BASE_CONVERSION

    conversion = min(conversion, 0.92)

    converted = (
        random.random() <= conversion
    )

    ticket = random.randint(
        SECTORS[sector][0],
        SECTORS[sector][1]
    )

    recurring = (
        random.random() <= RECURRENCE_RATE
    )

    lead = {

        "id": len(tower["leads"]) + 1,

        "timestamp": str(datetime.now()),

        "sector": sector,

        "urgency": urgency,

        "priority": priority,

        "financial_capacity": financial,

        "digital_maturity": maturity,

        "score": round(score, 2),

        "conversion_probability": round(conversion, 3),

        "converted": converted,

        "ticket": ticket,

        "recurring": recurring

    }

    return lead

# ============================================================
# PROCESSAMENTO
# ============================================================

def process_lead(lead):
    pass

    tower["leads"].append(lead)

    if lead["converted"]:
        pass

        tower["clients"] += 1

        tower["revenue"] += lead["ticket"]

        if lead["recurring"]:
            pass

            tower["recurring"] += (
                lead["ticket"] * 0.35
            )

# ============================================================
# SAVE ENGINE
# ============================================================

def save_runtime():
    pass

    report = {

        "timestamp": str(datetime.now()),

        "runtime": tower["runtime"],

        "mode": tower["mode"],

        "clients": tower["clients"],

        "revenue": round(
            tower["revenue"],
            2
        ),

        "recurring": round(
            tower["recurring"],
            2
        ),

        "total": round(
            tower["revenue"] +
            tower["recurring"],
            2
        ),

        "leads": tower["leads"]

    }

    with open(

        "REAL_TIME_TOWER.json",

        "w",

        encoding="utf-8"

    ) as f:

        json.dump(

            report,

            f,

            indent=4,

            ensure_ascii=False

        )

# ============================================================
# DASHBOARD
# ============================================================

def dashboard():
    pass

    total = (
        tower["revenue"] +
        tower["recurring"]
    )

    print("\n")

    print("===================================================")
    print(" IOTEC REAL-TIME COMMAND TOWER")
    print("===================================================")

    print(f"\nLeads captados: {len(tower['leads'])}")

    print(f"Clientes convertidos: {tower['clients']}")

    print(
        f"Receita acumulada: "
        f"R$ {total:,.2f}"
    )

    print(
        f"Receita recorrente: "
        f"R$ {tower['recurring']:,.2f}"
    )

    print("\nÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡ltimo lead:\n")

    last = tower["leads"][-1]

    print(f"SETOR: {last['sector'].upper()}")

    print(
        f"PROBABILIDADE: "
        f"{last['conversion_probability']}"
    )

    print(
        f"TICKET: "
        f"R$ {last['ticket']:,.2f}"
    )

    print(
        f"CONVERTIDO: "
        f"{last['converted']}"
    )

    print("\n===================================================")

# ============================================================
# RUNTIME LOOP
# ============================================================

print("\n")
print("===================================================")
print(" IOTEC REAL-TIME PROSPECTION ENGINE")
print("===================================================")
print("\n")

print("[ENGINE ONLINE]")
print("[COMMAND TOWER ACTIVE]")
print("[REAL-TIME MODE ENABLED]")
print("\n")

while True:
    pass

    lead = generate_lead()

    process_lead(lead)

    save_runtime()

    dashboard()

    time.sleep(SCAN_INTERVAL)




