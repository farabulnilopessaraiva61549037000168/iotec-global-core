import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import socket
import time
import sys
import threading
from pathlib import Path

NODE_ID = sys.argv[1] if len(sys.argv) > 1 else "UNKNOWN"

HOST = "127.0.0.1"
PORT = 6000

LOG_FILE = Path("cluster_logs.txt")


# =========================
# CENTRAL LOGGER
# =========================
def log(msg):
    pass

    line = f"[{NODE_ID}] {msg}"

    print(line)

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")


# =========================
# HEARTBEAT
# =========================
def heartbeat():
    pass

    while True:
        pass

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            sock.connect((HOST, PORT))

            msg = f"{NODE_ID}:alive:{time.time()}"

            sock.send(msg.encode())

            sock.close()

            log("heartbeat enviado")

        except Exception as e:
            pass

            log(f"falha heartbeat: {e}")

        time.sleep(2)


# =========================
# WORK LOOP
# =========================
def work():
    pass

    while True:
        pass

        log("executando tarefa")

        time.sleep(3)


# =========================
# START
# =========================
if __name__ == "__main__":
    pass

    print("\n==============================")
    print(f"NODE {NODE_ID} INICIADO")
    print("==============================\n")

    log("node online")

    threading.Thread(
        target=heartbeat,
        daemon=True
    ).start()

    threading.Thread(
        target=work,
        daemon=True
    ).start()

    while True:
        time.sleep(1)




