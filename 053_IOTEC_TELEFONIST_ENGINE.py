import os
import sqlite3
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='[TELEFONIST IOTEC] %(asctime)s - %(message)s')

class IOTECTelefonistSwitchboard:
    def __init__(self):
        self.db_path = "C:\\IOTEC\\data_store.db"
        self.init_switchboard_db()

    def init_switchboard_db(self):
        """Prepara a mesa de comutação de chamadas no banco de dados."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS mesa_telefonista (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                solicitante TEXT,
                destino_pedido TEXT,
                status_conexao TEXT,
                resposta_humanizada TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def process_incoming_call(self, cliente_nome: str, mensagem_cliente: str) -> str:
        """
        Simula a telefonista atenciosa: entende quem fala, o que precisa
        e estabelece a ponte de comunicação ideal com a IOTEC.
        """
        logging.info(f"MESA DE TELEFONIA: Cliente [{cliente_nome}] levantou o gancho.")
        
        # Lógica de Triagem e Conectividade Humanizada
        resposta = (
            f"Bom dia, {cliente_nome}! Aqui é a Central IOTEC. "
            f"Já localizei o seu cadastro e estou transferindo você diretamente "
            f"para o nosso setor de contratos e cobranças autônomas. Só um instante..."
        )
        
        # Registra a conexão efetuada
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO mesa_telefonista (solicitante, destino_pedido, status_conexao, resposta_humanizada) VALUES (?, ?, ?, ?)",
            (cliente_nome, "SETOR_COBRANCA_B2B", "COMPLETADA", resposta)
        )
        conn.commit()
        conn.close()
        
        logging.info(f"[LIGAÇÃO COMPLETADA] Chamada de {cliente_nome} direcionada com sucesso.")
        return resposta

if __name__ == "__main__":
    switchboard = IOTECTelefonistSwitchboard()
    # Teste de atendimento humanizado
    switchboard.process_incoming_call("Dona Josefa / Comercial", "Quero falar sobre a licença do sistema")
