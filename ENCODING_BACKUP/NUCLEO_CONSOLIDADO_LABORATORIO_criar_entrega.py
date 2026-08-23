import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def criar_entrega(pedido):
    nome_arquivo = f"C:\\IOTEC\\entregas\\{pedido['id']}.txt"

    with open(nome_arquivo, "w") as f:
        f.write(f"Entrega do serviÃƒÆ'Ã†â€™o: {pedido['servico']}\n")
        f.write("Status: concluÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­do\n")

    return nome_arquivo



