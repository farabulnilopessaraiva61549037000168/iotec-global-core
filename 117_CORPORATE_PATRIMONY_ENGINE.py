# ==============================================================================
# 117_CORPORATE_PATRIMONY_ENGINE.py
# IOTEC CORPORATE PATRIMONY ENGINE
# ==============================================================================

import json
from datetime import datetime

print("="*90)
print("IOTEC CORPORATE PATRIMONY ENGINE")
print("BALANÃƒâ€¡O PATRIMONIAL OPERACIONAL")
print("="*90)
print()

PATRIMONIO={

"Python Modules":117,
"Frameworks":6,
"Capacidades":15,
"Agentes":9,
"Centros EstratÃƒÂ©gicos":12,
"FÃƒÂ¡bricas":8,
"Estados":9,
"Cidades Piloto":36,
"Segmentos":18,
"MissÃƒÂµes":648,
"Empresas Descobertas":2,
"Oportunidades":2,
"Produtos":61,
"APIs":38,
"Campanhas":19,
"Clientes":0,
"Receita":0

}

print("="*90)
print("ATIVOS OPERACIONAIS")
print("="*90)
print()

for ativo,valor in PATRIMONIO.items():

    print(f"{ativo:30} {valor}")

print()

print("="*90)
print("ÃƒÂNDICES CORPORATIVOS")
print("="*90)
print()

indices={

"Conhecimento":96,

"Arquitetura":98,

"OrganizaÃƒÂ§ÃƒÂ£o":97,

"AutomaÃƒÂ§ÃƒÂ£o":87,

"Territorial":28,

"Comercial":34,

"Receita":2

}

for nome,indice in indices.items():

    barras="Ã¢â€"Ë†"*int(indice/5)

    print(f"{nome:20} {barras} {indice}%")

print()

print("="*90)
print("PASSIVOS OPERACIONAIS")
print("="*90)
print()

PASSIVOS=[

"Google Maps pendente",

"LinkedIn pendente",

"Clientes reais",

"Receita recorrente",

"ImplantaÃƒÂ§ÃƒÂ£o OpenAI",

"WhatsApp Business"

]

for item in PASSIVOS:

    print("Ã¢Å¡Â ",item)

print()

print("="*90)
print("PATRIMÃƒâ€NIO TOTAL")
print("="*90)
print()

pontos=sum(PATRIMONIO.values())

print("Ativos registrados.......",len(PATRIMONIO))
print("ÃƒÂndices..................",len(indices))
print("Passivos.................",len(PASSIVOS))
print("PatrimÃƒÂ´nio NumÃƒÂ©rico......",pontos)

print()

print("="*90)
print("MISSÃƒÆ'O")
print("="*90)
print()

print("O patrimÃƒÂ´nio")
print("da empresa")
print("nÃƒÂ£o ÃƒÂ© formado")
print("apenas por dinheiro.")

print()

print("Conhecimento")

print("Arquitetura")

print("Capacidades")

print("Agentes")

print("Produtos")

print("MissÃƒÂµes")

print("tambÃƒÂ©m sÃƒÂ£o")

print("ativos")

print("corporativos.")

print()

print("="*90)
print("FILOSOFIA")
print("="*90)
print()

print("Toda capacidade")
print("ÃƒÂ© patrimÃƒÂ´nio.")

print()

print("Todo algoritmo")
print("ÃƒÂ© patrimÃƒÂ´nio.")

print()

print("Todo conhecimento")
print("ÃƒÂ© patrimÃƒÂ´nio.")

print()

print("Toda missÃƒÂ£o")
print("gera patrimÃƒÂ´nio.")

print()

print("Toda oportunidade")
print("aumenta")
print("o valor")
print("da IOTEC.")

print()

saida={

"generated_at":datetime.now().isoformat(),

"ativos":PATRIMONIO,

"indices":indices,

"passivos":PASSIVOS

}

with open(

"IOTEC_CORPORATE_PATRIMONY.json",

"w",

encoding="utf8"

) as f:

    json.dump(

        saida,

        f,

        indent=4,

        ensure_ascii=False

    )

print("="*90)
print("ARQUIVO GERADO")
print("="*90)
print()

print("IOTEC_CORPORATE_PATRIMONY.json")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("PATRIMÃƒâ€NIO CORPORATIVO REGISTRADO.")


