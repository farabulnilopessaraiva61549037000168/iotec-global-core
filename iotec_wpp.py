import requests

WPP_URL = "http://localhost:21465"

def enviar_mensagem(telefone: str, mensagem: str):
    """Envia mensagem de texto via WPPConnect local."""
    try:
        payload = {"phone": telefone, "message": mensagem}
        res = requests.post(f"{WPP_URL}/send-message", json=payload, timeout=15)
        return res.json()
    except Exception as e:
        return {"status": "error", "error": str(e)}

def enviar_boleto(telefone: str, caminho_pdf: str, nome_arquivo: str = "Boleto_IOTEC.pdf", mensagem: str = ""):
    """Envia arquivo de boleto/fatura em PDF via WPPConnect local."""
    try:
        payload = {
            "phone": telefone,
            "filePath": caminho_pdf,
            "filename": nome_arquivo,
            "caption": mensagem
        }
        res = requests.post(f"{WPP_URL}/send-file", json=payload, timeout=30)
        return res.json()
    except Exception as e:
        return {"status": "error", "error": str(e)}

if __name__ == "__main__":
    # Teste rápido
    num = "88992073886"
    print("Testando disparo via Python...")
    print(enviar_mensagem(num, "🤖 *IOTEC Core Python*: Módulo de integração validado com sucesso!"))