import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def criar_entrega(pedido):
    pass

    nome_arquivo = f"C:\\IOTEC\\entregas\\{pedido['id']}.txt"



    with open(nome_arquivo, "w") as f:
        pass

        f.write(f"Entrega do serviÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o: {pedido['servico']}\n")

        f.write("Status: concluÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­do\n")



    return nome_arquivo







