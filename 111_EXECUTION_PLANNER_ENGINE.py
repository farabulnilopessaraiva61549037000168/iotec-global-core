# ==============================================================================
# 111_EXECUTION_PLANNER_ENGINE.py
# IOTEC EXECUTION PLANNER ENGINE
# ==============================================================================

import json
from datetime import datetime

print("="*90)
print("IOTEC EXECUTION PLANNER ENGINE")
print("PLANEJADOR DE EXECUÃƒâ€¡ÃƒÆ'O")
print("="*90)
print()

ARQUIVO="IOTEC_OPPORTUNITY_DATABASE.json"

try:

    with open(ARQUIVO,"r",encoding="utf8") as f:
        banco=json.load(f)

except:

    print("Banco de oportunidades nÃƒÂ£o encontrado.")
    raise SystemExit()

ORDEM=1
TAREFAS=[]

for oportunidade in banco["oportunidades"]:

    empresa=oportunidade["empresa"]

    plano=[

        "Pesquisar site oficial",
        "Pesquisar telefone",
        "Pesquisar e-mail",
        "Pesquisar LinkedIn",
        "Identificar decisor",
        "Gerar estratÃƒÂ©gia comercial",
        "Preparar apresentaÃƒÂ§ÃƒÂ£o",
        "Preparar proposta",
        "Registrar CRM"

    ]

    print("="*90)
    print("EMPRESA")
    print("="*90)
    print()

    print(empresa)
    print()

    print("PRIORIDADE :", oportunidade["prioridade"])
    print("STATUS..... :", oportunidade["status"])
    print()

    print("PLANO OPERACIONAL")
    print()

    etapa=1

    for tarefa in plano:

        print(f"{etapa:02d} - {tarefa}")

        TAREFAS.append({

            "ordem":ORDEM,

            "empresa":empresa,

            "etapa":etapa,

            "tarefa":tarefa,

            "status":"PENDENTE"

        })

        etapa+=1

    ORDEM+=1

    print()

saida={

    "generated_at":datetime.now().isoformat(),

    "total_empresas":len(banco["oportunidades"]),

    "total_tarefas":len(TAREFAS),

    "tarefas":TAREFAS

}

with open(

    "IOTEC_EXECUTION_QUEUE.json",

    "w",

    encoding="utf8"

) as f:

    json.dump(

        saida,

        f,

        indent=4,

        ensure_ascii=False

    )

print("="*90)
print("FILA DE EXECUÃƒâ€¡ÃƒÆ'O")
print("="*90)
print()

print("Empresas.............",len(banco["oportunidades"]))
print("Ordens...............",ORDEM-1)
print("Tarefas..............",len(TAREFAS))

print()

print("="*90)
print("MISSÃƒÆ'O")
print("="*90)
print()

print("Toda oportunidade")
print("gera uma ordem")
print("de trabalho.")

print()

print("Toda ordem")
print("ÃƒÂ© dividida")
print("em tarefas.")

print()

print("Cada tarefa")
print("poderÃƒÂ¡ ser")
print("executada")
print("por agentes")
print("especializados.")

print()

print("="*90)
print("ARQUIVO GERADO")
print("="*90)
print()

print("IOTEC_EXECUTION_QUEUE.json")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("EXECUTION PLANNER OPERACIONAL.")


