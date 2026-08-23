import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

class EmpresaFinanceiro:
    def __init__(self, nome_empresa, caixa_inicial=0.0, caixa_minimo=0.0):
        self.nome = nome_empresa
        self.caixa = float(caixa_inicial)
        self.caixa_minimo = float(caixa_minimo)
        self.livro_movimentacoes = []
        self.prolabore_valor = 0.0

    def registrar_entrada(self, valor, descricao):
        valor = float(valor)
        self.caixa += valor
        self.livro_movimentacoes.append(
            {"tipo": "entrada", "valor": valor, "descricao": descricao}
        )

    def registrar_saida(self, valor, descricao):
        valor = float(valor)
        if valor > self.caixa:
            raise ValueError("Saldo insuficiente no caixa da empresa.")
        self.caixa -= valor
        self.livro_movimentacoes.append(
            {"tipo": "saÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­da", "valor": valor, "descricao": descricao}
        )

    def definir_prolabore(self, valor):
        self.prolabore_valor = float(valor)

    def pagar_prolabore(self):
        if self.prolabore_valor <= 0:
            raise ValueError("Prolabore nÃƒÆ'Ã†â€™o definido.")
        if self.caixa - self.prolabore_valor < self.caixa_minimo:
            raise ValueError("Pagamento de prÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³-labore violaria o caixa mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­nimo.")
        self.registrar_saida(self.prolabore_valor, "PrÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³-labore do sÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³cio")
        return True

    def gerar_relatorio(self):
        rel = {
            "empresa": self.nome,
            "saldo_caixa": self.caixa,
            "caixa_minimo": self.caixa_minimo,
            "movimentacoes": self.livro_movimentacoes,
            "prolabore_atual": self.prolabore_valor,
        }
        return rel


