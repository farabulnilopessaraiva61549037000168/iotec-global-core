import os
import datetime

class CertificateWriterAgent:
    def __init__(self):
        self.role = "Especialista em Redação Jurídico-Comercial B2B"
        self.tone = "Formal, Jurídico-Técnico e Minimalista"

    def generate_certificate(self, company_name, city, sector, license_value="299.00"):
        today = datetime.date.today().strftime("%d/%m/%Y")
        
        cert = f"""
===================================================================================
                  CERTIDÃO TÉCNICA DE ADEQUAÇÃO E CAPACIDADE
                       SISTEMA IOTEC ENTERPRISE CORE
===================================================================================

CERTIFICAMOS, para os devidos fins de comprovação de eficiência operacional e 
automação regional, que a empresa:

Razão Social / Alvo : {company_name}
Pólo de Atuação     : {city}
Setor Econômico     : {sector}

Se encontra plenamente elegível e pré-credenciada para a integração da infraestrutura
em nuvem IOTEC Enterprise, com suporte operacional 24/7 e taxas de adesão reduzidas.

-----------------------------------------------------------------------------------
 CLÁUSULAS TÉCNICAS E VALORIZADORAS DO SERVIÇO:
-----------------------------------------------------------------------------------
 1. OPERAÇÃO NATIVA EM NUVEM: Isenção total de custos com servidores locais e
    manutenção de TI por parte do contratante.
 2. GARANTIA DE CONTINUIDADE: Protocolo de redundância regional com uptime de 99.9%.
 3. VALOR DA LICENÇA MENSAL: R$ {license_value} (fixo, sem taxa de adesão ou fidelidade).

Certidão emitida em {today}, sob o protocolo IOTEC-CERT-{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.

_____________________________________________________
DIRETORIA DE ENGENHARIA E COMPLIANCE - IOTEC BRASIL
Contato Oficial: IOTEC.BL@proton.me
===================================================================================
"""
        return cert

# Teste do Agente
if __name__ == "__main__":
    agent = CertificateWriterAgent()
    sample = agent.generate_certificate("Ações Contabilidade", "Fortaleza - CE", "Contabilidade")
    
    with open("CERTIDAO_EXEMPLO.txt", "w", encoding="utf-8") as f:
        f.write(sample)
    
    print("✅ Agente Redator de Certidões ativo! Exemplo gerado em CERTIDAO_EXEMPLO.txt")
