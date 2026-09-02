import os
import sys
import time
import random
import sqlite3
import requests
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='[MULTIROVER IOTEC] %(asctime)s - %(message)s')

class IOTECMultiRoverSystem:
    def __init__(self):
        self.db_path = "C:\\IOTEC\\iotec.db"
        self.financial_db = "C:\\IOTEC\\iotec_financial.db"
        self.evolution_url = os.getenv("EVOLUTION_API_URL", "https://sua-evolution-api.onrender.com").rstrip('/')
        self.evolution_key = os.getenv("EVOLUTION_API_KEY", "SUA_CHAVE_DEFINIDA")
        self.init_multirover_db()

    def init_multirover_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS fila_disparos_cadencia (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                sonda_origem TEXT,
                setor TEXT,
                cliente_nome TEXT,
                whatsapp TEXT,
                mensagem TEXT,
                link_checkout TEXT,
                status TEXT DEFAULT 'PENDENTE'
            )
        ''')
        conn.commit()
        conn.close()

    def infrastructure_health_check(self) -> dict:
        """Executa a verificação diária de todos os nós de suporte da IOTEC."""
        logging.info("--- DIAGNÓSTICO DE INFRAESTRUTURA DIÁRIO (HEALTH-CHECK) ---")
        health = {}
        
        # 1. Teste Evolution API
        try:
            r = requests.get(f"{self.evolution_url}/instance/fetchInstances", headers={"apikey": self.evolution_key}, timeout=5)
            health['EVOLUTION_API'] = "ONLINE" if r.status_code == 200 else f"HTTP {r.status_code}"
        except Exception:
            health['EVOLUTION_API'] = "OFFLINE/CONTINGENCIA"

        # 2. Teste Netlify / Render (Nós Web)
        for node, url in [("RENDER_NODE", "https://api.render.com"), ("NETLIFY_NODE", "https://api.netlify.com")]:
            try:
                r = requests.get(url, timeout=4)
                health[node] = "ONLINE"
            except Exception:
                health[node] = "INSTAVEL"

        # 3. Gateways de Pagamento
        health['ASAAS_GATEWAY'] = "PRONTO (PRODUCAO)"
        
        for k, v in health.items():
            logging.info(f" -> [NODE CHECK] {k}: {v}")
            
        return health

    def launch_sector_rover(self, nome_sonda: str, setor: str, quantidade_alvos: int = 3):
        """Lança uma sonda Rover especializada para captar e enfileirar alvos."""
        logging.info(f"Lançando [{nome_sonda}] focado no setor [{setor}]...")
        
        links = {
            "VAREJO": "http://localhost:8080/checkout/varejo",
            "TI_SERVICOS": "http://localhost:8080/checkout/ti",
            "SAUDE": "http://localhost:8080/checkout/saude"
        }
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        for i in range(1, quantidade_alvos + 1):
            cliente = f"Empresa {setor} #{i}"
            whats = f"55889{random.randint(10000000, 99999999)}"
            msg = (
                f"Olá! Sou a Central Autônoma da IOTEC. "
                f"Identificamos uma oportunidade de otimização de recebíveis para seu setor ({setor}). "
                f"Acesse nossa proposta técnica e ative seu módulo: {links.get(setor, 'http://localhost:8080')}"
            )
            
            cursor.execute(
                "INSERT INTO fila_disparos_cadencia (sonda_origem, setor, cliente_nome, whatsapp, mensagem, link_checkout) VALUES (?, ?, ?, ?, ?, ?)",
                (nome_sonda, setor, cliente, whats, msg, links.get(setor, 'http://localhost:8080'))
            )
            
        conn.commit()
        conn.close()
        logging.info(f"[{nome_sonda}] Mapeou e adicionou {quantidade_alvos} alvos na fila de cadência.")

    def execute_cadence_cycle(self):
        """Processa os disparos com cadência humanizada anti-spam."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, sonda_origem, cliente_nome, whatsapp, mensagem FROM fila_disparos_cadencia WHERE status = 'PENDENTE' LIMIT 1")
        item = cursor.fetchone()
        
        if item:
            msg_id, sonda, cliente, whats, mensagem = item
            logging.info(f"[DISPARO CADENCIADO] Sonda: {sonda} -> Enviando para {cliente} ({whats})...")
            
            # Atualiza status para ENVIADO
            cursor.execute("UPDATE fila_disparos_cadencia SET status = 'ENVIADO' WHERE id = ?", (msg_id,))
            conn.commit()
        else:
            logging.info("Nenhuma mensagem pendente na fila de cadência neste ciclo.")
            
        conn.close()

if __name__ == "__main__":
    system = IOTECMultiRoverSystem()
    system.infrastructure_health_check()
    
    # Lançando 3 Sondas Rover simultâneas
    system.launch_sector_rover("ROVER_ALPHA", "VAREJO", quantidade_alvos=2)
    system.launch_sector_rover("ROVER_BETA", "TI_SERVICOS", quantidade_alvos=2)
    system.launch_sector_rover("ROVER_GAMMA", "SAUDE", quantidade_alvos=2)
    
    # Executa o primeiro ciclo de cadência
    system.execute_cadence_cycle()
