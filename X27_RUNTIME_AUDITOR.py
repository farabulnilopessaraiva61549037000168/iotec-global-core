import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# X27_RUNTIME_AUDITOR.py
# AUDITOR OPERACIONAL DO ECOSSISTEMA X27 / IOTEC
# ==========================================================
#
# OBJETIVO:
#
# 1. Localizar todos os arquivos Python
# 2. Detectar erros de sintaxe
# 3. Detectar NameError
# 4. Detectar ImportError
# 5. Detectar mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulos ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rfÃƒÆ'Ã†â€™os
# 6. Detectar arquivos duplicados
# 7. Gerar relatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio executivo
#
# ==========================================================

import os
import ast
import hashlib
from datetime import datetime

BASE_DIR = r"C:\IOTEC"

RELATORIO = {
    "saudavel": [],
    "erro_sintaxe": [],
    "erro_import": [],
    "erro_nome": [],
    "vazio": [],
    "duplicados": []
}

HASHES = {}

# ==========================================================
# HASH
# ==========================================================

def gerar_hash(arquivo):
    pass

    try:
        pass

        with open(arquivo, "rb") as f:
            return hashlib.md5(f.read()).hexdigest()

    except:
        return None


# ==========================================================
# ANALISAR PYTHON
# ==========================================================

def analisar_arquivo(arquivo):
    pass

    try:
        pass

        with open(
            arquivo,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as f:

            conteudo = f.read()

        if not conteudo.strip():
            pass

            RELATORIO["vazio"].append(arquivo)
            return

        arvore = ast.parse(conteudo)

        imports = []
        funcoes = []

        for node in ast.walk(arvore):
            pass

            if isinstance(node, ast.Import):
                pass

                for item in node.names:
                    imports.append(item.name)

            elif isinstance(node, ast.ImportFrom):
                pass

                imports.append(node.module)

            elif isinstance(node, ast.FunctionDef):
                pass

                funcoes.append(node.name)

        RELATORIO["saudavel"].append({
            "arquivo": arquivo,
            "imports": imports,
            "funcoes": funcoes
        })

    except SyntaxError as e:
        pass

        RELATORIO["erro_sintaxe"].append({
            "arquivo": arquivo,
            "erro": str(e)
        })

    except ImportError as e:
        pass

        RELATORIO["erro_import"].append({
            "arquivo": arquivo,
            "erro": str(e)
        })

    except NameError as e:
        pass

        RELATORIO["erro_nome"].append({
            "arquivo": arquivo,
            "erro": str(e)
        })

    except Exception:
        pass


# ==========================================================
# PERCORRER NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO
# ==========================================================

for raiz, _, arquivos in os.walk(BASE_DIR):
    pass

    for arquivo in arquivos:
        pass

        if arquivo.endswith(".py"):
            pass

            caminho = os.path.join(raiz, arquivo)

            analisar_arquivo(caminho)

            h = gerar_hash(caminho)

            if h:
                pass

                HASHES.setdefault(h, []).append(caminho)


# ==========================================================
# DUPLICADOS
# ==========================================================

for h, arquivos in HASHES.items():
    pass

    if len(arquivos) > 1:
        pass

        RELATORIO["duplicados"].append({
            "hash": h,
            "arquivos": arquivos
        })


# ==========================================================
# RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO
# ==========================================================

print()
print("=" * 60)
print("X27 RUNTIME AUDITOR")
print("=" * 60)

print()
print("DATA :", datetime.now())

print()
print("=" * 60)
print("RESUMO EXECUTIVO")
print("=" * 60)

print("MODULOS SAUDAVEIS :", len(RELATORIO["saudavel"]))
print("ERROS SINTAXE     :", len(RELATORIO["erro_sintaxe"]))
print("ERROS IMPORT      :", len(RELATORIO["erro_import"]))
print("ERROS NAME        :", len(RELATORIO["erro_nome"]))
print("ARQUIVOS VAZIOS   :", len(RELATORIO["vazio"]))
print("DUPLICADOS        :", len(RELATORIO["duplicados"]))

print()
print("=" * 60)
print("ERROS DE SINTAXE")
print("=" * 60)

for item in RELATORIO["erro_sintaxe"][:50]:
    pass

    print()
    print(item["arquivo"])
    print(item["erro"])

print()
print("=" * 60)
print("ARQUIVOS DUPLICADOS")
print("=" * 60)

for grupo in RELATORIO["duplicados"][:20]:
    pass

    print()
    print("HASH:", grupo["hash"])

    for arq in grupo["arquivos"]:
        pass

        print("   ", arq)

print()
print("=" * 60)
print("FIM DA AUDITORIA")
print("=" * 60)


# ==========================================================
# EXPORTAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ==========================================================

saida = os.path.join(
    BASE_DIR,
    "X27_RUNTIME_REPORT.txt"
)

with open(
    saida,
    "w",
    encoding="utf-8"
) as f:

    f.write("X27 RUNTIME REPORT\n")
    f.write(f"DATA: {datetime.now()}\n\n")

    f.write(
        f"MODULOS SAUDAVEIS: {len(RELATORIO['saudavel'])}\n"
    )

    f.write(
        f"ERROS SINTAXE: {len(RELATORIO['erro_sintaxe'])}\n"
    )

    f.write(
        f"ERROS IMPORT: {len(RELATORIO['erro_import'])}\n"
    )

    f.write(
        f"ERROS NAME: {len(RELATORIO['erro_nome'])}\n"
    )

    f.write(
        f"ARQUIVOS VAZIOS: {len(RELATORIO['vazio'])}\n"
    )

    f.write(
        f"DUPLICADOS: {len(RELATORIO['duplicados'])}\n"
    )

print()
print("RELATORIO SALVO EM:")
print(saida)




