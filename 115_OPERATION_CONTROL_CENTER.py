# ==============================================================================
# 115_OPERATION_CONTROL_CENTER.py
# IOTEC OPERATION CONTROL CENTER
# ==============================================================================

import json
from datetime import datetime
from collections import Counter

print("="*90)
print("IOTEC OPERATION CONTROL CENTER")
print("CENTRO DE CONTROLE OPERACIONAL")
print("="*90)
print()

ARQUIVO="IOTEC_MISSION_QUEUE.json"

try:

    with open(ARQUIVO,"r",encoding="utf8") as f:

        banco=json.load(f)

except:

    print("Fila nÃƒÂ£o encontrada.")
    raise SystemExit()

fila=banco["fila"]

print("="*90)
print("PAINEL OPERACIONAL")
print("="*90)
print()

por_estado=Counter()
por_segmento=Counter()
por_agente=Counter()

for ordem in fila:

    por_estado[ordem["estado"]]+=1
    por_segmento[ordem["segmento"]]+=1
    por_agente[ordem["agente"]]+=1

print("MISSÃƒâ€¢ES POR ESTADO")
print()

for estado,total in sorted(por_estado.items()):

    print(f"{estado:3} {total:5}")

print()

print("="*90)
print("MISSÃƒâ€¢ES POR AGENTE")
print("="*90)
print()

for agente,total in sorted(por_agente.items()):

    print(f"{agente:20} {total:5}")

print()

print("="*90)
print("SEGMENTOS")
print("="*90)
print()

for segmento,total in sorted(por_segmento.items()):

    print(f"{segmento:20} {total:5}")

print()

print("="*90)
print("CAPACIDADE OPERACIONAL")
print("="*90)
print()

print("MissÃƒÂµes Totais........",len(fila))
print("Estados...............",len(por_estado))
print("Agentes...............",len(por_agente))
print("Segmentos.............",len(por_segmento))

print()

print("="*90)
print("STATUS DAS MISSÃƒâ€¢ES")
print("="*90)
print()

status=Counter()

for ordem in fila:

    status[ordem["status"]]+=1

for s,qtd in status.items():

    print(f"{s:20} {qtd}")

saida={

    "generated_at":datetime.now().isoformat(),

    "resumo":{

        "missoes":len(fila),

        "estados":len(por_estado),

        "segmentos":len(por_segmento),

        "agentes":len(por_agente)

    },

    "status":dict(status)

}

with open(

    "IOTEC_OPERATION_CONTROL.json",

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
print("MISSÃƒÆ'O")
print("="*90)
print()

print("Observar continuamente")
print("todo o territÃƒÂ³rio")
print("econÃƒÂ´mico.")
print()

print("Detectar gargalos.")
print("Redistribuir carga.")
print("Garantir execuÃƒÂ§ÃƒÂ£o.")
print()

print("="*90)
print("ARQUIVO GERADO")
print("="*90)
print()

print("IOTEC_OPERATION_CONTROL.json")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("CONTROL CENTER OPERACIONAL.")


