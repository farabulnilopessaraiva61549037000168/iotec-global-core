import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC RANKING INTELIGENTE
# ============================================================

import os
import json
from pathlib import Path
from datetime import datetime

BASE = Path("D:/IOTEC/_SANITIZADA")
STATE = Path("D:/IOTEC/state")

ranking = []

def score_file(path):
    score = 0
    name = path.name.lower()

    # tipo
    if path.suffix in [".png",".jpg",".jpeg",".webp",".gif"]:
        score += 50

    # tamanho (qualidade)
    size_kb = path.stat().st_size / 1024
    if size_kb > 200:
        score += 20

    # palavras fortes
    palavras = ["dashboard","premium","ui","interface","panel","elite"]
    for p in palavras:
        if p in name:
            score += 30

    # recente
    days = (datetime.now().timestamp() - path.stat().st_mtime) / 86400
    if days < 7:
        score += 20

    return score

for root, dirs, files in os.walk(BASE):
    for f in files:
        p = Path(root) / f
        s = score_file(p)

        ranking.append({
            "arquivo": str(p).replace("\","/"),
            "nome": f,
            "score": s
        })

ranking.sort(key=lambda x: x["score"], reverse=True)

STATE.mkdir(exist_ok=True)

with open(STATE / "ranking.json", "w", encoding="utf-8") as f:
    json.dump(ranking[:100], f, indent=2)

print("RANKING GERADO")


