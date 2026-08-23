import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json

class Complexo:
    def __init__(self):
        self.dados = {
            "gestao": {},
            "vendas": {},
            "financeiro": {},
            "clientes": {}
        }

    def adicionar_servico(self, nome, preco, estoque):
        self.dados["gestao"][nome] = {"preco": preco, "estoque": estoque}

    def realizar_venda(self, cliente, servico):
        if servico in self.dados["gestao"]:
            if self.dados["gestao"][servico]["estoque"] > 0:
                self.dados["gestao"][servico]["estoque"] -= 1
                self.dados["vendas"][cliente] = servico
                return f"Venda realizada para {cliente}: {servico}"
            else:
                return "Estoque esgotado!"
        return "ServiÃƒÆ'Ã†â€™o nÃƒÆ'Ã†â€™o encontrado!"

    def ajustar_precos(self):
        for servico, dados in self.dados["gestao"].items():
            demanda = sum(1 for venda in self.dados["vendas"].values() if venda == servico)
            if demanda > 50:
                self.dados["gestao"][servico]["preco"] *= 1.1  # Aumento de 10%
            elif demanda < 10:
                self.dados["gestao"][servico]["preco"] *= 0.9  # ReduÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de 10%
        return "PreÃƒÆ'Ã†â€™os ajustados com base na demanda."

    def gerar_relatorio_financeiro(self):
        relatorio = {
            "total_vendas": len(self.dados["vendas"]),
            "receita": sum(self.dados["gestao"][servico]["preco"] for servico in self.dados["vendas"].values()),
            "impostos": sum(self.dados["gestao"][servico]["preco"] * 0.15 for servico in self.dados["vendas"].values())
        }
        return json.dumps(relatorio, indent=4)

    def salvar_dados(self, arquivo="complexo_dados.json"):
        with open(arquivo, "w") as f:
            json.dump(self.dados, f, indent=4)
        return "Dados salvos com sucesso!"

# Exemplo de uso
sistema = Complexo()
sistema.adicionar_servico("Consultoria Premium", 5000, 100)
sistema.adicionar_servico("Plano AvanÃƒÆ'Ã†â€™ado", 2000, 50)

print(sistema.realizar_venda("Cliente A", "Consultoria Premium"))
print(sistema.ajustar_precos())
print(sistema.gerar_relatorio_financeiro())
print(sistema.salvar_dados())


