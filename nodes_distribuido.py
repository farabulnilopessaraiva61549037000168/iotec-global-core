import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# nodes.py
import socket
import threading
import time

HOST = "127.0.0.1"
PORT = 5000


class Node:
    def __init__(self, name):
        self.name = name
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.client.connect((HOST, PORT))
        print(f"[{self.name}] conectado")

    def send(self, msg):
        full = f"{self.name}:{msg}"
        self.client.send(full.encode())

    def listen(self):
        while True:
            try:
                data = self.client.recv(1024).decode()
                print(f"[{self.name} RECEBEU] {data}")
            except:
                break


class APINode(Node):
    def run(self):
        self.connect()
        threading.Thread(target=self.listen, daemon=True).start()

        while True:
            time.sleep(3)
            self.send("login_request:user123")


class WorkerNode(Node):
    def run(self):
        self.connect()
        threading.Thread(target=self.listen, daemon=True).start()


class LoggerNode(Node):
    def run(self):
        self.connect()
        threading.Thread(target=self.listen, daemon=True).start()


if __name__ == "__main__":
    pass

    print("NODE SYSTEM INICIANDO...")

    api = APINode("API_NODE")
    worker = WorkerNode("WORKER_NODE")
    logger = LoggerNode("LOGGER_NODE")

    threading.Thread(target=api.run).start()
    threading.Thread(target=worker.run).start()
    threading.Thread(target=logger.run).start()




