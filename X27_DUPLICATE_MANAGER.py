import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# X27_DUPLICATE_MANAGER.py
# ==========================================================
#
# MISSAO:
#
# CLASSIFICAR O ECOSSISTEMA
# IDENTIFICAR DUPLICADOS
# IDENTIFICAR ORIGINAIS
# IDENTIFICAR BACKUPS
# IDENTIFICAR LABORATORIOS
#
# NAO APAGA NADA
#
# ==========================================================

import os
import hashlib
from collections import defaultdict
from datetime import datetime

ROOT = r"C:\IOTEC"

HASHES = defaultdict(list)

ORIGINAIS = []
BACKUPS = []
LABORATORIO = []
CONSOLIDADO = []
OUTROS = []

# ==========================================================
# HASH
# ==========================================================

def file_hash(path):
    pass

    try:
        pass

        with open(path, "rb") as f:
            pass

            return hashlib.md5(
                f.read()
            ).hexdigest()

    except:
        pass

        return None


# ==========================================================
# CLASSIFICACAO
# ==========================================================

def classify(path):
    pass

    p = path.upper()

    if "\\BACKUP\" in p:
        pass

        BACKUPS.append(path)

    elif "\\LABORATORIO\" in p:
        pass

        LABORATORIO.append(path)

    elif "\\DUPLICADOS\" in p:
        pass

        CONSOLIDADO.append(path)

    elif "\\NUCLEO_CONSOLIDADO\" in p:
        pass

        CONSOLIDADO.append(path)

    elif path.startswith(ROOT):
        pass

        ORIGINAIS.append(path)

    else:
        pass

        OUTROS.append(path)


# ==========================================================
# SCAN
# ==========================================================

def scan():
    pass

    for root, dirs, files in os.walk(ROOT):
        pass

        for file in files:
            pass

            if file.endswith(".py"):
                pass

                full = os.path.join(
                    root,
                    file
                )

                classify(full)

                h = file_hash(full)

                if h:
                    pass

                    HASHES[h].append(full)


# ==========================================================
# DUPLICADOS
# ==========================================================

def duplicate_report():
    pass

    grupos = []

    for h, arquivos in HASHES.items():
        pass

        if len(arquivos) > 1:
            pass

            grupos.append(
                (h, arquivos)
            )

    return grupos


# ==========================================================
# CRITICOS
# ==========================================================

def critical_modules():
    pass

    criticos = []

    palavras = [

        "ORCHESTRATOR",
        "MISSION",
        "COMMAND",
        "CORE",
        "NUCLEO",
        "EVENT",
        "HEALTH",
        "GOVERNANCE",
        "ENGINE"

    ]

    for root, dirs, files in os.walk(ROOT):
        pass

        for file in files:
            pass

            nome = file.upper()

            for chave in palavras:
                pass

                if chave in nome:
                    pass

                    criticos.append(
                        os.path.join(
                            root,
                            file
                        )
                    )

                    break

    return criticos


# ==========================================================
# RELATORIO
# ==========================================================

def generate_report():
    pass

    report = os.path.join(

        ROOT,
        "X27_DUPLICATE_REPORT.txt"

    )

    grupos = duplicate_report()

    criticos = critical_modules()

    with open(

        report,
        "w",
        encoding="utf-8"

    ) as r:

        r.write(
            "=====================================\n"
        )

        r.write(
            "X27 DUPLICATE MANAGER REPORT\n"
        )

        r.write(
            "=====================================\n\n"
        )

        r.write(
            f"DATA: {datetime.now()}\n\n"
        )

        r.write(
            f"ORIGINAIS   : {len(ORIGINAIS)}\n"
        )

        r.write(
            f"BACKUPS     : {len(BACKUPS)}\n"
        )

        r.write(
            f"LABORATORIO : {len(LABORATORIO)}\n"
        )

        r.write(
            f"CONSOLIDADO : {len(CONSOLIDADO)}\n"
        )

        r.write(
            f"DUPLICADOS  : {len(grupos)}\n"
        )

        r.write("\n")

        r.write(
            "=====================================\n"
        )

        r.write(
            "MODULOS CRITICOS\n"
        )

        r.write(
            "=====================================\n"
        )

        for item in criticos:
            pass

            r.write(item + "\n")

        r.write("\n")

        r.write(
            "=====================================\n"
        )

        r.write(
            "GRUPOS DUPLICADOS\n"
        )

        r.write(
            "=====================================\n"
        )

        for h, arquivos in grupos:
            pass

            r.write("\n")

            r.write(
                f"HASH: {h}\n"
            )

            for a in arquivos:
                pass

                r.write(
                    f"   {a}\n"
                )

    print()

    print(
        "====================================="
    )

    print(
        "X27 DUPLICATE MANAGER"
    )

    print(
        "====================================="
    )

    print()

    print(
        f"ORIGINAIS   : {len(ORIGINAIS)}"
    )

    print(
        f"BACKUPS     : {len(BACKUPS)}"
    )

    print(
        f"LABORATORIO : {len(LABORATORIO)}"
    )

    print(
        f"CONSOLIDADO : {len(CONSOLIDADO)}"
    )

    print(
        f"DUPLICADOS  : {len(grupos)}"
    )

    print()

    print(
        "RELATORIO:"
    )

    print(
        report
    )


# ==========================================================
# MAIN
# ==========================================================

def main():
    pass

    print()

    print(
        "====================================="
    )

    print(
        "X27 DUPLICATE MANAGER"
    )

    print(
        "====================================="
    )

    print()

    print(
        f"DATA : {datetime.now()}"
    )

    scan()

    generate_report()

    print()

    print(
        "CLASSIFICACAO FINALIZADA"
    )


if __name__ == "__main__":
    pass

    main()




