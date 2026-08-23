import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 CAPACITY ENGINE
# ============================================================

from datetime import datetime

# ============================================================
# CAPACIDADE ATUAL
# ============================================================

CAPACIDADE = {

    "SAUDE": 40,

    "AGUA": 78,

    "ENERGIA": 83,

    "INTERNET": 65,

    "LOGISTICA": 70,

    "ABRIGOS": 55

}

# ============================================================
# CLASSIFICACAO
# ============================================================

def classificar(valor):
    pass

    if valor < 50:
        return "CRITICO"

    elif valor < 70:
        return "ATENCAO"

    elif valor < 85:
        return "OPERACIONAL"

    return "EXCELENTE"

# ============================================================
# RECOMENDACOES
# ============================================================

def recomendacoes(setor, valor):
    pass

    if setor == "SAUDE" and valor < 50:
        pass

        return [
            "Adicionar equipes medicas",
            "Expandir leitos",
            "Criar hospital de campanha"
        ]

    if setor == "INTERNET" and valor < 70:
        pass

        return [
            "Expandir links redundantes",
            "Adicionar internet satelital",
            "Expandir rede mesh"
        ]

    if setor == "ABRIGOS" and valor < 60:
        pass

        return [
            "Abrir novos abrigos",
            "Expandir capacidade",
            "Aumentar estoques"
        ]

    if setor == "LOGISTICA" and valor < 70:
        pass

        return [
            "Expandir frota",
            "Criar centro regional",
            "Melhorar rotas"
        ]

    return [
        "Manter monitoramento"
    ]

# ============================================================
# ANALISE
# ============================================================

def analisar():
    pass

    print("\n================================================")
    print("X27 CAPACITY ENGINE")
    print("================================================")

    print(f"DATA : {datetime.now()}")

    print("\n================================================")
    print("ANALISE DE CAPACIDADE")
    print("================================================")

    for setor, valor in CAPACIDADE.items():
        pass

        status = classificar(valor)

        print(f"\n{setor}")

        print(f"CAPACIDADE : {valor}%")

        print(f"STATUS     : {status}")

        print("\nRECOMENDACOES:")

        for item in recomendacoes(setor, valor):
            pass

            print(f" - {item}")

# ============================================================
# RESUMO
# ============================================================

def resumo():
    pass

    criticos = 0

    atencao = 0

    for valor in CAPACIDADE.values():
        pass

        if valor < 50:
            criticos += 1

        elif valor < 70:
            atencao += 1

    print("\n================================================")
    print("RESUMO EXECUTIVO")
    print("================================================")

    print(f"SETORES CRITICOS : {criticos}")

    print(f"SETORES ATENCAO  : {atencao}")

    if criticos > 0:
        pass

        print("PRIORIDADE: EXPANSAO IMEDIATA")

    else:
        pass

        print("PRIORIDADE: MONITORAMENTO")

# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    pass

    analisar()

    resumo()


