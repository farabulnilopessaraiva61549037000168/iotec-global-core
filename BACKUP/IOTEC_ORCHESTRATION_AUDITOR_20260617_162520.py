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



ROOT = input("Digite a pasta do nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo: ").strip()



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
    pass

    global FILES_ANALYZED



    try:
        pass

        with open(path, "r", encoding="utf-8") as f:
            pass

            tree = ast.parse(f.read(), filename=path)



        FILES_ANALYZED += 1



        calls = []



        for node in ast.walk(tree):
            pass

            if isinstance(node, ast.Call):
                pass

                if hasattr(node.func, "id"):
                    pass

                    calls.append(node.func.id)

                elif hasattr(node.func, "attr"):
                    pass

                    calls.append(node.func.attr)



        CALL_GRAPH[path] = calls



    except:
        pass

        pass



# ============================

# SCAN NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO

# ============================



for root, dirs, files in os.walk(ROOT):
    pass

    for file in files:
        pass

        if file.endswith(".py"):
            pass

            analyze_file(os.path.join(root, file))



# ============================

# ANÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂLISE ESTRUTURAL

# ============================



orchestration_score = 0

entrypoints = 0

connections = 0



for file, calls in CALL_GRAPH.items():
    pass



    name = file.lower()



    # sinais de orquestraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o por nome

    if any(k in name for k in KEYWORDS_ORCHESTRATION):
        pass

        orchestration_score += 2



    # entrypoints

    if any(k in name for k in ENTRYPOINT_HINTS):
        pass

        entrypoints += 1



    # conexÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes reais entre arquivos

    connections += len(calls)



# ============================

# DIAGNÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œSTICO FINAL

# ============================



print("\n===================================")

print("CORE ORCHESTRATION ANALYSIS")

print("===================================\n")



print(f"Arquivos analisados: {FILES_ANALYZED}")

print(f"ConexÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes detectadas (calls): {connections}")

print(f"Sinais de orquestraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o: {orchestration_score}")

print(f"Entrypoints detectados: {entrypoints}")



print("\n-----------------------------------")



# ============================

# CLASSIFICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O INTELIGENTE

# ============================



if orchestration_score > 50 and connections > 500:
    pass

    status = "ORQUESTRAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O FORTE - SISTEMA OPERACIONAL PROVÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂVEL"

elif orchestration_score > 20 and connections > 200:
    pass

    status = "ORQUESTRAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°DIA - ECOSSISTEMA PARCIAL"

elif orchestration_score > 5:
    pass

    status = "ORQUESTRAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O FRACA - MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œDULOS ISOLADOS"

else:
    pass

    status = "SEM ORQUESTRAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O REAL DETECTADA"



print("STATUS:")

print(status)



print("\n-----------------------------------")



# ============================

# INTERPRETAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O FINAL

# ============================



print("""

INTERPRETAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O:



- 'orquestraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o forte' = sistemas realmente conversam entre si

- 'mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©dia' = existem partes conectadas mas nÃƒÆ'Ã†â€™o centralizadas

- 'fraca' = apenas arquivos soltos com nomes inteligentes

- 'nenhuma' = projeto nÃƒÆ'Ã†â€™o tem coordenaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o real



IMPORTANTE:

Isso NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O mede inteligÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia da IA,

mas sim arquitetura real de execuÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o.

""")




