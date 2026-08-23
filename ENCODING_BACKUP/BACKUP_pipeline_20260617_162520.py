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
    "PRODUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O",
    "TESTE",
    "ENTREGUE"
]


def avancar_status(status_atual: str) -> str:
    idx = PIPELINE.index(status_atual)
    if idx < len(PIPELINE) - 1:
        return PIPELINE[idx + 1]
    return status_atual


