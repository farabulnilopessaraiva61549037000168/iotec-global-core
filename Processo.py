import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
class Processo:
    pass



    def __init__(self):
        pass

        self.status = "INICIADO"



    def pagamento_confirmado(self):
        pass

        self.status = "PAGAMENTO_CONFIRMADO"



    def processar(self):
        pass

        self.status = "EM_PROCESSAMENTO"



    def validar(self, completo):
        pass

        if completo:
            pass

            self.status = "APROVADO"

        else:
            pass

            self.status = "INCOMPLETO"



    def liberar(self):
        pass

        if self.status == "APROVADO":
            pass

            self.status = "LIBERADO"






