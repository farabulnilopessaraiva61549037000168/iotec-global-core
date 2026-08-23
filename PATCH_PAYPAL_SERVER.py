from pathlib import Path

ARQ = Path(r"C:\IOTEC\paypal_server.py")

texto = ARQ.read_text(encoding="utf-8", errors="ignore")

if "/order-status/<order_id>" in texto:
    print("ROTA JA EXISTE")
    raise SystemExit

bloco = r'''

@app.route("/order-status/<order_id>")
def order_status(order_id):

    token = get_access_token()

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.get(
        f"{BASE_URL}/v2/checkout/orders/{order_id}",
        headers=headers
    )

    if response.status_code != 200:
        return jsonify({
            "success": False,
            "http": response.status_code,
            "response": response.text
        }), response.status_code

    dados = response.json()

    return jsonify({
        "success": True,
        "order_id": dados.get("id"),
        "status": dados.get("status"),
        "intent": dados.get("intent")
    })

'''

texto = texto.replace(
    "if __name__ == "__main__":",
    bloco + "\nif __name__ == "__main__":"
)

ARQ.write_text(texto, encoding="utf-8")

print("="*70)
print("PATCH PAYPAL SERVER")
print("="*70)
print("Rota /order-status instalada.")


