import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
Painel Hermes - NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo Financeiro Ambu (ProtÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³tipo Inicial)

Autor: Sistema Ambu

VersÃƒÆ'Ã†â€™o: 1.0 - Matriz de AtivaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o CNPJ + Ciclo Vivo de Receita

import datetime from dataclasses import dataclass

@dataclass class Receita: origem: str valor: float data: datetime.date

@dataclass class Despesa: tipo: str valor: float data: datetime.date

class PainelHermes: def init(self): self.receitas = [] self.despesas = []

def adicionar_receita(self, origem, valor): nova = Receita(origem=origem, valor=valor, data=datetime.date.today()) self.receitas.append(nova) def adicionar_despesa(self, tipo, valor): nova = Despesa(tipo=tipo, valor=valor, data=datetime.date.today()) self.despesas.append(nova) def receita_total(self): return sum(r.valor for r in self.receitas) def despesa_total(self): return sum(d.valor for d in self.despesas) def saldo_atual(self): return self.receita_total() - self.despesa_total() def relatorio(self): print("\n=== RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO DO SISTEMA HERMES ===") print(f"Receita Total: R$ {self.receita_total():,.2f}") print(f"Despesa Total: R$ {self.despesa_total():,.2f}") print(f"Saldo Atual: R$ {self.saldo_atual():,.2f}") print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  LÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³gica do Ciclo: Dados ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Receita ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Reinvestimento ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Dados") if self.saldo_atual() >= 10000: print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ LiberaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o possÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vel: reativar CNPJ antigo e parcelar pendÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncias.") else: print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Aguardando receita mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­nima para destravar operaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes do nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo anterior.")

ExecuÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de Exemplo (simulaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o do sistema)

if name == "main": hermes = PainelHermes() hermes.adicionar_receita("PayPal", 3200) hermes.adicionar_receita("PIX Farabulim", 1800) hermes.adicionar_despesa("Softwares", 800) hermes.adicionar_despesa("Investimento IA", 900) hermes.relatorio()



