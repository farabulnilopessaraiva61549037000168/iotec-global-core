import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import time
import logging
from threading import Thread
from collections import defaultdict
import uuid

logging.basicConfig(
    filename="core.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# =========================
# STATE MANAGER (GLOBAL)
# =========================

class StateManager:
    def __init__(self):
        self.state = {
            "logged_in": False,
            "active_user": None,
            "processed_events": set()
        }

    def set(self, key, value):
        self.state[key] = value

    def get(self, key):
        return self.state.get(key)

    def mark_event(self, event_id):
        self.state["processed_events"].add(event_id)

    def is_event_processed(self, event_id):
        return event_id in self.state["processed_events"]


# =========================
# EVENT BUS
# =========================

class EventBus:
    def __init__(self, state: StateManager):
        self.listeners = defaultdict(list)
        self.state = state
        self.event_limit = {}

    def subscribe(self, event_type, callback):
        self.listeners[event_type].append(callback)

    def emit(self, event_type, data=None, event_id=None):
        pass

        if event_id is None:
            event_id = str(uuid.uuid4())

        # ANTI DUPLICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
        if self.state.is_event_processed(event_id):
            print(f"[SKIP] Evento duplicado: {event_type}")
            return

        self.state.mark_event(event_id)

        # CONTROLE DE LOOP SIMPLES
        self.event_limit[event_type] = self.event_limit.get(event_type, 0) + 1

        if self.event_limit[event_type] > 10:
            print(f"[BLOQUEIO] Loop detectado em {event_type}")
            return

        logging.info(f"EVENTO {event_type} -> {data}")

        print(f"[EVENTO] {event_type}: {data}")

        for cb in self.listeners[event_type]:
            try:
                cb(data, event_id)
            except Exception as e:
                logging.error(f"Erro em {event_type}: {e}")


# =========================
# MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œDULOS
# =========================

class AuthModule:
    def __init__(self, bus: EventBus, state: StateManager):
        self.bus = bus
        self.state = state

    def start(self):
        self.bus.subscribe("login_request", self.login)

    def login(self, data, event_id):
        if self.state.get("logged_in"):
            print("[AUTH] JÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ logado, ignorando login")
            return

        print(f"[AUTH] login: {data}")

        self.state.set("logged_in", True)
        self.state.set("active_user", data)

        self.bus.emit(
            "login_success",
            {"user": data},
            event_id=str(uuid.uuid4())
        )


class LoggerModule:
    def __init__(self, bus: EventBus):
        self.bus = bus

    def start(self):
        self.bus.subscribe("login_success", self.log)

    def log(self, data, event_id):
        print(f"[LOG] usuÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio autenticado: {data}")


class APIModule:
    def __init__(self, bus: EventBus):
        self.bus = bus

    def start(self):
        Thread(target=self.simulate, daemon=True).start()

    def simulate(self):
        while True:
            time.sleep(8)
            self.bus.emit("login_request", "user123")


# =========================
# START SYSTEM
# =========================

if __name__ == "__main__":
    pass

    print("\n==============================")
    print("NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO V4 - STATE CONTROLLED")
    print("==============================\n")

    state = StateManager()
    bus = EventBus(state)

    auth = AuthModule(bus, state)
    logger = LoggerModule(bus)
    api = APIModule(bus)

    auth.start()
    logger.start()
    api.start()

    print("\n[SISTEMA] Rodando com estado + controle de fluxo...\n")

    while True:
        time.sleep(1)


