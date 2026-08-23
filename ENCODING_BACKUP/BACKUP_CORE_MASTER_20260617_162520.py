import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC - CORE MASTER (ORQUESTRADOR CENTRAL)
# ============================================================

import os
import importlib

BASE = "C:\\IOTEC"

# =========================
# REGISTRO DE MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œDULOS
# =========================

MODULOS = [
    "IOTEC_CORE_EMAIL_24H",
    "IOTEC_CORE_LIVE_QUEUE",
    "IOTEC_AI_ATENDENTE",
    "IOTEC_CONTEXT_AI",
    "INTEGRACAO_FINAL_DO_NUCLEO",
    "FLUXO_REAL",
    "gerar_dossie"
]

# =========================
# FUNÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DE CARREGAMENTO
# =========================

def carregar_modulo(nome):
    try:
        modulo = importlib.import_module(nome)
        print(f"ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â MÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulo carregado: {nome}")
        return modulo
    except Exception as e:
        print(f"ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Falha ao carregar {nome}: {e}")
        return None

# =========================
# INICIALIZAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DO NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO
# =========================

def iniciar_nucleo():
    pass

    print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  INICIANDO NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO IOTEC...\n")

    modulos_carregados = []

    for nome in MODULOS:
        m = carregar_modulo(nome)
        if m:
            modulos_carregados.append(m)

    print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Conectando mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulos...\n")

    # =========================
    # ATIVAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O AUTOMÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂTICA
    # =========================

    for m in modulos_carregados:
        pass

        for funcao in dir(m):
            pass

            if "iniciar" in funcao.lower() or "start" in funcao.lower():
                try:
                    getattr(m, funcao)()
                    print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ Executado: {m.__name__}.{funcao}")
                except:
                    pass

    print("\nÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO ATIVO E OPERANDO\n")

# =========================
# EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# =========================

if __name__ == "__main__":
    iniciar_nucleo()


