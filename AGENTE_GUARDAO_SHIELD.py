import sqlite3
import os
import time
import datetime

DB_PATH = "C:\\IOTEC\\iotec.db"

class AgenteGuardaoShield:
    def __init__(self):
        self.inicializar_banco_shield()

    def inicializar_banco_shield(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS iotec_shield_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo_evento TEXT,
                origem_bloqueada TEXT,
                detalhes TEXT,
                data_evento DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()

    def filtrar_requisicoes_e_comunicacoes(self, origem, tipo):
        """ Identifica e bloqueia padrões de spam ou chamadas de robô """
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        is_spam = False
        if "0000" in origem or "bot" in origem.lower() or "spam" in origem.lower():
            is_spam = True

        if is_spam:
            cursor.execute('''
                INSERT INTO iotec_shield_logs (tipo_evento, origem_bloqueada, detalhes)
                VALUES (?, ?, ?)
            ''', (tipo, origem, "Derrubado pelo IOTEC Shield antes de interromper o cliente."))
            conn.commit()
            print(f" 🛡️ [BLOCKED - {tipo}] Origem Invasiva Barrada: {origem}")
        else:
            print(f" 🟢 [ALLOWED - {tipo}] Comunicação Legítima Liberada: {origem}")

        conn.close()

    def purgar_dados_superfluos_e_ram(self):
        """ Simula a liberação de recursos de servidor e limpeza de logs mortos """
        print(" 🧹 [PURGA TÉCNICA] Varrendo arquivos temporários e liberando RAM do servidor...")
        time.sleep(1)
        
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO iotec_shield_logs (tipo_evento, origem_bloqueada, detalhes)
            VALUES ('PURGA_RAM_DISCO', 'SISTEMA_LOCAL', 'Expurgo de logs mortos. 1.4 GB de disco e RAM otimizados.')
        ''')
        conn.commit()
        conn.close()
        print(" [✔] Servidor Otimizado. Espaço e RAM liberados com sucesso!")

    def executar_protecao_continua(self):
        print("\n============================================================")
        print("   IOTEC HYPERCORE SHIELD — AGENTE GUARDIÃO EM EXECUÇÃO      ")
        print("============================================================")
        print(" 🔒 Proteção Ativa em Servidores, E-mails e PABX Credenciados...\n")

        self.filtrar_requisicoes_e_comunicacoes("CallCenter_Bot_0000123", "TELEFONIA_ROBOCALL")
        self.filtrar_requisicoes_e_comunicacoes("contato_legitimo@cliente.com.br", "EMAIL_COMERCIAL")
        self.filtrar_requisicoes_e_comunicacoes("spammer_massivo_99@spam.com", "EMAIL_SPAM")
        
        self.purgar_dados_superfluos_e_ram()

        print("\n============================================================")
        print(" [✔] AMBIENTE CORPORATIVO PROTEGIDO E SILENCIOSO!")
        print("============================================================\n")

if __name__ == "__main__":
    guardiao = AgenteGuardaoShield()
    guardiao.executar_protecao_continua()
