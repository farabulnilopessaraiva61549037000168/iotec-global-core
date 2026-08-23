# ==========================================================
# 061_IOTEC_CONSTITUTION_BUILDER.py
# IOTEC CONSTITUTION BUILDER
# ==========================================================

import json
from datetime import datetime

CONSTITUTION = {

    "company": "IOTEC",

    "version": "1.0",

    "created": str(datetime.now()),

    "architecture": {

        "official_core":
            "IOTEC_GLOBAL_CORE.py",

        "operational_core":
            "IOTEC_GLOBAL_OPERATIONAL_CORE.py",

        "official_entry":
            "053_CLIENT_ORCHESTRATOR_ENGINE.py",

        "gateway":
            "IOTEC_GATEWAY_CORE.py",

        "control_tower":
            "049_CONTROL_TOWER_ENGINE.py",

        "mission_dispatch":
            "051_MISSION_DISPATCH_ENGINE.py",

        "task_execution":
            "052_TASK_EXECUTION_ENGINE.py",

        "payment_gateway":
            "paypal_server.py",

        "crm":
            "REAL_LEAD_BRIDGE.py"

    },

    "laws":[

        "Existe apenas um Nucleo Oficial.",

        "Existe apenas uma Porta Oficial.",

        "Todo cliente entra pelo Client Orchestrator.",

        "Todo pagamento passa pelo Gateway Financeiro.",

        "Toda comunicacao entre ecossistemas passa pela Control Tower.",

        "Laboratorios nao executam producao.",

        "Backups nunca executam.",

        "Todo novo modulo deve pertencer a um ecossistema.",

        "Todo modulo deve possuir um responsavel.",

        "Toda venda deve terminar em entrega ou cancelamento."

    ]

}

ARQUIVO="IOTEC_CONSTITUTION.json"

with open(

    ARQUIVO,

    "w",

    encoding="utf8"

) as f:

    json.dump(

        CONSTITUTION,

        f,

        indent=4,

        ensure_ascii=False

    )

print("="*70)
print("IOTEC CONSTITUTION BUILDER")
print("="*70)
print()

print("Arquivo criado:")
print(ARQUIVO)

print()

print("="*70)
print("NÃƒÅ¡CLEO OFICIAL")
print("="*70)
print()

print(CONSTITUTION["architecture"]["official_core"])

print()

print("="*70)
print("PORTA OFICIAL")
print("="*70)
print()

print(CONSTITUTION["architecture"]["official_entry"])

print()

print("="*70)
print("LEIS DA EMPRESA")
print("="*70)
print()

for i,lei in enumerate(CONSTITUTION["laws"],1):

    print(f"{i:02d} - {lei}")

print()

print("="*70)
print("MISSÃƒÆ'O")
print("="*70)
print()

print("A IOTEC agora possui")
print("uma ConstituiÃƒÂ§ÃƒÂ£o Oficial.")

print()

print("Todo novo mÃƒÂ³dulo")
print("deverÃƒÂ¡ consultar")
print("este documento.")


