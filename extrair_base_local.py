import urllib.request
import zipfile
import os
import csv
import json

# =========================================================
# IOTEC - SELECIONADORA DE BASE LOCAL (DADOS ABERTOS RFB)
# =========================================================
# Arquivo público da Receita Federal contendo Estabelecimentos
URL_BASE_RFB = "https://dadosabertos.rfb.gov.br/CNPJ/Estabelecimentos0.zip"
ARQUIVO_ZIP = "estabelecimentos.zip"
PASTA_EXTRAIDA = "dados_rfb"

# Filtros do Funil IOTEC
CNAES_TRANSPORTE = ["4930202", "5250804", "5212500"]  # Carga, Logística, Terminais
UFS_ALVO = ["SP", "MG", "PR", "SC", "CE", "RJ", "GO"]

def baixar_e_extrair():
    if not os.path.exists(ARQUIVO_ZIP):
        print("📥 Baixando amostra da base oficial da Receita Federal (Aguarde...)...")
        urllib.request.urlretrieve(URL_BASE_RFB, ARQUIVO_ZIP)
        print("✅ Download concluído.")

    print("📂 Extraindo arquivos...")
    with zipfile.ZipFile(ARQUIVO_ZIP, 'r') as zip_ref:
        zip_ref.extractall(PASTA_EXTRAIDA)
    print("✅ Arquivos prontos para mineração offline.")

def processar_base_offline():
    print("\n" + "="*60)
    print("🚀 IOTEC - MINERAÇÃO OFFLINE DE TRANSPORTADORAS")
    print("="*60 + "\n")

    leads_qualificados = []
    
    # Procura o arquivo extraído na pasta
    arquivos = [f for f in os.listdir(PASTA_EXTRAIDA) if not f.endswith('.zip')]
    if not arquivos:
        print("❌ Nenhum arquivo de dados localizado.")
        return

    arquivo_csv = os.path.join(PASTA_EXTRAIDA, arquivos[0])
    
    print("🔍 Varrendo registros da Receita Federal sem limite de API...")
    
    with open(arquivo_csv, mode='r', encoding='latin-1') as f:
        # A base da Receita é delimitada por ponto e vírgula
        leitor = csv.reader(f, delimiter=';')
        
        for linha in leitor:
            if len(linha) < 30:
                continue
                
            # Estrutura do Layout da Receita Federal
            cnpj_basico = linha[0]
            cnpj_ordem = linha[1]
            cnpj_dv = linha[2]
            cnpj_completo = f"{cnpj_basico}{cnpj_ordem}{cnpj_dv}"
            
            sit_cadastral = linha[5]  # '02' significa ATIVA na Receita
            cnae_principal = linha[11]
            uf = linha[19]
            ddd1 = linha[21]
            tel1 = linha[22]
            
            # Filtro: Apenas ATIVAS (02), nos CNAEs de Transporte e UFs selecionadas
            if sit_cadastral == "02" and cnae_principal in CNAES_TRANSPORTE and uf in UFS_ALVO:
                tel_limpo = "".join(filter(str.isdigit, f"{ddd1}{tel1}"))
                
                if len(tel_limpo) >= 10:
                    tel_wapp = tel_limpo if tel_limpo.startswith("55") else f"55{tel_limpo}"
                    
                    lead = {
                        "cnpj": cnpj_completo,
                        "razao_social": f"TRANSPORTADORA REGISTRADA ({cnpj_completo})",
                        "status": "ATIVA",
                        "cnae": cnae_principal,
                        "uf": uf,
                        "municipio": linha[20],
                        "telefone": tel_wapp,
                        "link_whatsapp": f"https://web.whatsapp.com/send?phone={tel_wapp}"
                    }
                    leads_qualificados.append(lead)
                    print(f"✅ CAPTURADO OFFLINE: CNPJ {cnpj_completo} | UF: {uf} | Tel: {tel_wapp}")
                    
                    # Limite de segurança para demonstração do lote
                    if len(leads_qualificados) >= 50:
                        break

    print("\n" + "-"*60)
    print("💾 EXPORTANDO RESULTADOS...")
    print("-"*60)

    with open("leads_iotec.json", "w", encoding="utf-8") as f:
        json.dump(leads_qualificados, f, ensure_ascii=False, indent=4)
        
    print("📁 Arquivo 'leads_iotec.json' atualizado com sucesso.")
    print(f"📦 Total de empresas ativas mineradas: {len(leads_qualificados)}")

if __name__ == "__main__":
    try:
        baixar_e_extrair()
        processar_base_offline()
    except Exception as e:
        print(f"❌ Erro durante o processamento local: {e}")