import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
PIPELINE = [

    "CAPTADO",

    "PROPOSTA",

    "FECHADO",

    "PRODUÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O",

    "TESTE",

    "ENTREGUE"

]





def avancar_status(status_atual: str) -> str:
    pass

    idx = PIPELINE.index(status_atual)

    if idx < len(PIPELINE) - 1:
        pass

        return PIPELINE[idx + 1]

    return status_atual






