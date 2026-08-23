# ==============================================================================
# IOTEC PRODUCT DISCOVERY ENGINE
# MÃ"DULO 001 - INVENTÃRIO DO PATRIMÃ"NIO DIGITAL
# NÃƒO ALTERA ARQUIVOS ORIGINAIS
# ==============================================================================

from pathlib import Path
import shutil
import json
from datetime import datetime

print("="*80)
print("IOTEC PRODUCT DISCOVERY ENGINE")
print("MÃ"DULO 001")
print("="*80)

HOME = Path.home()

PASTAS_RAIZ = [
    HOME / "Desktop" / "DIVERSOS",
    HOME / "Downloads",
    HOME / "Documents"
]

LAB = HOME / "Documents" / "IOTEC_PRODUCT_LAB"

(LAB / "CATALOGO").mkdir(parents=True, exist_ok=True)
(LAB / "PROJETOS").mkdir(exist_ok=True)
(LAB / "RELATORIOS").mkdir(exist_ok=True)
(LAB / "LOGS").mkdir(exist_ok=True)

EXTENSOES = {
    ".html",
    ".htm",
    ".py",
    ".js",
    ".css",
    ".json",
    ".tsx",
    ".jsx",
    ".sql",
    ".db",
    ".sqlite",
    ".sqlite3",
    ".pdf",
    ".docx",
    ".xlsx",
    ".pptx"
}

catalogo = []

for pasta in PASTAS_RAIZ:

    if not pasta.exists():
        continue

    print(f"\nEscaneando: {pasta}")

    for arquivo in pasta.rglob("*"):

        try:

            if not arquivo.is_file():
                continue

            if arquivo.suffix.lower() not in EXTENSOES:
                continue

            info = {
                "nome": arquivo.name,
                "arquivo": str(arquivo),
                "extensao": arquivo.suffix.lower(),
                "tamanho_mb": round(
                    arquivo.stat().st_size / (1024 * 1024),
                    2
                ),
                "modificado": datetime.fromtimestamp(
                    arquivo.stat().st_mtime
                ).strftime("%Y-%m-%d %H:%M:%S")
            }

            catalogo.append(info)

        except:
            pass

saida = LAB / "CATALOGO" / "CATALOGO_INICIAL.json"

with open(saida, "w", encoding="utf-8") as f:
    json.dump(catalogo, f, indent=4, ensure_ascii=False)

print("\n")
print("="*80)
print("FINALIZADO")
print("="*80)

print(f"Arquivos encontrados: {len(catalogo)}")
print(f"CatÃ¡logo salvo em:\n{saida}")

