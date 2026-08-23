# -*- coding: utf-8 -*-
# Gerador de Dossiê IOTEC Nucleus - Versão Corrigida

EMISSOR_NOME = "FARABULINI LOPES SARAIVA"
EMISSOR_CNPJ = "61.549.037/0001-68"
EMISSOR_WHATSAPP = "(88) 99930-6416"
EMISSOR_EMAIL = "iotec.bl@proton.me"

def gerar_dossie(cliente_razao, cliente_cnpj, cliente_cidade, atividade):
    print("==================================================")
    print(f"GERANDO DOSSIÊ DE CAÇA PARA O ALVO: {cliente_razao}")
    print("==================================================")
    print(f"[-] ALVO      : {cliente_razao} (CNPJ: {cliente_cnpj})")
    print(f"[-] CIDADE    : {cliente_cidade}")
    print(f"[-] EMISSOR   : {EMISSOR_NOME} ({EMISSOR_CNPJ})")
    print(f"[-] CONTATO   : {EMISSOR_WHATSAPP} | {EMISSOR_EMAIL}")
    print("==================================================")
    print("[✓] Dossiê atualizado e pronto para disparo!")

if __name__ == '__main__':
    # Exemplo de teste com um ALVO externo (Cliente)
    gerar_dossie("SUPERMERCADO EXEMPLO LTDA", "12.345.678/0001-90", "Quixadá/CE", "Comércio Varejista")