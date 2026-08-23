import uuid
import requests
import logging

logging.basicConfig(level=logging.INFO, format='[MESA-NEGOCIACAO-IOTEC] %(message)s')

MERCADO_PAGO_TOKEN = "APP_USR-6181905353270296-072908-78bbbbe69e0e9d7df828a6037067be76-1263677665"

def criar_cobranca_pix(valor, descricao, email_cliente):
    url = "https://api.mercadopago.com/v1/payments"
    
    idempotency_key = str(uuid.uuid4())
    
    headers = {
        "Authorization": f"Bearer {MERCADO_PAGO_TOKEN}",
        "Content-Type": "application/json",
        "X-Idempotency-Key": idempotency_key
    }
    
    payload = {
        "transaction_amount": float(valor),
        "description": descricao,
        "payment_method_id": "pix",
        "payer": {
            "email": email_cliente
        }
    }
    
    try:
        logging.info(f"Gerando cobrança Pix de R$ {valor:.2f} para {email_cliente}...")
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code in [200, 201]:
            data = response.json()
            pix_copia_cola = data.get("point_of_interaction", {}).get("transaction_data", {}).get("qr_code")
            qr_code_base64 = data.get("point_of_interaction", {}).get("transaction_data", {}).get("qr_code_base64")
            payment_id = data.get("id")
            
            return {
                "status": "sucesso",
                "payment_id": payment_id,
                "pix_copia_cola": pix_copia_cola,
                "qr_code_base64": qr_code_base64
            }
        else:
            logging.error(f"Erro na API do Gateway: {response.status_code} - {response.text}")
            return {"status": "erro", "detalhes": response.text}
            
    except Exception as e:
        logging.error(f"Falha de conexão com o Gateway de Pagamentos: {e}")
        return {"status": "erro", "detalhes": str(e)}
