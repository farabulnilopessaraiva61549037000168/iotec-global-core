import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import time
import logging
from threading import Thread

logging.basicConfig(
    filename='core.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

# =========================
# MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œDULO BASE
# =========================

class BaseModule:
    def __init__(self, name):
        self.name = name
        self.running = False
        self.fail_count = 0
        self.state = "STOPPED"  # ONLINE / DEGRADED / FAILED / ISOLATED

    def start(self):
        self.running = True
        self.state = "ONLINE"
        logging.info(f"{self.name} iniciado")

    def stop(self):
        self.running = False
        self.state = "STOPPED"
        logging.warning(f"{self.name} parado")

    def fail(self):
        self.fail_count += 1

        if self.fail_count >= 3:
            self.state = "ISOLATED"
        else:
            self.state = "DEGRADED"

    def health(self):
        return self.running


# =========================
# ORQUESTRADOR
# =========================

class Orchestrator:
    def __init__(self):
        self.modules = []

    def register(self, module):
        self.modules.append(module)
        logging.info(f"Registrado: {module.name}")
        print(f"[REGISTRO] {module.name}")

    def start_all(self):
        for m in self.modules:
            try:
                m.start()
                print(f"[START] {m.name}")
            except Exception as e:
                logging.error(f"Erro start {m.name}: {e}")

    def restart_module(self, module):
        if module.state == "ISOLATED":
            print(f"[BLOQUEADO] {module.name} isolado (nÃƒÆ'Ã†â€™o reinicia)")
            return

        try:
            module.start()
            module.fail_count = 0
            print(f"[RECOVERY] {module.name} reiniciado")
        except Exception as e:
            logging.error(f"Erro restart {module.name}: {e}")

    def healthcheck(self):
        while True:
            for m in self.modules:
                try:
                    if m.health():
                        print(f"[OK] {m.name} ONLINE")
                        m.state = "ONLINE"
                    else:
                        m.fail()

                        print(f"[FALHA] {m.name} estado: {m.state}")
                        logging.warning(f"{m.name} falhou ({m.fail_count})")

                        self.restart_module(m)

                except Exception as e:
                    logging.error(f"Erro health {m.name}: {e}")

            time.sleep(5)


# =========================
# MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œDULOS EXEMPLO
# =========================

class AuthModule(BaseModule):
    pass

class DatabaseModule(BaseModule):
    pass

class APIModule(BaseModule):
    pass


# =========================
# START
# =========================

if __name__ == "__main__":
    pass

    print("\n==============================")
    print("NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO V2 - FAILSAFE SYSTEM")
    print("==============================\n")

    orch = Orchestrator()

    orch.register(AuthModule("AUTH"))
    orch.register(DatabaseModule("DATABASE"))
    orch.register(APIModule("API"))

    orch.start_all()

    Thread(target=orch.healthcheck, daemon=True).start()

    print("\n[SISTEMA] Rodando com controle de falhas...\n")

    while True:
        time.sleep(1)


