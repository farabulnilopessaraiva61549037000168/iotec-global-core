import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =========================================================
# IOTEC EXECUTION BRAIN
# MAPA VIVO DE EXECUÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O REAL DO NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡CLEO
# =========================================================

import os
import ast
import json
from collections import defaultdict

ROOT = input("Caminho do nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleo: ").strip()

# =========================================================
# FILTROS
# =========================================================

IGNORE_DIRS = [
    "venv",
    "__pycache__",
    "site-packages",
    "dist-packages",
    "node_modules",
    ".git"
]

ENTRY_KEYWORDS = [
    "app",
    "main",
    "boot",
    "start",
    "run",
    "api",
    "server",
    "router",
    "core",
    "engine",
    "orchestrator"
]

# =========================================================
# ESTRUTURAS
# =========================================================

graph = defaultdict(set)
reverse_graph = defaultdict(set)

runtime_candidates = []
dead_modules = []
entrypoints = []

# =========================================================
# UTILIDADES
# =========================================================

def valid_path(path):
    low = path.lower()

    return not any(x in low for x in IGNORE_DIRS)


def module_name(path):
    return os.path.splitext(os.path.basename(path))[0]


# =========================================================
# EXTRAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O AST
# =========================================================

def extract_calls(file_path):
    calls = set()
    imports = set()

    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            tree = ast.parse(f.read())

        for node in ast.walk(tree):
            pass

            # imports
            if isinstance(node, ast.Import):
                for n in node.names:
                    imports.add(n.name.split(".")[0])

            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.add(node.module.split(".")[0])

            # chamadas
            elif isinstance(node, ast.Call):
                pass

                if isinstance(node.func, ast.Name):
                    calls.add(node.func.id)

                elif isinstance(node.func, ast.Attribute):
                    calls.add(node.func.attr)

        return imports, calls

    except:
        return set(), set()


# =========================================================
# SCAN
# =========================================================

print("\n[EXECUTION BRAIN] Escaneando nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleo...\n")

all_files = []

for root, dirs, files in os.walk(ROOT):
    pass

    dirs[:] = [d for d in dirs if valid_path(d)]

    for file in files:
        pass

        if not file.endswith(".py"):
            continue

        full = os.path.join(root, file)

        if not valid_path(full):
            continue

        all_files.append(full)

# =========================================================
# BUILD GRAPH
# =========================================================

for file in all_files:
    pass

    current = module_name(file)

    imports, calls = extract_calls(file)

    for i in imports:
        graph[current].add(i)
        reverse_graph[i].add(current)

    score = len(imports) + len(calls)

    if score >= 10:
        runtime_candidates.append((current, score))

    if score == 0:
        dead_modules.append(current)

    if any(k in current.lower() for k in ENTRY_KEYWORDS):
        entrypoints.append(current)

# =========================================================
# RANKING
# =========================================================

runtime_candidates.sort(key=lambda x: x[1], reverse=True)

top_runtime = runtime_candidates[:25]

# =========================================================
# DETECTAR CÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â°REBRO CENTRAL
# =========================================================

brain_score = []

for node in graph:
    pass

    outgoing = len(graph[node])
    incoming = len(reverse_graph[node])

    total = outgoing + incoming

    brain_score.append((node, total))

brain_score.sort(key=lambda x: x[1], reverse=True)

# =========================================================
# EXPORT
# =========================================================

report = {
    "total_modules": len(all_files),
    "brain": brain_score[:20],
    "runtime_candidates": top_runtime,
    "entrypoints": entrypoints[:50],
    "dead_modules": dead_modules[:50],
    "connections": {
        k: list(v)
        for k, v in graph.items()
    }
}

with open(
    "IOTEC_EXECUTION_BRAIN_REPORT.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(report, f, indent=2)

# =========================================================
# OUTPUT
# =========================================================

print("=======================================")
print(" IOTEC EXECUTION BRAIN")
print("=======================================\n")

print("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã¢â‚¬Å¡  CÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â°REBRO OPERACIONAL:\n")

for node, score in brain_score[:15]:
    print(f"{node} -> {score} conexÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âµes")

print("\nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¥ MÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"DULOS MAIS EXECUTÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂVEIS:\n")

for node, score in top_runtime:
    print(f"{node} -> score {score}")

print("\nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âª ENTRYPOINTS:\n")

for e in entrypoints[:20]:
    print(e)

print("\nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã¢â‚¬Â¦  POSSÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂVEIS MÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"DULOS MORTOS:\n")

for d in dead_modules[:20]:
    print(d)

print("\n=======================================")
print("ANÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂLISE FINALIZADA")
print("=======================================\n")

print("RelatÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³rio salvo:")
print("IOTEC_EXECUTION_BRAIN_REPORT.json")


