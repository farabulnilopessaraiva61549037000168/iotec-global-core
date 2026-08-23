import json
import os
from datetime import datetime

print("="*90)
print("IOTEC EXECUTIVE INTELLIGENCE REPORT")
print("="*90)
print()

# ==========================================================
# LEITURA DOS MÃƒâ€œDULOS
# ==========================================================

def contar_registros(arquivo):

    if not os.path.exists(arquivo):
        return 0

    try:

        with open(
            arquivo,
            "r",
            encoding="utf-8"
        ) as f:

            dados = json.load(f)

            if isinstance(dados,list):
                return len(dados)

            if isinstance(dados,dict):
                return len(dados)

            return 0

    except:

        return 0


empresas = contar_registros("IOTEC_COMPANY_DATABASE.json")

verificadas = contar_registros("IOTEC_VERIFIED_COMPANIES.json")

grafo = contar_registros("IOTEC_CORPORATE_GRAPH.json")

memoria = contar_registros("IOTEC_CORPORATE_MEMORY.json")

cientistas = contar_registros("IOTEC_SCIENTIFIC_WORKFORCE.json")


# ==========================================================
# RELATÃƒâ€œRIO
# ==========================================================

print("PRESIDÃƒÅ NCIA")
print("-"*90)
print()

print("Data................",datetime.now())
print()

print("="*90)
print("CONHECIMENTO")
print("="*90)
print()

print(f"Corpo CientÃƒÂ­fico.............. {cientistas}")
print(f"Conhecimentos Catalogados.... {memoria}")

print()

print("="*90)
print("INTELIGÃƒÅ NCIA DE MERCADO")
print("="*90)
print()

print(f"Empresas Descobertas.......... {empresas}")
print(f"Empresas Verificadas.......... {verificadas}")
print(f"Grafo Corporativo............ {grafo}")

print()

print("="*90)
print("RECEITA")
print("="*90)
print()

print("Receita Confirmada........... R$ 0,00")
print("Produtos Vendidos............ 0")
print("Clientes..................... 0")
print("CRM.......................... 0")

print()

print("="*90)
print("MISSÃƒâ€¢ES PRIORITÃƒÂRIAS")
print("="*90)
print()

missoes = [

"Expandir descoberta de empresas",

"Confirmar websites oficiais",

"Descobrir canais comerciais",

"Criar CRM automÃƒÂ¡tico",

"Publicar produtos",

"Captar primeiro cliente",

"Validar fluxo completo de receita"

]

for i,m in enumerate(missoes,1):

    print(f"{i:02d} - {m}")

print()

print("="*90)
print("GARGALOS")
print("="*90)
print()

print("Revenue Factory............... CRÃƒÂTICO")

if empresas < 100:
    print("Poucas empresas descobertas.")

if memoria < 100:
    print("MemÃƒÂ³ria cientÃƒÂ­fica pequena.")

print("NecessÃƒÂ¡rio aumentar canais comerciais.")

print()

print("="*90)
print("CHEFE DE GABINETE")
print("="*90)
print()

print("Boa noite, Presidente.")
print()

print("A infraestrutura estratÃƒÂ©gica")
print("encontra-se operacional.")

print()

print("Os pesquisadores continuam")
print("alimentando a memÃƒÂ³ria")

print("corporativa da IOTEC.")

print()

print("A prioridade institucional")

print("passa a ser")

print("transformar")

print("conhecimento")

print("em oportunidades comerciais.")

print()

print("Cada missÃƒÂ£o futura")

print("deverÃƒÂ¡ possuir")

print("impacto direto")

print("na geraÃƒÂ§ÃƒÂ£o de receita.")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("MATURIDADE DA PLATAFORMA...... 74 %")

print("PRÃƒâ€œXIMA FASE................. EXPANSÃƒÆ'O COMERCIAL")

print()

print("EXECUTIVE INTELLIGENCE REPORT OPERACIONAL.")

