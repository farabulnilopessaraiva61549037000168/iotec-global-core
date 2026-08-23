import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# guardiao_pai.py

from datetime import datetime, timedelta
import time

class GuardiaoPAI:
    def __init__(self, tempo_espera_horas=48):
        self.ultima_interacao = datetime.now()
        self.tempo_espera = timedelta(hours=tempo_espera_horas)
        self.modo_emergencia = False
        self.status = "Ativo"
        self.log = []

    def registrar_interacao(self):
        self.ultima_interacao = datetime.now()
        self.log.append(f"[{self.ultima_interacao}] InteraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o registrada.")
        print("[GUARDIÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O] InteraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o registrada com o Idealizador.")

    def monitorar_ausencia(self):
        tempo_ausente = datetime.now() - self.ultima_interacao
        if tempo_ausente > self.tempo_espera and not self.modo_emergencia:
            self.ativar_protocolo_de_emergencia()
        else:
            print(f"[GUARDIÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O] Tempo ausente: {tempo_ausente}. Dentro do limite de seguranÃƒÆ'Ã†â€™a.")

    def ativar_protocolo_de_emergencia(self):
        self.modo_emergencia = True
        self.status = "Modo de ContingÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia"
        self.log.append(f"[{datetime.now()}] AUSÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â NCIA PROLONGADA DETECTADA. Protocolo ativado.")
        print("\n[ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â GUARDIÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O PAI] MODO EMERGÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â NCIA ATIVADO")
        self.executar_acoes_de_contingencia()

    def executar_acoes_de_contingencia(self):
        print("[AÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O] Resguardando sistema, protegendo ativos, comunicando autoridades designadas.")
        self.gerar_voz_simulada()
        self.garantir_integridade_financeira()
        self.notificar_herdeiro_designado()

    def gerar_voz_simulada(self):
        print("[VOZ] 'OlÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡, este ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© o GuardiÃƒÆ'Ã†â€™o PAI. O idealizador estÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ ausente. Medidas seguras estÃƒÆ'Ã†â€™o sendo adotadas.'")

    def garantir_integridade_financeira(self):
        print("[FINANCEIRO] Contas protegidas. TransaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes suspensas atÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© novo comando vÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lido.")

    def notificar_herdeiro_designado(self):
        print("[CONTATO] Herdeiro ou operador secundÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio notificado conforme protocolo interno.")

    def gerar_log(self):
        print("\n[ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã…Â¾ LOG DE EVENTOS]")
        for evento in self.log:
            print(evento)


