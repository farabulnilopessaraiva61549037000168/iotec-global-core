import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# AURORA RISK ENGINE
# ============================================================
#
# Objetivo:
# Calcular o ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Ândice Aurora de Risco
#
# Autor da VisÃƒÆ'Ã†â€™o:
# Bruno Lopes
#
# ============================================================

from datetime import datetime
import json
import os

DATABASE_FILE = "AURORA_DATABASE.json"

# ============================================================
# CARREGAR BANCO
# ============================================================

def carregar_banco():
    pass

    if not os.path.exists(DATABASE_FILE):
        pass

        print("[ERRO] Banco Aurora nÃƒÆ'Ã†â€™o encontrado")
        return None

    with open(DATABASE_FILE, "r", encoding="utf-8") as f:
        pass

        return json.load(f)

# ============================================================
# CLASSIFICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ============================================================

def classificar_indice(indice):
    pass

    if indice <= 20:
        return "NORMAL"

    elif indice <= 40:
        return "ATENCAO"

    elif indice <= 60:
        return "ALERTA"

    elif indice <= 80:
        return "EMERGENCIA POTENCIAL"

    else:
        return "CRITICO"

# ============================================================
# CÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂLCULO DO ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂNDICE
# ============================================================

def calcular_indice():
    pass

    db = carregar_banco()

    if db is None:
        return

    eventos = len(db.get("eventos", []))
    alertas = len(db.get("alertas", []))
    fontes = len(db.get("fontes", []))

    # --------------------------------------------------------
    # Fatores iniciais
    # --------------------------------------------------------

    risco_hidrico = min(eventos * 10, 100)

    risco_agricola = min(eventos * 8, 100)

    risco_energetico = min(alertas * 7, 100)

    risco_humano = min((eventos * 5) + (alertas * 5), 100)

    # --------------------------------------------------------
    # ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Ândice Aurora
    # --------------------------------------------------------

    indice_aurora = int(

        (
            risco_hidrico +
            risco_agricola +
            risco_energetico +
            risco_humano
        ) / 4

    )

    status = classificar_indice(indice_aurora)

    # --------------------------------------------------------
    # RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO
    # --------------------------------------------------------

    print("\n================================================")
    print("AURORA RISK ENGINE")
    print("================================================\n")

    print(f"DATA ANALISE : {datetime.now()}")

    print("\nFONTES ATIVAS")
    print("-------------")
    print(fontes)

    print("\nRISCOS")
    print("-------------")

    print(f"RISCO HIDRICO    : {risco_hidrico}")
    print(f"RISCO AGRICOLA   : {risco_agricola}")
    print(f"RISCO ENERGETICO : {risco_energetico}")
    print(f"RISCO HUMANO     : {risco_humano}")

    print("\n================================================")

    print(f"INDICE AURORA : {indice_aurora}")

    print(f"STATUS        : {status}")

    print("================================================\n")

# ============================================================
# REGISTRAR RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO
# ============================================================

def salvar_relatorio():
    pass

    db = carregar_banco()

    if db is None:
        return

    eventos = len(db.get("eventos", []))
    alertas = len(db.get("alertas", []))

    indice = int(

        (
            min(eventos * 10, 100) +
            min(eventos * 8, 100) +
            min(alertas * 7, 100) +
            min((eventos * 5) + (alertas * 5), 100)

        ) / 4

    )

    status = classificar_indice(indice)

    relatorio = {

        "data": datetime.now().isoformat(),

        "indice_aurora": indice,

        "status": status

    }

    arquivo = "AURORA_RISK_REPORT.json"

    with open(
        arquivo,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            relatorio,
            f,
            ensure_ascii=False,
            indent=4
        )

    print(f"[OK] RelatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio salvo: {arquivo}")

# ============================================================
# EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ============================================================

if __name__ == "__main__":
    pass

    calcular_indice()

    salvar_relatorio()




