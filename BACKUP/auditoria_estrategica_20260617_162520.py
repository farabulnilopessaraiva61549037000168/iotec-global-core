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

# CLASSIFICAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O DE VALOR

# =========================



def avaliar(nome):
    pass

    nome = nome.lower()

    score = 0



    if "auditoria" in nome: score += 4

    if "dados" in nome: score += 4

    if "automacao" in nome: score += 3

    if "sistema" in nome: score += 2

    if "teste" in nome: score -= 2



    return score



def nivel(score):
    pass

    if score >= 4: return "ALTO"

    elif score >= 2: return "MEDIO"

    else: return "BAIXO"



# =========================

# ESTIMATIVA DE RECEITA

# =========================



def estimar_receita(nivel):
    pass

    if nivel == "ALTO":
        pass

        return {"ticket": 500, "potencial_mensal": 5000}

    elif nivel == "MEDIO":
        pass

        return {"ticket": 200, "potencial_mensal": 2000}

    else:
        pass

        return {"ticket": 50, "potencial_mensal": 500}



# =========================

# REGIÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ES (SIMULAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O ESTRATÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â°GICA)

# =========================



def sugerir_regiao(nome):
    pass

    nome = nome.lower()



    if "dados" in nome:
        pass

        return "EUA / Europa"

    elif "automacao" in nome:
        pass

        return "Brasil / AmÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©rica Latina"

    elif "auditoria" in nome:
        pass

        return "Global"

    else:
        pass

        return "Local"



# =========================

# ANÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂLISE PRINCIPAL

# =========================



def analisar():
    pass

    relatorio = []



    for root, dirs, files in os.walk(BASE):
        pass

        for file in files:
            pass

            ext = os.path.splitext(file)[1].lower()



            if ext in EXTENSOES:
                pass

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
        pass

        json.dump(relatorio, f, indent=2)



    print("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÆ'Ã¢â‚¬Â¦  RELATÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"RIO ESTRATÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â°GICO GERADO EM:", RELATORIO)



if __name__ == "__main__":
    pass

    analisar()




