"""
===================================================================================
                       IOTEC NUCLEUS - SUITE INTEGRADA B2B
===================================================================================
 Arquiteto-Chefe: Farabulini Lopes Saraiva
 CNPJ: 61.549.037/0001-68 | WhatsApp Corporativo: (88) 99930-6416
===================================================================================
"""

import urllib.parse
import webbrowser
import time
from prospector_b2b import ProspectorB2B
from gerador_dossie_pdf import GeradorDossiePDF
import manifest

class MotorSuiteB2B:
    def __init__(self):
        self.prospector = ProspectorB2B()
        self.gerador_pdf = GeradorDossiePDF()

    def processar_lote_completo(self, lista_cnpjs: list, abrir_whatsapp: bool = True):
        manifest.exibir_banner_identidade()
        total = len(lista_cnpjs)
        print(f"[+] INICIANDO SUITE INTEGRADA PARA {total} EMPRESAS ALVO...\n")

        for index, cnpj in enumerate(lista_cnpjs, 1):
            print(f"===========================================================================")
            print(f"   [ALVO {index}/{total}] PROSPECTANDO CNPJ: {cnpj}")
            print(f"===========================================================================")
            
            # 1. Captura Dados Públicos Reais
            empresa = self.prospector.consultar_cnpj_real(cnpj)
            if not empresa or not empresa.get("razao_social"):
                print(f"[!] Falha ao obter dados do CNPJ {cnpj}. Pulando...\n")
                continue

            # 2. Gera o Dossiê Institucional em PDF
            caminho_pdf = self.gerador_pdf.gerar_pdf(empresa)

            # 3. Prepara Mensagem Customizada para o WhatsApp Business
            razao = empresa.get("razao_social")
            cidade = empresa.get("cidade")
            uf = empresa.get("uf")
            tel_destino = empresa.get("telefone")
            
            # Higieniza telefone
            tel_limpo = str(tel_destino).replace("(", "").replace(")", "").replace("-", "").replace(" ", "")

            texto_msg = (
                f"Olá! Apresentação institucional da IOTEC Nucleus.\n\n"
                f"Prezada diretoria da *{razao}*,\n\n"
                f"Elaboramos um Dossiê Exclusivo de Cartografia Econômica para a sua unidade em {cidade}/{uf}.\n\n"
                f"📄 O relatório formal foi gerado e salvo em formato PDF (Ref: {cnpj}).\n\n"
                f"Atenciosamente,\n"
                f"*{manifest.EMPRESA_TITULAR}*\n"
                f"CNPJ: {manifest.CNPJ_TITULAR}\n"
                f"WhatsApp Corporativo: {manifest.WHATSAPP_CORPORATIVO}"
            )

            print(f"[✓] Dossiê PDF salvo em: {caminho_pdf}")
            print(f"[✓] Abordagem preparada para {razao}")

            # 4. Envio via WhatsApp Web (Se habilitado)
            if abrir_whatsapp and "Dados Pessoais Protegidos" not in tel_limpo and tel_limpo != "N/A":
                msg_encoded = urllib.parse.quote(texto_msg)
                link_wa = f"https://web.whatsapp.com/send?phone=55{tel_limpo}&text={msg_encoded}"
                print(f"[+] Abrindo WhatsApp Web para envio...")
                webbrowser.open(link_wa)
                time.sleep(4)
            else:
                print(f"[i] Telefone protegido ou de teste internalizado. PDF gerado com sucesso.\n")

if __name__ == "__main__":
    suite = MotorSuiteB2B()
    
    # Adicione a lista de CNPJs que deseja prospectar
    cnpjs_alvo = [
        "61549037000168" # CNPJ Exemplo IOTEC
    ]
    
    suite.processar_lote_completo(cnpjs_alvo, abrir_whatsapp=False)