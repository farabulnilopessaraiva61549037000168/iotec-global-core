import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 INTELLIGENCE ENGINE
# ============================================================

from datetime import datetime
import random

# ============================================================
# CLASSIFICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ============================================================

def classificar(valor):
    pass

    if valor >= 80:
        return "CRITICO"

    elif valor >= 60:
        return "ALERTA"

    elif valor >= 40:
        return "ATENCAO"

    return "NORMAL"

# ============================================================
# NODE AGUA
# ============================================================

def analisar_agua():
    pass

    reservatorio = random.randint(5, 100)

    status = classificar(100 - reservatorio)

    print("\n================================================")
    print("NODE AGUA")
    print("================================================")

    print(f"RESERVATORIOS : {reservatorio}%")

    print(f"STATUS        : {status}")

    if reservatorio < 20:
        pass

        print("\nACOES:")

        print("- Acionar caminhÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes-pipa")
        print("- Priorizar hospitais")
        print("- Priorizar escolas")
        print("- Monitoramento contÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­nuo")

# ============================================================
# NODE SAUDE
# ============================================================

def analisar_saude():
    pass

    leitos = random.randint(0, 100)

    status = classificar(100 - leitos)

    print("\n================================================")
    print("NODE SAUDE")
    print("================================================")

    print(f"LEITOS LIVRES : {leitos}")

    print(f"STATUS        : {status}")

    if leitos < 20:
        pass

        print("\nACOES:")

        print("- Transferir pacientes")
        print("- Acionar hospitais parceiros")
        print("- Expandir capacidade")

# ============================================================
# NODE ABRIGOS
# ============================================================

def analisar_abrigos():
    pass

    capacidade = 500

    ocupacao = random.randint(50, 600)

    percentual = int((ocupacao / capacidade) * 100)

    status = classificar(percentual)

    print("\n================================================")
    print("NODE ABRIGOS")
    print("================================================")

    print(f"CAPACIDADE : {capacidade}")

    print(f"OCUPACAO   : {ocupacao}")

    print(f"STATUS     : {status}")

    if percentual > 90:
        pass

        print("\nACOES:")

        print("- Abrir novo abrigo")
        print("- Solicitar colchÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes")
        print("- Solicitar alimentaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o")

# ============================================================
# NODE ENERGIA
# ============================================================

def analisar_energia():
    pass

    disponibilidade = random.randint(10, 100)

    status = classificar(100 - disponibilidade)

    print("\n================================================")
    print("NODE ENERGIA")
    print("================================================")

    print(f"DISPONIBILIDADE : {disponibilidade}%")

    print(f"STATUS          : {status}")

    if disponibilidade < 30:
        pass

        print("\nACOES:")

        print("- Acionar geradores")
        print("- Priorizar hospitais")
        print("- Priorizar telecomunicaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes")

# ============================================================
# NODE LOGISTICA
# ============================================================

def analisar_logistica():
    pass

    rotas = random.randint(0, 100)

    status = classificar(100 - rotas)

    print("\n================================================")
    print("NODE LOGISTICA")
    print("================================================")

    print(f"ROTAS DISPONIVEIS : {rotas}%")

    print(f"STATUS            : {status}")

    if rotas < 40:
        pass

        print("\nACOES:")

        print("- Redefinir rotas")
        print("- Acionar transporte alternativo")
        print("- Atualizar mapa operacional")

# ============================================================
# COMMAND SUMMARY
# ============================================================

def resumo():
    pass

    print("\n================================================")
    print("X27 COMMAND SUMMARY")
    print("================================================")

    print(f"DATA: {datetime.now()}")

    print("\nANALISE OPERACIONAL CONCLUIDA")

    print("\nRECOMENDACAO:")
    print("Verificar ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡reas crÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­ticas")
    print("Priorizar recursos")
    print("Atualizar WAR ROOM")

# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    pass

    print("=" * 60)
    print("X27 INTELLIGENCE ENGINE")
    print("=" * 60)

    analisar_agua()

    analisar_saude()

    analisar_abrigos()

    analisar_energia()

    analisar_logistica()

    resumo()


