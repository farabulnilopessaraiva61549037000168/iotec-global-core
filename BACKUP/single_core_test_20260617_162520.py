import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import time

print("SISTEMA SIMPLES INICIADO")

state = {"online": True, "counter": 0}

while True:
    state["counter"] += 1

    print(f"[CORE] heartbeat {state['counter']} - status: OK")

    time.sleep(2)


