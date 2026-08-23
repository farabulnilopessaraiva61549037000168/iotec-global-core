# ==============================================================================
# IOTEC_INTERFACE_AUDITOR.py
# Auditor de Interfaces da IOTEC
# ==============================================================================

from pathlib import Path
import os

# ALTERE AQUI SE NECESSÃRIO
BASE = Path.home() / "Desktop" / "DIVERSOS" / "INTERFACES"

VIDEOS = {".mp4", ".webm", ".mov", ".avi", ".mkv"}
PAGINAS = {".html", ".htm"}

print("=" * 80)
print("IOTEC - AUDITOR DE INTERFACES")
print("=" * 80)

if not BASE.exists():
    print(f"\nPasta nÃ£o encontrada:\n{BASE}")
    raise SystemExit()

htmls = []
videos = []

for arq in BASE.rglob("*"):
    if arq.suffix.lower() in PAGINAS:
        htmls.append(arq)

    if arq.suffix.lower() in VIDEOS:
        videos.append(arq)

print(f"\nInterfaces HTML : {len(htmls)}")
print(f"VÃ­deos encontrados: {len(videos)}")

print("\n================ INTERFACES ================\n")

for h in htmls:
    print(h)

print("\n================ VÃDEOS ================\n")

for v in videos:
    print(v)

print("\n================ VERIFICANDO HTML ================\n")

for h in htmls:

    try:
        texto = h.read_text(encoding="utf-8", errors="ignore")

        possui_video = "<video" in texto.lower()

        possui_form = "<form" in texto.lower()

        possui_email = "@" in texto

        possui_tel = "tel:" in texto.lower()

        possui_site = "http://" in texto.lower() or "https://" in texto.lower()

        print("-" * 80)
        print(h.name)

        print("VÃ­deo........:", "SIM" if possui_video else "NÃƒO")
        print("FormulÃ¡rio...:", "SIM" if possui_form else "NÃƒO")
        print("Email........:", "SIM" if possui_email else "NÃƒO")
        print("Telefone.....:", "SIM" if possui_tel else "NÃƒO")
        print("Site.........:", "SIM" if possui_site else "NÃƒO")

    except Exception as e:
        print(h, e)

print("\nFim da auditoria.")

