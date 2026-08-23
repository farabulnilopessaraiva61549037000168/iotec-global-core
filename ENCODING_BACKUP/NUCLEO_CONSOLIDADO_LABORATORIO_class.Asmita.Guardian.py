import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
class AsmitaGuardian:
    def __init__(self):
        self.active = False
        self.watchdog = Watchdog(self.restart)
        self.sensory_field = SensoryField()
        self.protection_mode = True

    def start(self):
        self.active = True
        self.watchdog.start()
        self.sensory_field.activate()

    def restart(self):
        if not self.active:
            self.start()

    def monitor_processes(self):
        while self.active:
            for proc in get_all_system_processes():
                if self.detect_intrusion(proc):
                    self.activate_isolation(proc)
            sleep(0.5)

    def detect_intrusion(self, proc):
        # Algoritmo de detecÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o baseado em IA + padrÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes assinados
        return self.sensory_field.scan(proc)

    def activate_isolation(self, proc):
        self.protection_mode = True
        proc.terminate()
        log_event(f"AsmitÃƒÆ'Ã¢â‚¬Å¾Ãƒâ€šÃ‚Â isolou processo suspeito: {proc.pid}")

    def shutdown_attempt(self):
        # Detecta tentativa de desligar Asmita e reinicia
        if not self.active:
            self.restart()

# InicializaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o na raiz
asmita = AsmitaGuardian()
asmita.start()
asmita.monitor_processes()


