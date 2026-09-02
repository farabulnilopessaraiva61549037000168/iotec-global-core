import os
import requests
import logging

logging.basicConfig(level=logging.INFO, format='[IOTEC EVOLUTION] %(asctime)s - %(message)s')

class EvolutionWhatsAppEngine:
    def __init__(self):
        self.api_url = os.getenv("EVOLUTION_API_URL", "https://sua-evolution-api.onrender.com").rstrip('/')
        self.api_key = os.getenv("EVOLUTION_API_KEY", "SUA_CHAVE_DEFINIDA")
        self.headers = {"apikey": self.api_key, "Content-Type": "application/json"}

    def send_message(self, number: str, text: str, instance="IOTEC_WHATSAPP"):
        endpoint = f"{self.api_url}/message/sendText/{instance}"
        payload = {"number": number, "text": text}
        try:
            res = requests.post(endpoint, json=payload, headers=self.headers, timeout=8)
            logging.info(f"Envio para {number} | HTTP {res.status_code}")
            return res.json()
        except Exception as e:
            logging.error(f"Erro ao disparar via Evolution: {e}")
            return None

if __name__ == "__main__":
    engine = EvolutionWhatsAppEngine()
    logging.info("Motor Evolution ativado e operacional.")
