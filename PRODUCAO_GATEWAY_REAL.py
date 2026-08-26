import os
import requests
import json

class GatewayProducaoReal:
    def __init__(self):
        self.asaas_token = os.getenv("ASAAS_API_KEY")
        self.smtp_pass = os.getenv("SMTP_PASSWORD")

    def validar_conexao_caixa(self):
        if not self.asaas_token:
            print("===============================================================================")
            print(" ⚠️ ALERTA DE PRODUÇÃO: CHAVE DE API DO ASAAS NÃO ENCONTRADA!")
            print("===============================================================================")
            print(" [!] Para gerar Pix real, defina a variável no PowerShell:")
            print('     $env:ASAAS_API_KEY="sua_chave_aqui"')
            print("===============================================================================\n")
            return False
        
        headers = {"access_token": self.asaas_token}
        response = requests.get("https://www.asaas.com/api/v3/finance/balance", headers=headers)
        
        if response.status_code == 200:
            saldo = response.json().get("balance", 0.0)
            print("===============================================================================")
            print(" 🟢 CONEXÃO COM CAIXA REAL ESTABELECIDA (ASAAS)")
            print("===============================================================================")
            print(f" ├─ Emissor: Farabulini Lopes Saraiva (CNPJ: 61.549.037/0001-68)")
            print(f" └─ Saldo em Conta Real: R$ {saldo:,.2f}")
            print("===============================================================================\n")
            return True
        else:
            print(f" ❌ FALHA DE AUTENTICAÇÃO COM GATEWAY: {response.text}")
            return False

if __name__ == "__main__":
    gateway = GatewayProducaoReal()
    gateway.validar_conexao_caixa()
