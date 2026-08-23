# ==========================================================
# 080_OFFICIAL_ASSET_FILTER.py
# IOTEC OFFICIAL ASSET FILTER
# ==========================================================

from pathlib import Path
import json

ROOT = Path("C:/IOTEC")

IGNORAR_PASTAS = {

    ".git",
    ".github",
    "venv",
    ".venv",
    "env",
    "node_modules",
    "__pycache__",
    "site-packages",
    "dist",
    "build",
    "docs",
    "documentation",
    "examples",
    "example",
    "demo",
    "tests",
    "test"

}

IGNORAR_ARQUIVOS = [

    "help",
    "git-",
    "bootstrap",
    "jquery",
    "react",
    "vue",
    "angular",
    "node",
    "python",
    "pip",
    "readme",
    "license",
    "copying",
    "changelog"

]

oficiais = []
terceiros = []

print("="*70)
print("IOTEC OFFICIAL ASSET FILTER")
print("="*70)
print()

print("Separando patrimÃƒÂ´nio oficial...")
print()

for arquivo in ROOT.rglob("*"):

    if not arquivo.is_file():
        continue

    caminho = str(arquivo).lower()

    ignorar = False

    for pasta in IGNORAR_PASTAS:

        if f"\\{pasta.lower()}\" in caminho:

            ignorar = True
            break

    nome = arquivo.name.lower()

    if not ignorar:

        for item in IGNORAR_ARQUIVOS:

            if item in nome:

                ignorar = True
                break

    registro = {

        "arquivo":arquivo.name,
        "caminho":str(arquivo)

    }

    if ignorar:

        terceiros.append(registro)

    else:

        oficiais.append(registro)

print("="*70)
print("RESULTADO")
print("="*70)
print()

print(f"PatrimÃƒÂ´nio Oficial : {len(oficiais)}")
print(f"DependÃƒÂªncias....... : {len(terceiros)}")

print()

with open(
    "IOTEC_OFFICIAL_ASSETS.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        oficiais,
        f,
        indent=4,
        ensure_ascii=False
    )

with open(
    "IOTEC_EXTERNAL_ASSETS.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        terceiros,
        f,
        indent=4,
        ensure_ascii=False
    )

print("="*70)
print("ARQUIVOS GERADOS")
print("="*70)
print()

print("IOTEC_OFFICIAL_ASSETS.json")
print("IOTEC_EXTERNAL_ASSETS.json")

print()

print("="*70)
print("MISSÃƒÆ'O")
print("="*70)
print()

print("A Executive Skin")
print("passa a trabalhar")
print("somente com")
print("o patrimÃƒÂ´nio")
print("oficial da IOTEC.")

print()

print("DependÃƒÂªncias externas")
print("continuam preservadas,")
print("mas deixam de")
print("interferir nas")
print("decisÃƒÂµes da plataforma.")


