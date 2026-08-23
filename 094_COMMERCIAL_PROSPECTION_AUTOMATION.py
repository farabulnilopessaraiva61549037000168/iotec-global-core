# -*- coding: utf-8 -*-
import json
import time
import os
import requests

RENDER_URL = "https://iotec-global-core.onrender.com"
BASE_FILE = "base_empresas_reais.json"

def carregar_base_real():
    if not os.path.exists(BASE_FILE):
        print(f"❌ Arquivo {BASE_FILE} não encontrado!")
        return []
    # utf-8-sig remove automaticamente o marcador BOM do Windows/PowerShell
    with open(BASE_FILE, "r", encoding="utf-8-sig") as f:
        return json.load(f)

def gerar_mensagem_whatsapp(empresa, pacote_nome, servico, valor, checkout_url):
    return f"""🚨 *ALERTA DE REGULARIDADE E OPORTUNIDADE B2B - IOTEC*

Olá, equipe da *{empresa}*!

Identificamos oportunidades ativas de contratos públicos/B2B e pendências de regularidade técnica para o seu setor.

📋 *Plano Recomendado:* {servico} (*Pacote {pacote_nome}*)
💰 *Investimento:* R$ {valor:.2f}

⚡ *Benefícios Imediatos:*
• Liberação de Certidões e Dossiê em tempo recorde.
• Habilitação técnica para Licitações e Grandes Contratos B2B.
• Proteção contra impedimentos fiscais e emissão de notas.

🔗 *Acesse o checkout oficial e garanta a emissão imediata:*
{checkout_url}

_Atenciosamente,_
*Central de Inteligência Operacional IOTEC*"""

def executar_prospeccao_real():
    alvos = carregar_base_real()
    if not alvos:
        print("⚠️ Nenhuma empresa encontrada na base. Preencha o arquivo base_empresas_reais.json!")
        return

    print("==================================================")
    print(" 🚀 INICIANDO DISPARO ATIVO COM EMPRESAS REAIS ")
    print("==================================================")

    for idx, alvo in enumerate(alvos, 1):
        if "DIGITE_CNPJ" in alvo["cnpj"]:
            print(f"\n[{idx}/{len(alvos)}] ⚠️ Pulando exemplo não preenchido: {alvo['empresa']}")
            continue

        print(f"\n[{idx}/{len(alvos)}] Processando: {alvo['empresa']} ({alvo['cnpj']})")
        
        payload = {
            "cnpj": alvo["cnpj"],
            "empresa": alvo["empresa"],
            "telefone": alvo["telefone"],
            "servico": alvo["servico"],
            "valor": alvo["valor"]
        }

        try:
            res = requests.post(f"{RENDER_URL}/api/leads/registrar", json=payload, timeout=10)
            if res.status_code in [200, 201]:
                data = res.json()
                checkout_url = data.get("checkout_url")
                
                print(f"  ├─ Status   : REGISTRADO NA NUVEM")
                print(f"  ├─ Lead ID  : {data.get('lead_id')}")
                print(f"  └─ Checkout : {checkout_url}")

                msg = gerar_mensagem_whatsapp(
                    empresa=alvo["empresa"],
                    pacote_nome=alvo["pacote_nome"],
                    servico=alvo["servico"],
                    valor=alvo["valor"],
                    checkout_url=checkout_url
                )

                print("\n  📲 [TEXTO PRONTO PARA DISPARO WHATSAPP]")
                print("  --------------------------------------------------")
                for line in msg.splitlines():
                    print(f"  | {line}")
                print("  --------------------------------------------------")
            else:
                print(f"  └─ Erro ao registrar lead na nuvem: HTTP {res.status_code}")
        except Exception as e:
            print(f"  └─ Erro de conexão com o servidor Render: {e}")

        time.sleep(1)

if __name__ == "__main__":
    executar_prospeccao_real()
