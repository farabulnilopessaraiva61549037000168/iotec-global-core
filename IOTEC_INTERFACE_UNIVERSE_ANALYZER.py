# ==============================================================================
# IOTEC_INTERFACE_UNIVERSE_ANALYZER.py
# Analisa todo o universo das interfaces da IOTEC
# NÃ£o modifica nenhum arquivo
# ==============================================================================

from pathlib import Path
from bs4 import BeautifulSoup
import re

BASE = Path.home() / "Desktop" / "DIVERSOS" / "INTERFACES"

print("="*100)
print("               IOTEC - UNIVERSO DAS INTERFACES")
print("="*100)

if not BASE.exists():
    print("Pasta nÃ£o encontrada:")
    print(BASE)
    raise SystemExit()

htmls = sorted(BASE.rglob("*.htm")) + sorted(BASE.rglob("*.html"))

print(f"\nInterfaces encontradas: {len(htmls)}")

relatorio = []

for html in htmls:

    try:

        texto = html.read_text(encoding="utf-8", errors="ignore")

        soup = BeautifulSoup(texto,"html.parser")

        titulo = soup.title.string.strip() if soup.title else "SEM TÃTULO"

        h1 = [x.get_text(" ",strip=True) for x in soup.find_all("h1")]

        h2 = [x.get_text(" ",strip=True) for x in soup.find_all("h2")]

        botoes = len(soup.find_all("button"))

        formularios = len(soup.find_all("form"))

        videos = len(soup.find_all("video"))

        imagens = len(soup.find_all("img"))

        scripts = len(soup.find_all("script"))

        css = len(soup.find_all("link"))

        links = len(soup.find_all("a"))

        inputs = len(soup.find_all("input"))

        iframes = len(soup.find_all("iframe"))

        email = bool(re.search(r'[\w\.-]+@[\w\.-]+',texto))

        telefone = "tel:" in texto.lower()

        mapas = "leaflet" in texto.lower() or "google.maps" in texto.lower()

        graficos = (
            "chart.js" in texto.lower() or
            "echarts" in texto.lower() or
            "plotly" in texto.lower()
        )

        palavras = []

        for palavra in [
            "AI","INTELLIGENCE","OMEGA","GLOBAL","CONTROL",
            "NETWORK","LIVE","BROADCAST","EXECUTIVE",
            "CORPORATE","DASHBOARD","OPERATION","IOTEC",
            "IBEX","ANALYSIS","SECURITY"
        ]:

            if palavra.lower() in texto.lower():
                palavras.append(palavra)

        relatorio.append({

            "arquivo":html,
            "titulo":titulo,
            "h1":len(h1),
            "h2":len(h2),
            "videos":videos,
            "imagens":imagens,
            "formularios":formularios,
            "botoes":botoes,
            "inputs":inputs,
            "scripts":scripts,
            "css":css,
            "links":links,
            "iframes":iframes,
            "email":email,
            "telefone":telefone,
            "graficos":graficos,
            "mapas":mapas,
            "palavras":palavras

        })

    except Exception as erro:

        print(html)
        print(erro)

print("\n")

for r in relatorio:

    print("="*100)

    print(r["arquivo"].name)

    print("-"*100)

    print("TÃ­tulo........:",r["titulo"])
    print("H1............:",r["h1"])
    print("H2............:",r["h2"])
    print("VÃ­deos........:",r["videos"])
    print("Imagens.......:",r["imagens"])
    print("FormulÃ¡rios...:",r["formularios"])
    print("BotÃµes........:",r["botoes"])
    print("Inputs........:",r["inputs"])
    print("Links.........:",r["links"])
    print("Scripts.......:",r["scripts"])
    print("CSS...........:",r["css"])
    print("Iframes.......:",r["iframes"])
    print("Email.........:",r["email"])
    print("Telefone......:",r["telefone"])
    print("GrÃ¡ficos......:",r["graficos"])
    print("Mapas.........:",r["mapas"])
    print("Temas.........:",", ".join(r["palavras"]))

print("\n")
print("="*100)
print("FIM DA ANÃLISE")
print("="*100)

