import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# DETECÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DE ALTO RETORNO
# ============================================================

def verificar_roi_alto(setor, api_nome):
    data = carregar_perf()
    chave = f"{setor}:{api_nome}"

    if chave not in data:
        return False

    roi = calcular_roi(data[chave])

    if roi > 5:
        registrar_mensagem(
            tipo="ALAVANCAGEM",
            modulo="ESTRATEGIA",
            descricao=f"ROI alto detectado em {setor} via {api_nome}.",
            impacto="Alta geraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de valor.",
            acao="Aumentar frequÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia de execuÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o.",
            prioridade="ALTA"
        )
        return True

    return False


