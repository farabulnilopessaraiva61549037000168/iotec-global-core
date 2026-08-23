# ==========================================================
# 063_OPERATION_READINESS_ENGINE.py
# IOTEC OPERATION READINESS ENGINE
# ==========================================================

import json
import os

ROOT = r"C:\IOTEC"

CONSTITUTION = "IOTEC_CONSTITUTION.json"

CHECKS = {

    "ConstituiÃƒÂ§ÃƒÂ£o": CONSTITUTION,

    "NÃƒÂºcleo Oficial": "IOTEC_GLOBAL_CORE.py",

    "Core Operacional": "IOTEC_GLOBAL_OPERATIONAL_CORE.py",

    "Entrada Oficial": "053_CLIENT_ORCHESTRATOR_ENGINE.py",

    "Gateway": "IOTEC_GATEWAY_CORE.py",

    "Control Tower": "049_CONTROL_TOWER_ENGINE.py",

    "Mission Dispatch": "051_MISSION_DISPATCH_ENGINE.py",

    "Task Execution": "052_TASK_EXECUTION_ENGINE.py",

    "Gateway Financeiro": "paypal_server.py",

    "CRM": "REAL_LEAD_BRIDGE.py"

}

print("="*70)
print("IOTEC OPERATION READINESS ENGINE")
print("="*70)
print()

ok = 0
total = len(CHECKS)

for nome,arquivo in CHECKS.items():

    encontrado = False

    for pasta,dirs,files in os.walk(ROOT):

        if arquivo in files:

            encontrado = True
            caminho = os.path.join(pasta,arquivo)
            break

    if encontrado:

        ok += 1

        print(f"[OK] {nome}")
        print("Arquivo :",arquivo)
        print("Local   :",caminho)

    else:

        print(f"[ERRO] {nome}")
        print("Arquivo :",arquivo)

    print("-"*60)

print()

print("="*70)
print("MATURIDADE OPERACIONAL")
print("="*70)

percentual = round((ok/total)*100,1)

print()

print("Componentes :",ok,"/",total)
print("ProntidÃƒÂ£o   :",percentual,"%")

print()

print("="*70)
print("CHECKLIST DA PRIMEIRA VENDA")
print("="*70)

print()

print("[ ] Produto Comercial definido")
print("[ ] Lead recebido")
print("[ ] Cliente identificado")
print("[ ] Proposta emitida")
print("[ ] Checkout criado")
print("[ ] Pagamento confirmado")
print("[ ] ProduÃƒÂ§ÃƒÂ£o iniciada")
print("[ ] Entrega realizada")
print("[ ] Venda registrada")

print()

print("="*70)
print("MISSÃƒÆ'O DA PRESIDÃƒÅ NCIA")
print("="*70)

if percentual == 100:

    print()
    print("A arquitetura oficial estÃƒÂ¡ pronta.")
    print("O foco agora deixa de ser")
    print("infraestrutura e passa a ser")
    print("OPERAÃƒâ€¡ÃƒÆ'O.")
else:

    print()
    print("Ainda existem componentes")
    print("oficiais ausentes.")


