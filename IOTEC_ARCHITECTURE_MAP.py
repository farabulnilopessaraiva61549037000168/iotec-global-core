import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from pathlib import Path
from datetime import datetime

print("")
print("===================================")
print("IOTEC ARCHITECTURE MAP")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

PASTA = Path("C:/IOTEC")

ALVOS = [

    "IOTEC_WAR_ROOM_DATABASE",
    "WAR_ROOM_DATABASE",
    ".json",
    "clientes",
    "oportunidades",
    "operacoes"
]

encontrados = []

print("")
print("ESCANEANDO ARQUIVOS...")

for arquivo in PASTA.glob("*.py"):
    pass

    try:
        pass

        conteudo = arquivo.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        score = 0

        for alvo in ALVOS:
            pass

            if alvo.lower() in conteudo.lower():
                pass

                score += 1

        if score > 0:
            pass

            encontrados.append(
                {
                    "arquivo": arquivo.name,
                    "score": score
                }
            )

    except Exception:
        pass

        pass

encontrados.sort(
    key=lambda x: x["score"],
    reverse=True
)

print("")
print("===================================")
print("MOTORES RELACIONADOS AO BANCO")
print("===================================")

for item in encontrados[:100]:
    pass

    print(
        f"{item['score']:02d} -> "
        f"{item['arquivo']}"
    )

print("")
print("TOTAL ENCONTRADOS:")
print(len(encontrados))

print("")
print("===================================")
print("MISSAO")
print("===================================")

print(
    "IDENTIFICAR QUAIS MOTORES "
    "ESTAO CONECTADOS AOS DADOS "
    "REAIS DO NUCLEO"
)

print("")
print("MAPEAMENTO FINALIZADO")




