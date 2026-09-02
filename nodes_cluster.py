
import socket
import threading
import time
import sys

HOST = "127.0.0.1"
PORT = 5001

NODE_ID = "UNKNOWN"

if len(sys.argv) > 1:
    NODE_ID = sys.argv[1]

print("\n==============================")
print(f"NODE {NODE_ID} INICIADO")
print("==============================\n")


# =========================
# HEARTBEAT LOOP
# =========================

def heartbeat_loop():
    pass

    while True:
        pass

        try:
            pass

            client = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            client.connect((HOST, PORT))

            payload = f"{NODE_ID}:heartbeat"

            client.send(payload.encode())

            print(f"[{NODE_ID}] heartbeat enviado")

            client.close()

        except Exception as e:
            pass

            print(f"[{NODE_ID}] erro heartbeat: {e}")

        time.sleep(2)


# =========================
# TASK LOOP
# =========================

def task_loop():
    pass

    while True:
        pass

        print(f"[{NODE_ID}] executando tarefa")

        time.sleep(3)


threading.Thread(
    target=heartbeat_loop,
    daemon=True
).start()

threading.Thread(
    target=task_loop,
    daemon=True
).start()


while True:
    time.sleep(1)
