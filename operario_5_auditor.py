import os
import mercadopago
from dotenv import load_dotenv

load_dotenv()

def verificar_caixa_mercadopago():
    token = os.getenv("MERCADOPAGO_ACCESS_TOKEN") or "APP_USR-561773473993112-072908-8b6a47ee7d27ead1ad1a2efe465c7c6a-3575880146"
    sdk = mercadopago.SDK(token)
    
    # Busca pagamentos com status 'approved'
    search_result = sdk.payment().search({"filters": {"status": "approved"}})
    results = search_result.get("response", {}).get("results", [])
    
    total_receita = sum(p.get("transaction_amount", 0) for p in results)
    clientes_confirmados = len(results)
    
    return clientes_confirmados, total_receita

if __name__ == "__main__":
    clientes, receita = verificar_caixa_mercadopago()
    print(f"[AGENTE 5 MP] Clientes Confirmados: {clientes} | Receita Acumulada: R$ {receita:.2f}")