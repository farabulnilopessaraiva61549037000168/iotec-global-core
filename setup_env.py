import os

# Conteúdo base do arquivo .env para produção
env_content = """# ==========================================
# IOTEC PLATFORM - AMBIENTE DE PRODUÇÃO
# ==========================================

# Módulo 015_PAYMENT_GATEWAY_ENGINE
PAYMENT_ENV=production
PIX_KEY=seu_chave_pix_aqui
PIX_SECRET_TOKEN=seu_token_secret_aqui

# Módulo 099H_PAYPAL_PIX_GATEWAY
PAYPAL_CLIENT_ID=seu_paypal_client_id
PAYPAL_CLIENT_SECRET=seu_paypal_client_secret
PAYPAL_ENV=live

# Módulo 015_AUDIT_ENGINE
AUDIT_LOG_LEVEL=INFO
COMPLIANCE_PCI_MODE=STRICT

# ENTERPRISE_WEB_CORE
WEB_PORT=8080
ALLOWED_HOSTS=*
"""

env_path = "C:\\IOTEC\\.env"

# Cria o arquivo .env se não existir
if not os.path.exists(env_path):
    with open(env_path, "w", encoding="utf-8") as f:
        f.write(env_content)
    print(">>> Arquivo '.env' criado em C:\\IOTEC\\.env!")
    print(">>> Edite as chaves de API reais antes de iniciar as transações.")
else:
    print(">>> Arquivo '.env' já existe em C:\\IOTEC\\.env. Mantido sem alterações.")

print(">>> Verificação de ambiente concluída com sucesso.")
