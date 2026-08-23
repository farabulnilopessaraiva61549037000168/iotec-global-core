import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import json

BASE = "C:\\IOTEC"
RELATORIO = os.path.join(BASE, "relatorio_valor.json")

EXTENSOES_RELEVANTES = [".html", ".js", ".json", ".txt"]

def avaliar_arquivo(nome):
    nome_lower = nome.lower()

    score = 0

    if "auditoria" in nome_lower: score += 3
    if "dados" in nome_lower: score += 3
    if "automacao" in nome_lower: score += 3
    if "sistema" in nome_lower: score += 2
    if "teste" in nome_lower: score -= 2

    return score

def classificar(score):
    if score >= 3:
        return "ALTO"
    elif score >= 1:
        return "MEDIO"
    else:
        return "BAIXO"

def analisar():
    resultados = []

    for root, dirs, files in os.walk(BASE):
        for file in files:
            ext = os.path.splitext(file)[1].lower()

            if ext in EXTENSOES_RELEVANTES:
                score = avaliar_arquivo(file)
                nivel = classificar(score)

                resultados.append({
                    "arquivo": file,
                    "caminho": root,
                    "score": score,
                    "nivel": nivel
                })

    with open(RELATORIO, "w") as f:
        json.dump(resultados, f, indent=2)

    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  RelatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio gerado em:", RELATORIO)

if __name__ == "__main__":
    analisar()


