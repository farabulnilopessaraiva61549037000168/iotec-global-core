# -*- coding: utf-8 -*-
# IOTEC NUCLEUS — Módulo Central & Radar Transnordestina

class IOTECNucleus:
    def __init__(self):
        self.nome_fantasia = "IOTEC — Construtora e Distribuidora de Tecnologia"
        self.razao_social  = "FARABULINI LOPES SARAIVA"
        self.cnpj          = "61.549.037/0001-68"
        self.whatsapp      = "(88) 99306-4168"
        self.email         = "iotec.bl@proton.me"

    def obter_cabecalho(self):
        return f"""
===========================================================================
               {self.nome_fantasia.upper()}
               VETOR DE EXPANSÃO: CORREDOR LOGÍSTICO TRANSNORDESTINA
===========================================================================
Emissor Oficial: {self.nome_fantasia}
Entidade Mantenedora: {self.razao_social} (CNPJ: {self.cnpj})
Contatos Oficiais: {self.email} | WhatsApp: {self.whatsapp}
===========================================================================
"""

class SensorTransnordestina:
    CIDADES_CHAVE = ["Quixadá", "Quixeramobim", "Iguatu", "Missão Velha", "Senador Pompeu", "Baturité", "Caucaia", "Pecém"]
    SETORES_ALVO = {
        "POSTOS_LOGISTICA": "Redes de Postos e Pátios de Manutenção de Frotas",
        "CONSTRUCAO_MINERACAO": "Pedreiras, Usinas de Concreto e Insumos Civis",
        "AGRO_LATICINIOS": "Cooperativas e Entrepostos de Grãos/Leite"
    }

    def gerar_plano_abordagem(self, empresa_alvo, cidade, setor_chave):
        print(f"\n[🚂 DIRETRIZ TRANSNORDESTINA] Alvo: {empresa_alvo}")
        print(f"[-] Localização Estratégica : {cidade} (Eixo da Ferrovia)")
        print(f"[-] Setor Mapeado           : {self.SETORES_ALVO.get(setor_chave, 'Serviços Gerais')}")
        print("[-] Plano de Ação Gerado    : Prospecção B2B via WhatsApp Web com Dossiê de Geointeligência.")
        print("[✓] Roteiro pronto para emissão e disparo!")

if __name__ == '__main__':
    nucleo = IOTECNucleus()
    print(nucleo.obter_cabecalho())
    radar = SensorTransnordestina()
    radar.gerar_plano_abordagem("POSTO E CHURRASCARIA SERTÃO REAL", "Quixadá", "POSTOS_LOGISTICA")