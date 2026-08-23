import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
class ComplexoDigital:
    def __init__(self):
        self.nome = "Complexo IO ÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Âmega"
        self.estagios = ["superfÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­cie", "subsolo", "mares de dados", "cÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©us digitais"]
        self.mineracao = {
            "tipo": "multi-dimensional",
            "camadas": self.estagios,
            "metodo": "captura inteligente de dados em tempo real",
            "automacao": True
        }
        self.fiscalizacao = {
            "modo": "transparente",
            "imposto_percentual": 25,
            "relatorio_mensal": True
        }
        self.economia = {
            "ganhos_brutos": 0,
            "imposto_pago": 0,
            "lucro_liquido": 0
        }

    def processar_fluxo(self, ganho_bruto_dia):
        imposto = ganho_bruto_dia * (self.fiscalizacao["imposto_percentual"] / 100)
        liquido = ganho_bruto_dia - imposto
        self.economia["ganhos_brutos"] += ganho_bruto_dia
        self.economia["imposto_pago"] += imposto
        self.economia["lucro_liquido"] += liquido

    def relatorio_desenvolvimento_autonomia(self):
        print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO DE DESENVOLVIMENTO E AUTONOMIA:")
        print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¹ Nome do Complexo: {self.nome}")
        print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¹ EstÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡gios Operacionais: {', '.join(self.estagios)}")
        print(f"ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Tipo de MineraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o: {self.mineracao['tipo']}")
        print(f"ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â MÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©todo de MineraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o: {self.mineracao['metodo']}")
        print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã…Â¾ AutomaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o: {'Ativada' if self.mineracao['automacao'] else 'Desativada'}")
        print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¹Ã¢â‚¬Â  Modo de FiscalizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o: {self.fiscalizacao['modo']}")
        print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢Ãƒâ€šÃ‚Â° Imposto Percentual: {self.fiscalizacao['imposto_percentual']}%")
        print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  Economia Atual:")
        for chave, valor in self.economia.items():
            print(f"   - {chave.replace('_', ' ').title()}: R$ {valor:,.2f}")

if __name__ == "__main__":
    IO_OMEGA = ComplexoDigital()

    # Exemplo de captaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de R$180.000 em um dia tÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­pico
    IO_OMEGA.processar_fluxo(180_000)
    IO_OMEGA.relatorio_desenvolvimento_autonomia()


