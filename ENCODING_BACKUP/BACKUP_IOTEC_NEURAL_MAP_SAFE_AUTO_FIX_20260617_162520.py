import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import json

ROOT = r"C:\IOTEC"

# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â« tudo que NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© seu sistema
BLACKLIST_PATHS = [
    "venv",
    "site-packages",
    "dist-packages",
    "__pycache__",
    "pip",
    "distutils",
    "lib\\python",
    "lib/python"
]

# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â« mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulos ruÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­do (nÃƒÆ'Ã†â€™o entram no cÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©rebro)
BLACKLIST_MODULES = {
    "sys","os","json","time","re","math",
    "datetime","logging","subprocess",
    "functools","itertools","threading",
    "flask","psutil"
}


def is_valid_path(path: str) -> bool:
    p = path.lower()
    return not any(b in p for b in BLACKLIST_PATHS)


def scan_files(root):
    files = []

    for r, _, f in os.walk(root):
        pass

        # ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¥ BLOQUEIO DE AMBIENTE EXTERNO
        if not is_valid_path(r):
            continue

        for file in f:
            if file.endswith(".py"):
                full = os.path.join(r, file)

                if is_valid_path(full):
                    files.append(full)

    return files


def extract_deps(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        deps = set()

        for line in lines:
            line = line.strip()

            if line.startswith("import "):
                mod = line.replace("import ", "").split(" ")[0]
                deps.add(mod)

            elif line.startswith("from "):
                parts = line.split()
                if len(parts) > 1:
                    deps.add(parts[1])

        # ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¥ FILTRO REAL DO CÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°REBRO
        clean = {d for d in deps if d not in BLACKLIST_MODULES}

        return clean

    except:
        return set()


def build_map():
    files = scan_files(ROOT)

    graph = {}
    noise = {}

    for f in files:
        deps = extract_deps(f)
        graph[f] = list(deps)

        for d in deps:
            if d in BLACKLIST_MODULES:
                noise[d] = noise.get(d, 0) + 1

    return graph, noise


def get_brain(graph):
    score = {k: len(v) for k, v in graph.items()}
    return sorted(score.items(), key=lambda x: x[1], reverse=True)[:15]


def run():
    print("\n[SAFE AUTO FIX] Iniciando anÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise limpa do nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo...\n")

    graph, noise = build_map()

    brain = get_brain(graph)

    print("\n===================================")
    print(" ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  CÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°REBRO REAL DO SISTEMA (LIMPO)")
    print("===================================\n")

    for f, s in brain:
        print(f"{os.path.basename(f)} -> {s} conexÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes")

    print("\nÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡  RUÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂDO EXTERNO FILTRADO:\n")

    for k, v in sorted(noise.items(), key=lambda x: x[1], reverse=True):
        print(f"{k} -> {v}")

    report = {
        "brain": brain,
        "noise": noise
    }

    with open("IOTEC_NEURAL_MAP_SAFE_REPORT.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print("\nRelatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio salvo: IOTEC_NEURAL_MAP_SAFE_REPORT.json")


if __name__ == "__main__":
    run()


