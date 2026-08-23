# ==============================================================================
# 105_CAPABILITY_ROUTER.py
# IOTEC CAPABILITY ROUTER
# ==============================================================================
#
# O Kernel nÃƒÂ£o procura fornecedores.
# O Kernel procura capacidades.
#
# ==============================================================================

from datetime import datetime

print("="*90)
print("IOTEC CAPABILITY ROUTER")
print("ROTEADOR DE CAPACIDADES")
print("="*90)
print()

# --------------------------------------------------------------------
# MISSÃƒÆ'O
# --------------------------------------------------------------------

MISSAO = {

    "nome":"Descoberta Comercial",

    "capacidade":"EMPRESAS",

    "consulta":"Engenharia Fortaleza"

}

print("MISSÃƒÆ'O")
print("-"*90)

print("Nome.......",MISSAO["nome"])
print("Capacidade.",MISSAO["capacidade"])
print("Consulta...",MISSAO["consulta"])

print()

# --------------------------------------------------------------------
# CONECTORES
# --------------------------------------------------------------------

CONECTORES=[

{

"nome":"Google Maps",

"online":False,

"capacidades":[

"EMPRESAS",
"MAPA",
"ROTAS",
"AVALIAÃƒâ€¡Ãƒâ€¢ES"

]

},

{

"nome":"OpenStreetMap",

"online":True,

"capacidades":[

"EMPRESAS",
"MAPA",
"ENDEREÃƒâ€¡OS"

]

},

{

"nome":"CSV",

"online":True,

"capacidades":[

"EMPRESAS",
"EMAIL",
"TELEFONE",
"CNPJ"

]

},

{

"nome":"Excel",

"online":True,

"capacidades":[

"EMPRESAS",
"EMAIL"

]

}

]

print("="*90)
print("BUSCA DE CAPACIDADES")
print("="*90)
print()

escolhido=None

for c in CONECTORES:

    status="ONLINE" if c["online"] else "OFFLINE"

    print(c["nome"])
    print("Status......",status)
    print("Capacidades.",", ".join(c["capacidades"]))
    print()

    if escolhido is None:

        if c["online"]:

            if MISSAO["capacidade"] in c["capacidades"]:

                escolhido=c

print("="*90)
print("DECISÃƒÆ'O")
print("="*90)
print()

if escolhido:

    print("Fornecedor escolhido:")

    print(escolhido["nome"])

else:

    print("Nenhum fornecedor encontrado.")

print()

# --------------------------------------------------------------------
# SIMULAÃƒâ€¡ÃƒÆ'O
# --------------------------------------------------------------------

empresas=[

{

"nome":"Empresa Alpha",

"cidade":"Fortaleza",

"origem":escolhido["nome"]

},

{

"nome":"Empresa Beta",

"cidade":"Fortaleza",

"origem":escolhido["nome"]

}

]

print("="*90)
print("ENTREGA")
print("="*90)
print()

for e in empresas:

    print("Ã¢Å"â€œ",e["nome"])
    print("Cidade...",e["cidade"])
    print("Origem...",e["origem"])
    print()

print("="*90)
print("DOUTRINA")
print("="*90)
print()

print("O Kernel nunca")
print("depende de um")
print("fornecedor.")

print()

print("O Kernel depende")
print("da capacidade")
print("de cumprir")
print("a missÃƒÂ£o.")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("Capacidade.........",MISSAO["capacidade"])
print("Conector...........",escolhido["nome"])
print("Data................",datetime.now().strftime("%d/%m/%Y %H:%M"))

print()

print("CAPABILITY ROUTER OPERACIONAL.")


