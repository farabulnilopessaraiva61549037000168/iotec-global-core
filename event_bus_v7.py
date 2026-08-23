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
# SESSION MANAGER
# =========================

class SessionManager:
    def __init__(self):
        self.active = False
        self.user = None
        self.login_attempts = 0
        self.max_attempts = 3

    def start_session(self, user):
        self.active = True
        self.user = user
        self.login_attempts = 0
        print(f"[SESSION] iniciada para {user}")

    def close_session(self):
        print("[SESSION] encerrada")
        self.active = False
        self.user = None

    def can_emit(self):
        return self.active and self.login_attempts < self.max_attempts


# =========================
# EVENT BUS
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
            "data": data,
            "status": "CREATED"
        }

        print(f"[ENQUEUE] {event_type}: {data}")
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
            event["status"] = "PROCESSING"

            print(f"[PROCESSANDO] {event['type']} -> {event['data']}")

            for cb in self.bus.listeners[event["type"]]:
                cb(event)

            event["status"] = "DONE"
            print(f"[FINALIZADO] {event['type']}")


# =========================
# MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œDULOS
# =========================

class AuthModule:
    def __init__(self, bus: EventBus, session: SessionManager):
        self.bus = bus
        self.session = session

    def start(self):
        self.bus.subscribe("login_request", self.login)

    def login(self, event):
        user = event["data"]

        if not self.session.active:
            self.session.start_session(user)

        print(f"[AUTH] login {user}")

        self.session.login_attempts += 1

        self.bus.emit("login_success", user)

        if self.session.login_attempts >= self.session.max_attempts:
            self.session.close_session()


class LoggerModule:
    def __init__(self, bus: EventBus):
        self.bus = bus

    def start(self):
        self.bus.subscribe("login_success", self.log)

    def log(self, event):
        print(f"[LOG] usuÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio autenticado: {event['data']}")


class APIModule:
    def __init__(self, bus: EventBus, session: SessionManager):
        self.bus = bus
        self.session = session

    def start(self):
        Thread(target=self.run, daemon=True).start()

    def run(self):
        while True:
            time.sleep(2)

            # ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¥ CLOSED LOOP RULE
            if self.session.can_emit():
                self.bus.emit("login_request", "user123")
            else:
                print("[API] sessÃƒÆ'Ã†â€™o encerrada ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ parando geraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o")
                break


# =========================
# START
# =========================

if __name__ == "__main__":
    pass

    print("\n==============================")
    print("NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO V7 - CLOSED LOOP SYSTEM")
    print("==============================\n")

    bus = EventBus()
    session = SessionManager()

    auth = AuthModule(bus, session)
    logger = LoggerModule(bus)
    api = APIModule(bus, session)

    worker = Worker(bus)

    auth.start()
    logger.start()
    api.start()
    worker.start()

    print("\n[SISTEMA] rodando com ciclo fechado...\n")

    while True:
        time.sleep(1)




