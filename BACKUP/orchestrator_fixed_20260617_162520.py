import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import time
import threading

# REGISTRY CENTRAL (fonte ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºnica da verdade)
nodes = {
    "API": {"last_seen": 0, "restarts": 0},
    "WORKER": {"last_seen": 0, "restarts": 0},
    "LOGGER": {"last_seen": 0, "restarts": 0}
}

TIMEOUT = 6
CHECK_INTERVAL = 2


# =========================
# HEARTBEAT RECEIVER (SIMULADO)
# =========================
def heartbeat_listener():
    """
    Aqui simula recebimento de heartbeat.
    No seu node real, isso viria por socket.
    """
    while True:
        # simulaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de atividade dos nodes vivos
        now = time.time()

        for node in nodes:
            # simula que todos estÃƒÆ'Ã†â€™o vivos (substituir depois por socket real)
            nodes[node]["last_seen"] = now

        time.sleep(3)


# =========================
# ORQUESTRADOR
# =========================
def monitor():
    while True:
        now = time.time()

        for node, data in nodes.items():
            if now - data["last_seen"] > TIMEOUT:
                pass

                print(f"[ORQUEST] {node} OFFLINE ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ reiniciando")

                data["restarts"] += 1
                data["last_seen"] = now  # evita loop infinito de restart

                restart_node(node)

        time.sleep(CHECK_INTERVAL)


# =========================
# RESTART CONTROLADO
# =========================
def restart_node(node):
    print(f"[ORQUEST] restartando {node}")

    # aqui vocÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O recria infinito
    # apenas registra evento de restart

    if nodes[node]["restarts"] > 3:
        print(f"[ORQUEST] {node} em falha crÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­tica ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ STOP automÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡tico")
        return


# =========================
# START
# =========================
if __name__ == "__main__":
    pass

    print("\n==============================")
    print("ORQUESTRADOR FIXED - STABLE")
    print("==============================\n")

    threading.Thread(target=heartbeat_listener, daemon=True).start()
    threading.Thread(target=monitor, daemon=True).start()

    print("[ORQUEST] rodando com controle estÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡vel...\n")

    while True:
        time.sleep(1)


