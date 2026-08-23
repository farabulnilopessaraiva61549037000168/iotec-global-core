import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import json

ROOT = r"C:\IOTEC"

NOISE_MODULES = {
    "sys","os","json","time","re","math",
    "datetime","logging","subprocess",
    "functools","itertools","threading",
    "flask","psutil"
}

def scan_files(root):
    files = []
    for r, _, f in os.walk(root):
        for file in f:
            if file.endswith(".py"):
                files.append(os.path.join(r, file))
    return files


def extract_deps(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        imports = set()

        for line in content.splitlines():
            line = line.strip()

            if line.startswith("import "):
                imports.add(line.replace("import ", "").split(" ")[0])

            if line.startswith("from "):
                parts = line.split(" ")
                if len(parts) > 1:
                    imports.add(parts[1])

        # FILTRO REAL (sem mexer no arquivo)
        clean = {d for d in imports if d not in NOISE_MODULES}

        return clean

    except:
        return set()


def build_neural_map():
    files = scan_files(ROOT)

    graph = {}
    noise_hits = {}

    for f in files:
        deps = extract_deps(f)

        graph[f] = list(deps)

        for d in deps:
            if d in NOISE_MODULES:
                noise_hits[d] = noise_hits.get(d, 0) + 1

    return graph, noise_hits


def find_core_brain(graph):
    score = {}

    for file, deps in graph.items():
        score[file] = len(deps)

    sorted_files = sorted(score.items(), key=lambda x: x[1], reverse=True)

    return sorted_files[:10]


def run():
    print("\n[NEURAL FIX] Iniciando anÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡lise segura...\n")

    graph, noise = build_neural_map()

    core = find_core_brain(graph)

    print("\n===================================")
    print(" NEURAL MAP CLEAN (REAL CORE)")
    print("===================================\n")

    print("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã¢â‚¬Å¡  TOP NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"S REAIS DO SEU SISTEMA:\n")
    for f, s in core:
        print(f"{os.path.basename(f)} -> {s} conexÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âµes")

    print("\nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã¢â‚¬Å¡  RUÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂDO (IGNORADO NO CÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â°REBRO):\n")
    for k, v in sorted(noise.items(), key=lambda x: x[1], reverse=True):
        print(f"{k} -> {v}")

    report = {
        "core": core,
        "noise": noise
    }

    with open("IOTEC_NEURAL_MAP_CLEAN.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print("\nRelatÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³rio salvo: IOTEC_NEURAL_MAP_CLEAN.json")


if __name__ == "__main__":
    run()




