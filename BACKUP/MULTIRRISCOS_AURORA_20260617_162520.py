import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# EVENTOS MULTIRRISCOS AURORA
# ============================================================

EVENTOS = {

    # HIDROLÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œGICOS

    "SECA": 20,
    "ESTIAGEM": 15,
    "COLAPSO_HIDRICO": 60,
    "ENCHENTE": 35,
    "INUNDACAO": 40,
    "ENXURRADA": 45,
    "ROMPIMENTO_BARRAGEM": 85,

    # CLIMÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂTICOS

    "ONDA_CALOR": 25,
    "FRIO_EXTREMO": 15,
    "TEMPESTADE_SEVERA": 40,
    "GRANIZO": 30,
    "VENDAVAL": 35,
    "CICLONE": 70,
    "TORNADO": 75,

    # AMBIENTAIS

    "QUEIMADA": 30,
    "INCENDIO_FLORESTAL": 50,
    "DESERTIFICACAO": 45,
    "CONTAMINACAO_RIO": 60,

    # GEOLÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œGICOS

    "TERREMOTO": 80,
    "TSUNAMI": 95,
    "ERUPCAO_VULCANICA": 100,
    "AFUNDAMENTO_SOLO": 65,
    "EROSAO_COSTEIRA": 40,

    # INFRAESTRUTURA

    "FALHA_ENERGETICA": 25,
    "COLAPSO_TELECOM": 30,
    "QUEDA_PONTE": 70,
    "INTERRUPCAO_ABASTECIMENTO": 50,

    # HUMANITÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂRIOS

    "CRISE_ALIMENTAR": 80,
    "DESLOCAMENTO_POPULACIONAL": 70,
    "COLAPSO_ABRIGOS": 65,
    "ESCASSEZ_MEDICAMENTOS": 75

}


