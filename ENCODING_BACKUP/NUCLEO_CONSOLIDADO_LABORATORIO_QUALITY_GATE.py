import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC - QUALITY GATE (bloqueio de liberaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o)
# ============================================================

def validar_interface(resultados):
    """
    resultados = {
        "botoes_ok": True,
        "contraste_ok": True,
        "responsivo_ok": True,
        "erros_tratados": True,
        "animacoes_ok": True
    }
    """
    falhas = [k for k, v in resultados.items() if not v]

    if falhas:
        print("ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ BLOQUEADO - Falhas detectadas:")
        for f in falhas:
            print("-", f)
        return False

    print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ APROVADO - Interface pronta para liberaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o")
    return True


# SimulaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o
resultado_teste = {
    "botoes_ok": True,
    "contraste_ok": True,
    "responsivo_ok": True,
    "erros_tratados": True,
    "animacoes_ok": True
}

validar_interface(resultado_teste)


