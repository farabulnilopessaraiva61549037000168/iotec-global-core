import sys
import requests

print("=" * 65)
print("     📡 IOTEC - AUDITORIA DE COMUNICAÇÃO INTERNA")
print("=" * 65)

# 1. Teste de Leitura da Memória do Núcleo
try:
    from core_memory import INSTITUICAO, CESTA_PRODUTOS, RAMOS_ATUACAO
    print("✅ [1/3] Memória do Núcleo (core_memory.py): CONECTADA")
    print(f"      Empresa: {INSTITUICAO['nome_fantasia']} | CNPJ: {INSTITUICAO['cnpj']}")
    print(f"      Ramos Mapeados: {len(RAMOS_ATUACAO)} | Produtos na Cesta: {len(CESTA_PRODUTOS)}")
except Exception as e:
    print(f"❌ [1/3] Falha na Memória do Núcleo: {e}")

# 2. Teste de Conexão com o Backend Local
url_local = "http://127.0.0.1:5000/api/estado-operacoes"
try:
    resp = requests.get(url_local, timeout=3)
    if resp.status_code == 200:
        print("✅ [2/3] Comunicação com Servidor Local (app.py): ATIVA (Porta 5000)")
    else:
        print(f"⚠️ [2/3] Servidor Local respondeu com status {resp.status_code}")
except Exception as e:
    print("⚠️ [2/3] Servidor Local (app.py) não está rodando nesta máquina no momento.")

# 3. Teste de Endpoint de Negociação/Presidência na Nuvem
url_presidencia = "https://iotec-platform-1.onrender.com/presidencia"
try:
    resp_nuvem = requests.get(url_presidencia, timeout=10)
    if resp_nuvem.status_code == 200:
        print("✅ [3/3] Sinal da Nuvem (Render /presidencia): OPERACIONAL 24/7")
    else:
        print(f"⚠️ [3/3] Render respondeu com status: {resp_nuvem.status_code}")
except Exception as e:
    print(f"❌ [3/3] Falha de conexão com a Nuvem Render: {e}")

print("=" * 65)