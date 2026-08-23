# ==============================================================================
# IOTEC_ASSETS_FINDER.py
# Procura a pasta assets e os arquivos necessÃ¡rios
# ==============================================================================

from pathlib import Path

HOME = Path.home()

ARQUIVOS = [
    "styles-Bd_rp9Qu.css",
    "main-lf3U0thA.js",
    "index-V_TESZOS.js",
    "hero-bg-BMYctp9A.jpg"
]

print("=" * 80)
print("IOTEC ASSETS FINDER")
print("=" * 80)

encontrados = 0

for nome in ARQUIVOS:

    print(f"\nProcurando: {nome}")

    achou = False

    for arq in HOME.rglob(nome):

        print("   ", arq)
        encontrados += 1
        achou = True

    if not achou:
        print("   NÃƒO ENCONTRADO")

print("\n")

print("Pastas assets encontradas:\n")

for pasta in HOME.rglob("assets"):

    if pasta.is_dir():
        print(pasta)

print("\nArquivos encontrados:", encontrados)

