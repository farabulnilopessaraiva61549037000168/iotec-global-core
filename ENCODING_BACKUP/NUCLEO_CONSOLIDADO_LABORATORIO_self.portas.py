import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

# estrutura_nucleo.py
class NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂºcleoOmega:
    def __init__(self):
        self.guardioes = []
        self.portas_seguras = 3

    def adicionar_guardiao(self, nome):
        self.guardioes.append(nome)

    def status(self):
        return f"NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo com {len(self.guardioes)} guardiÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes e {self.portas_seguras} portas de verificaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o"


