import json
import datetime

class RemessaCoreIntegration:
    def __init__(self):
        self.cnpj = "61.549.037/0001-68"
        self.owner = "FARABULINI LOPES SARAIVA"
        self.config_path = "remessa_credentials.json"

    def setup_account_data(self, currency, iban, swift, routing_number, account_number):
        data = {
            "cnpj": self.cnpj,
            "owner": self.owner,
            "currency": currency,
            "iban": iban,
            "swift": swift,
            "routing_number": routing_number,
            "account_number": account_number,
            "updated_at": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            
        print("==========================================================================================")
        print(f" 🌍  IOTEC CROSS-BORDER CORE | DADOS DE LIQUIDAÇÃO REGISTRADOS ({currency})              ")
        print("==========================================================================================")
        print(f" [CNPJ BENEFICIÁRIO : {self.cnpj}]")
        print(f" [TITULAR           : {self.owner}]")
        print(f" [MOEDA SELECIONADA : {currency}]")
        print(f" [IBAN / CONTA      : {iban}]")
        print(f" [SWIFT / BIC       : {swift}]")
        print("==========================================================================================")
        print(" ✅ DADOS CONECTADOS AO NÚCLEO DA IOTEC PARA CONVERSÃO AUTOMÁTICA EM REAIS.")
        print("==========================================================================================")

if __name__ == "__main__":
    core = RemessaCoreIntegration()
    # Dados de modelo para inicialização do módulo no core
    core.setup_account_data(
        currency="USD",
        iban="US00REMESSAONLINE0000001",
        swift="REMBBRSPXXX",
        routing_number="026073150",
        account_number="61549037000168"
    )
