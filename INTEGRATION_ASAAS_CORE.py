import json
import datetime

class AsaasCoreIntegration:
    def __init__(self):
        self.cnpj = "61.549.037/0001-68"
        self.owner = "FARABULINI LOPES SARAIVA"
        self.config_path = "asaas_credentials.json"

    def set_api_key(self, api_key):
        data = {
            "cnpj": self.cnpj,
            "owner": self.owner,
            "asaas_api_key": api_key,
            "status": "CONFIGURED",
            "updated_at": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print("==========================================================================================")
        print(" 💳  IOTEC ASAAS ENGINE | CHAVE DE INTEGRACAO NACIONAL CONECTADA                           ")
        print("==========================================================================================")
        print(f" [CNPJ BENEFICIÁRIO : {self.cnpj}]")
        print(f" [TITULAR           : {self.owner}]")
        print(f" [STATUS CONEXÃO    : ATIVA (Boletos/PIX/Antecipação)]")
        print("==========================================================================================")

if __name__ == "__main__":
    asaas = AsaasCoreIntegration()
    # Token temporario aguardando o colar da chave oficial
    asaas.set_api_key("$aact_Ydac951d283...PENDING_OFFICIAL_KEY")
