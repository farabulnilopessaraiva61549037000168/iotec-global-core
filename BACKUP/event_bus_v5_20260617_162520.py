import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import time
import logging
import uuid
from threading import Thread
from collections import deque, defaultdict

logging.basicConfig(
    filename="core.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# =========================
# STATE
# =========================

class StateManager:
    def __init__(self):
        self.state = {
            "logged_in": False,
            "active_user": None
        }

# =========================
# EVENT BUS (SÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ ENFILEIRA)
# =========================

class EventBus:
    def __init__(self):
        self.queue = deque()
        self.listeners = defaultdict(list)

    def subscribe(self, event_type, callback):
        self.listeners[event_type].append(callback)

    def emit(self, event_type, data=None):
        event = {
            "id": str(uuid.uuid4()),
            "type": event_type,
            "data": data
        }

        print(f"[ENQUEUE] {event_type} -> {data}")
        self.queue.append(event)

        logging.info(f"Enfileirado: {event_type}")

# =========================
# WORKER (PROCESSA FILA)
# =========================

class Worker:
    def __init__(self, bus: EventBus):
        self.bus = bus
        self.running = True

    def start(self):
        Thread(target=self.run, daemon=True).start()

    def run(self):
        while self.running:
            if len(self.bus.queue) == 0:
                time.sleep(0.5)
                continue

            event = self.bus.queue.popleft()

            event_type = event["type"]
            data = event["data"]

            print(f"[PROCESSANDO] {event_type}: {data}")

            if event_type in self.bus.listeners:
                for cb in self.bus.listeners[event_type]:
                    try:
                        cb(data)
                    except Exception as e:
                        logging.error(f"Erro worker: {e}")

# =========================
# MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œDULOS
# =========================

class AuthModule:
    def __init__(self, bus: EventBus, state: StateManager):
        self.bus = bus
        self.state = state

    def start(self):
        self.bus.subscribe("login_request", self.login)

    def login(self, data):
        if self.state.state["logged_in"]:
            print("[AUTH] jÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ logado -> ignorado")
            return

        print(f"[AUTH] login {data}")

        self.state.state["logged_in"] = True
        self.state.state["active_user"] = data

        self.bus.emit("login_success", data)


class LoggerModule:
    def __init__(self, bus: EventBus):
        self.bus = bus

    def start(self):
        self.bus.subscribe("login_success", self.log)

    def log(self, data):
        print(f"[LOG] usuÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio autenticado: {data}")


class APIModule:
    def __init__(self, bus: EventBus):
        self.bus = bus

    def start(self):
        Thread(target=self.simulate, daemon=True).start()

    def simulate(self):
        while True:
            time.sleep(6)
            self.bus.emit("login_request", "user123")


# =========================
# START
# =========================

if __name__ == "__main__":
    pass

    print("\n==============================")
    print("NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO V5 - EVENT QUEUE SYSTEM")
    print("==============================\n")

    bus = EventBus()
    state = StateManager()

    auth = AuthModule(bus, state)
    logger = LoggerModule(bus)
    api = APIModule(bus)

    worker = Worker(bus)

    auth.start()
    logger.start()
    api.start()

    worker.start()

    print("\n[SISTEMA] rodando com fila + worker...\n")

    while True:
        time.sleep(1)


