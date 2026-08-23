# ==============================================================================
# 104_MISSION_ORCHESTRATOR.py
# IOTEC MISSION ORCHESTRATOR
# ==============================================================================
#
# O Kernel nunca depende de um fornecedor.
# O Kernel depende da capacidade de cumprir uma missÃƒÂ£o.
#
# ==============================================================================

from datetime import datetime

print("=" * 90)
print("IOTEC MISSION ORCHESTRATOR")
print("ORQUESTRADOR DE MISSÃƒâ€¢ES")
print("=" * 90)
print()

MISSAO = {

    "nome": "Descoberta de Empresas",

    "objetivo": "Encontrar empresas reais para alimentar a InteligÃƒÂªncia Comercial.",

    "consulta": "Engenharia Fortaleza"

}

print("MISSÃƒÆ'O")
print("-" * 90)
print("Objetivo :", MISSAO["objetivo"])
print("Consulta :", MISSAO["consulta"])
print()

# ---------------------------------------------------------------------
# CAPACIDADES DISPONÃƒÂVEIS
# ---------------------------------------------------------------------

CONECTORES = [

    {
        "nome": "Google Maps",
        "status": False,
        "prioridade": 1
    },

    {
        "nome": "OpenStreetMap",
        "status": True,
        "prioridade": 2
    },

    {
        "nome": "CSV Corporativo",
        "status": True,
        "prioridade": 3
    },

    {
        "nome": "Excel Corporativo",
        "status": True,
        "prioridade": 4
    },

    {
        "nome": "API PÃƒÂºblica",
        "status": False,
        "prioridade": 5
    }

]

print("=" * 90)
print("CONECTORES")
print("=" * 90)
print()

selecionado = None

for c in CONECTORES:

    situacao = "ONLINE" if c["status"] else "INDISPONÃƒÂVEL"

    cor = "Ã°Å¸Å¸Â¢" if c["status"] else "Ã°Å¸â€Â´"

    print(f"{cor} {c['nome']:25} {situacao}")

    if selecionado is None and c["status"]:

        selecionado = c

print()

print("=" * 90)
print("DECISÃƒÆ'O DO KERNEL")
print("=" * 90)
print()

if selecionado:

    print("MissÃƒÂ£o atribuÃƒÂ­da para:")
    print()
    print(">>>", selecionado["nome"])

else:

    print("Nenhum conector disponÃƒÂ­vel.")

print()

# ---------------------------------------------------------------------
# RESULTADO PADRONIZADO
# ---------------------------------------------------------------------

EMPRESAS = [

    {
        "nome": "Empresa Exemplo A",
        "cidade": "Fortaleza",
        "segmento": "Engenharia"
    },

    {
        "nome": "Empresa Exemplo B",
        "cidade": "Fortaleza",
        "segmento": "Engenharia"
    }

]

print("=" * 90)
print("ENTREGA AO KERNEL")
print("=" * 90)
print()

for empresa in EMPRESAS:

    print(f"Ã¢Å"â€œ {empresa['nome']}")
    print(f"  Cidade.... {empresa['cidade']}")
    print(f"  Segmento.. {empresa['segmento']}")
    print()

print("=" * 90)
print("FILOSOFIA")
print("=" * 90)
print()

print("O Kernel nÃƒÂ£o pergunta")
print("qual fornecedor")
print("estÃƒÂ¡ disponÃƒÂ­vel.")
print()

print("O Kernel pergunta")
print("quem consegue")
print("cumprir a missÃƒÂ£o.")
print()

print("Toda missÃƒÂ£o")
print("deve possuir")
print("uma segunda")
print("alternativa.")
print()

print("=" * 90)
print("STATUS")
print("=" * 90)
print()

print("MissÃƒÂ£o................ ONLINE")
print("Conector..............", selecionado["nome"] if selecionado else "NENHUM")
print("Data..................", datetime.now().strftime("%d/%m/%Y %H:%M"))
print()

print("MISSION ORCHESTRATOR OPERACIONAL.")


