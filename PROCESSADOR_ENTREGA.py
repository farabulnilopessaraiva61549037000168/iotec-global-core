from token_asaas import TOKEN
import requests
import json
import os

headers = {"access_token": TOKEN, "Content-Type": "application/json"}
DIRETORIO_ENTREGAS = r"C:\IOTEC\ENTREGAS_CLIENTES"

PALETAS_CLIENTE = {
    "TITANIUM_CORPORATE": {
        "nome": "Titanium Corporate (Padrão Bancário)",
        "bg": "#121316", "card": "#1C1E22", "accent": "#D97706", "text": "#E2E8F0"
    },
    "OBSIDIAN_EMERALD": {
        "nome": "Obsidian Emerald (Cyber Compliance)",
        "bg": "#0B0F17", "card": "#151B26", "accent": "#10B981", "text": "#F8FAFC"
    },
    "DEEP_SLATE_VIOLET": {
        "nome": "Deep Slate Violet (Analytics & IA)",
        "bg": "#0F172A", "card": "#1E293B", "accent": "#8B5CF6", "text": "#F8FAFC"
    }
}

def mapear_produto_e_tema(nome_cliente):
    nome = nome_cliente.upper()
    if "BANCO DO BRASIL" in nome:
        return {
            "tipo": "FINANCEIRO_COMPLIANCE",
            "descricao": "IOTEC Compliance Engine v2.1 (Auditoria e Bacen)",
            "tema": PALETAS_CLIENTE["TITANIUM_CORPORATE"]
        }
    elif "SENDAS" in nome or "DISTRIBUIDORA" in nome:
        return {
            "tipo": "SUPPLY_CHAIN_INDUSTRIAL",
            "descricao": "IOTEC Analytics v2.1 (Supply Chain & Dados)",
            "tema": PALETAS_CLIENTE["DEEP_SLATE_VIOLET"]
        }
    else:
        return {
            "tipo": "AUTOMAÇÃO_INDUSTRIAL_GERAL",
            "descricao": "IOTEC Core Engine v2.1 (Automação de Processos)",
            "tema": PALETAS_CLIENTE["OBSIDIAN_EMERALD"]
        }

def gerar_pacote_entrega(cliente_nome, cobranca_id, produto_info):
    pasta_cliente = os.path.join(DIRETORIO_ENTREGAS, cobranca_id)
    if not os.path.exists(pasta_cliente):
        os.makedirs(pasta_cliente)
    
    licenca_path = os.path.join(pasta_cliente, "LICENCA_E_CONTRATO_JURIDICO.txt")
    tema = produto_info["tema"]
    
    conteudo_contrato = f"""
===============================================================================
 🚀 IOTEC GLOBAL — SISTEMAS AUTOMATIZADOS & TECNOLOGIA B2B
 MARCA REGISTRADA / ECOSSISTEMA: IOTEC® / IOTEC GLOBAL
 PROVEDOR OFICIAL (RAZÃO SOCIAL): Farabulini Lopes Saraiva | CNPJ: 61.549.037/0001-68
===============================================================================
 CLIENTE CONTRATANTE: {cliente_nome}
 CÓDIGO DA FATURA LIQUIDADA: {cobranca_id}
 MÓDULO CONTRATADO: {produto_info['descricao']}
 AMBIENTE VISUAL APLICADO: {tema['nome']}
===============================================================================
 CHAVE DE AUTENTICAÇÃO API: LIC-IOTEC-{cobranca_id.upper()}-PROD
===============================================================================

 📜 CLÁUSULAS DE RESGUARDO E LIMITAÇÃO DE RESPONSABILIDADE (JURÍDICO V2.1)
 ─────────────────────────────────────────────────────────────────────────────
 1. NATUREZA DA OBRIGAÇÃO: O presente módulo constitui uma ferramenta de
    meio de análise de dados, scoring e auditoria automatizada desenvolvida pela
    IOTEC GLOBAL. A ferramenta auxilia no processo decisório do CONTRATANTE.

 2. AUTONOMIA DECISÓRIA: A decisão final sobre a aprovação, retenção ou 
    liquidação financeira de qualquer transação analisada é de responsabilidade
    exclusiva da instituição CONTRATANTE ({cliente_nome}).

 3. LIMITAÇÃO DE RESPONSABILIDADE (LIABILITY CAP): Sob nenhuma hipótese a
    responsabilidade civil ou indenizatória da IOTEC / Farabulini Lopes Saraiva
    excederá o valor total efetivamente pago pela fatura correspondente ao ciclo
    operacional vigente ({cobranca_id}).

 4. PROPRIEDADE INTELECTUAL: A marca IOTEC, seus algoritmos e código-fonte
    permanecem sob propriedade intelectual exclusiva do PROVEDOR.
===============================================================================
 DOCUMENTO GERADO AUTOMATICAMENTE PELO NÚCLEO IOTEC GLOBAL VIA ASAAS PIX.
===============================================================================
"""
    with open(licenca_path, 'w', encoding='utf-8') as f:
        f.write(conteudo_contrato)
        
    print(f" [📦] PACOTE IOTEC GLOBAL COM CONTRATO GERADO EM: {pasta_cliente}")

def processar_entregas():
    print("===============================================================================")
    print(" 🚀 MONITOR DE ENTREGAS IOTEC GLOBAL & RESGUARDO JURÍDICO")
    print("===============================================================================")
    
    try:
        res = requests.get("https://www.asaas.com/api/v3/payments?status=RECEIVED", headers=headers, timeout=10)
        if res.status_code == 200:
            pagamentos = res.json().get("data", [])
            print(f" 🔍 Pagamentos liquidados no Asaas: {len(pagamentos)}")
            
            if not pagamentos:
                print(" ⏳ Nenhum Pix liquidado até o momento. Aguardando pagamentos...")
            
            for pag in pagamentos:
                cliente_id = pag.get("customer")
                cobranca_id = pag.get("id")
                
                res_cli = requests.get(f"https://www.asaas.com/api/v3/customers/{cliente_id}", headers=headers)
                nome_cliente = res_cli.json().get("name", "Cliente") if res_cli.status_code == 200 else "Cliente"
                
                prod = mapear_produto_e_tema(nome_cliente)
                print(f"\n [✔] PAGAMENTO CONFIRMADO | Cliente: {nome_cliente}")
                gerar_pacote_entrega(nome_cliente, cobranca_id, prod)
        else:
            print(f" [❌] Erro ao consultar Asaas: Status {res.status_code}")
            
    except Exception as e:
        print(f" [❌] Falha no monitor: {e}")

if __name__ == "__main__":
    processar_entregas()
