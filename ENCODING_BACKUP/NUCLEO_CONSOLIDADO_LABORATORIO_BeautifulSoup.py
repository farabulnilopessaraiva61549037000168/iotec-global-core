import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import requests
from bs4 import BeautifulSoup

# Simulando um "detector" simples em site de notÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­cias
def detector_de_dados(url, palavras_chave):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    textos = soup.get_text().lower()

    achados = []
    for palavra in palavras_chave:
        if palavra in textos:
            achados.append(palavra)

    return achados

# Exemplo de uso
site = "https://www.bbc.com/news"
palavras = ['energia', 'bitcoin', 'tecnologia', 'guerra', 'clima']
print("Achados valiosos:", detector_de_dados(site, palavras))


