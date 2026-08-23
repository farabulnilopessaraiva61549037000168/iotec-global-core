import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os

ROOT = "C:/IOTEC"

extensoes = {
    ".py": 0,
    ".js": 0,
    ".html": 0,
    ".css": 0
}

linhas_total = 0
arquivos_total = 0

def contar_linhas(caminho):
    try:
        with open(caminho, "r", encoding="utf-8", errors="ignore") as f:
            return len(f.readlines())
    except:
        return 0

for root, dirs, files in os.walk(ROOT):
    for file in files:
        arquivos_total += 1
        caminho = os.path.join(root, file)

        linhas = contar_linhas(caminho)
        linhas_total += linhas

        for ext in extensoes:
            if file.endswith(ext):
                extensoes[ext] += 1

# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  Score tÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©cnico (simples)
score = (linhas_total / 1000) + (arquivos_total * 0.5)

# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢Ãƒâ€šÃ‚Â° Estimativa de valor (base tÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©cnica)
valor_usd = score * 50
valor_brl = valor_usd * 5

# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã…Â¾ RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO
print("\n===== RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO DO NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO IOTEC =====\n")

print(f"Arquivos totais: {arquivos_total}")
print(f"Linhas de cÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³digo: {linhas_total}\n")

print("DistribuiÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o por tipo:")
for ext, qtd in extensoes.items():
    print(f"{ext}: {qtd}")

print("\nScore tÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©cnico:", round(score, 2))

print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢Ãƒâ€šÃ‚Â° VALUATION ESTIMADO:")
print(f"USD: ${round(valor_usd, 2)}")
print(f"BRL: R$ {round(valor_brl, 2)}")

print("\n====================================\n")


