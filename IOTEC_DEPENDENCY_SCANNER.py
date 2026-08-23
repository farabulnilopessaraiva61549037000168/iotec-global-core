from pathlib import Path
from bs4 import BeautifulSoup

ARQUIVO = Path.home() / "Desktop" / "DIVERSOS" / "INTERFACES" / "WEB_READY" / "index.html"

html = ARQUIVO.read_text(encoding="utf-8", errors="ignore")
soup = BeautifulSoup(html, "html.parser")

print("="*80)
print("DEPENDÃŠNCIAS DA INTERFACE")
print("="*80)

print("\nCSS")
for x in soup.find_all("link"):
    href = x.get("href")
    if href:
        print(href)

print("\nJAVASCRIPT")
for x in soup.find_all("script"):
    src = x.get("src")
    if src:
        print(src)

print("\nIMAGENS")
for x in soup.find_all("img"):
    src = x.get("src")
    if src:
        print(src)

print("\nVÃDEOS")
for x in soup.find_all("video"):
    if x.get("src"):
        print(x.get("src"))

    for s in x.find_all("source"):
        if s.get("src"):
            print(s.get("src"))

