# ==============================================================================
# 103_CAPABILITY_GRAPH_ENGINE.py
# IOTEC CAPABILITY GRAPH ENGINE
# ==============================================================================

import json
from pathlib import Path
from datetime import datetime

ROOT = Path(r"C:\IOTEC")

print("=" * 90)
print("IOTEC CAPABILITY GRAPH ENGINE")
print("=" * 90)
print()

print("Construindo Grafo de Capacidades...")
print()

graph = {
    "generated_at": datetime.now().isoformat(),
    "capabilities": [
        {
            "name": "Knowledge Management",
            "department": "Knowledge Factory",
            "inputs": [
                "Python",
                "JSON",
                "HTML"
            ],
            "outputs": [
                "DocumentaÃƒÂ§ÃƒÂ£o",
                "Livros",
                "Conhecimento"
            ],
            "consumers": [
                "Engineering",
                "Commercial"
            ],
            "status": "ONLINE"
        },
        {
            "name": "Commercial Intelligence",
            "department": "Commercial Factory",
            "inputs": [
                "Produtos",
                "Clientes",
                "Empresas"
            ],
            "outputs": [
                "Propostas",
                "CRM",
                "Pipeline"
            ],
            "consumers": [
                "Revenue Factory"
            ],
            "status": "ONLINE"
        },
        {
            "name": "Deployment",
            "department": "Deployment Factory",
            "inputs": [
                "Portais",
                "APIs"
            ],
            "outputs": [
                "Render",
                "Netlify"
            ],
            "consumers": [
                "Clientes"
            ],
            "status": "ONLINE"
        },
        {
            "name": "Revenue",
            "department": "Revenue Factory",
            "inputs": [
                "Clientes",
                "Produtos",
                "Contratos"
            ],
            "outputs": [
                "Receita"
            ],
            "consumers": [
                "Financeiro"
            ],
            "status": "AGUARDANDO"
        }
    ]
}

arquivo = ROOT / "IOTEC_CAPABILITY_GRAPH.json"

with open(
    arquivo,
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        graph,
        f,
        indent=4,
        ensure_ascii=False
    )

print("=" * 90)
print("CAPACIDADES")
print("=" * 90)
print()

for item in graph["capabilities"]:

    print(f"Ã°Å¸Å¸Â¢ {item['name']}")
    print(f"   Departamento : {item['department']}")
    print(f"   Status....... : {item['status']}")
    print()

print("=" * 90)
print("ARQUIVO GERADO")
print("=" * 90)
print()

print("IOTEC_CAPABILITY_GRAPH.json")

print()

print("=" * 90)
print("MISSÃƒÆ'O")
print("=" * 90)
print()

print("O Kernel passa")
print("a compreender")
print("capacidades")
print("e nÃƒÂ£o apenas")
print("arquivos.")
print()

print("Cada departamento")
print("produz valor")
print("para outro")
print("departamento.")
print()

print("=" * 90)
print("STATUS")
print("=" * 90)
print()

print("CAPABILITY GRAPH OPERACIONAL.")


