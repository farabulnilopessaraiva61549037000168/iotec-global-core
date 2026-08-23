import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# modulo_relatorios.py

class Relatorio:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def gerar(self):
        print("[Relatorio] Gerando relatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio...")
        return "\n".join(self.itens)


