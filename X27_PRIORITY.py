import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 PRIORITY ENGINE
# ============================================================
#
# PRIORIZAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O ESTRATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°GICA
#
# Combina:
# - Capacidade
# - DependÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncias
# - Impacto
# - Criticidade
#
# ============================================================

from datetime import datetime

# ============================================================
# DADOS
# ============================================================

SETORES = {

    "SAUDE": {

        "capacidade": 40,

        "impacto": 10,

        "dependencias_criticas": 1

    },

    "INTERNET": {

        "capacidade": 65,

        "impacto": 8,

        "dependencias_criticas": 1

    },

    "ABRIGOS": {

        "capacidade": 55,

        "impacto": 7,

        "dependencias_criticas": 1

    },

    "LOGISTICA": {

        "capacidade": 70,

        "impacto": 6,

        "dependencias_criticas": 0

    },

    "ENERGIA": {

        "capacidade": 83,

        "impacto": 9,

        "dependencias_criticas": 0

    },

    "AGUA": {

        "capacidade": 78,

        "impacto": 10,

        "dependencias_criticas": 0

    }

}

# ============================================================
# CALCULO
# ============================================================

def calcular_prioridade(dados):
    pass

    deficit = 100 - dados["capacidade"]

    score = (

        deficit

        +

        (dados["impacto"] * 5)

        +

        (dados["dependencias_criticas"] * 25)

    )

    return score

# ============================================================
# ANALISE
# ============================================================

def gerar_prioridades():
    pass

    ranking = []

    for setor, dados in SETORES.items():
        pass

        score = calcular_prioridade(dados)

        ranking.append(

            {

                "setor": setor,

                "score": score,

                "capacidade": dados["capacidade"]

            }

        )

    ranking.sort(

        key=lambda x: x["score"],

        reverse=True

    )

    return ranking

# ============================================================
# CLASSIFICACAO
# ============================================================

def classificar(score):
    pass

    if score >= 110:
        pass

        return "CRITICO"

    elif score >= 80:
        pass

        return "ALTO"

    elif score >= 60:
        pass

        return "MODERADO"

    return "BAIXO"

# ============================================================
# EXIBICAO
# ============================================================

def exibir(ranking):
    pass

    print("\n================================================")

    print("X27 PRIORITY ENGINE")

    print("================================================")

    print(f"DATA : {datetime.now()}")

    print("\nRANKING ESTRATEGICO")

    print("================================================")

    posicao = 1

    for item in ranking:
        pass

        print("\n------------------------------------------------")

        print(f"PRIORIDADE : {posicao}")

        print(f"SETOR      : {item['setor']}")

        print(f"CAPACIDADE : {item['capacidade']}%")

        print(f"SCORE      : {item['score']}")

        print(

            f"RISCO      : "

            f"{classificar(item['score'])}"

        )

        posicao += 1

# ============================================================
# PLANO EXECUTIVO
# ============================================================

def plano(ranking):
    pass

    print("\n================================================")

    print("PLANO EXECUTIVO")

    print("================================================")

    top3 = ranking[:3]

    for item in top3:
        pass

        print(

            f"[PRIORIDADE MAXIMA] "

            f"{item['setor']}"

        )

# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    pass

    ranking = gerar_prioridades()

    exibir(ranking)

    plano(ranking)




