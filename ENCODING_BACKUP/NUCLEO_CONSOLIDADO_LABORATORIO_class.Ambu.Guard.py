import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
class AmbuGuard:
    def __init__(self, system):
        self.system = system
        self.logs = []

    def monitor_failures(self):
        if self.system.detect_anomaly():
            self.trigger_emergency_protocol()

    def trigger_emergency_protocol(self):
        self.deploy_scrolls()
        self.activate_cloaking()
        self.system.restore_last_stable_state()

    def deploy_scrolls(self):
        print("Enviando pergaminhos ocultos para as aldeias conectadas...")

    def activate_cloaking(self):
        print("Sistema estÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ agora sob manto de sombra. IPs rastreadores bloqueados.")


