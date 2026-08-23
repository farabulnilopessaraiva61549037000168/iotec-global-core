import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

import random
from datetime import datetime

class MineradorDigital:
    def __init__(self):
        self.fontes = ['superfÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­cie', 'subsolo', 'oceano_digital', 'ar_digital']
        self.coleta_diaria = {}
        self.taxa_imposto = 0.25  # 25%

    def simular_coleta(self):
        print(f"\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¡ Coleta iniciada - {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        for fonte in self.fontes:
            bruto = round(random.uniform(500, 20000), 2)  # SimulaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de valor bruto por fonte
            imposto = round(bruto * self.taxa_imposto, 2)
            liquido = round(bruto - imposto, 2)
            self.coleta_diaria[fonte] = {
                'bruto': bruto,
                'imposto': imposto,
                'liquido': liquido
            }

    def relatorio_do_dia(self):
        total_bruto = sum(v['bruto'] for v in self.coleta_diaria.values())
        total_liquido = sum(v['liquido'] for v in self.coleta_diaria.values())
        print(f"\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO DE MINERAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DIGITAL:")
        for fonte, dados in self.coleta_diaria.items():
            print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â Fonte: {fonte.upper()}")
            print(f"   - Bruto: R$ {dados['bruto']}")
            print(f"   - Imposto: R$ {dados['imposto']}")
            print(f"   - LÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­quido: R$ {dados['liquido']}\n")
        print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â TOTAL BRUTO: R$ {round(total_bruto,2)}")
        print(f"ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ TOTAL LÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂQUIDO: R$ {round(total_liquido,2)}")

# EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
if __name__ == "__main__":
    sistema = MineradorDigital()
    sistema.simular_coleta()
    sistema.relatorio_do_dia()


