"""
===================================================================================
                       IOTEC NUCLEUS - PIPELINE INTEGRADO B2B
===================================================================================
 Arquiteto-Chefe: Farabulini Lopes Saraiva
 Entidade Proprietária: CNPJ 61.549.037/0001-68
 WhatsApp Corporativo: (88) 99930-6416
===================================================================================
"""

import urllib.parse
from prospector_b2b import ProspectorB2B
import manifest

class PipelineProspeccao:
    def __init__(self):
        self.prospector = ProspectorB2B()

    def processar_alvo(self, cnpj_alvo: str, telefone_decisor: str = None) -> dict:
        print(f"\n[+] PROSPECTOR: Consultando CNPJ {cnpj_alvo}...")
        empresa = self.prospector.consultar_cnpj_real(cnpj_alvo)

        if not empresa or not empresa.get("razao_social"):
            print("[!] Empresa não encontrada ou falha na consulta.")
            return {}

        razao = empresa.get("razao_social")
        cidade = empresa.get("cidade")
        uf = empresa.get("uf")
        
        print(f"[✓] ALVO CAPTURADO: {razao} ({cidade}/{uf})")

        # Gerar mensagem comercial personalizada
        mensagem_comercial = (
            f"Olá! Apresentação institucional da IOTEC Nucleus.\n\n"
            f"Prezados diretores da {razao},\n\n"
            f"Identificamos oportunidades de otimização de artérias econômicas e liquidez para empresas do seu setor em {cidade}/{uf}.\n\n"
            f"Nossa estrutura de Cartografia Econômica atua sob diretriz de Veracidade Financeira (Zero Simulação).\n\n"
            f"Atenciosamente,\n"
            f"Farabulini Lopes Saraiva\n"
            f"CNPJ: {manifest.CNPJ_TITULAR}\n"
            f"Contato Oficial: {manifest.WHATSAPP_CORPORATIVO}"
        )

        # Tratar telefone para link direto do WhatsApp Web
        tel_destino = telefone_decisor or empresa.get("telefone")
        tel_limpo = str(tel_destino).replace("(", "").replace(")", "").replace("-", "").replace(" ", "")

        mensagem_encoded = urllib.parse.quote(mensagem_comercial)
        link_whatsapp = f"https://web.whatsapp.com/send?phone=55{tel_limpo}&text={mensagem_encoded}"

        print("\n┌" + "─" * 73 + "┐")
        print("│                  DOSSIÊ DE PROSPECÇÃO B2B GERADO                        │")
        print("├" + "─" * 73 + "┤")
        print(f"│ EMPRESA   : {razao:<59} │")
        print(f"│ LOCAL     : {cidade}/{uf:<57} │")
        print(f"│ DESTINO   : {tel_limpo:<59} │")
        print("├" + "─" * 73 + "┤")
        print("│ MENSAGEM GERADA COM SUCESSO.                                            │")
        print("└" + "─" * 73 + "┘\n")

        return {
            "empresa": razao,
            "telefone": tel_limpo,
            "mensagem": mensagem_comercial,
            "link_whatsapp_web": link_whatsapp
        }

if __name__ == "__main__":
    manifest.exibir_banner_identidade()
    pipeline = PipelineProspeccao()
    
    # Teste de pipeline com o próprio CNPJ ou insira qualquer CNPJ comercial alvo
    resultado = pipeline.processar_alvo("61549037000168", "88999306416")