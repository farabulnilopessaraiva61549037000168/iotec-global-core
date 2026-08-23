# ==============================================================================
# 114_MISSION_DISPATCHER_ENGINE.py
# IOTEC MISSION DISPATCHER ENGINE
# ==============================================================================

import json
from datetime import datetime

print("="*90)
print("IOTEC MISSION DISPATCHER ENGINE")
print("DESPACHANTE DE MISSÃƒâ€¢ES")
print("="*90)
print()

ARQUIVO="IOTEC_TERRITORIAL_MISSIONS.json"

try:

    with open(ARQUIVO,"r",encoding="utf8") as f:

        banco=json.load(f)

except:

    print("MissÃƒÂµes nÃƒÂ£o encontradas.")
    raise SystemExit()

missoes = banco.get("missoes", [])["missoes"]

AGENTES={

"CE":"CE_AGENT",
"PE":"PE_AGENT",
"BA":"BA_AGENT",
"RN":"RN_AGENT",
"PB":"PB_AGENT",
"PI":"PI_AGENT",
"MA":"MA_AGENT",
"AL":"AL_AGENT",
"SE":"SE_AGENT"

}

FILA=[]

print("="*90)
print("DESPACHO")
print("="*90)
print()

for missao in MISSOES:

    agente=AGENTES.get(

        missao["uf"],

        "BRAZIL_AGENT"

    )

    ordem={

        "id":missao["id"],

        "estado":missao["uf"],

        "cidade":missao["cidade"],

        "segmento":missao["segmento"],

        "agente":agente,

        "status":"AGUARDANDO",

        "proxima_etapa":"DISCOVERY"

    }

    FILA.append(ordem)

print("Total de Ordens :",len(FILA))
print()

print("Primeiras MissÃƒÂµes")
print()

for ordem in FILA[:20]:

    print(

        f"[{ordem['agente']}] "

        f"{ordem['cidade']}"

        f" -> "

        f"{ordem['segmento']}"

    )

saida={

"generated_at":datetime.now().isoformat(),

"total":len(FILA),

"fila":FILA

}

with open(

"IOTEC_MISSION_QUEUE.json",

"w",

encoding="utf8"

) as f:

    json.dump(

        saida,

        f,

        indent=4,

        ensure_ascii=False

    )

print()

print("="*90)
print("FILOSOFIA")
print("="*90)
print()

print("Nenhuma missÃƒÂ£o")
print("fica sem destino.")

print()

print("Cada estado")
print("possui")

print("um agente")

print("territorial.")

print()

print("Cada agente")

print("recebe")

print("automaticamente")

print("suas missÃƒÂµes.")

print()

print("="*90)
print("ARQUIVO GERADO")
print("="*90)
print()

print("IOTEC_MISSION_QUEUE.json")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("MissÃƒÂµes..............",len(FILA))
print("Estados..............",len(AGENTES))
print("Data.................",datetime.now().strftime("%d/%m/%Y %H:%M"))

print()

print("MISSION DISPATCHER OPERACIONAL.")


