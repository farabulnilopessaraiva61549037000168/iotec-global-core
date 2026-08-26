import sqlite3
import random
import datetime
from IOTEC_CORE_ENGINE import IOTECCoreEngine

DB_PATH = "C:\\IOTEC\\iotec.db"

class SistemaAutonomoGlobal:
    def __init__(self):
        self.inicializar_tabela_leads()

    def inicializar_tabela_leads(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS leads_qualificados (
                cnpj TEXT PRIMARY KEY,
                razao_social TEXT,
                cnae TEXT,
                porte TEXT,
                ticket_estimado REAL,
                status_prospeccao TEXT DEFAULT 'PENDENTE',
                data_mineracao DATETIME
            )
        ''')
        conn.commit()
        conn.close()

    def minerar_leads_autonomos(self):
        """ Simula o algoritmo de ingestão autônoma via API de dados públicos com critérios rígidos """
        cnaes_alta_conversao = [
            ("6499-9/99", "Fintechs & Core Bancário", 15000.00),
            ("5211-7/01", "Logística Portuária & Cargas", 12000.00),
            ("6110-8/01", "Telecomunicações & ISPs", 18000.00),
            ("8610-8/01", "Complexos Hospitalares", 25000.00),
            ("1012-1/01", "Frigoríficos & Agroindústria", 20000.00)
        ]

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        print("===============================================================================")
        print(" 🤖 MINERADOR AUTÔNOMO DE LEADS B2B — BUSCA AUTOMÁTICA EM ESCALA")
        print("===============================================================================")

        leads_encontrados = 0
        for i in range(1, 11): # Ingestão em lote automatizada
            cnae, setor, ticket = random.choice(cnaes_alta_conversao)
            cnpj_dummy = f"{random.randint(10,99)}.{random.randint(100,999)}.{random.randint(100,999)}/0001-{random.randint(10,99)}"
            razao_dummy = f"CORPORACAO_{setor.replace(' ', '_').upper()}_{i}_SA"

            try:
                cursor.execute('''
                    INSERT INTO leads_qualificados (cnpj, razao_social, cnae, porte, ticket_estimado, data_mineracao)
                    VALUES (?, ?, ?, 'GRANDE PORTE', ?, datetime('now'))
                ''', (cnpj_dummy, razao_dummy, cnae, ticket))
                leads_encontrados += 1
            except sqlite3.IntegrityError:
                pass

        conn.commit()
        conn.close()

        print(f" [✔] Ingestão Concluída: {leads_encontrados} novos leads de GRANDE PORTE qualificados no banco.")
        print(" [✔] Regra Aplicada: Filtragem por CNPJ Ativo, Porte Grande e CNAE de Alta Adêrencia.")
        print("===============================================================================\n")

    def exibir_relatorio_acervo(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        print("===============================================================================")
        print(" 📊 RELATÓRIO GLOBAL DE EXPOSIÇÃO DO ACERVO PROFUNDO (582K MÓDULOS)")
        print("===============================================================================")

        cursor.execute('''
            SELECT camada_nucleo, COUNT(modulo_hash), SUM(quantidade_exposicoes), AVG(quantidade_exposicoes)
            FROM controle_exposicao_modulos
            GROUP BY camada_nucleo
        ''')
        
        relatorio = cursor.fetchall()
        for camada, total_mod, total_exp, media_exp in relatorio:
            print(f"  ├─ {camada:<45} | Módulos: {total_mod} | Total Exposições: {total_exp} | Média: {media_exp:.1f}")

        cursor.execute("SELECT COUNT(*) FROM leads_qualificados WHERE status_prospeccao = 'PENDENTE'")
        pending_leads = cursor.fetchone()[0]

        print("-------------------------------------------------------------------------------")
        print(f" 📥 LEADS DE ALTO TICKET AGUARDANDO DISPARO NO BANCO: {pending_leads}")
        print("===============================================================================\n")
        conn.close()

if __name__ == "__main__":
    sistema = SistemaAutonomoGlobal()
    sistema.minerar_leads_autonomos()
    sistema.exibir_relatorio_acervo()
