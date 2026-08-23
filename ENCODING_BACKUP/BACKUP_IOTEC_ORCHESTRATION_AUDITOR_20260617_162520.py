import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import ast
from collections import defaultdict

# ============================
# CONFIG
# ============================

ROOT = input("Digite a pasta do nÃƒÆ'Ã‚Âºcleo: ").strip()

KEYWORDS_ORCHESTRATION = [
    "orchestrator", "engine", "workflow", "pipeline",
    "queue", "worker", "dispatch", "router", "controller",
    "manager", "agent", "event", "trigger", "state",
    "async", "task", "schedule", "execute", "run"
]

ENTRYPOINT_HINTS = [
    "main", "app", "start", "boot", "server", "run"
]

CALL_GRAPH = defaultdict(list)
FILES_ANALYZED = 0

# ============================
# ANALISAR PY FILES
# ============================

def analyze_file(path):
    global FILES_ANALYZED

    try:
        with open(path, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read(), filename=path)

        FILES_ANALYZED += 1

        calls = []

        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                if hasattr(node.func, "id"):
                    calls.append(node.func.id)
                elif hasattr(node.func, "attr"):
                    calls.append(node.func.attr)

        CALL_GRAPH[path] = calls

    except:
        pass

# ============================
# SCAN NÃƒÆ'Ã…Â¡CLEO
# ============================

for root, dirs, files in os.walk(ROOT):
    for file in files:
        if file.endswith(".py"):
            analyze_file(os.path.join(root, file))

# ============================
# ANÃƒÆ'Ã‚ÂLISE ESTRUTURAL
# ============================

orchestration_score = 0
entrypoints = 0
connections = 0

for file, calls in CALL_GRAPH.items():
    pass

    name = file.lower()

    # sinais de orquestraÃƒÆ'Ã‚Â§ÃƒÆ'Ã‚Â£o por nome
    if any(k in name for k in KEYWORDS_ORCHESTRATION):
        orchestration_score += 2

    # entrypoints
    if any(k in name for k in ENTRYPOINT_HINTS):
        entrypoints += 1

    # conexÃƒÆ'Ã‚Âµes reais entre arquivos
    connections += len(calls)

# ============================
# DIAGNÃƒÆ'Ã¢â‚¬Å"STICO FINAL
# ============================

print("\n===================================")
print("CORE ORCHESTRATION ANALYSIS")
print("===================================\n")

print(f"Arquivos analisados: {FILES_ANALYZED}")
print(f"ConexÃƒÆ'Ã‚Âµes detectadas (calls): {connections}")
print(f"Sinais de orquestraÃƒÆ'Ã‚Â§ÃƒÆ'Ã‚Â£o: {orchestration_score}")
print(f"Entrypoints detectados: {entrypoints}")

print("\n-----------------------------------")

# ============================
# CLASSIFICAÃƒÆ'Ã¢â‚¬Â¡ÃƒÆ'Ã†â€™O INTELIGENTE
# ============================

if orchestration_score > 50 and connections > 500:
    status = "ORQUESTRAÃƒÆ'Ã¢â‚¬Â¡ÃƒÆ'Ã†â€™O FORTE - SISTEMA OPERACIONAL PROVÃƒÆ'Ã‚ÂVEL"
elif orchestration_score > 20 and connections > 200:
    status = "ORQUESTRAÃƒÆ'Ã¢â‚¬Â¡ÃƒÆ'Ã†â€™O MÃƒÆ'Ã¢â‚¬Â°DIA - ECOSSISTEMA PARCIAL"
elif orchestration_score > 5:
    status = "ORQUESTRAÃƒÆ'Ã¢â‚¬Â¡ÃƒÆ'Ã†â€™O FRACA - MÃƒÆ'Ã¢â‚¬Å"DULOS ISOLADOS"
else:
    status = "SEM ORQUESTRAÃƒÆ'Ã¢â‚¬Â¡ÃƒÆ'Ã†â€™O REAL DETECTADA"

print("STATUS:")
print(status)

print("\n-----------------------------------")

# ============================
# INTERPRETAÃƒÆ'Ã¢â‚¬Â¡ÃƒÆ'Ã†â€™O FINAL
# ============================

print("""
INTERPRETAÃƒÆ'Ã¢â‚¬Â¡ÃƒÆ'Ã†â€™O:

- 'orquestraÃƒÆ'Ã‚Â§ÃƒÆ'Ã‚Â£o forte' = sistemas realmente conversam entre si
- 'mÃƒÆ'Ã‚Â©dia' = existem partes conectadas mas nÃƒÆ'Ã‚Â£o centralizadas
- 'fraca' = apenas arquivos soltos com nomes inteligentes
- 'nenhuma' = projeto nÃƒÆ'Ã‚Â£o tem coordenaÃƒÆ'Ã‚Â§ÃƒÆ'Ã‚Â£o real

IMPORTANTE:
Isso NÃƒÆ'Ã†â€™O mede inteligÃƒÆ'Ã‚Âªncia da IA,
mas sim arquitetura real de execuÃƒÆ'Ã‚Â§ÃƒÆ'Ã‚Â£o.
""")


