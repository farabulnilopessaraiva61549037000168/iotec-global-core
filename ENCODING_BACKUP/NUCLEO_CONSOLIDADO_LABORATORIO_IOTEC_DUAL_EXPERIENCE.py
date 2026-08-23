import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC_DUAL_EXPERIENCE.py
# ============================================================

import os
import json

BASE = r"C:\Users\Bruno Lopes\IOTEC_PLATFORM"
DOWNLOADS = os.path.join(os.path.expanduser("~"), "Downloads")

SAIDA = os.path.join(BASE, "_DUAL_EXPERIENCE")
CORPORATIVO = os.path.join(SAIDA, "corporativo")
ECOSSISTEMA = os.path.join(SAIDA, "ecossistema")

os.makedirs(CORPORATIVO, exist_ok=True)
os.makedirs(ECOSSISTEMA, exist_ok=True)

def detectar_interfaces():
    encontrados = []

    for base in [BASE, DOWNLOADS]:
        for root, dirs, files in os.walk(base):
            for f in files:
                if f.endswith(".html") or f.endswith(".py"):
                    encontrados.append(os.path.join(root, f))

    return encontrados

def classificar(nome):
    nome_u = nome.upper()

    if any(x in nome_u for x in ["FINANCE", "ANALISE", "AUDIT", "DATA"]):
        return "corporativo"

    if any(x in nome_u for x in ["PORTAL", "NEWS", "MEDIA", "GLOBAL"]):
        return "ecossistema"

    return "hibrido"

def gerar_pagina(nome, tipo):
    pass

    estilo = ""

    if tipo == "corporativo":
        estilo = "background:#02050a;color:#62d8ff;"
    else:
        estilo = "background:#0b1728;color:#7ef0c7;"

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>{nome}</title>
</head>

<body style="{estilo};font-family:Segoe UI;padding:40px;">
<h1>{nome}</h1>
<p>Modo: {tipo}</p>
<p>Gerado automaticamente pelo sistema dual</p>
</body>
</html>
"""

    return html

def main():
    pass

    interfaces = detectar_interfaces()

    relatorio = {
        "total": len(interfaces),
        "corporativo": 0,
        "ecossistema": 0
    }

    for i in interfaces:
        nome = os.path.basename(i)
        tipo = classificar(nome)

        if tipo == "corporativo":
            destino = CORPORATIVO
            relatorio["corporativo"] += 1
        else:
            destino = ECOSSISTEMA
            relatorio["ecossistema"] += 1

        pagina = gerar_pagina(nome, tipo)

        with open(os.path.join(destino, nome + ".html"), "w", encoding="utf-8") as f:
            f.write(pagina)

    with open(os.path.join(SAIDA, "relatorio.json"), "w") as f:
        json.dump(relatorio, f, indent=4)

    print("DUAL EXPERIENCE GERADO COM SUCESSO")

if __name__ == "__main__":
    main()


