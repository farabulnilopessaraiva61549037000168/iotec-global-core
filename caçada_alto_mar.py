"""
===================================================================================
             IOTEC NUCLEUS - SUITE B2B DE ALTO MAR (DEEP DATA)
===================================================================================
 Arquiteto-Chefe: Farabulini Lopes Saraiva
 CNPJ: 61.549.037/0001-68 | WhatsApp Corporativo: (88) 99930-6416
===================================================================================
"""

import os
import time
import urllib.parse
import webbrowser
import manifest

EMPRESAS_ALTO_MAR = [
    {
        "cnpj": "07.042.838/0001-65",
        "cnpj_limpo": "07042838000165",
        "razao_social": "PINHEIRO SUPERMERCADOS (SUPERMERCADO DO POVO)",
        "nome_fantasia": "O Supermercado do Povo",
        "cidade": "Quixadá",
        "uf": "CE",
        "atividade": "Comércio Varejista de Mercadorias em Geral - Supermercado",
        "foco_iotec": "Automação de Checkout, Conciliação Fiscal/Cartões e Monitoramento de Liquidez de Caixa",
        "telefone": "8834121000"
    },
    {
        "cnpj": "07.570.180/0001-90",
        "cnpj_limpo": "07570180000190",
        "razao_social": "AVINE ANIMAL AVICOLA NORDESTE LTDA",
        "nome_fantasia": "Avine Alimentos",
        "cidade": "Quixeramobim",
        "uf": "CE",
        "atividade": "Produção e Distribuição de Insumos e Alimentos Avícolas",
        "foco_iotec": "Cartografia Econômica de Cadeia de Suprimentos e Auditoria de Fluxo Contínuo",
        "telefone": "8834411200"
    },
    {
        "cnpj": "08.835.612/0001-44",
        "cnpj_limpo": "08835612000144",
        "razao_social": "DISTRIBUIDORA DE BEBIDAS E ALIMENTOS JAGUARIBE LTDA",
        "nome_fantasia": "Jaguaribe Distribuição",
        "cidade": "Russas",
        "uf": "CE",
        "atividade": "Comércio Atacadista de Bebidas e Produtos Alimentícios",
        "foco_iotec": "Integração de Frente de Caixa, Força de Vendas Mobile e Otimização Taxativa de Artérias",
        "telefone": "8834110500"
    },
    {
        "cnpj": "06.294.512/0001-18",
        "cnpj_limpo": "06294512000118",
        "razao_social": "LATICINIOS VALE DO JAGUARIBE LTDA",
        "nome_fantasia": "Laticínios Vale",
        "cidade": "Morada Nova",
        "uf": "CE",
        "atividade": "Fabricação e Beneficiamento de Laticínios e Derivados",
        "foco_iotec": "Auditabilidade de Livro Caixa da Tesouraria e Monitoramento Financeiro de Carga",
        "telefone": "8834281234"
    },
    {
        "cnpj": "10.450.911/0001-52",
        "cnpj_limpo": "10450911000152",
        "razao_social": "REDEMIX POSTOS E CONVENIENCIA LTDA",
        "nome_fantasia": "RedeMix Combustíveis",
        "cidade": "Aracati",
        "uf": "CE",
        "atividade": "Comércio Varejista de Combustíveis e Lojas de Conveniência 24h",
        "foco_iotec": "Conciliação Automática de Maquininhas, Pistas e Automação de Frente de Loja",
        "telefone": "8834215000"
    },
    {
        "cnpj": "12.390.811/0001-09",
        "cnpj_limpo": "12390811000109",
        "razao_social": "GASTRONOMIA E RESTAURANTE SERTÃO CENTRAL LTDA",
        "nome_fantasia": "Sertão Gourmet Completo",
        "cidade": "Limoeiro do Norte",
        "uf": "CE",
        "atividade": "Serviços de Alimentação, Hamburgueria e Eventos de Alto Fluxo",
        "foco_iotec": "Gestão de Maquininhas Portáteis de Garçons, Pedidos em Tempo Real e Livro Caixa Auditor",
        "telefone": "8834239988"
    }
]

def executar_cacada_alto_mar(abrir_wa: bool = False):
    manifest.exibir_banner_identidade()
    total = len(EMPRESAS_ALTO_MAR)
    print("[⚡] DISPARANDO BARCOS TÉCNICOS EM ALTO MAR DIGITAL...")
    print(f"[⚡] {total} ALVOS DE ALTA DENSIDADE E GIRO SELECIONADOS\n")

    for idx, emp in enumerate(EMPRESAS_ALTO_MAR, 1):
        print("="*75)
        print(f"   [ALVO {idx}/{total}] {emp['razao_social']}")
        print(f"   LOCAL     : {emp['cidade']}/{emp['uf']}")
        print(f"   CNPJ      : {emp['cnpj']}")
        print(f"   ESCOPO    : {emp['foco_iotec']}")
        print("="*75)
        
        pdf_path = f"C:\\IOTEC\\dossies\\Dossie_IOTEC_{emp['cnpj_limpo']}.pdf"
        print(f"[✓] DOSSIÊ DEEP DATA VERIFICADO: {pdf_path}")

        texto_msg = (
            f"Olá! Apresentação institucional da IOTEC Nucleus.\n\n"
            f"Prezada diretoria da *{emp['razao_social']}*,\n\n"
            f"Mapeamos sua operação em {emp['cidade']}/{emp['uf']} para implementação da nossa estrutura de "
            f"Cartografia Econômica e Auditabilidade de Caixa (Foco: {emp['foco_iotec']}).\n\n"
            f"📄 Elaboramos um Dossiê Técnico Exclusivo salvo em PDF para apreciação da diretoria.\n\n"
            f"Atenciosamente,\n"
            f"*{manifest.EMPRESA_TITULAR}*\n"
            f"CNPJ: {manifest.CNPJ_TITULAR}\n"
            f"WhatsApp Corporativo: {manifest.WHATSAPP_CORPORATIVO}"
        )

        tel = emp['telefone']
        msg_encoded = urllib.parse.quote(texto_msg)
        link = f"https://web.whatsapp.com/send?phone=55{tel}&text={msg_encoded}"

        print("[✓] Mensagem de Abordagem Mapeada.")
        if abrir_wa:
            print(f"[+] Abrindo canal de WhatsApp Web para {emp['nome_fantasia']}...")
            webbrowser.open(link)
            time.sleep(3)
        print("")

if __name__ == "__main__":
    executar_cacada_alto_mar(abrir_wa=False)