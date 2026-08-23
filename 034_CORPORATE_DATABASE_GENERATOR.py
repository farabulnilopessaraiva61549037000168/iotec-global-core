import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC CORPORATE DATABASE GENERATOR
VERSÃƒÆ'O ENTERPRISE 7.0

Cria a primeira Base Corporativa da IOTEC

======================================================================
"""

import csv
from datetime import datetime

empresas = [

# Nome, Segmento, Subsegmento, PaÃƒÂ­s

("Microsoft","Tecnologia","Software","USA"),
("Google","Tecnologia","Internet","USA"),
("Amazon","Tecnologia","Cloud","USA"),
("Apple","Tecnologia","Hardware","USA"),
("Oracle","Tecnologia","Banco de Dados","USA"),
("IBM","Tecnologia","Consultoria","USA"),
("Intel","Tecnologia","Semicondutores","USA"),
("AMD","Tecnologia","Semicondutores","USA"),
("NVIDIA","Tecnologia","IA","USA"),
("Cisco","Tecnologia","Redes","USA"),
("Dell","Tecnologia","Computadores","USA"),
("HP","Tecnologia","Computadores","USA"),
("Lenovo","Tecnologia","Computadores","China"),
("Huawei","Tecnologia","Telecom","China"),
("Samsung","Tecnologia","EletrÃƒÂ´nicos","Coreia do Sul"),
("Sony","Tecnologia","EletrÃƒÂ´nicos","JapÃƒÂ£o"),
("LG","Tecnologia","EletrÃƒÂ´nicos","Coreia do Sul"),
("Xiaomi","Tecnologia","EletrÃƒÂ´nicos","China"),

("Siemens","IndÃƒÂºstria","AutomaÃƒÂ§ÃƒÂ£o","Alemanha"),
("Bosch","IndÃƒÂºstria","AutomaÃƒÂ§ÃƒÂ£o","Alemanha"),
("ABB","Energia","AutomaÃƒÂ§ÃƒÂ£o","SuÃƒÂ­ÃƒÂ§a"),
("Schneider Electric","Energia","AutomaÃƒÂ§ÃƒÂ£o","FranÃƒÂ§a"),
("General Electric","Energia","Industrial","USA"),
("Hitachi","Industrial","Tecnologia","JapÃƒÂ£o"),

("Midea","EletrodomÃƒÂ©sticos","Linha Branca","China"),
("Haier","EletrodomÃƒÂ©sticos","Linha Branca","China"),
("Whirlpool","EletrodomÃƒÂ©sticos","Linha Branca","USA"),
("Electrolux","EletrodomÃƒÂ©sticos","Linha Branca","SuÃƒÂ©cia"),

("Toyota","Automotivo","VeÃƒÂ­culos","JapÃƒÂ£o"),
("Honda","Automotivo","VeÃƒÂ­culos","JapÃƒÂ£o"),
("Volkswagen","Automotivo","VeÃƒÂ­culos","Alemanha"),
("BMW","Automotivo","VeÃƒÂ­culos","Alemanha"),
("Mercedes-Benz","Automotivo","VeÃƒÂ­culos","Alemanha"),
("Volvo","Automotivo","VeÃƒÂ­culos","SuÃƒÂ©cia"),
("Scania","Automotivo","CaminhÃƒÂµes","SuÃƒÂ©cia"),
("Hyundai","Automotivo","VeÃƒÂ­culos","Coreia do Sul"),
("BYD","Automotivo","VeÃƒÂ­culos ElÃƒÂ©tricos","China"),
("Tesla","Automotivo","VeÃƒÂ­culos ElÃƒÂ©tricos","USA"),

("Petrobras","Energia","PetrÃƒÂ³leo","Brasil"),
("Shell","Energia","PetrÃƒÂ³leo","Reino Unido"),
("Chevron","Energia","PetrÃƒÂ³leo","USA"),
("ExxonMobil","Energia","PetrÃƒÂ³leo","USA"),
("BP","Energia","PetrÃƒÂ³leo","Reino Unido"),
("Equinor","Energia","PetrÃƒÂ³leo","Noruega"),
("TotalEnergies","Energia","PetrÃƒÂ³leo","FranÃƒÂ§a"),
("WEG","Energia","Motores","Brasil"),

("ItaÃƒÂº Unibanco","Financeiro","Banco","Brasil"),
("Banco do Brasil","Financeiro","Banco","Brasil"),
("Caixa EconÃƒÂ´mica Federal","Financeiro","Banco","Brasil"),
("Bradesco","Financeiro","Banco","Brasil"),
("Santander","Financeiro","Banco","Espanha"),
("Nubank","Financeiro","Fintech","Brasil"),
("Visa","Financeiro","Pagamentos","USA"),
("Mastercard","Financeiro","Pagamentos","USA"),
("PayPal","Financeiro","Pagamentos","USA"),
("Stripe","Financeiro","Pagamentos","USA")

]

ARQUIVO = "companies_master.csv"

with open(
    ARQUIVO,
    "w",
    newline="",
    encoding="utf-8-sig"
) as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow([

        "company_name",
        "segment",
        "subcategory",
        "country",

        "state",
        "city",

        "website",

        "linkedin",

        "phone",

        "email",

        "employees",

        "annual_revenue",

        "products",

        "services",

        "priority",

        "opportunity_score",

        "status",

        "notes"

    ])

    for empresa in empresas:

        writer.writerow([

            empresa[0],
            empresa[1],
            empresa[2],
            empresa[3],

            "",          # Estado
            "",          # Cidade

            "",          # Site

            "",          # LinkedIn

            "",          # Telefone

            "",          # Email

            "",          # FuncionÃƒÂ¡rios

            "",          # Receita

            "",          # Produtos

            "",          # ServiÃƒÂ§os

            "ALTA",      # Prioridade

            50,          # Score Inicial

            "NOVA",      # Status

            ""           # ObservaÃƒÂ§ÃƒÂµes

        ])

print()

print("="*70)
print("IOTEC CORPORATE DATABASE GENERATOR")
print("="*70)
print(datetime.now())
print("="*70)

print()

print("Arquivo criado.............",ARQUIVO)
print("Empresas...................",len(empresas))
print("VersÃƒÂ£o..................... Enterprise 7.0")

print()

print("="*70)
print("BASE CORPORATIVA GERADA COM SUCESSO")
print("="*70)



