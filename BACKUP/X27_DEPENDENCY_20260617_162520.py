import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 DEPENDENCY ENGINE
# ============================================================
#
# Descobre dependÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncias crÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­ticas
# e identifica causas-raiz
#
# ============================================================

from datetime import datetime

# ============================================================
# DEPENDÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â NCIAS
# ============================================================

DEPENDENCIAS = {

    "SAUDE": {

        "ENERGIA": "OK",

        "COMUNICACAO": "ALERTA",

        "LOGISTICA": "OK",

        "RECURSOS_HUMANOS": "CRITICO"

    },

    "INTERNET": {

        "ENERGIA": "ALERTA",

        "SATELITE": "OK",

        "MESH": "OK",

        "LINK_REDUNDANTE": "CRITICO"

    },

    "ABRIGOS": {

        "AGUA": "OK",

        "ENERGIA": "OK",

        "ALIMENTACAO": "ALERTA",

        "CAPACIDADE": "CRITICO"

    }

}

# ============================================================
# CAUSAS RAIZ
# ============================================================

CAUSAS = {

    "SAUDE":
        "INSUFICIENCIA DE EQUIPES",

    "INTERNET":
        "FALTA DE REDUNDANCIA",

    "ABRIGOS":
        "CAPACIDADE INSUFICIENTE"

}

# ============================================================
# ANALISE
# ============================================================

def analisar():
    pass

    print("\n================================================")

    print("X27 DEPENDENCY ENGINE")

    print("================================================")

    print(f"DATA : {datetime.now()}")

    for setor, deps in DEPENDENCIAS.items():
        pass

        print("\n------------------------------------------------")

        print(f"SETOR : {setor}")

        print("\nDEPENDENCIAS:")

        impacto = "BAIXO"

        for dep, status in deps.items():
            pass

            print(f"{dep:<25} {status}")

            if status == "CRITICO":
                pass

                impacto = "ALTO"

        print("\nIMPACTO:")

        print(impacto)

        print("\nCAUSA RAIZ:")

        print(CAUSAS[setor])

# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    pass

    analisar()


