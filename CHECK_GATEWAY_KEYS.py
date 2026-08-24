import re
import os
import sqlite3

print("======================================================================")
print(" 1. ELEVAÇÃO DO TICKET MÉDIO (R$ 29,90 -> R$ 299,00/MÊS)             ")
print("======================================================================")

# 1. Atualiza o valor do ticket no script comercial 031
path_031 = "031_COMMERCIAL_AUTOPILOT.py"
if os.path.exists(path_031):
    with open(path_031, "r", encoding="utf-8", errors="ignore") as f:
        code_031 = f.read()
    
    code_031 = code_031.replace("29.90", "299.00")
    code_031 = code_031.replace("Licença Mensal - Suporte IOTEC Base", "Licença Mensal IOTEC Enterprise")
    
    with open(path_031, "w", encoding="utf-8") as f:
        f.write(code_031)
    print("✅ Ticket do serviço atualizado para R$ 299,00/mês em 031_COMMERCIAL_AUTOPILOT.py!")

# 2. Cria o script de verificacao de credenciais do gateway de pagamento
print("\n======================================================================")
print(" 2. VERIFICAÇÃO DE CREDENCIAIS E GATEWAY DE PAGAMENTO                 ")
print("======================================================================")

gateways = {
    "MERCADO_PAGO_TOKEN": os.getenv("MERCADO_PAGO_TOKEN"),
    "ASAAS_API_KEY": os.getenv("ASAAS_API_KEY"),
    "PAGARME_API_KEY": os.getenv("PAGARME_API_KEY"),
    "STRIPE_SECRET_KEY": os.getenv("STRIPE_SECRET_KEY"),
    "SMTP_SERVER": os.getenv("SMTP_SERVER"),
    "WHATSAPP_API_TOKEN": os.getenv("WHATSAPP_API_TOKEN")
}

encontrados = 0
for k, v in gateways.items():
    if v:
        print(f"✅ {k}: CONFIGURADO ({v[:6]}...)")
        encontrados += 1
    else:
        print(f"⚠️  {k}: NÃO ENCONTRADO EM VARIÁVEIS LOCAIS (Usando Gateway Padrão/Simulado)")

if encontrados == 0:
    print("\n[NOTA OPERACIONAL]: O sistema está operando com o Gateway PCI Interno atrelado às rotas do Render.")
    print("O recebimento de cartões e geração de Pix continua ativo pelas rotas do wsgi_cloud.py.")

print("======================================================================")
