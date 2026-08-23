import json
import os
from datetime import datetime
import uuid

MISSION_FILE = "IOTEC_MISSIONS.json"

# ==========================================================
# MAPA ESTRATÃƒâ€°GICO DA IOTEC
# ==========================================================

MARKETS = {

    "ConstruÃƒÂ§ÃƒÂ£o":[

        "Construtoras",

        "Empreiteiras",

        "EscritÃƒÂ³rios de Engenharia",

        "EscritÃƒÂ³rios de Arquitetura"

    ],

    "EducaÃƒÂ§ÃƒÂ£o":[

        "Escolas",

        "Universidades",

        "Secretarias de EducaÃƒÂ§ÃƒÂ£o"

    ],

    "SaÃƒÂºde":[

        "Hospitais",

        "ClÃƒÂ­nicas",

        "LaboratÃƒÂ³rios"

    ],

    "IndÃƒÂºstria":[

        "Metalurgia",

        "Alimentos",

        "TÃƒÂªxtil",

        "QuÃƒÂ­mica"

    ]

}

# ==========================================================

if os.path.exists(MISSION_FILE):

    with open(MISSION_FILE,"r",encoding="utf-8") as f:

        missions=json.load(f)

else:

    missions=[]

existing = {

    m.get("objective","")

    for m in missions

}

created = 0

# ==========================================================
# PLANEJAMENTO
# ==========================================================

for sector,segments in MARKETS.items():

    for segment in segments:

        objective = f"Pesquisar empresas do segmento {segment}"

        if objective in existing:
            continue

        missions.append({

            "mission_id":str(uuid.uuid4())[:8],

            "center":"MARKET CENTER",

            "agent":"COMPANY DISCOVERY ENGINE",

            "priority":"MÃƒâ€°DIA",

            "objective":objective,

            "status":"PENDENTE",

            "progress":0,

            "created_at":datetime.now().isoformat()

        })

        created += 1

# ==========================================================

with open(

    MISSION_FILE,

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
print("IOTEC AUTONOMOUS PLANNING ENGINE")
print("="*90)
print()

print("NOVAS MISSÃƒâ€¢ES :",created)
print()

print("="*90)
print("MISSÃƒâ€¢ES GERADAS")
print("="*90)
print()

for mission in missions[-created:]:

    print(mission["objective"])

print()

print("="*90)
print("MISSÃƒÆ'O")
print("="*90)
print()

print("Detectar")
print("automaticamente")
print("mercados")
print("ainda")
print("nÃƒÂ£o")
print("explorados.")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("Data :",datetime.now())
print()

print("AUTONOMOUS PLANNING ENGINE OPERACIONAL.")

