import sqlite3
import logging

logging.basicConfig(level=logging.INFO, format='[ROVER OTA] %(asctime)s - %(message)s')

def update_rover_knowledge():
    conn = sqlite3.connect("C:\\IOTEC\\iotec_kernel.db")
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS firmware_conhecimento (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            versao TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            diretriz TEXT,
            status TEXT
        )
    ''')
    
    # Injeta a diretriz de autonomia e evolução contínua
    cursor.execute(
        "INSERT INTO firmware_conhecimento (versao, diretriz, status) VALUES (?, ?, ?)",
        ("v2.4_AUTONOMOUS", "Operação local independente + Atualização contínua de estratégias B2B", "EMBARCADO")
    )
    
    conn.commit()
    conn.close()
    logging.info("Novo conhecimento técnico e comercial gravado com sucesso nos discos do Rover.")

if __name__ == "__main__":
    update_rover_knowledge()
