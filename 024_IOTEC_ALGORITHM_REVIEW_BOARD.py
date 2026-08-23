import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from pathlib import Path
import hashlib
import json
from datetime import datetime

ROOT = Path(r"C:\IOTEC")

IGNORAR = [
    "BACKUP",
    "LABORATORIO",
    "DUPLICADOS",
    "ENCODING_BACKUP",
    "__pycache__",
    "venv",
    "node_modules",
    ".git",
    "_SANITIZADA",
    "MINERADORA_BRUTA",
    "site-packages"
]

CRITERIOS = {
    "def ":10,
    "class ":8,
    "return ":8,
    "try:":5,
    "except":5,
    "json":3,
    "database":3,
    "sql":3,
    "paypal":3,
    "api":3,
    "score":2
}

print("="*70)
print("IOTEC ALGORITHM REVIEW BOARD")
print("="*70)
print()

algoritmos=[]

for arquivo in ROOT.rglob("*.py"):

    caminho=str(arquivo)

    if any(x.lower() in caminho.lower() for x in IGNORAR):
        continue

    try:
        texto=arquivo.read_text(
            encoding="utf-8",
            errors="ignore"
        )
    except:
        continue

    score=0

    for palavra,pontos in CRITERIOS.items():

        score+=texto.count(palavra)*pontos

    tamanho=len(texto.splitlines())

    if tamanho>100:
        score+=5

    if tamanho>300:
        score+=5

    if tamanho>700:
        score+=5

    problemas=[]

    if "ROOT.rglob("*")" in texto:
        problemas.append(
            "Pesquisa irrestrita (ROOT.rglob('*'))"
        )

    if ".py" in texto and ".html" in texto:
        problemas.append(
            "Mistura HTML com PY"
        )

    if "score" in texto.lower() and "explic" not in texto.lower():
        problemas.append(
            "Possui Score sem justificativa"
        )

    if "continue" not in texto:
        problemas.append(
            "Poucos filtros de descarte"
        )

    assinatura=hashlib.md5(
        texto.encode(
            errors="ignore"
        )
    ).hexdigest()

    algoritmos.append({

        "arquivo":caminho,

        "score":score,

        "linhas":tamanho,

        "problemas":problemas,

        "assinatura":assinatura

    })

algoritmos.sort(
    key=lambda x:x["score"],
    reverse=True
)

print("ALGORITMOS ANALISADOS:",len(algoritmos))
print()

print("="*70)
print("TOP 20")
print("="*70)

for i,a in enumerate(algoritmos[:20],1):

    print()

    print(f"{i:02d}")

    print(a["arquivo"])

    print("Score :",a["score"])

    print("Linhas:",a["linhas"])

    if a["problemas"]:

        print("SituaÃƒÂ§ÃƒÂ£o : REVISÃƒÆ'O NECESSÃƒÂRIA")

        for p in a["problemas"]:

            print(" -",p)

    else:

        print("SituaÃƒÂ§ÃƒÂ£o : APROVADO")

print()

print("="*70)
print("BANCA ACADÃƒÅ MICA")
print("="*70)

print()

print("Todo algoritmo deverÃƒÂ¡ responder:")

print()

print("Ã¢â‚¬Â¢ Qual problema resolve?")

print("Ã¢â‚¬Â¢ Quais entradas aceita?")

print("Ã¢â‚¬Â¢ Quais saÃƒÂ­das produz?")

print("Ã¢â‚¬Â¢ Quais critÃƒÂ©rios utiliza?")

print("Ã¢â‚¬Â¢ Pode produzir falso positivo?")

print("Ã¢â‚¬Â¢ Pode produzir falso negativo?")

print("Ã¢â‚¬Â¢ Existe justificativa para o Score?")

print("Ã¢â‚¬Â¢ Existe explicaÃƒÂ§ÃƒÂ£o da decisÃƒÂ£o?")

print()

relatorio={

    "data":str(datetime.now()),

    "algoritmos":algoritmos

}

with open(

    "IOTEC_ALGORITHM_REVIEW.json",

    "w",

    encoding="utf-8"

) as f:

    json.dump(

        relatorio,

        f,

        indent=4,

        ensure_ascii=False

    )

print("="*70)
print("RELATÃƒâ€œRIO GERADO")
print("="*70)

print()

print("Arquivo:")

print("IOTEC_ALGORITHM_REVIEW.json")



