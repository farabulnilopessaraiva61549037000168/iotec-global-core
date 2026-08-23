"""
===================================================================================
                       IOTEC NUCLEUS - PROSPECÇÃO B2B EM LOTE
===================================================================================
 Arquiteto-Chefe: Farabulini Lopes Saraiva
 CNPJ: 61.549.037/0001-68 | WhatsApp: (88) 99930-6416
===================================================================================
"""

import webbrowser
import time
from pipeline_prospeccao import PipelineProspeccao
import manifest

def executar_prospeccao_lote(lista_cnpjs: list, abrir_navegador: bool = True):
    manifest.exibir_banner_identidade()
    pipeline = PipelineProspeccao()
    
    total = len(lista_cnpjs)
    print(f"[+] INICIANDO PROCESSAMENTO DE {total} CNPJs ALVO...\n")

    for index, cnpj in enumerate(lista_cnpjs, 1):
        print(f"--- [{index}/{total}] Processando CNPJ: {cnpj} ---")
        dossie = pipeline.processar_alvo(cnpj)
        
        if dossie and abrir_navegador and dossie.get("link_whatsapp_web"):
            link = dossie["link_whatsapp_web"]
            print(f"[+] Abrindo link de envio no navegador para: {dossie['empresa']}")
            webbrowser.open(link)
            print("[i] Aguardando 5 segundos para a próxima consulta...\n")
            time.sleep(5)

if __name__ == "__main__":
    # Insira aqui os CNPJs das empresas que você deseja prospectar
    # Exemplo: CNPJs de indústrias, distribuidores ou comércios da região
    cnpjs_para_prospectar = [
        "61549037000168", # Próprio IOTEC (Exemplo)
        # Adicione novos CNPJs aqui entre aspas e separados por vírgula
    ]
    
    executar_prospeccao_lote(cnpjs_para_prospectar, abrir_navegador=False)