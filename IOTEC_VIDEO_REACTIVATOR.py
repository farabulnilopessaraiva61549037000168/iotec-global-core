# ==============================================================================
# IOTEC_VIDEO_REACTIVATOR.py
# Procura automaticamente vÃ­deos e religa os fundos das interfaces
# NÃƒO altera HTML ainda. Apenas gera um diagnÃ³stico.
# ==============================================================================

from pathlib import Path
import re

BASE = Path.home() / "Desktop" / "DIVERSOS" / "INTERFACES"

VIDEO_EXT = (".mp4", ".webm", ".mov", ".avi", ".mkv")

print("=" * 80)
print("IOTEC VIDEO REACTIVATOR")
print("=" * 80)

videos = []

# procura vÃ­deos no Desktop inteiro
for arq in Path.home().joinpath("Desktop").rglob("*"):
    if arq.suffix.lower() in VIDEO_EXT:
        videos.append(arq)

print(f"\nVÃ­deos encontrados: {len(videos)}\n")

for html in BASE.rglob("*.htm"):

    texto = html.read_text(encoding="utf-8", errors="ignore")

    refs = re.findall(
        r'<source[^>]*src=["\']([^"\']+)["\']',
        texto,
        flags=re.IGNORECASE
    )

    refs += re.findall(
        r'<video[^>]*src=["\']([^"\']+)["\']',
        texto,
        flags=re.IGNORECASE
    )

    print("-" * 80)
    print(html.name)

    if refs:

        print("ReferÃªncias encontradas:")

        for r in refs:
            print("   ", r)

    else:

        print("Nenhum caminho de vÃ­deo encontrado.")

print("\nFim.")

