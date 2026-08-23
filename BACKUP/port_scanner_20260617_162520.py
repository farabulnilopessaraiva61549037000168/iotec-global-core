import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import socket


def is_port_free(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', port)) != 0


def get_free_ports(start=5173, amount=5):
    ports = []
    current = start

    while len(ports) < amount:
        if is_port_free(current):
            ports.append(current)
        current += 1

    return ports


if __name__ == '__main__':
    print(get_free_ports())


