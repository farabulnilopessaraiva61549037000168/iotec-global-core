import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
class Processo:
    pass

    def __init__(self):
        self.status = "INICIADO"

    def pagamento_confirmado(self):
        self.status = "PAGAMENTO_CONFIRMADO"

    def processar(self):
        self.status = "EM_PROCESSAMENTO"

    def validar(self, completo):
        if completo:
            self.status = "APROVADO"
        else:
            self.status = "INCOMPLETO"

    def liberar(self):
        if self.status == "APROVADO":
            self.status = "LIBERADO"


