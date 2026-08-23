import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import json
from datetime import datetime

BASE = "C:\\IOTEC"
RELATORIO = os.path.join(BASE, "relatorio_estrategico.json")

EXTENSOES = [".html", ".js", ".json", ".txt"]

# =========================
# CLASSIFICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DE VALOR
# =========================

def avaliar(nome):
    nome = nome.lower()
    score = 0

    if "auditoria" in nome: score += 4
    if "dados" in nome: score += 4
    if "automacao" in nome: score += 3
    if "sistema" in nome: score += 2
    if "teste" in nome: score -= 2

    return score

def nivel(score):
    if score >= 4: return "ALTO"
    elif score >= 2: return "MEDIO"
    else: return "BAIXO"

# =========================
# ESTIMATIVA DE RECEITA
# =========================

def estimar_receita(nivel):
    if nivel == "ALTO":
        return {"ticket": 500, "potencial_mensal": 5000}
    elif nivel == "MEDIO":
        return {"ticket": 200, "potencial_mensal": 2000}
    else:
        return {"ticket": 50, "potencial_mensal": 500}

# =========================
# REGIÃƒÆ'Ã†â€™ES (SIMULAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O ESTRATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°GICA)
# =========================

def sugerir_regiao(nome):
    nome = nome.lower()

    if "dados" in nome:
        return "EUA / Europa"
    elif "automacao" in nome:
        return "Brasil / AmÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©rica Latina"
    elif "auditoria" in nome:
        return "Global"
    else:
        return "Local"

# =========================
# ANÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂLISE PRINCIPAL
# =========================

def analisar():
    relatorio = []

    for root, dirs, files in os.walk(BASE):
        for file in files:
            ext = os.path.splitext(file)[1].lower()

            if ext in EXTENSOES:
                score = avaliar(file)
                n = nivel(score)
                receita = estimar_receita(n)
                regiao = sugerir_regiao(file)

                caminho = os.path.join(root, file)

                tamanho = os.path.getsize(caminho)
                data_mod = datetime.fromtimestamp(os.path.getmtime(caminho)).strftime("%Y-%m-%d")

                relatorio.append({
                    "arquivo": file,
                    "caminho": root,
                    "nivel": n,
                    "score": score,
                    "regiao_sugerida": regiao,
                    "receita_estimada": receita,
                    "metadata": {
                        "tamanho_bytes": tamanho,
                        "ultima_modificacao": data_mod
                    }
                })

    with open(RELATORIO, "w") as f:
        json.dump(relatorio, f, indent=2)

    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO ESTRATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°GICO GERADO EM:", RELATORIO)

if __name__ == "__main__":
    analisar()


