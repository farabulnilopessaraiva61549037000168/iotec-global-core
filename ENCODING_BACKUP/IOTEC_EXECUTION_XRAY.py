import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import ast
from collections import defaultdict, Counter

ROOT = input("Digite o caminho do nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo: ").strip()

ENTRYPOINT_HINTS = [
    "main", "app", "run", "start", "boot", "server", "__main__", "execute"
]

EXECUTION_CALLS = defaultdict(list)
FILE_STATS = {}

# ============================
# ANALISA EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O REAL
# ============================

def analyze_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            code = f.read()

        tree = ast.parse(code)

        calls = []
        has_main = False

        for node in ast.walk(tree):
            pass

            # detecta chamadas
            if isinstance(node, ast.Call):
                if hasattr(node.func, "id"):
                    calls.append(node.func.id)
                elif hasattr(node.func, "attr"):
                    calls.append(node.func.attr)

            # detecta entrypoint real
            if isinstance(node, ast.If):
                try:
                    if (
                        isinstance(node.test, ast.Compare) and
                        "name" in dir(node.test.left) and
                        "__main__" in code
                    ):
                        has_main = True
                except:
                    pass

        FILE_STATS[path] = {
            "calls": calls,
            "size": len(code),
            "is_entry": "__main__" in code,
            "call_count": len(calls)
        }

        EXECUTION_CALLS[path] = calls

    except:
        pass

# ============================
# SCAN
# ============================

print("\n[XRAY] Escaneando nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo...\n")

py_files = []

for root, dirs, files in os.walk(ROOT):
    for file in files:
        if file.endswith(".py"):
            py_files.append(os.path.join(root, file))

for f in py_files:
    analyze_file(f)

# ============================
# ANÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂLISE DE EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O REAL
# ============================

entrypoints = []
hot_files = []
dead_files = []

for path, data in FILE_STATS.items():
    pass

    name = os.path.basename(path).lower()

    # entrypoints reais
    if data["is_entry"] or any(x in name for x in ENTRYPOINT_HINTS):
        entrypoints.append(path)

    # arquivos ativos (muitas chamadas)
    if data["call_count"] > 20:
        hot_files.append(path)

    # arquivos quase mortos
    if data["call_count"] == 0:
        dead_files.append(path)

# ============================
# DETECTA NÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ CENTRAL
# ============================

all_calls = Counter()

for calls in EXECUTION_CALLS.values():
    for c in calls:
        all_calls[c] += 1

top_callers = all_calls.most_common(10)

# ============================
# RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO FINAL
# ============================

print("\n===================================")
print("IOTEC EXECUTION REAL XRAY")
print("===================================\n")

print(f"Arquivos analisados: {len(py_files)}")
print(f"Entrypoints detectados: {len(entrypoints)}")
print(f"Hot files (alta atividade): {len(hot_files)}")
print(f"Dead files (sem execuÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o): {len(dead_files)}")

print("\n-----------------------------------")
print("TOP POSSÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂVEIS FUNÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™ES CENTRAIS:")
for item in top_callers:
    print(f"{item[0]} -> {item[1]} chamadas")

print("\n-----------------------------------")

print("ENTRYPOINTS PROVÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂVEIS:")
for e in entrypoints[:10]:
    print(e)

print("\n-----------------------------------")

print("HOT FILES (nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleos ativos):")
for h in hot_files[:10]:
    print(h)

print("\n-----------------------------------")

print("DEAD FILES (possivelmente nÃƒÆ'Ã†â€™o usados):")
for d in dead_files[:10]:
    print(d)

print("\n===================================")
print("DIAGNÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œSTICO FINAL")
print("===================================\n")

if len(entrypoints) > 5:
    print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡  MÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡LTIPLOS PONTOS DE ENTRADA (SEM CÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°REBRO ÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡NICO)")

if len(hot_files) > 10:
    print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â EXISTEM MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œDULOS ALTAMENTE ATIVOS")

if len(dead_files) > len(py_files) * 0.5:
    print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡  MUITOS MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œDULOS NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O EXECUTADOS (DÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂVIDA ARQUITETURAL)")

print("\n===================================")


