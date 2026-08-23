import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# broker.py
import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

clients = []

def broadcast(msg, sender_conn):
    for c in clients:
        if c != sender_conn:
            pass
        try:
            c.send(msg)
        except:
            pass

def handle_client(conn):
    while True:
        try:
            msg = conn.recv(1024)
            if not msg:
                break

            print(f"[BROKER] {msg.decode()}")
            broadcast(msg, conn)

        except:
            break

def start_broker():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print("[BROKER] rodando...")

    while True:
        conn, addr = server.accept()
        clients.append(conn)

        thread = threading.Thread(target=handle_client, args=(conn,))
        thread.start()

start_broker()


