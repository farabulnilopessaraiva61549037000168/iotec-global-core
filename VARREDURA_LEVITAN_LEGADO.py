import os
import sqlite3
import re

DB_PATH = "C:\\IOTEC\\iotec.db"
DISCO_RAIZ = "C:\\"

# Pastas conhecidas ou padrões a serem buscados
PADROES_PASTAS = ["IOTEC", "REGULOS", "PROJETOS", "SISTEMAS", "BOTS", "DEV", "PYTHON"]

def inicializar_banco_legado():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS acervo_legado_completo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_arquivo TEXT,
            caminho_absoluto TEXT UNIQUE,
            origem_projeto TEXT, -- REGULOS, IOTEC_ANTIGO, OUTROS
            categoria_identificada TEXT,
            status_aproveitamento TEXT DEFAULT 'CATALOGADO'
        )
    ''')
    conn.commit()
    conn.close()

class MineradorLegadoDisco:
    def __init__(self):
        inicializar_banco_legado()

    def varrer_disco_c(self):
        print("============================================================")
        print("   IOTEC ENGINE — VARREDURA PROFUNDA DE LEVIATÃ/RÉGULOS   ")
        print("============================================================\n")

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        pastas_encontradas = []
        try:
            # Lista pastas no diretório C:\
            itens_raiz = os.listdir(DISCO_RAIZ)
            for item in itens_raiz:
                caminho = os.path.join(DISCO_RAIZ, item)
                if os.path.isdir(caminho):
                    nome_up = item.upper()
                    if any(p in nome_up for p in PADROES_PASTAS):
                        pastas_encontradas.append(caminho)
        except Exception as e:
            print(f"[-] Erro ao ler raiz do C:: {e}")

        print(f"📂 Pastas de projetos/legado mapeadas no C:: {pastas_encontradas}\n")

        total_arquivos = 0
        regulos_count = 0
        iotec_count = 0

        for pasta in pastas_encontradas:
            print(f"🔍 Varrendo estrutura em: {pasta} ...")
            for raiz, _, arquivos in os.walk(pasta):
                # Ignora pastas temporarias ou de ambiente virtual
                if any(x in raiz for x in ["venv", "__pycache__", ".git", "node_modules", "AppData"]):
                    continue

                for arq in arquivos:
                    if arq.endswith(".py") or arq.endswith(".js") or arq.endswith(".html"):
                        caminho_full = os.path.join(raiz, arq)
                        
                        # Origem
                        if "REGULOS" in caminho_full.upper():
                            origem = "REGULOS_HISTORICO"
                            regulos_count += 1
                        elif "IOTEC" in caminho_full.upper():
                            origem = "IOTEC_MATRIZ"
                            iotec_count += 1
                        else:
                            origem = "OUTROS_PROJETOS"

                        # Categorizacao
                        nome_lc = arq.lower()
                        if any(k in nome_lc for k in ["mail", "venda", "lead", "cadencia", "crm"]):
                            cat = "AUTOMACAO_COMERCIAL"
                        elif any(k in nome_lc for k in ["pagamento", "pix", "paypal", "caixa", "financeiro"]):
                            cat = "GATEWAYS_E_FINANCEIRO"
                        elif any(k in nome_lc for k in ["bot", "whatsapp", "sac", "atendimento"]):
                            cat = "ATENDIMENTO_E_SAC"
                        elif any(k in nome_lc for k in ["miner", "raspador", "scra", "dados"]):
                            cat = "MINERACAO_E_INVENTARIO"
                        else:
                            cat = "UTILITARIO_OPERACIONAL"

                        try:
                            cursor.execute('''
                                INSERT OR REPLACE INTO acervo_legado_completo
                                (nome_arquivo, caminho_absoluto, origem_projeto, categoria_identificada)
                                VALUES (?, ?, ?, ?)
                            ''', (arq, caminho_full, origem, cat))
                            total_arquivos += 1
                        except:
                            pass

        conn.commit()

        # Resumo do resgate
        cursor.execute("SELECT origem_projeto, COUNT(*) FROM acervo_legado_completo GROUP BY origem_projeto")
        resumo = cursor.fetchall()

        print("\n============================================================")
        print(" 📦 RESUMO DO ACERVO RESGATADO NO DISCO (RÉGULOS + IOTEC)")
        print("============================================================")
        for orig, qtd in resumo:
            print(f" ├─ Origem: {orig:<20} | Total de Arquivos/Módulos: {qtd}")
        print("============================================================")
        print(f" [✔] Total Geral: {total_arquivos} módulos recuperados e prontos para empacotamento.")
        print("============================================================\n")

        conn.close()

if __name__ == "__main__":
    minerador = MineradorLegadoDisco()
    minerador.varrer_disco_c()
