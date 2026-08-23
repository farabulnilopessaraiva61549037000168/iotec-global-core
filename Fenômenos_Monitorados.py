import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
FENOMENOS = [

    "SECA",
    "ESTIAGEM_PROLONGADA",
    "ENCHENTE",
    "INCENDIO_FLORESTAL",
    "ONDA_DE_CALOR",
    "ONDA_DE_FRIO",
    "COLAPSO_ENERGETICO",
    "COLAPSO_LOGISTICO",
    "COLAPSO_COMUNICACAO",
    "FALHA_GPS",
    "PRAGAS_AGRICOLAS",
    "DOENCAS_ANIMAIS",
    "CRISE_HUMANITARIA"

]




