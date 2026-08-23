import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os

import ast

from collections import defaultdict, Counter



ROOT = input("Digite o caminho do nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleo: ").strip()



ENTRYPOINT_HINTS = [

    "main", "app", "run", "start", "boot", "server", "__main__", "execute"

]



EXECUTION_CALLS = defaultdict(list)

FILE_STATS = {}



# ============================

# ANALISA EXECUÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O REAL

# ============================



def analyze_file(path):
    pass

    try:
        pass

        with open(path, "r", encoding="utf-8") as f:
            pass

            code = f.read()



        tree = ast.parse(code)



        calls = []

        has_main = False



        for node in ast.walk(tree):
            pass



            # detecta chamadas

            if isinstance(node, ast.Call):
                pass

                if hasattr(node.func, "id"):
                    pass

                    calls.append(node.func.id)

                elif hasattr(node.func, "attr"):
                    pass

                    calls.append(node.func.attr)



            # detecta entrypoint real

            if isinstance(node, ast.If):
                pass

                try:
                    pass

                    if (

                        isinstance(node.test, ast.Compare) and

                        "name" in dir(node.test.left) and

                        "__main__" in code

                    ):

                        has_main = True

                except:
                    pass

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

        pass



# ============================

# SCAN

# ============================



print("\n[XRAY] Escaneando nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleo...\n")



py_files = []



for root, dirs, files in os.walk(ROOT):
    pass

    for file in files:
        pass

        if file.endswith(".py"):
            pass

            py_files.append(os.path.join(root, file))



for f in py_files:
    pass

    analyze_file(f)



# ============================

# ANÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂLISE DE EXECUÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O REAL

# ============================



entrypoints = []

hot_files = []

dead_files = []



for path, data in FILE_STATS.items():
    pass



    name = os.path.basename(path).lower()



    # entrypoints reais

    if data["is_entry"] or any(x in name for x in ENTRYPOINT_HINTS):
        pass

        entrypoints.append(path)



    # arquivos ativos (muitas chamadas)

    if data["call_count"] > 20:
        pass

        hot_files.append(path)



    # arquivos quase mortos

    if data["call_count"] == 0:
        pass

        dead_files.append(path)



# ============================

# DETECTA NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å" CENTRAL

# ============================



all_calls = Counter()



for calls in EXECUTION_CALLS.values():
    pass

    for c in calls:
        pass

        all_calls[c] += 1



top_callers = all_calls.most_common(10)



# ============================

# RELATÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"RIO FINAL

# ============================



print("\n===================================")

print("IOTEC EXECUTION REAL XRAY")

print("===================================\n")



print(f"Arquivos analisados: {len(py_files)}")

print(f"Entrypoints detectados: {len(entrypoints)}")

print(f"Hot files (alta atividade): {len(hot_files)}")

print(f"Dead files (sem execuÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o): {len(dead_files)}")



print("\n-----------------------------------")

print("TOP POSSÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂVEIS FUNÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ES CENTRAIS:")

for item in top_callers:
    pass

    print(f"{item[0]} -> {item[1]} chamadas")



print("\n-----------------------------------")



print("ENTRYPOINTS PROVÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂVEIS:")

for e in entrypoints[:10]:
    pass

    print(e)



print("\n-----------------------------------")



print("HOT FILES (nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleos ativos):")

for h in hot_files[:10]:
    pass

    print(h)



print("\n-----------------------------------")



print("DEAD FILES (possivelmente nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o usados):")

for d in dead_files[:10]:
    pass

    print(d)



print("\n===================================")

print("DIAGNÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"STICO FINAL")

print("===================================\n")



if len(entrypoints) > 5:
    pass

    print("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã¢â‚¬Å¡  MÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡LTIPLOS PONTOS DE ENTRADA (SEM CÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â°REBRO ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡NICO)")



if len(hot_files) > 10:
    pass

    print("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â EXISTEM MÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"DULOS ALTAMENTE ATIVOS")



if len(dead_files) > len(py_files) * 0.5:
    pass

    print("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã¢â‚¬Å¡  MUITOS MÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"DULOS NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O EXECUTADOS (DÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂVIDA ARQUITETURAL)")



print("\n===================================")




