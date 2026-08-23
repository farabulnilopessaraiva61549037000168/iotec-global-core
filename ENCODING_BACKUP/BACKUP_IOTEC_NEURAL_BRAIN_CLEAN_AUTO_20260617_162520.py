import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
from collections import defaultdict

ROOT = r"C:\IOTEC"

# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â« RUÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂDO DO SISTEMA
BLACKLIST_PATHS = [
    "venv", "site-packages", "dist-packages",
    "__pycache__", "pip", "distutils",
    "lib\\python", "lib/python"
]

BLACKLIST_MODULES = {
    "sys","os","json","time","re","math",
    "datetime","logging","subprocess",
    "functools","itertools","threading",
    "flask","psutil"
}


def is_valid(path):
    p = path.lower()
    return not any(b in p for b in BLACKLIST_PATHS)


def scan_py_files():
    files = []

    for r, _, f in os.walk(ROOT):
        if not is_valid(r):
            continue

        for file in f:
            if file.endswith(".py"):
                full = os.path.join(r, file)
                if is_valid(full):
                    files.append(full)

    return files


def extract_deps(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        deps = set()

        for l in lines:
            l = l.strip()

            if l.startswith("import "):
                deps.add(l.split("import ")[1].split(" ")[0])

            elif l.startswith("from "):
                parts = l.split()
                if len(parts) > 1:
                    deps.add(parts[1])

        return {d for d in deps if d not in BLACKLIST_MODULES}

    except:
        return set()


def build_graph():
    files = scan_py_files()

    graph = defaultdict(set)

    for f in files:
        deps = extract_deps(f)

        # ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¥ normalizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de identidade (remove duplicaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o)
        node = os.path.basename(f)

        for d in deps:
            graph[node].add(d)

    return graph


def compute_brain(graph):
    score = []

    for node, deps in graph.items():
        score.append((node, len(deps)))

    # ordenaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o limpa
    score.sort(key=lambda x: x[1], reverse=True)

    return score[:20]


def run():
    print("\n===================================")
    print(" ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  NEURAL BRAIN CLEAN (FINAL)")
    print("===================================\n")

    graph = build_graph()

    brain = compute_brain(graph)

    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  CÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°REBRO REAL CONSOLIDADO:\n")

    for node, score in brain:
        print(f"{node} -> {score} conexÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes")

    print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  TOTAL DE NÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œS:", len(graph))

    # salvar mapa limpo
    with open("IOTEC_NEURAL_BRAIN_FINAL.json", "w", encoding="utf-8") as f:
        import json
        json.dump({k: list(v) for k, v in graph.items()}, f, indent=2)

    print("\nRelatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio salvo: IOTEC_NEURAL_BRAIN_FINAL.json")


if __name__ == "__main__":
    run()


