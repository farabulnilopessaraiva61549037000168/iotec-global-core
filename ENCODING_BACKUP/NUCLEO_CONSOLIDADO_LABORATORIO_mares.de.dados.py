import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# complex_system_init.py
# CÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³digo simbÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³lico para comunicar ao notebook as funÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes do Complexo

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

        print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¡ MineraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o ativa nas camadas: {', '.join(self.estagios)}")
        print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢Ãƒâ€šÃ‚Â° Ganho bruto hoje: R$ {ganho_bruto_dia:,.2f}")
        print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¾ Imposto recolhido: R$ {imposto:,.2f}")
        print(f"ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Lucro lÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­quido retido: R$ {liquido:,.2f}")

    def status(self):
        print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  STATUS ATUAL DO COMPLEXO:")
        for chave, valor in self.economia.items():
            print(f" - {chave.replace('_', ' ').title()}: R$ {valor:,.2f}")

# ExecuÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o simbÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³lica do sistema:
if __name__ == "__main__":
    IO_OMEGA = ComplexoDigital()

    # Exemplo de captaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de R$180.000 em um dia tÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­pico
    IO_OMEGA.processar_fluxo(180_000)
    IO_OMEGA.status()


