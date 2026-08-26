import os
import sys
import requests

def configurar_asaas():
    print("===============================================================================")
    print(" 💳 CONFIGURAÇÃO DE CAIXA REAL — ASAAS (PIX / BOLETO)")
    print("===============================================================================")
    cliente_id = input("INSERIR ID CLIENTE ASAAS > ").strip()
    if not cliente_id:
        print(" [!] ID do Cliente não fornecido. Pulo da etapa Asaas.\n")
        return None, None
    
    token = input("INSERIR TOKEN ASAAS > ").strip()
    if not token:
        print(" [!] Token não fornecido. Pulo da etapa Asaas.\n")
        return None, None

    # Teste de conexão real via API do Asaas
    headers = {"access_token": token}
    try:
        res = requests.get("https://www.asaas.com/api/v3/finance/balance", headers=headers, timeout=10)
        if res.status_code == 200:
            saldo = res.json().get("balance", 0.0)
            print(f" [🟢 CONEXÃO SUCESSO] Asaas Autenticado! Saldo Atual: R$ {saldo:,.2f}\n")
            return cliente_id, token
        else:
            print(f" [❌ FALHA DE AUTENTICAÇÃO ASAAS] Resposta do Servidor: {res.status_code}\n")
            return None, None
    except Exception as e:
        print(f" [❌ ERRO DE CONEXÃO] Não foi possível contatar o Asaas: {e}\n")
        return None, None

def configurar_remessa():
    print("===============================================================================")
    print(" 🌐 CONFIGURAÇÃO DE CAIXA REAL — REMESSA ONLINE (PAGAMENTOS INTERNACIONAIS)")
    print("===============================================================================")
    cliente_id = input("INSERIR ID CLIENTE REMESSA.COM > ").strip()
    if not cliente_id:
        print(" [!] ID do Cliente não fornecido. Pulo da etapa Remessa.com.\n")
        return None, None
    
    token = input("INSERIR TOKEN REMESSA.COM > ").strip()
    if not token:
        print(" [!] Token não fornecido. Pulo da etapa Remessa.com.\n")
        return None, None

    print(f" [🟢 CREDENCIAIS REGISTRADAS] Remessa.com vinculado ao ID {cliente_id}\n")
    return cliente_id, token

if __name__ == "__main__":
    asaas_id, asaas_token = configurar_asaas()
    remessa_id, remessa_token = configurar_remessa()

    # Persistência local segura para os Daemons de Produção
    env_content = f"""# CREDENCIAIS DE CAIXA REAL - FARABULINI LOPES SARAIVA
ASAAS_CLIENT_ID={asaas_id or ''}
ASAAS_API_KEY={asaas_token or ''}
REMESSA_CLIENT_ID={remessa_id or ''}
REMESSA_API_KEY={remessa_token or ''}
"""
    with open("C:\\IOTEC\\.env", "w", encoding="utf-8") as f:
        f.write(env_content)

    print("===============================================================================")
    print(" 🛡️ INTEGRALIZAÇÃO CONCLUÍDA")
    print("===============================================================================")
    print(" [✔] As credenciais ativas foram salvas em C:\\IOTEC\\.env")
    print(" [✔] O sistema IOTEC agora usará cobranças bancárias autênticas.")
    print("===============================================================================\n")
