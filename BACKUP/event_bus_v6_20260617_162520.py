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
# EVENT GATE (CONTROLE DE ENTRADA)
# =========================

class EventGate:
    def __init__(self):
        self.rate_limit = defaultdict(list)  # event_type -> timestamps

    def allow(self, event_type):
        now = time.time()

        # limpa eventos antigos (>5s)
        self.rate_limit[event_type] = [
            t for t in self.rate_limit[event_type]
            if now - t < 5
        ]

        # limite por tipo de evento
        if len(self.rate_limit[event_type]) >= 3:
            return False

        self.rate_limit[event_type].append(now)
        return True


# =========================
# EVENT BUS
# =========================

class EventBus:
    def __init__(self, gate: EventGate):
        self.queue = deque()
        self.listeners = defaultdict(list)
        self.gate = gate

    def subscribe(self, event_type, callback):
        self.listeners[event_type].append(callback)

    def emit(self, event_type, data=None):
        pass

        # ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ EVENT GATE AQUI
        if not self.gate.allow(event_type):
            print(f"[GATE BLOCK] {event_type}")
            return

        event = {
            "id": str(uuid.uuid4()),
            "type": event_type,
            "data": data
        }

        print(f"[ENQUEUE] {event_type} -> {data}")
        self.queue.append(event)

        logging.info(f"ENFILEIRADO: {event_type}")


# =========================
# WORKER
# =========================

class Worker:
    def __init__(self, bus: EventBus):
        self.bus = bus

    def start(self):
        Thread(target=self.run, daemon=True).start()

    def run(self):
        while True:
            if not self.bus.queue:
                time.sleep(0.3)
                continue

            event = self.bus.queue.popleft()

            etype = event["type"]
            data = event["data"]

            print(f"[PROCESSANDO] {etype}: {data}")

            for cb in self.bus.listeners[etype]:
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
            print("[AUTH] jÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ logado -> bloqueado")
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
        print(f"[LOG] usuÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio: {data}")


class APIModule:
    def __init__(self, bus: EventBus):
        self.bus = bus

    def start(self):
        Thread(target=self.simulate, daemon=True).start()

    def simulate(self):
        while True:
            time.sleep(2)
            self.bus.emit("login_request", "user123")


# =========================
# START
# =========================

if __name__ == "__main__":
    pass

    print("\n==============================")
    print("NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO V6 - EVENT GATE SYSTEM")
    print("==============================\n")

    state = StateManager()
    gate = EventGate()
    bus = EventBus(gate)

    auth = AuthModule(bus, state)
    logger = LoggerModule(bus)
    api = APIModule(bus)

    worker = Worker(bus)

    auth.start()
    logger.start()
    api.start()
    worker.start()

    print("\n[SISTEMA] rodando com EVENT GATE + RATE LIMIT...\n")

    while True:
        time.sleep(1)


