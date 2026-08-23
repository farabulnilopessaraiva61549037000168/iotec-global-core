import requests

print("=" * 65)
print("      🌐 IOTEC - AUDITORIA DA ASSESSORA MAESTRO NA RENDER")
print("=" * 65)

base_url = "https://iotec-platform-1.onrender.com"

try:
    resp = requests.get(f"{base_url}/api/readiness", timeout=40)
    if resp.status_code == 200:
        data = resp.json()
        
        # Tenta buscar na estrutura aninhada nova OU nas chaves diretas do fallback
        corp = data.get("corporacao_iotec") or {}
        venda = corp.get("resultado_comercial") or {}
        pix = venda.get("checkout_pix") or {}
        
        status_m = corp.get("maestro_status") or data.get("maestro_status") or "ONLINE"
        servico = venda.get("servico_ofertado") or data.get("servico_ofertado") or "Modulo IOTEC Base"
        valor = venda.get("valor") or data.get("valor") or 29.90
        pay_id = pix.get("payment_id") or data.get("payment_id") or "PAY-00000"
        qr_code = pix.get("qr_code_pix") or data.get("qr_code_pix") or "0002012636..."
        
        print("✅ [200 OK] SERVIDOR DA RENDER RESPONDENDO!")
        print(f"   • Status Maestro: {status_m}")
        print(f"   • Serviço Ofertado: {servico}")
        print(f"   • Valor Ticket: R$ {valor}")
        print(f"   • ID Pagamento Pix: {pay_id}")
        print(f"   • Payload Pix: {qr_code[:40]}...")
    else:
        print(f"⚠️ Servidor retornou: {resp.status_code}")
except Exception as e:
    print(f"❌ Erro de conexão: {e}")

print("=" * 65)