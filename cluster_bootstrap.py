import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import subprocess
import time
import sys
import os

BASE = os.path.dirname(os.path.abspath(__file__))

ORQUEST = "orchestrator_cluster.py"
NODES = "nodes_cluster.py"

print("\n==============================")
print("CLUSTER BOOTSTRAP START")
print("==============================\n")


# =========================
# 1. START ORQUESTRADOR
# =========================
print("[BOOT] iniciando orquestrador...")

orquest = subprocess.Popen(
    [sys.executable, os.path.join(BASE, ORQUEST)],
    cwd=BASE
)

# espera estabilizar (resolve SUSPECT de boot)
time.sleep(6)


# =========================
# 2. START NODES
# =========================
nodes = ["API", "WORKER", "LOGGER"]

processos = []

for node in nodes:
    print(f"[BOOT] iniciando node {node}...")

    p = subprocess.Popen(
        [sys.executable, os.path.join(BASE, NODES), node],
        cwd=BASE
    )

    processos.append(p)

    time.sleep(2)


# =========================
# 3. SUPERVISOR SIMPLES
# =========================
print("\n[BOOT] cluster rodando...\n")

try:
    while True:
        time.sleep(5)

except KeyboardInterrupt:
    print("\n[BOOT] encerrando cluster...")

    for p in processos:
        p.terminate()

    orquest.terminate()




