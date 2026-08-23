import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# DNA Digital e Chakras Financeiros - MÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulo base

class DNA_Digital:
    def __init__(self):
        # Cada nucleotÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­deo representa um cÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³digo funcional no sistema
        self.genoma = []  # lista de nucleotÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­deos/cÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³digos
        self.mutacoes = 0

    def adicionar_nucleotideo(self, codigo):
        self.genoma.append(codigo)
        print(f"NucleotÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­deo {codigo} adicionado ao DNA digital.")

    def mutacionar(self, indice, novo_codigo):
        if 0 <= indice < len(self.genoma):
            antigo = self.genoma[indice]
            self.genoma[indice] = novo_codigo
            self.mutacoes += 1
            print(f"NucleotÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­deo {indice} mutado de {antigo} para {novo_codigo}.")
        else:
            print("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Ândice fora do alcance do DNA digital.")

    def mostrar_dna(self):
        return "->".join(self.genoma)


class ChakraFinanceiro:
    def __init__(self):
        self.reservatorio_grande = 100000.0  # reserva maior, tipo caixa mestre
        self.reservatorio_menor = 5000.0     # reserva menor para operaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes rÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡pidas

    def usar_reserva_menor(self, valor):
        if valor <= self.reservatorio_menor:
            self.reservatorio_menor -= valor
            print(f"Usado {valor} da reserva menor. Restam {self.reservatorio_menor}.")
        else:
            print("Reserva menor insuficiente, tentando usar da reserva grande.")
            self.usar_reserva_maior(valor)

    def usar_reserva_maior(self, valor):
        if valor <= self.reservatorio_grande:
            self.reservatorio_grande -= valor
            print(f"Usado {valor} da reserva grande. Restam {self.reservatorio_grande}.")
        else:
            print("Reserva grande insuficiente para essa operaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o.")

    def mostrar_reservatorios(self):
        return {
            "reservatorio_grande": self.reservatorio_grande,
            "reservatorio_menor": self.reservatorio_menor
        }


# Teste inicial

dna = DNA_Digital()
dna.adicionar_nucleotideo("Hashirama")
dna.adicionar_nucleotideo("ÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Âmega")
dna.adicionar_nucleotideo("Bifrost")

print("DNA atual:", dna.mostrar_dna())

chakra = ChakraFinanceiro()
chakra.usar_reserva_menor(2000)
chakra.usar_reserva_menor(4000)
chakra.usar_reserva_maior(50000)

print("ReservatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rios:", chakra.mostrar_reservatorios())


