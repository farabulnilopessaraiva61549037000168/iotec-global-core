import sqlite3
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='[DETETIVE IOTEC] %(asctime)s - %(message)s')

class IOTECDetetiveConsultor:
    def __init__(self):
        self.db_kernel = "C:\\IOTEC\\iotec_kernel.db"
        self.init_detetive_brain()

    def init_detetive_brain(self):
        """Cria o banco de rotinas e momentos de oportunidade das empresas."""
        conn = sqlite3.connect(self.db_kernel)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS inteligencia_empresarial (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cnpj TEXT UNIQUE,
                razao_social TEXT,
                rotina_diaria TEXT,
                momento_crise TEXT,
                gatilho_compra TEXT,
                melhor_horario_contato TEXT,
                status_inteligencia TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def assimilar_e_antecipar(self):
        """Analisa os dados das empresas e traça o perfil de oportunidade exato."""
        logging.info("=== DETETIVE CONSULTOR: Mapeando rotinas e antecipando necessidades ===")
        
        conn = sqlite3.connect(self.db_kernel)
        cursor = conn.cursor()
        
        # Lê empresas qualificadas do banco
        cursor.execute("SELECT cnpj, razao_social, setor, gargalo_principal FROM empresas_qualificadas")
        empresas = cursor.fetchall()
        
        for emp in empresas:
            cnpj, razao, setor, gargalo = emp
            
            # Análise preditiva do perfil conforme o setor
            if "VAREJO" in setor or "DISTRIBUICAO" in setor:
                rotina = "Pico de faturamento quinzenal (dias 5 e 20). Alta liquidação de estoques."
                crise = "Inadimplência elevada em boletos bancários de 30/60 dias."
                gatilho = "Oferecer conciliação Pix imediata antes da rodada de pagamentos de fornecedores."
                horario = "Segunda a Quinta, das 09:30 às 11:30"
            else:
                rotina = "Fechamento de contratos recorrentes e licenças no final do mês."
                crise = "Perda de margem com taxas altas de gateways de cartão e boletos."
                gatilho = "Apresentar cobrança automatizada via Pix Asaas com emissão de nota automática."
                horario = "Terça a Sexta, das 14:00 às 16:30"

            cursor.execute('''
                INSERT OR REPLACE INTO inteligencia_empresarial 
                (cnpj, razao_social, rotina_diaria, momento_crise, gatilho_compra, melhor_horario_contato, status_inteligencia)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (cnpj, razao, rotina, crise, gatilho, horario, "SOLUCAO_PRONTA"))

            print(f"\n[ALVO SOB OBSERVAÇÃO]: {razao} ({cnpj})")
            print(f" ├─ Rotina Identificada: {rotina}")
            print(f" ├─ Ponto de Crise: {crise}")
            print(f" ├─ Gatilho Perfeito: {gatilho}")
            print(f" └─ Janela Ideal de Contato: {horario}")

        conn.commit()
        conn.close()

if __name__ == "__main__":
    detetive = IOTECDetetiveConsultor()
    detetive.assimilar_e_antecipar()
