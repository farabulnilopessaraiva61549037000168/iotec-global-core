import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# Painel replicador - mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulo base
class PainelReplicador:
    def __init__(self):
        self.modos = []
        self.painel_atual = None

    def registrar_painel(self, painel):
        self.modos.append(painel)

    def ativar_painel(self, nome_painel):
        for painel in self.modos:
            if painel.nome == nome_painel:
                self.painel_atual = painel
                painel.exibir()

    def alternar(self):
        # Alterna entre painÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©is automaticamente (modo dinÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢mico)
        for painel in self.modos:
            painel.exibir()

# Exemplo de uso
if __name__ == "__main__":
    painel = PainelReplicador()
    # painÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©is importados de outras camadas, ex: IO, Cidade, Torre


