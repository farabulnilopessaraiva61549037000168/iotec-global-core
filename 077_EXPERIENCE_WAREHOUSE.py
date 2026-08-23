# ==========================================================
# 077_EXPERIENCE_WAREHOUSE.py
# IOTEC EXPERIENCE WAREHOUSE
# ==========================================================

from pathlib import Path
from collections import Counter
import json
from datetime import datetime

ROOT = Path("C:/IOTEC")

EXTENSOES = {
    ".html": "HTML",
    ".htm": "HTML",
    ".css": "CSS",
    ".js": "JAVASCRIPT"
}

CATEGORIAS = {
    "dashboard": "Dashboard",
    "cockpit": "Cockpit",
    "login": "Login",
    "portal": "Portal",
    "landing": "Landing Page",
    "cliente": "Cliente",
    "client": "Cliente",
    "finance": "Financeiro",
    "payment": "Financeiro",
    "commercial": "Comercial",
    "crm": "CRM",
    "report": "Relatorio",
    "catalog": "Catalogo",
    "catalogo": "Catalogo"
}

print("="*70)
print("IOTEC EXPERIENCE WAREHOUSE")
print("="*70)
print()

print("Catalogando patrimonio visual...")
print()

arquivos = []
tipos = Counter()
categorias = Counter()

for arq in ROOT.rglob("*"):

    if not arq.is_file():
        continue

    ext = arq.suffix.lower()

    if ext not in EXTENSOES:
        continue

    tipo = EXTENSOES[ext]
    tipos[tipo] += 1

    categoria = "Geral"

    nome = arq.stem.lower()

    for chave, valor in CATEGORIAS.items():

        if chave in nome:
            categoria = valor
            break

    categorias[categoria] += 1

    arquivos.append({

        "arquivo": arq.name,
        "categoria": categoria,
        "tipo": tipo,
        "caminho": str(arq)

    })

print("="*70)
print("PATRIMONIO VISUAL")
print("="*70)
print()

print(f"Arquivos encontrados : {len(arquivos)}")
print()

print("="*70)
print("POR TIPO")
print("="*70)

for nome, qtd in tipos.most_common():

    print(f"{nome:<20}{qtd}")

print()

print("="*70)
print("POR CATEGORIA")
print("="*70)

for nome, qtd in categorias.most_common():

    print(f"{nome:<20}{qtd}")

print()

warehouse = {

    "created": str(datetime.now()),
    "total": len(arquivos),
    "files": arquivos

}

with open("IOTEC_EXPERIENCE_WAREHOUSE.json","w",encoding="utf-8") as f:

    json.dump(warehouse,f,indent=4,ensure_ascii=False)

print("="*70)
print("ARQUIVO GERADO")
print("="*70)
print()

print("IOTEC_EXPERIENCE_WAREHOUSE.json")

print()

print("="*70)
print("MISSAO")
print("="*70)
print()

print("Todo HTML passa a integrar")
print("o patrimonio permanente")
print("da IOTEC.")

print()

print("Nenhuma interface")
print("sera perdida.")


