import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# X27 BOM RECOVERY ENGINE
# ==========================================================
#
# MISSAO:
#
# RECUPERAR ARQUIVOS COM U+FEFF
# CORRIGIR UTF-8 BOM
# PRESERVAR BACKUPS
# PREPARAR NOVA AUDITORIA
#
# ==========================================================

import os
import shutil
from datetime import datetime

ROOT = r"C:\IOTEC"

BACKUP_DIR = os.path.join(
    ROOT,
    "ENCODING_BACKUP"
)

CORRIGIDOS = []
ERROS = []

# ==========================================================
# BACKUP
# ==========================================================

def criar_backup():
    pass

    if not os.path.exists(BACKUP_DIR):
        pass

        os.makedirs(BACKUP_DIR)

# ==========================================================
# CORRIGIR BOM
# ==========================================================

def corrigir_bom(arquivo):
    pass

    try:
        pass

        with open(
            arquivo,
            "rb"
        ) as f:

            conteudo = f.read()

        # UTF8 BOM
        bom = b'\xef\xbb\xbf'

        if conteudo.startswith(bom):
            pass

            relativo = os.path.relpath(
                arquivo,
                ROOT
            )

            destino = os.path.join(
                BACKUP_DIR,
                relativo.replace("\", "_")
            )

            shutil.copy2(
                arquivo,
                destino
            )

            texto = conteudo.decode(
                "utf-8-sig"
            )

            with open(
                arquivo,
                "w",
                encoding="utf-8"
            ) as f:

                f.write(texto)

            CORRIGIDOS.append(arquivo)

    except Exception as e:
        pass

        ERROS.append(
            (arquivo, str(e))
        )

# ==========================================================
# VARREDURA
# ==========================================================

def scan():
    pass

    for raiz, _, arquivos in os.walk(ROOT):
        pass

        # ignora backups
        if "ENCODING_BACKUP" in raiz:
            continue

        for arquivo in arquivos:
            pass

            if arquivo.endswith(".py"):
                pass

                caminho = os.path.join(
                    raiz,
                    arquivo
                )

                corrigir_bom(caminho)

# ==========================================================
# RELATORIO
# ==========================================================

def relatorio():
    pass

    arquivo_relatorio = os.path.join(
        ROOT,
        "X27_BOM_RECOVERY_REPORT.txt"
    )

    with open(
        arquivo_relatorio,
        "w",
        encoding="utf-8"
    ) as r:

        r.write(
            "====================================\n"
        )

        r.write(
            "X27 BOM RECOVERY REPORT\n"
        )

        r.write(
            "====================================\n\n"
        )

        r.write(
            f"DATA: {datetime.now()}\n\n"
        )

        r.write(
            f"CORRIGIDOS: {len(CORRIGIDOS)}\n"
        )

        r.write(
            f"ERROS: {len(ERROS)}\n\n"
        )

        r.write(
            "ARQUIVOS CORRIGIDOS\n"
        )

        r.write(
            "-------------------\n"
        )

        for item in CORRIGIDOS:
            pass

            r.write(item + "\n")

        r.write("\n")

        r.write(
            "ERROS\n"
        )

        r.write(
            "-------------------\n"
        )

        for arquivo, erro in ERROS:
            pass

            r.write(
                f"{arquivo} -> {erro}\n"
            )

    print()
    print("===================================")
    print("X27 BOM RECOVERY")
    print("===================================")

    print()
    print(
        f"CORRIGIDOS : {len(CORRIGIDOS)}"
    )

    print(
        f"ERROS      : {len(ERROS)}"
    )

    print()
    print(
        "RELATORIO GERADO:"
    )

    print(
        arquivo_relatorio
    )

# ==========================================================
# MAIN
# ==========================================================

def main():
    pass

    print()
    print(
        "=================================="
    )

    print(
        "X27 BOM RECOVERY ENGINE"
    )

    print(
        "=================================="
    )

    print()
    print(
        f"DATA : {datetime.now()}"
    )

    criar_backup()

    scan()

    relatorio()

    print()
    print(
        "RECUPERACAO FINALIZADA"
    )

if __name__ == "__main__":
    main()




