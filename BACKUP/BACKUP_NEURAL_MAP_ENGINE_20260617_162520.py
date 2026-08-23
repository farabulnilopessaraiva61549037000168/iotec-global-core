import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os

import re

import json

from collections import defaultdict, Counter



ROOT = input("Caminho do nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleo: ").strip()



graph = defaultdict(set)

reverse_graph = defaultdict(set)



files_index = []



# -----------------------------

# 1. COLETA DE ARQUIVOS

# -----------------------------

def collect_files():
    pass

    for root, _, files in os.walk(ROOT):
        pass

        for f in files:
            pass

            if f.endswith(".py"):
                pass

                full_path = os.path.join(root, f)

                files_index.append(full_path)



# -----------------------------

# 2. EXTRAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O DE DEPENDÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â¦ NCIAS

# -----------------------------

def extract_links(file_path):
    pass

    try:
        pass

        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            pass

            content = f.read()



        imports = re.findall(r"import (\w+)", content)

        from_imports = re.findall(r"from (\w+) import", content)



        deps = set(imports + from_imports)



        return deps



    except:
        pass

        return set()



# -----------------------------

# 3. CONSTRUÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O DO GRAFO

# -----------------------------

def build_graph():
    pass

    name_map = {}



    for f in files_index:
        pass

        name_map[os.path.basename(f).replace(".py", "")] = f



    for f in files_index:
        pass

        module_name = os.path.basename(f).replace(".py", "")

        deps = extract_links(f)



        for d in deps:
            pass

            if d in name_map:
                pass

                graph[module_name].add(d)

                reverse_graph[d].add(module_name)



# -----------------------------

# 4. CENTRALIDADE (cÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©rebro real)

# -----------------------------

def compute_centrality():
    pass

    scores = Counter()



    for node in graph:
        pass

        scores[node] += len(graph[node]) * 2  # influencia direta



    for node in reverse_graph:
        pass

        scores[node] += len(reverse_graph[node]) * 3  # dependÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncia recebida



    return scores



# -----------------------------

# 5. DETECTA MÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"DULO CÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â°REBRO

# -----------------------------

def select_brain(scores):
    pass

    if not scores:
        pass

        return None



    return scores.most_common(1)[0]



# -----------------------------

# 6. DETECTA ILHAS (dead zones)

# -----------------------------

def detect_isolated():
    pass

    isolated = []



    all_nodes = set(list(graph.keys()) + list(reverse_graph.keys()))



    for node in all_nodes:
        pass

        if len(graph[node]) == 0 and len(reverse_graph[node]) == 0:
            pass

            isolated.append(node)



    return isolated



# -----------------------------

# 7. HOT NODES

# -----------------------------

def detect_hot_nodes():
    pass

    return sorted(reverse_graph.items(), key=lambda x: len(x[1]), reverse=True)[:10]



# -----------------------------

# 8. EXECUÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

# -----------------------------

def run():
    pass

    print("\n[NEURAL MAP] Escaneando nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleo...")



    collect_files()

    build_graph()



    scores = compute_centrality()

    brain = select_brain(scores)

    isolated = detect_isolated()

    hot = detect_hot_nodes()



    report = {

        "total_files": len(files_index),

        "nodes": len(graph),

        "brain_node": brain,

        "isolated_nodes": isolated,

        "hot_nodes": [(k, len(v)) for k, v in hot],

        "centrality_scores": dict(scores)

    }



    with open("IOTEC_NEURAL_MAP_REPORT.json", "w", encoding="utf-8") as f:
        pass

        json.dump(report, f, indent=4, ensure_ascii=False)



    print("\n===================================")

    print("IOTEC NEURAL MAP ENGINE")

    print("===================================")



    print("Arquivos analisados:", len(files_index))

    print("NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³s no grafo:", len(graph))



    print("\nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã¢â‚¬Å¡  CÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â°REBRO REAL DO SISTEMA:")

    print(brain)



    print("\nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¥ HOT NODES:")

    for h in hot:
        pass

        print(h[0], "->", len(h[1]), "conexÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âµes")



    print("\nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã¢â‚¬Â¦  ISOLADOS:")

    print(len(isolated), "mÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³dulos")



    print("\nRelatÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³rio salvo: IOTEC_NEURAL_MAP_REPORT.json")



run()


