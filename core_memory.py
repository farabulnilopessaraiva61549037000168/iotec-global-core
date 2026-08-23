# ==============================================================================
#           IOTEC - MATRIZ DE MEMÓRIA & SISTEMA INTEGRADO DO NÚCLEO
# ==============================================================================
# CNPJ: 61.549.037/0001-68 | Responsável Técnico: Farabulini Lopes Saraiva

import os

INSTITUICAO = {
    "nome_fantasia": "IOTEC TECNOLOGIA",
    "razao_social": "IOTEC TECNOLOGIAS AVANÇADAS",
    "cnpj": "61.549.037/0001-68",
    "email_oficial": "iotec.bl@proton.me",
    "responsavel": "Farabulini Lopes Saraiva"
}

RAMOS_ATUACAO = {
    "LOGISTICA_TRANSPORTE": {
        "setor": "Transportes & Frotas (BRs e Corredores)",
        "servicos": [
            {"nome": "Checkup de Sinais de Frota & Latência", "faixa_preco": "R$ 29,90 a R$ 97,00"},
            {"nome": "Auditoria de Telemetria e Pontos Cegos", "faixa_preco": "R$ 150,00 a R$ 490,00"}
        ]
    },
    "INDUSTRIA_MANUFATURA": {
        "setor": "Polos Industriais (Calçados, Têxtil, Alimentos)",
        "servicos": [
            {"nome": "Diagnóstico de Sensores de Linha de Produção", "faixa_preco": "R$ 97,00 a R$ 290,00"},
            {"nome": "Integração de Relatórios de Estoque/Pátio", "faixa_preco": "R$ 490,00 a R$ 1.500,00"}
        ]
    }
}

CESTA_PRODUTOS = {
    "CHECKUP_EXPRESS": {
        "codigo": "ITEM-01",
        "nome": "Checkup Express de Conectividade & Telemetria",
        "valor_padrao": 29.90,
        "bastidores": "Verificação de rotas de dados de frotas e auditoria rápida de sensores IoT em rodovias."
    },
    "DOSSIE_TECNICO": {
        "codigo": "ITEM-02",
        "nome": "Dossiê Técnico de Latência e Sinal BR-116",
        "valor_padrao": 97.00,
        "bastidores": "Mapeamento de sombras de cobertura e latência ao longo dos eixos rodoviários."
    },
    "CONSULTORIA_MASCATE": {
        "codigo": "ITEM-03",
        "nome": "Consultoria de Integração IoT & Frotas Rodoviárias",
        "valor_padrao": 290.00,
        "bastidores": "Sessão consultiva para integração de gateways em galpões e frotas."
    },
    "MODULO_ENTERPRISE": {
        "codigo": "ITEM-04",
        "nome": "Arquitetura Customizada para Hubs e Polos Industriais",
        "valor_padrao": 1500.00,
        "bastidores": "Projeto completo de monitoramento para parques industriais."
    }
}

PARAMETROS_NEGOCIACAO = {
    "permitir_desconto_automatico": True,
    "margem_desconto_maxima_mascate": 0.20,
    "requer_aprovacao_presidencia": 500.00,
    "status_mesa": "INTEGRACAO_TOTAL_OK"
}

def notificar_presidencia(cliente, localizacao, ramo, dor, valor_sugerido, agente_nome):
    mensagem = f"""
🚨 *NOVA OPORTUNIDADE DETECTADA PELO SISTEMA IOTEC!*

🤖 *Agente Caçador:* {agente_nome}
🏢 *Cliente/Empresa:* {cliente}
📍 *Localização/Eixo:* {localizacao}
🏭 *Ramo:* {ramo}
⚠️ *Gargalo/Dor:* {dor}
💰 *Valor Sugerido para o Pix:* R$ {valor_sugerido:.2f}

👉 *Acesse a Mesa de Operações para Autorizar:*
https://iotec-platform-1.onrender.com/presidencia
"""
    print("=" * 65)
    print("📢 ALERTANDO A PRESIDÊNCIA EM TEMPO REAL...")
    print(mensagem.strip())
    print("=" * 65)
    
    return {
        "alerta": "ENVIADO",
        "cliente": cliente,
        "localizacao": localizacao,
        "ramo": ramo,
        "dor": dor,
        "valor": valor_sugerido,
        "agente": agente_nome
    }

def gerar_relatorio_operacoes(lista_negociacoes):
    total_negociacoes = len(lista_negociacoes)
    oportunidades_novas = sum(1 for n in lista_negociacoes if "OPORTUNIDADE" in n.get("status", ""))
    volume_potencial = sum(n.get("oferta_inicial", 0) for n in lista_negociacoes)

    return {
        "status_servidor": "OPERACIONAL (NUVEM RENDER 24/7)",
        "radar_corredores": "ATIVO (Eixo BR-116 e Polos Industriais)",
        "total_oportunidades_no_radar": total_negociacoes,
        "novas_notificacoes_presidencia": oportunidades_novas,
        "valor_total_em_negociacao": round(volume_potencial, 2),
        "capacidade_entrega": "AUTOMÁTICA (Relatórios & Dossiês em PDF/Web)"
    }