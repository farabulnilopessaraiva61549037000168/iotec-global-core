# C:\IOTEC\camadas_internas.py
import json

class TORINucleoInterno:
    def __init__(self):
        self.empresa_cnpj = "61.549.037/0001-68"
        
    def listar_capacidades_impressao(self):
        """ Retorna a matriz de documentos/certidões por Modal e Órgão Emissor """
        capacidades = {
            "Camada_02_Aduaneiro_e_Comex": [
                {"nome": "DTA / DTC - Trânsito Aduaneiro", "orgao": "Receita Federal / Siscomex", "tipo": "Aduaneiro"},
                {"nome": "DUIMP / Extrato de Importação", "orgao": "Portal Único Siscomex", "tipo": "Aduaneiro"},
                {"nome": "Certificado OEA - Segurança Logística", "orgao": "Receita Federal", "tipo": "Compliance"}
            ],
            "Camada_03_Transporte_Multimodal": [
                {"nome": "RNTRC - Rodoviário de Cargas", "orgao": "ANTT", "tipo": "Terrestre"},
                {"nome": "Declaração de Adimplência Aquaviária", "orgao": "ANTAQ", "tipo": "Marítimo"},
                {"nome": "CE Mercante / Liberação AFRMM", "orgao": "Siscomex Carga", "tipo": "Marítimo"},
                {"nome": "CCT Aéreo / Manifestos AWB", "orgao": "ANAC / Receita Federal", "tipo": "Aéreo"},
                {"nome": "TIF / Manifesto Ferroviário", "orgao": "ANTT / Malha Ferroviária", "tipo": "Ferroviário"}
            ],
            "Camada_04_Regularidade_Corporativa": [
                {"nome": "CND Federal e Dívida Ativa", "orgao": "Receita Federal / PGFN", "tipo": "Fiscal"},
                {"nome": "CRF - Regularidade FGTS", "orgao": "Caixa Econômica", "tipo": "Trabalhista"},
                {"nome": "CNDT - Certidão Trabalhista", "orgao": "Tribunal Superior do Trabalho", "tipo": "Trabalhista"},
                {"nome": "Ficha Cadastral / Certidão JUCESP", "orgao": "JUCESP SP", "tipo": "Societário"}
            ]
        }
        return capacidades

if __name__ == "__main__":
    tori = TORINucleoInterno()
    print(json.dumps(tori.listar_capacidades_impressao(), indent=4, ensure_ascii=False))