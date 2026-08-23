import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# INJEÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O ÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂNIBUS 03: InteligÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia de SobrevivÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia
def protocolo_autossobrevivencia(ciclo, clientes_inativos, oportunidades_mortas):
    """
    EstratÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©gia de reinicializaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o para salvar o dia:
    - Recontatar leads esquecidos
    - Reaproveitar propostas nÃƒÆ'Ã†â€™o finalizadas
    - Publicar oferta automÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡tica com base em estoque digital
    """
    if ciclo == "encerramento" and not houve_lucro():
        contatos = recontatar_clientes(clientes_inativos)
        produtos = reciclar_propostas(oportunidades_mortas)
        publicar_ofertas_automaticas(contatos, produtos)


