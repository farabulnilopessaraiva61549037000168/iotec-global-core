import json
import os
import subprocess
from datetime import datetime

MISSIONS = "IOTEC_MISSIONS.json"
EVENTS = "IOTEC_EVENTS.json"

# ==========================================================
# UTILIDADES
# ==========================================================

def load_json(file):

    if not os.path.exists(file):
        return []

    try:

        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)

    except:
        return []

# ==========================================================

missions = load_json(MISSIONS)
events = load_json(EVENTS)

pending = sum(1 for m in missions if m.get("status") == "PENDENTE")
running = sum(1 for m in missions if m.get("status") == "EM EXECUÃƒâ€¡ÃƒÆ'O")
completed = sum(1 for m in missions if m.get("status") == "CONCLUÃƒÂDA")

new_events = sum(1 for e in events if e.get("status") == "NOVO")

print("=" * 90)
print("IOTEC KERNEL SCHEDULER")
print("=" * 90)
print()

print("MISSÃƒâ€¢ES")
print("-" * 90)
print("Pendentes.....:", pending)
print("Executando....:", running)
print("ConcluÃƒÂ­das....:", completed)
print()

print("EVENTOS NOVOS.:", new_events)
print()

# ==========================================================
# DECISÃƒÆ'O
# ==========================================================

if pending > 0:

    decision = "Executar fila de missÃƒÂµes."

elif new_events > 0:

    decision = "Despachar eventos."

elif completed == 0:

    decision = "Gerar novas missÃƒÂµes."

else:

    decision = "Sistema em espera."

print("=" * 90)
print("DECISÃƒÆ'O DO KERNEL")
print("=" * 90)
print()

print(decision)
print()

print("=" * 90)
print("CHEFE DE GABINETE")
print("=" * 90)
print()

print("Boa noite, Presidente.")
print()

print("O Kernel")
print("avaliou")
print("automaticamente")
print("o estado")
print("da plataforma")
print("e definiu")
print("a prÃƒÂ³xima")
print("aÃƒÂ§ÃƒÂ£o.")
print()

print("=" * 90)
print("STATUS")
print("=" * 90)
print()

print("Data :", datetime.now())
print()

print("KERNEL SCHEDULER OPERACIONAL.")

