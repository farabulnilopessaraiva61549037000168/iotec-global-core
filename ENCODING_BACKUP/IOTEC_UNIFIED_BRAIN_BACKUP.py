import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import json
from datetime import datetime
from collections import defaultdict

ROOT = input("Caminho do nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo: ").strip()

ORCHESTRATION_KEYWORDS = [
    "engine", "core", "orchestrator", "brain",
    "central", "master", "pipeline", "controller",
    "consolidation", "boot"
]

report = {
    "timestamp": str(datetime.now()),
    "root": ROOT,
    "orchestrators_found": [],
    "ranking": [],
    "selected_brain": None,
    "conflicts": [],
    "summary": {}
}

def scan_orchestrators():
    for root, _, files in os.walk(ROOT):
        for f in files:
            path = os.path.join(root, f).lower()

            if any(k in path for k in ORCHESTRATION_KEYWORDS):
                report["orchestrators_found"].append(path)

def score_orchestrator(path):
    score = 0

    try:
        size = os.path.getsize(path)
        score += min(size / 1000, 50)

        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

            score += content.count("def ")
            score += content.count("class ")
            score += content.count("import ")
            score -= content.count("Exception")

    except:
        score -= 10

    return score

def rank_orchestrators():
    scores = []

    for o in report["orchestrators_found"]:
        scores.append((o, score_orchestrator(o)))

    scores.sort(key=lambda x: x[1], reverse=True)
    report["ranking"] = scores

def select_brain():
    if report["ranking"]:
        report["selected_brain"] = report["ranking"][0]

def detect_conflicts():
    names = defaultdict(list)

    for o, score in report["ranking"]:
        base = os.path.basename(o)
        names[base].append(o)

    for k, v in names.items():
        if len(v) > 1:
            report["conflicts"].append(v)

def generate_summary():
    report["summary"] = {
        "total_orchestrators": len(report["orchestrators_found"]),
        "conflicts": len(report["conflicts"]),
        "selected_brain": report["selected_brain"]
    }

def save():
    with open("IOTEC_UNIFIED_BRAIN_REPORT.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, ensure_ascii=False)

def run():
    print("\n[BRAIN] Escaneando nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo...")
    scan_orchestrators()

    print("[BRAIN] Ranqueando cÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©rebros...")
    rank_orchestrators()

    print("[BRAIN] Selecionando cÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©rebro principal...")
    select_brain()

    print("[BRAIN] Detectando conflitos...")
    detect_conflicts()

    generate_summary()
    save()

    print("\n===================================")
    print("IOTEC UNIFIED BRAIN")
    print("===================================")

    print("Orquestradores encontrados:", len(report["orchestrators_found"]))
    print("Conflitos:", len(report["conflicts"]))
    print("CÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©rebro selecionado:", report["selected_brain"])

    print("\nRelatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio salvo: IOTEC_UNIFIED_BRAIN_REPORT.json")

run()


