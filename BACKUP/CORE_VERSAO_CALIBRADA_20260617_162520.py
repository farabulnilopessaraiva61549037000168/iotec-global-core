import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""

IOTEC CORE ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â VERSÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O CALIBRADA (REALISTA)

Autor: Bruno Lopes



Objetivo:

Simular crescimento real de um sistema SaaS com:

- CaptaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o variÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡vel

- ConversÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o limitada

- Ticket controlado

- Receita lÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­quida

- SaturaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o de mercado

"""



import random



class IoTecCore:
    pass



    def __init__(self):
        pass

        self.leads = 0

        self.users = 0

        self.products = 0



        # ParÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢metros calibrados

        self.conversion_rate = 0.02   # 2% inicial

        self.ticket = 30.0            # R$30

        self.max_conversion = 0.10    # 10% teto realista

        self.max_ticket = 50.0        # teto de preÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o



        self.market_limit = 5000      # limite de mercado

        self.cost_fixed = 2000        # custo mensal



        self.revenue = 0

        self.profit = 0



    # ============================

    # CAPTAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O REALISTA

    # ============================

    def capture_data(self):
        pass

        new_leads = random.randint(5, 25)

        self.leads += new_leads



    # ============================

    # PROCESSAMENTO

    # ============================

    def process_data(self):
        pass

        self.products += 1



    # ============================

    # CONVERSÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O REALISTA

    # ============================

    def convert_users(self):
        pass

        potential = int(self.leads * self.conversion_rate)



        # Limite de mercado

        available_space = self.market_limit - self.users

        conversions = min(potential, available_space)



        self.users += conversions



    # ============================

    # MONETIZAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

    # ============================

    def monetize(self):
        pass

        self.revenue = self.users * self.ticket

        self.profit = self.revenue - self.cost_fixed



    # ============================

    # OTIMIZAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O CONTROLADA

    # ============================

    def optimize(self):
        pass

        # crescimento lento e realista

        self.conversion_rate = min(self.conversion_rate * 1.01, self.max_conversion)

        self.ticket = min(self.ticket * 1.005, self.max_ticket)



    # ============================

    # CICLO

    # ============================

    def run_cycle(self):
        pass

        self.capture_data()

        self.process_data()

        self.convert_users()

        self.monetize()

        self.optimize()



    # ============================

    # VALUATION REALISTA

    # ============================

    def calculate_value(self):
        pass

        multiple = 24  # padrÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o SaaS

        return self.profit * multiple



    def report(self):
        pass

        return {

            "leads": self.leads,

            "usuarios": self.users,

            "produtos": self.products,

            "receita": round(self.revenue, 2),

            "lucro": round(self.profit, 2),

            "valuation": round(self.calculate_value(), 2),

            "ticket": round(self.ticket, 2),

            "conversao": round(self.conversion_rate, 4)

        }





# ============================

# EXECUÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

# ============================



if __name__ == "__main__":
    pass



    core = IoTecCore()



    # SimulaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o (100 ciclos)

    for _ in range(100):
        pass

        core.run_cycle()



    print("==== RELATÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"RIO CALIBRADO ====")

    for k, v in core.report().items():
        pass

        print(f"{k}: {v}")




