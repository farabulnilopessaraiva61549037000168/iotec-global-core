import json
import uuid
from datetime import datetime

OUTPUT = "IOTEC_MISSIONS.json"

# ==========================================================
# MISSÃƒâ€¢ES GERADAS PELA CONTROL TOWER
# ==========================================================

missions = [

    {

        "center":"COMMERCIAL CENTER",

        "agent":"CONTACT DISCOVERY ENGINE",

        "priority":"CRÃƒÂTICA",

        "objective":"Descobrir Website Oficial",

    },

    {

        "center":"COMMERCIAL CENTER",

        "agent":"CONTACT DISCOVERY ENGINE",

        "priority":"CRÃƒÂTICA",

        "objective":"Descobrir E-mail Corporativo",

    },

    {

        "center":"COMMERCIAL CENTER",

        "agent":"CONTACT DISCOVERY ENGINE",

        "priority":"ALTA",

        "objective":"Descobrir Telefone Comercial",

    },

    {

        "center":"COMMERCIAL CENTER",

        "agent":"CONTACT DISCOVERY ENGINE",

        "priority":"ALTA",

        "objective":"Descobrir LinkedIn",

    },

    {

        "center":"MARKET CENTER",

        "agent":"COMPANY DISCOVERY ENGINE",

        "priority":"MÃƒâ€°DIA",

        "objective":"Encontrar novas empresas",

    },

    {

        "center":"SCIENTIFIC CENTER",

        "agent":"MARKET SCIENTIST",

        "priority":"MÃƒâ€°DIA",

        "objective":"Pesquisar tendÃƒÂªncias do setor",

    }

]

# ==========================================================

queue=[]

for mission in missions:

    queue.append({

        "mission_id":str(uuid.uuid4())[:8],

        "status":"PENDENTE",

        "progress":0,

        "created_at":datetime.now().isoformat(),

        **mission

    })

with open(

    OUTPUT,

    "w",

    encoding="utf-8"

) as f:

    json.dump(

        queue,

        f,

        indent=4,

        ensure_ascii=False

    )

print("="*90)
print("IOTEC MISSION ORCHESTRATOR")
print("="*90)
print()

print("MISSÃƒâ€¢ES")

print("-"*90)

print()

for item in queue:

    print(item["mission_id"])

    print("Centro.....:",item["center"])

    print("Agente.....:",item["agent"])

    print("Prioridade.:",item["priority"])

    print("Objetivo...:",item["objective"])

    print("Status.....:",item["status"])

    print()

print("="*90)
print("RESUMO")
print("="*90)
print()

print("MissÃƒÂµes Criadas :",len(queue))

print()

print("="*90)
print("CHEFE DE GABINETE")
print("="*90)
print()

print()

print("Boa noite, Presidente.")

print()

print("A Torre de Controle")

print("transformou")

print("o gargalo")

print("em missÃƒÂµes")

print("executÃƒÂ¡veis.")

print()

print("Cada Centro")

print("recebe")

print("somente")

print("as tarefas")

print("compatÃƒÂ­veis")

print("com sua")

print("especialidade.")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print(datetime.now())

print()

print("MISSION ORCHESTRATOR OPERACIONAL.")

