import sqlite3
import json
import datetime

class BrainiacStrategicMemory:
    def __init__(self):
        self.db_path = "iotec.db"
        self.strategic_directives = {
            "valuation_target_brl": "R$ 1.800.000,00 a R$ 10.700.000,00",
            "valuation_target_usd": "US$ 325.000 a US$ 1.950.000",
            "aesthetic_signature": "High-Ticket Minimal / Soft Ocean / Tone Pastel",
            "expansion_hubs": ["Nordeste-Core", "Arterias Logisticas", "Emirates/Dubai", "Miami", "Lisboa"],
            "ticket_pricing": "R$ 299,00/mes (BRL) | US$ 53,82/mes (USD)",
            "cadence_safety": "300 abordagens/dia (150 novas / 150 follow-ups)",
            "checkout_gateways": ["PayPal", "PicPay", "Pix", "Stripe Global"]
        }

    def assimilate_directives(self):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        
        # Cria tabela de diretrizes estrategicas caso nao exista
        cur.execute("""
            CREATE TABLE IF NOT EXISTS brainiac_memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT UNIQUE,
                value TEXT,
                updated_at TEXT
            )
        """)
        
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for key, val in self.strategic_directives.items():
            val_str = json.dumps(val, ensure_ascii=False) if isinstance(val, list) else str(val)
            cur.execute("""
                INSERT INTO brainiac_memory (key, value, updated_at)
                VALUES (?, ?, ?)
                ON CONFLICT(key) DO UPDATE SET value=excluded.value, updated_at=excluded.updated_at
            """, (key, val_str, now))
            
        conn.commit()
        conn.close()
        
        print("======================================================================")
        print(" 🧠 BRAINIAC CORE - MEMÓRIA ESTRATÉGICA E PATRIMONIAL ATUALIZADA      ")
        print("======================================================================")
        print(" • Diretrizes Assimiladas : Valuation, Artérias, Estética e Hubs Globais")
        print(" • Alvo de Valuation (USD):", self.strategic_directives["valuation_target_usd"])
        print(" • Padrão Estético        :", self.strategic_directives["aesthetic_signature"])
        print(" • Status no iotec.db     : Gravado na tabela 'brainiac_memory'")
        print("======================================================================")

if __name__ == "__main__":
    memory = BrainiacStrategicMemory()
    memory.assimilate_directives()
