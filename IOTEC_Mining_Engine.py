import pandas as pd
import os
from datetime import datetime

class IOTECMiningEngine:
    """
    IOTEC - Core Intelligence & Lead Extraction Engine (v1.2)
    Mineração direta na raiz do projeto.
    """
    
    def __init__(self, pasta_base="C:/IOTEC", pasta_saida="C:/IOTEC/iotec_output"):
        self.pasta_base = pasta_base
        self.pasta_saida = pasta_saida
        self.cnaes_alvo = ['4930201', '4930202', '4930203', '4930204', '4930205']
        
        if not os.path.exists(self.pasta_saida):
            os.makedirs(self.pasta_saida)

    def processar_chunk(self, chunk, leads_list):
        try:
            # Mapeamento dinâmico de colunas (caso o arquivo tenha cabeçalho ou não)
            cols = chunk.columns
            
            # Se for formato numérico (sem header) ou com nomes de colunas
            for _, row in chunk.iterrows():
                # Tenta obter CNAE e Status Cadastral
                cnae = str(row.get(11, row.get('cnae', row.get('CNAE', '')))).strip()
                sit_cadastral = str(row.get(5, row.get('situacao_cadastral', row.get('Status', '')))).strip().zfill(2)
                
                # Se encontrar CNAE de transporte
                if any(c in cnae for c in self.cnaes_alvo) or cnae in self.cnaes_alvo:
                    cnpj = str(row.get(0, row.get('cnpj', row.get('CNPJ', '')))).strip()
                    telefone = str(row.get(17, row.get('telefone', row.get('Telefone', '')))).strip()
                    email = str(row.get(21, row.get('email', row.get('Email', '')))).strip().lower()
                    uf = str(row.get(19, row.get('uf', row.get('UF', '')))).strip()
                    
                    leads_list.append({
                        'IOTEC_ID': f"IOT-{cnpj}",
                        'CNPJ': cnpj,
                        'CNAE': cnae,
                        'UF': uf,
                        'Telefone': telefone,
                        'Email': email,
                        'Status_Abordagem': 'Pendente'
                    })
        except Exception:
            pass

    def executar_mineracao(self):
        data_execucao = datetime.now().strftime("%Y%m%d_%H%M")
        arquivo_final = os.path.join(self.pasta_saida, f"IOTEC_Leads_Transportes_{data_execucao}.csv")
        
        print(f"[{datetime.now().strftime('%H:%M:%S')}] ⚙️ IOTEC Engine: Processando base de dados raiz...")
        
        # Arquivos prioritários encontrados na raiz
        arquivos_alvo = ['empresas.csv', 'companies_master.csv', 'novas_empresas.csv', 'leads_iotec.csv']
        leads_iotec = []

        for arq in arquivos_alvo:
            caminho = os.path.join(self.pasta_base, arq)
            if os.path.exists(caminho):
                print(f"📦 IOTEC Mining: Minerando -> {arq}")
                try:
                    chunks = pd.read_csv(
                        caminho, sep=None, engine='python', encoding='latin1', 
                        dtype=str, chunksize=20000, on_bad_lines='skip'
                    )
                    for chunk in chunks:
                        self.processar_chunk(chunk, leads_iotec)
                except Exception as e:
                    print(f"⚠️ Erro ao ler {arq}: {e}")

        if leads_iotec:
            df_final = pd.DataFrame(leads_iotec)
            df_final.drop_duplicates(subset=['CNPJ'], inplace=True)
            df_final.to_csv(arquivo_final, index=False, encoding='utf-8-sig')
            print(f"\n✅ IOTEC Engine: Extração Concluída! {len(df_final)} potenciais clientes extraídos!")
            print(f"📁 Arquivo final gerado em: {arquivo_final}")
        else:
            print("\n⚠️ Nenhum lead novo filtrado. Verifique o conteúdo dos arquivos CSV.")

if __name__ == "__main__":
    engine = IOTECMiningEngine()
    engine.executar_mineracao()