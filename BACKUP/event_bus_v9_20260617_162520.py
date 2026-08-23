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
import os
from threading import Thread
from collections import deque, defaultdict

LOG_FILE = "event_log.json"

logging.basicConfig(
    filename="core.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# =========================
# STATE MANAGER
# =========================

class StateManager:
    def __init__(self):
        self.state = {
            "logged_in": False,
            "active_user": None
        }

    def rebuild_from_event(self, event):
        if event["type"] == "login_success":
            self.state["logged_in"] = True
            self.state["active_user"] = event["data"]


# =========================
# EVENT STORE
# =========================

class EventStore:
    def __init__(self, file=LOG_FILE):
        self.file = file
        self.events = self.load()

    def load(self):
        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                try:
                    return json.load(f)
                except:
                    return []
        return []

    def append(self, event):
        self.events.append(event)
        self.save()

    def save(self):
        with open(self.file, "w") as f:
            json.dump(self.events, f, indent=2)


# =========================
# RECOVERY ENGINE
# =========================

class RecoveryEngine:
    def __init__(self, store: EventStore, state: StateManager):
        self.store = store
        self.state = state

    def rebuild(self):
        print("\n[RECOVERY] reconstruindo sistema...\n")

        for event in self.store.events:
            print(f"[REPLAY] {event['type']}")

            self.state.rebuild_from_event(event)

        print("\n[RECOVERY] estado reconstruÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­do")
        print(f"[STATE] {self.state.state}\n")


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

            for cb in self.bus.listeners[event["type"]]:
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
        print(f"[LOG] usuÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio: {event['data']}")


class APIModule:
    def __init__(self, bus: EventBus):
        self.bus = bus

    def start(self):
        Thread(target=self.run, daemon=True).start()

    def run(self):
        for _ in range(2):
            time.sleep(2)
            self.bus.emit("login_request", "user123")

        print("[API] terminou execuÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o")


# =========================
# START SYSTEM
# =========================

if __name__ == "__main__":
    pass

    print("\n==============================")
    print("NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO V9 - RECOVERY SYSTEM")
    print("==============================\n")

    store = EventStore()
    state = StateManager()

    recovery = RecoveryEngine(store, state)
    recovery.rebuild()

    bus = EventBus(store)

    auth = AuthModule(bus, state)
    logger = LoggerModule(bus)
    api = APIModule(bus)

    worker = Worker(bus)

    auth.start()
    logger.start()
    api.start()
    worker.start()

    print("\n[SISTEMA] rodando com RECOVERY ativo...\n")

    while True:
        time.sleep(1)


