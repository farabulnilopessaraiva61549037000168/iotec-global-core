import os
import sqlite3
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='[IOTEC CHAT] %(asctime)s - %(message)s')

DB_PATH = "C:\\IOTEC\\data_store.db"

def init_chat_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS live_chat_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            remetente TEXT,
            numero TEXT,
            mensagem TEXT,
            direcao TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/webhook/evolution/messages', methods=['POST'])
def receive_message_event():
    data = request.json
    try:
        msg_data = data.get('data', {})
        key = msg_data.get('key', {})
        from_me = key.get('fromMe', False)
        number = key.get('remoteJid', '').split('@')[0]
        
        message = msg_data.get('message', {}).get('conversation') or \
                  msg_data.get('message', {}).get('extendedTextMessage', {}).get('text', '')

        direcao = "ENVIADO (AGENTE)" if from_me else "RECEBIDO (CLIENTE)"
        remetente = "AGENTE_IOTEC" if from_me else number

        if message:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO live_chat_logs (remetente, numero, mensagem, direcao) VALUES (?, ?, ?, ?)",
                (remetente, number, message, direcao)
            )
            conn.commit()
            conn.close()
            logging.info(f"[{direcao}] {number}: {message}")

        return jsonify({"status": "SUCCESS"}), 200
    except Exception as e:
        logging.error(f"Erro ao processar mensagem: {e}")
        return jsonify({"status": "ERROR", "message": str(e)}), 500

if __name__ == "__main__":
    init_chat_db()
    app.run(host='0.0.0.0', port=5001)
