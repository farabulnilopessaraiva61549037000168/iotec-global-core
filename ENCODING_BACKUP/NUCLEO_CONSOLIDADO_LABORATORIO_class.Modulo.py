import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
class Modulo:
    def __init__(self, nome, funcao):
        self.nome = nome
        self.funcao = funcao

class NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂºcleoOrganizador:
    def __init__(self):
        self.matriz = {}  # Guarda mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulos organizados

    def agregar(self, modulo):
        if modulo.funcao in self.matriz:
            print(f"[FUSÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O] {modulo.nome} se funde a {self.matriz[modulo.funcao].nome}.")
            self.matriz[modulo.funcao].nome += f"+{modulo.nome}"
        else:
            print(f"[ADICIONADO] {modulo.nome} com funÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o {modulo.funcao} foi adicionado.")
            self.matriz[modulo.funcao] = modulo

    def exibir_matriz(self):
        print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â [MATRIZ ORGANIZACIONAL ATUAL]")
        for funcao, modulo in self.matriz.items():
            print(f" - {modulo.nome} ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ {funcao}")

# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¥ SimulaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o
if __name__ == "__main__":
    nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo = NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂºcleoOrganizador()

    # Simulando chegada de mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulos
    mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulos = [
        Modulo("Scanner Alpha", "Varredura"),
        Modulo("Scanner Beta", "Varredura"),
        Modulo("Executor Prime", "AÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o"),
        Modulo("Executor Omega", "AÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o"),
        Modulo("RelatorioX", "RelatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rios"),
        Modulo("GeradorZ", "RelatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rios"),
        Modulo("FirewallX", "SeguranÃƒÆ'Ã†â€™a"),
    ]

    for m in mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulos:
        nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo.agregar(m)

    nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo.exibir_matriz()


