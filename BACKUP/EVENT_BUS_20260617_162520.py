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

logging.basicConfig(
    filename='core.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

# =========================
# EVENT BUS
# =========================

class EventBus:
    def __init__(self):
        self.listeners = defaultdict(list)

    def subscribe(self, event_type, callback):
        self.listeners[event_type].append(callback)
        logging.info(f"Listener registrado: {event_type}")

    def emit(self, event_type, data=None):
        logging.info(f"Evento: {event_type} -> {data}")
        print(f"[EVENTO] {event_type}: {data}")

        for callback in self.listeners[event_type]:
            try:
                callback(data)
            except Exception as e:
                logging.error(f"Erro evento {event_type}: {e}")


# =========================
# MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œDULO BASE
# =========================

class BaseModule:
    def __init__(self, name, bus: EventBus):
        self.name = name
        self.bus = bus
        self.running = False

    def start(self):
        self.running = True
        print(f"[START] {self.name}")

    def health(self):
        return self.running


# =========================
# MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œDULOS
# =========================

class AuthModule(BaseModule):
    def start(self):
        super().start()

        self.bus.subscribe("login_request", self.on_login)

    def on_login(self, data):
        print(f"[AUTH] processando login: {data}")
        self.bus.emit("login_success", {"user": data})


class APIModule(BaseModule):
    def start(self):
        super().start()

        # simula evento de entrada
        Thread(target=self.simulate_request, daemon=True).start()

    def simulate_request(self):
        while True:
            time.sleep(7)
            self.bus.emit("login_request", "user123")


class LoggerModule(BaseModule):
    def start(self):
        super().start()

        self.bus.subscribe("login_success", self.log_success)

    def log_success(self, data):
        print(f"[LOG] login confirmado: {data}")


# =========================
# START
# =========================

if __name__ == "__main__":
    pass

    print("\n==============================")
    print("NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO V3 - EVENT SYSTEM")
    print("==============================\n")

    bus = EventBus()

    auth = AuthModule("AUTH", bus)
    api = APIModule("API", bus)
    logger = LoggerModule("LOGGER", bus)

    auth.start()
    api.start()
    logger.start()

    print("\n[SISTEMA] Event-driven ativo...\n")

    while True:
        time.sleep(1)


