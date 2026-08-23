import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import time
import json
import logging
import uuid
from threading import Thread
from collections import deque, defaultdict
import os

LOG_FILE = "event_log.json"

logging.basicConfig(
    filename="core.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# =========================
# EVENT STORE (PERSISTÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â NCIA)
# =========================

class EventStore:
    def __init__(self, file=LOG_FILE):
        self.file = file
        self.events = []
        self._load()

    def _load(self):
        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                try:
                    self.events = json.load(f)
                    print(f"[STORE] {len(self.events)} eventos carregados")
                except:
                    self.events = []

    def append(self, event):
        self.events.append(event)
        self._save()

    def _save(self):
        with open(self.file, "w") as f:
            json.dump(self.events, f, indent=2)

    def replay(self):
        print("\n[REPLAY] reexecutando eventos...\n")
        return self.events


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
# EVENT BUS
# =========================

class EventBus:
    def __init__(self, store: EventStore):
        self.queue = deque()
        self.listeners = defaultdict(list)
        self.store = store

    def subscribe(self, event_type, callback):
        self.listeners[event_type].append(callback)

    def emit(self, event_type, data=None):
        pass

        event = {
            "id": str(uuid.uuid4()),
            "type": event_type,
            "data": data,
            "ts": time.time()
        }

        print(f"[EVENTO] {event_type}: {data}")

        # ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¥ PERSISTÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â NCIA
        self.store.append(event)

        self.queue.append(event)


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
                cb(event)


# =========================
# MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œDULOS
# =========================

class AuthModule:
    def __init__(self, bus: EventBus, state: StateManager):
        self.bus = bus
        self.state = state

    def start(self):
        self.bus.subscribe("login_request", self.login)

    def login(self, event):
        user = event["data"]

        if not self.state.state["logged_in"]:
            print(f"[AUTH] login {user}")
            self.state.state["logged_in"] = True
            self.state.state["active_user"] = user

            self.bus.emit("login_success", user)
        else:
            print("[AUTH] jÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ logado")


class LoggerModule:
    def __init__(self, bus: EventBus):
        self.bus = bus

    def start(self):
        self.bus.subscribe("login_success", self.log)

    def log(self, event):
        print(f"[LOG] usuÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio autenticado: {event['data']}")


class APIModule:
    def __init__(self, bus: EventBus):
        self.bus = bus
        self.running = True

    def start(self):
        Thread(target=self.run, daemon=True).start()

    def run(self):
        count = 0

        while count < 3:  # ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¥ LIMITA EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O REAL
            time.sleep(2)
            self.bus.emit("login_request", "user123")
            count += 1

        print("[API] finalizou geraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de eventos")


# =========================
# START SYSTEM
# =========================

if __name__ == "__main__":
    pass

    print("\n==============================")
    print("NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO V8 - PERSISTENCE SYSTEM")
    print("==============================\n")

    store = EventStore()
    state = StateManager()
    bus = EventBus(store)

    auth = AuthModule(bus, state)
    logger = LoggerModule(bus)
    api = APIModule(bus)

    worker = Worker(bus)

    auth.start()
    logger.start()
    api.start()
    worker.start()

    print("\n[SISTEMA] rodando com persistÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia...\n")

    while True:
        time.sleep(1)




