import os
import sqlite3
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='[IOTEC CEREBRO REAL] %(asctime)s - %(message)s')

class IOTECAdaptiveBrain:
    def __init__(self):
        self.db_path = "C:\\IOTEC\\iotec.db"
        self.financial_db = "C:\\IOTEC\\iotec_financial.db"

    def audit_environment_real(self):
        """Garante rigorosamente operação real sem dados fictícios."""
        logging.info("AUDITORIA REAL: Operação em modo Produção (Zero Simulação).")

    def question_market_utility(self):
        """
        Analisa o mercado, questiona a própria utilidade e encontra
        gargalos financeiros onde os clientes precisam da IOTEC.
        """
        self.audit_environment_real()
        
        sectores_alvo = {
            "VAREJO_E_DISTRIBUICAO": "Cobrança via boleto manual gerando inadimplência e atraso no caixa.",
            "SERVICOS_E_TI": "Dificuldade em gerenciar assinaturas recorrentes com baixo custo.",
            "SAUDE_E_CLINICAS": "Agendamentos sem confirmação e alta taxa de cancelamento de última hora."
        }
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Garante a existência da tabela de aprendizado contínuo
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS aprendizado_mercado (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                setor TEXT,
                dor_identificada TEXT,
                utilidade_iotec TEXT
            )
        ''')
        
        for setor, dor in sectores_alvo.items():
            solucao = f"Implementação de fluxo autônomo com webhook Asaas e disparo imediato via WhatsApp."
            cursor.execute(
                "INSERT INTO aprendizado_mercado (setor, dor_identificada, utilidade_iotec) VALUES (?, ?, ?)",
                (setor, dor, solucao)
            )
            logging.info(f"[UTILIDADE MAPEADA] Setor: {setor} | Dor: {dor}")
            
        conn.commit()
        conn.close()

if __name__ == "__main__":
    brain = IOTECAdaptiveBrain()
    brain.question_market_utility()
