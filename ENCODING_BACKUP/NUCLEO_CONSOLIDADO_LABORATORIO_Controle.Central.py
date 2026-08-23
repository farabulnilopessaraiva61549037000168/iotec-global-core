import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# Torre de Controle Central - integra tudo
class TorreControle:
    def __init__(self, io, minerador, painel):
        self.io = io
        self.minerador = minerador
        self.painel = painel

    def iniciar_complexo(self):
        print(self.io.apresentar())
        self.minerador.escavar()
        self.painel.alternar()

# ComposiÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o do sistema
if __name__ == "__main__":
    io = IO()
    minerador = MineradorDigital()
    painel = PainelReplicador()
    torre = TorreControle(io, minerador, painel)
    torre.iniciar_complexo()



