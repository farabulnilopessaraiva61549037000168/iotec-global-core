import sqlite3
import datetime

class EmiratesGlobalModule:
    def __init__(self):
        self.supported_currencies = {
            "BRL": {"symbol": "R$", "rate": 1.0},
            "USD": {"symbol": "$", "rate": 0.18},
            "EUR": {"symbol": "€", "rate": 0.16},
            "AED": {"symbol": "AED", "rate": 0.66}
        }
        self.active_hubs = ["Dubai (EAU)", "Lisboa (EU)", "Miami (USA)", "Singapura (APAC)"]

    def generate_international_certificate(self, company_name, target_hub, currency="USD"):
        curr_data = self.supported_currencies.get(currency, self.supported_currencies["USD"])
        ticket_val = round(299.00 * curr_data["rate"], 2)
        
        cert = f"""
===================================================================================
                IOTEC ENTERPRISE - INTERNATIONAL COMPLIANCE CERTIFICATE
===================================================================================

THIS IS TO CERTIFY that the organization detailed below has been fully cleared 
for automated cloud infrastructure integration within the IOTEC Global Core:

Target Organization : {company_name}
Global Hub / Region : {target_hub}
Status              : ELEGIBLE / ACTIVE 24-7

-----------------------------------------------------------------------------------
 TECHNICAL & FINANCIAL SPECIFICATIONS:
-----------------------------------------------------------------------------------
 • Native Cloud Deployment : Zero local server footprint. Render Cloud 24/7.
 • Rate-Limited Engine     : High-deliverability B2B pipeline.
 • Enterprise Tier         : {curr_data['symbol']} {ticket_val} / month (No lock-in contract).

Issued on {datetime.date.today().strftime('%Y-%m-%d')} under Protocol IOTEC-INT-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.

_____________________________________________________
DIRETORIA DE COMPLIANCE & GLOBAL OPERATIONS - IOTEC
Official Direct Contact: IOTEC.BL@proton.me
===================================================================================
"""
        return cert

if __name__ == "__main__":
    global_engine = EmiratesGlobalModule()
    sample = global_engine.generate_international_certificate("Global Logistics LLC", "Dubai (EAU)", "USD")
    
    with open("CERTIDAO_INTERNACIONAL.txt", "w", encoding="utf-8") as f:
        f.write(sample)
        
    print("======================================================================")
    print(" ✈️ MÓDULO GLOBAL EMIRATES ATIVADO COM SUCESSO                        ")
    print("======================================================================")
    print(" • Hubs Ativos        :", ", ".join(global_engine.active_hubs))
    print(" • Moedas Suportadas  : USD, EUR, AED, BRL")
    print(" • Certidão Exemplo   : Gerada em CERTIDAO_INTERNACIONAL.txt")
    print("======================================================================")
