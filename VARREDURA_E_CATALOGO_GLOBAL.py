import os
import sqlite3
import json
import re

DB_PATH = "C:\\IOTEC\\iotec.db"
BASE_DIR = "C:\\IOTEC"

def inicializar_catalogo_global():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS catalogo_global_produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo_produto TEXT UNIQUE,
            nome_solucao TEXT,
            categoria_nicho TEXT,
            polo_alvo TEXT,
            ticket_sugerido REAL,
            descricao_comercial TEXT,
            arquivo_origem TEXT
        )
    ''')
    conn.commit()
    conn.close()

class ResgatadorLegadoIOTEC:
    def __init__(self):
        inicializar_catalogo_global()

    def varrer_e_catalogar(self):
        print("============================================================")
        print("   IOTEC CORE — VARREDURA DE ACERVO E CATALOGAÇÃO GLOBAL   ")
        print("============================================================\n")

        arquivos = [f for f in os.listdir(BASE_DIR) if f.endswith('.py')]
        print(f"🔍 [VARREDURA] {len(arquivos)} scripts encontrados no repositório local.")

        # Matriz de classificação por polo e setor econômico
        categorias = {
            "FINANCEIRO_TESOURARIA": ("Polo Financeiro & Serviços", 490.00, ["caixa", "pagamento", "paypal", "pix", "faturamento", "cobrança", "auditoria"]),
            "LOGISTICA_CORREDOR": ("Corredores Logísticos & Frotas", 890.00, ["frota", "rota", "combustivel", "rastreamento", "logistica", "transporte"]),
            "INDUSTRIA_E_ENG": ("Polos Industriais & Engenharia", 1200.00, ["obra", "insumo", "construcao", "medicao", "fabricacao", "projeto"]),
            "AGRO_E_DISTRIBUICAO": ("Polos Agropecuários & Atacado", 750.00, ["mineradora", "carga", "mídia", "broadcast", "leads"]),
            "AUTOMACAO_COMERCIAL": ("Varejo & Serviços Locais", 290.00, ["crm", "vendas", "callcenter", "whatsapp", "sac", "onboarding"])
        }

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        catalogados = 0
        for arq in arquivos:
            caminho_completo = os.path.join(BASE_DIR, arq)
            try:
                with open(caminho_completo, 'r', encoding='utf-8', errors='ignore') as f:
                    conteudo = f.read().lower()

                # Identifica a categoria relevante
                categoria_fit = "OUTROS_SERVICOS"
                polo_fit = "Global"
                ticket = 350.00

                for cat, info in categorias.items():
                    polo, val, keywords = info
                    if any(kw in conteudo for kw in keywords) or any(kw in arq.lower() for kw in keywords):
                        categoria_fit = cat
                        polo_fit = polo
                        ticket = val
                        break

                nome_limpo = arq.replace(".py", "").replace("_", " ").upper()
                cod_prod = f"PROD-{hash(arq) & 0xffff:04X}"

                cursor.execute('''
                    INSERT OR REPLACE INTO catalogo_global_produtos
                    (codigo_produto, nome_solucao, categoria_nicho, polo_alvo, ticket_sugerido, descricao_comercial, arquivo_origem)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                    cod_prod, 
                    nome_limpo, 
                    categoria_fit, 
                    polo_fit, 
                    ticket, 
                    f"Solução proprietária IOTEC do módulo {arq}", 
                    arq
                ))
                catalogados += 1

            except Exception as e:
                continue

        conn.commit()
        
        # Exibe resumo do catálogo catalogado
        cursor.execute("SELECT categoria_nicho, COUNT(*), AVG(ticket_sugerido) FROM catalogo_global_produtos GROUP BY categoria_nicho")
        resumo = cursor.fetchall()

        print("============================================================")
        print(" 📦 NOVO CATÁLOGO DIVERSIFICADO IOTEC (PRONTO PARA COMPRAS)")
        print("============================================================")
        for cat, qtd, avg_t in resumo:
            print(f" ├─ Categoria: {cat:<25} | {qtd:>3} Soluções | Ticket Médio: R$ {avg_t:,.2f}")
        print("============================================================")
        print(f" [✔] Total de {catalogados} frentes de produtos catalogadas no iotec.db!")
        print("============================================================\n")

        conn.close()

if __name__ == "__main__":
    resgatador = ResgatadorLegadoIOTEC()
    resgatador.varrer_e_catalogar()
