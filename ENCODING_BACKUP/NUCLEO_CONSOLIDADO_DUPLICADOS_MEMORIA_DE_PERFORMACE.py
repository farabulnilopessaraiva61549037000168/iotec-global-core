import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC - MEMÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIA DE PERFORMANCE
# ============================================================

import json

PERF_PATH = os.path.join(BASE, "performance.json")

def carregar_perf():
    if not os.path.exists(PERF_PATH):
        with open(PERF_PATH, "w", encoding="utf-8") as f:
            json.dump({}, f)
    with open(PERF_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_perf(data):
    with open(PERF_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def atualizar_perf(setor, api_nome, valor, custo, sucesso):
    data = carregar_perf()

    chave = f"{setor}:{api_nome}"
    if chave not in data:
        data[chave] = {
            "tentativas": 0,
            "sucessos": 0,
            "valor_total": 0.0,
            "custo_total": 0.0
        }

    data[chave]["tentativas"] += 1
    if sucesso:
        data[chave]["sucessos"] += 1
        data[chave]["valor_total"] += valor

    data[chave]["custo_total"] += custo

    salvar_perf(data)

def calcular_roi(reg):
    custo = reg["custo_total"] if reg["custo_total"] > 0 else 1e-6
    return reg["valor_total"] / custo

def priorizar_setor(setores):
    data = carregar_perf()

    scores = {}
    for s in setores:
        # mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©dia simples dos ROIs das APIs do setor
        rois = []
        for k, v in data.items():
            if k.startswith(s + ":"):
                rois.append(calcular_roi(v))
        scores[s] = sum(rois)/len(rois) if rois else 0.0

    # fallback: se todos zero, escolhe aleatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio
    melhor = max(scores, key=lambda k: scores[k]) if any(scores.values()) else random.choice(setores)
    return melhor


