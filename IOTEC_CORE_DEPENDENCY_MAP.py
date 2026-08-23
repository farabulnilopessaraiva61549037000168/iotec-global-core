import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from pathlib import Path
from datetime import datetime
import re

print("")
print("===================================")
print("IOTEC CORE DEPENDENCY MAP")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

PASTA = Path("C:/IOTEC")

PADROES = [

    "IOTEC_WAR_ROOM_DATABASE",
    "json.load",
    "json.dump",
    "open(",
    "sqlite3.connect",
    "clientes",
    "oportunidades",
    "operacoes",
    "receita",
    "fatura",
    "pagamento"
]

resultado = []

print("")
print("ESCANEANDO DEPENDENCIAS...")

for arquivo in PASTA.glob("*.py"):
    pass

    try:
        pass

        texto = arquivo.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        score = 0
        encontrados = []

        for padrao in PADROES:
            pass

            ocorrencias = texto.lower().count(
                padrao.lower()
            )

            if ocorrencias > 0:
                pass

                score += ocorrencias
                encontrados.append(
                    f"{padrao}({ocorrencias})"
                )

        imports = re.findall(
            r"^\s*(?:import|from)\s+([a-zA-Z0-9_\.]+)",
            texto,
            flags=re.MULTILINE
        )

        if score > 0:
            pass

            resultado.append({

                "arquivo":
                arquivo.name,

                "score":
                score,

                "imports":
                len(imports),

                "dependencias":
                encontrados[:10]
            })

    except Exception:
        pass

        pass

resultado.sort(
    key=lambda x: x["score"],
    reverse=True
)

print("")
print("===================================")
print("TOP MOTORES CRITICOS")
print("===================================")

for item in resultado[:50]:
    pass

    print("")
    print("ARQUIVO:")
    print(item["arquivo"])

    print("SCORE:")
    print(item["score"])

    print("IMPORTS:")
    print(item["imports"])

    print("DEPENDENCIAS:")

    for dep in item["dependencias"]:
        pass

        print(" -", dep)

print("")
print("===================================")
print("RESUMO")
print("===================================")

print(
    "ARQUIVOS RELEVANTES:"
)

print(
    len(resultado)
)

if len(resultado) > 0:
    pass

    print("")
    print("ARQUIVO MAIS CRITICO:")

    print(
        resultado[0]["arquivo"]
    )

    print("SCORE:")

    print(
        resultado[0]["score"]
    )

print("")
print("===================================")
print("MISSAO")
print("===================================")

print(
    "IDENTIFICAR OS MOTORES "
    "QUE PARTICIPAM DO FLUXO "
    "REAL DE CLIENTES, "
    "OPORTUNIDADES, "
    "OPERACOES E RECEITA."
)

print("")
print("MAPEAMENTO FINALIZADO")




