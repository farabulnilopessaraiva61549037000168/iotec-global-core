# ==============================================================================
# 116_DISCOVERY_EXECUTION_ENGINE.py
# IOTEC DISCOVERY EXECUTION ENGINE
# ==============================================================================

import json
from datetime import datetime

print("="*90)
print("IOTEC DISCOVERY EXECUTION ENGINE")
print("EXECUTOR DE MISSÃƒâ€¢ES DE DESCOBERTA")
print("="*90)
print()

ARQUIVO = "IOTEC_MISSION_QUEUE.json"

try:

    with open(ARQUIVO,"r",encoding="utf8") as f:
        banco = json.load(f)

except:

    print("Fila de missÃƒÂµes nÃƒÂ£o encontrada.")
    raise SystemExit()

fila = banco["fila"]

MAX_EXECUCOES = 10

executadas = 0

print("="*90)
print("EXECUÃƒâ€¡ÃƒÆ'O")
print("="*90)
print()

for missao in fila:

    if executadas >= MAX_EXECUCOES:
        break

    if missao["status"] != "AGUARDANDO":
        continue

    consulta = f"{missao['segmento']} {missao['cidade']}"

    missao["status"] = "EM EXECUÃƒâ€¡ÃƒÆ'O"

    missao["consulta"] = consulta

    missao["inicio"] = datetime.now().isoformat()

    print(f"[{missao['agente']}]")
    print("MissÃƒÂ£o :", missao["id"])
    print("Cidade :", missao["cidade"])
    print("Segmento:", missao["segmento"])
    print("Consulta:", consulta)
    print("PrÃƒÂ³ximo :", "OPENSTREETMAP_CONNECTOR")
    print()

    executadas += 1

with open(
    "IOTEC_MISSION_QUEUE.json",
    "w",
    encoding="utf8"
) as f:

    json.dump(
        banco,
        f,
        indent=4,
        ensure_ascii=False
    )

print("="*90)
print("RESUMO")
print("="*90)
print()

print("MissÃƒÂµes iniciadas :", executadas)
print("PrÃƒÂ³xima etapa..... OpenStreetMap")
print()

print("="*90)
print("FILOSOFIA")
print("="*90)
print()

print("MissÃƒÂµes deixam")
print("de esperar.")

print()

print("Agora entram")
print("na linha")
print("de execuÃƒÂ§ÃƒÂ£o.")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("DISCOVERY EXECUTION OPERACIONAL.")


