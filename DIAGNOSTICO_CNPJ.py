import requests
import json
import os

CNPJ = "61549037000168"
RAZAO_SOCIAL = "FARABULINI LOPES SARAIVA"
TOKEN_PATH = r"C:\IOTEC\token.txt"

print("===================================================================")
print(f" 🛡️  DIAGNOSTICO DE CREDENCIAIS CNPJ: {CNPJ}")
print("===================================================================")

# 1. Verifica o token atualmente salvo no arquivo local
if os.path.exists(TOKEN_PATH):
    with open(TOKEN_PATH, 'r', encoding='utf-8') as f:
        token_atual = f.read().strip()
    
    print(f"--> Analisando token.txt atual (Tamanho: {len(token_atual)} chars)...")
    
    headers = {
        "access_token": token_atual,
        "Content-Type": "application/json",
        "User-Agent": "IOTEC_DAEMON"
    }
    
    # Teste de resposta em Producao
    try:
        res = requests.get("https://www.asaas.com/api/v3/myAccount", headers=headers, timeout=10)
        if res.status_code == 200:
            dados = res.json()
            print("\n [✔] CONTA LOCALIZADA E CHAVE ATIVA!")
            print(f"     Nome da Conta: {dados.get('name')}")
            print(f"     Email: {dados.get('email')}")
            print(f"     CPF/CNPJ: {dados.get('cpfCnpj')}")
            print("\n STATUS: Pronto para rodar o DAEMON_VENDAS_AUTONOMO.py!")
            exit(0)
        else:
            print(f" [❌] Producao retornou HTTP {res.status_code}: {res.text}")
    except Exception as e:
        print(f" [❌] Erro de conexao: {e}")

# 2. Instrucoes de acionamento do suporte para desbloqueio do CNPJ
print("\n-------------------------------------------------------------------")
print(" 📌 SOLUÇÃO AUTOMÁTICA PARA LIBERAÇÃO DO CNPJ JA EM USO")
print("-------------------------------------------------------------------")
print(" O CNPJ ja foi cadastrado na base do Asaas. Para recuperar a chave sem")
print(" criar conta nova e manter o CNPJ nas faturas:")
print("\n 1. Envie o e-mail/solicitacao abaixo para o suporte (suporte@asaas.com.br):")
print(f"    Assunto: Recuperacao de Acesso API - CNPJ {CNPJ}")
print(f"    Texto: Solicito redefinicao de acesso e envio da chave de API")
print(f"           para a empresa {RAZAO_SOCIAL} (CNPJ: {CNPJ}).")
print("\n 2. Assim que receber a nova chave, execute este comando no terminal:")
print("    notepad C:\\IOTEC\\token.txt")
print("-------------------------------------------------------------------")
