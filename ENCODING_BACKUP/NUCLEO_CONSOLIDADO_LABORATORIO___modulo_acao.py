import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# modulo_acao.py

class Executor:
    def __init__(self):
        self.log = []

    def executar(self, tarefa):
        print(f"[Executor] Executando: {tarefa}")
        self.log.append(tarefa)
        return f"Tarefa '{tarefa}' concluÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­da."


