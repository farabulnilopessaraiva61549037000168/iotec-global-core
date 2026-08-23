import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import time
import threading

TIMEOUT = 5
COOLDOWN_TIME = 8

nodes = {
    "API": {"last_seen": time.time(), "state": "HEALTHY", "cooldown_until": 0},
    "WORKER": {"last_seen": time.time(), "state": "HEALTHY", "cooldown_until": 0},
    "LOGGER": {"last_seen": time.time(), "state": "HEALTHY", "cooldown_until": 0},
}


# =========================
# SIMULA HEARTBEAT (DEPOIS TROCA POR SOCKET REAL)
# =========================
def heartbeat_simulator():
    while True:
        now = time.time()
        for n in nodes:
            nodes[n]["last_seen"] = now
        time.sleep(2)


# =========================
# FSM TRANSITION
# =========================
def update_state(node, now):
    data = nodes[node]

    # COOLDOWN BLOQUEIA TUDO
    if now < data["cooldown_until"]:
        data["state"] = "COOLDOWN"
        return

    diff = now - data["last_seen"]

    if diff < TIMEOUT:
        data["state"] = "HEALTHY"

    elif diff < TIMEOUT * 2:
        data["state"] = "SUSPECT"

    else:
        data["state"] = "RESTARTING"
        restart(node)


# =========================
# RESTART CONTROLADO
# =========================
def restart(node):
    data = nodes[node]

    print(f"[FSM] RESTARTING {node}")

    # evita loop infinito
    data["cooldown_until"] = time.time() + COOLDOWN_TIME
    data["last_seen"] = time.time()
    data["state"] = "COOLDOWN"

    print(f"[FSM] {node} em COOLDOWN")


# =========================
# MONITOR FSM
# =========================
def monitor():
    while True:
        now = time.time()

        for node in nodes:
            update_state(node, now)
            print(f"[FSM] {node} -> {nodes[node]['state']}")

        time.sleep(2)


# =========================
# START
# =========================
if __name__ == "__main__":
    pass

    print("\n==============================")
    print("FSM ORQUESTRADOR - STABLE CORE")
    print("==============================\n")

    threading.Thread(target=heartbeat_simulator, daemon=True).start()
    threading.Thread(target=monitor, daemon=True).start()

    while True:
        time.sleep(1)




