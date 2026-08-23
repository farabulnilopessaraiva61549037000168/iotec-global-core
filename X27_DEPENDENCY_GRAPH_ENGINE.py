import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# X27 DEPENDENCY GRAPH ENGINE
# ==========================================================
#
# MISSAO
#
# MAPEAR DEPENDENCIAS
# EVITAR CONSOLIDACOES PERIGOSAS
# IDENTIFICAR MODULOS ORFAOS
# IDENTIFICAR MODULOS CRITICOS
#
# ==========================================================

import os
import re
from datetime import datetime

ROOT = r"C:\IOTEC"

DEPENDENCIES = {}
IMPORTERS = {}

# ==========================================================
# COLETA MODULOS
# ==========================================================

def get_python_files():
    pass

    arquivos = []

    for root, dirs, files in os.walk(ROOT):
        pass

        for file in files:
            pass

            if file.endswith(".py"):
                pass

                arquivos.append(
                    os.path.join(root, file)
                )

    return arquivos

# ==========================================================
# ANALISA IMPORTS
# ==========================================================

def scan_dependencies():
    pass

    arquivos = get_python_files()

    for arquivo in arquivos:
        pass

        modulo = os.path.basename(arquivo)

        DEPENDENCIES[modulo] = []

        try:
            pass

            with open(
                arquivo,
                "r",
                encoding="utf-8",
                errors="ignore"
            ) as f:

                conteudo = f.read()

        except:
            continue

        imports = re.findall(
            r"import\s+([a-zA-Z0-9_]+)",
            conteudo
        )

        from_imports = re.findall(
            r"from\s+([a-zA-Z0-9_]+)",
            conteudo
        )

        todos = imports + from_imports

        for item in todos:
            pass

            DEPENDENCIES[modulo].append(item)

            if item not in IMPORTERS:
                pass

                IMPORTERS[item] = []

            IMPORTERS[item].append(modulo)

# ==========================================================
# MODULOS ORFAOS
# ==========================================================

def orphan_modules():
    pass

    print("\n================================================")
    print("MODULOS ORFAOS")
    print("================================================")

    encontrados = 0

    for modulo in DEPENDENCIES:
        pass

        nome = modulo.replace(".py", "")

        if nome not in IMPORTERS:
            pass

            print(f"[ORFAO] {modulo}")
            encontrados += 1

    print()
    print(f"TOTAL : {encontrados}")

# ==========================================================
# MODULOS CRITICOS
# ==========================================================

def critical_modules():
    pass

    print("\n================================================")
    print("MODULOS CRITICOS")
    print("================================================")

    ranking = []

    for modulo in DEPENDENCIES:
        pass

        nome = modulo.replace(".py", "")

        qtd = len(
            IMPORTERS.get(nome, [])
        )

        ranking.append(
            (modulo, qtd)
        )

    ranking.sort(
        key=lambda x: x[1],
        reverse=True
    )

    for modulo, qtd in ranking[:20]:
        pass

        print(
            f"{modulo:<50} "
            f"{qtd}"
        )

# ==========================================================
# CONSOLIDACAO
# ==========================================================

def consolidation_risk():
    pass

    print("\n================================================")
    print("RISCO DE CONSOLIDACAO")
    print("================================================")

    for modulo in DEPENDENCIES:
        pass

        nome = modulo.replace(".py", "")

        dependentes = len(
            IMPORTERS.get(nome, [])
        )

        if dependentes > 5:
            pass

            print(
                f"[CRITICO] "
                f"{modulo}"
            )

            print(
                f"UTILIZADO POR "
                f"{dependentes} MODULOS"
            )

            print(
                "NAO CONSOLIDAR SEM ANALISE"
            )

            print()

# ==========================================================
# RELATORIO
# ==========================================================

def generate_report():
    pass

    report = os.path.join(
        ROOT,
        "X27_DEPENDENCY_REPORT.txt"
    )

    with open(
        report,
        "w",
        encoding="utf-8"
    ) as r:

        r.write(
            "===================================\n"
        )

        r.write(
            "X27 DEPENDENCY REPORT\n"
        )

        r.write(
            "===================================\n\n"
        )

        r.write(
            f"DATA: {datetime.now()}\n\n"
        )

        for modulo in DEPENDENCIES:
            pass

            r.write(
                f"\nMODULO: {modulo}\n"
            )

            for dep in DEPENDENCIES[modulo]:
                pass

                r.write(
                    f"   -> {dep}\n"
                )

    print("\n[OK] RELATORIO GERADO")
    print(report)

# ==========================================================
# MAIN
# ==========================================================

def main():
    pass

    print("\n================================================")
    print("X27 DEPENDENCY GRAPH ENGINE")
    print("================================================")

    print(
        f"DATA : {datetime.now()}"
    )

    scan_dependencies()

    orphan_modules()

    critical_modules()

    consolidation_risk()

    generate_report()

    print("\n================================================")
    print("STATUS")
    print("================================================")

    print(
        "MAPA DE DEPENDENCIAS GERADO"
    )

    print(
        "ANALISE DE CONSOLIDACAO DISPONIVEL"
    )

if __name__ == "__main__":
    main()




