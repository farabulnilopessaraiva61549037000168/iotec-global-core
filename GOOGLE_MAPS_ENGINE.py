import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import requests

API_KEY = "AIzaSyB8aJ1IHAPECPr-DPJiPJVt2lLUOmAhJ1A"

BASE_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"

print("="*70)
print("IOTEC GOOGLE MAPS ENGINE")
print("="*70)
print()

consulta = "engenharia Fortaleza"

print("Pesquisando:", consulta)
print()

try:

    resposta = requests.get(
        BASE_URL,
        params={
            "query": consulta,
            "key": API_KEY
        },
        timeout=30
    )

    print("HTTP:", resposta.status_code)

    dados = resposta.json()

    status = dados.get("status")

    print("STATUS GOOGLE:", status)
    print()

    if status != "OK":
        print(dados)
        raise SystemExit()

    resultados = dados.get("results", [])

    print("Empresas encontradas:", len(resultados))
    print()

    for empresa in resultados[:10]:

        print("="*60)
        print(empresa.get("name",""))
        print(empresa.get("formatted_address",""))
        print("AvaliaÃ§Ã£o:", empresa.get("rating","N/D"))

except Exception as e:

    print()
    print("ERRO:")
    print(e)






