# ==============================================================================
# IOTEC_WEB_READY.py
# Prepara uma interface da IOTEC para publicaÃ§Ã£o na Web
# ==============================================================================

from pathlib import Path
import shutil

BASE = Path.home() / "Desktop" / "DIVERSOS" / "INTERFACES"
DESTINO = BASE / "WEB_READY"

# ESCOLHA A INTERFACE
ARQUIVO = "IBEX _ IOTEC â€" Executive AI Operations.htm"

print("="*80)
print("IOTEC WEB READY")
print("="*80)

if not BASE.exists():
    print("Pasta INTERFACES nÃ£o encontrada.")
    raise SystemExit()

DESTINO.mkdir(exist_ok=True)

origem = BASE / ARQUIVO

if not origem.exists():
    print(f"Arquivo nÃ£o encontrado: {origem}")
    raise SystemExit()

# Copia HTML
shutil.copy2(origem, DESTINO / "index.html")

# Copia pastas de apoio, se existirem
for pasta in ["assets", "css", "js", "images", "img", "media_core", "videos"]:
    p = BASE / pasta
    if p.exists():
        destino_pasta = DESTINO / pasta
        if destino_pasta.exists():
            shutil.rmtree(destino_pasta)
        shutil.copytree(p, destino_pasta)
        print(f"[OK] Copiada pasta: {pasta}")

print("\nEstrutura criada em:")
print(DESTINO)

print("\nPrÃ³ximo passo:")
print("1. Abra a pasta WEB_READY.")
print("2. Verifique se existe index.html.")
print("3. Arraste a pasta para o Netlify ou outro serviÃ§o de hospedagem.")
print("="*80)

