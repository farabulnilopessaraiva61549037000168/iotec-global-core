import json
import os
from datetime import datetime

WORLD_MAP = "IOTEC_WORLD_MAP.json"

if not os.path.exists(WORLD_MAP):

    print("Mapa econÃƒÂ´mico inexistente.")
    raise SystemExit()

with open(WORLD_MAP,"r",encoding="utf-8") as f:

    world = json.load(f)

# ==========================================================
# ESTATÃƒÂSTICAS
# ==========================================================

countries = set()
states = set()
cities = set()
sectors = set()

coverage_sum = 0

for node in world:

    countries.add(node["country"])
    states.add(node["state"])
    cities.add(node["city"])
    sectors.add(node["sector"])

    coverage_sum += node.get("coverage",0)

average = 0

if len(world)>0:

    average = coverage_sum/len(world)

# ==========================================================
# AGRUPAMENTO
# ==========================================================

sector_counter = {}

for node in world:

    sector = node["sector"]

    sector_counter.setdefault(sector,0)

    sector_counter[sector]+=1

# ==========================================================

print("="*90)
print("IOTEC COVERAGE INTELLIGENCE ENGINE")
print("="*90)
print()

print("COBERTURA GLOBAL")
print("-"*90)
print()

print("PaÃƒÂ­ses...............",len(countries))
print("Estados..............",len(states))
print("Cidades..............",len(cities))
print("Setores..............",len(sectors))
print("NÃƒÂ³s EconÃƒÂ´micos.......",len(world))
print()

print("Cobertura MÃƒÂ©dia...... {:.1f}%".format(average))

print()

print("="*90)
print("SETORES")
print("="*90)
print()

for sector,total in sorted(sector_counter.items()):

    print("{:<20} {}".format(sector,total))

print()

print("="*90)
print("PRÃƒâ€œXIMA EXPANSÃƒÆ'O")
print("="*90)
print()

pending = [n for n in world if n["coverage"] == 0]

for node in pending[:15]:

    print(
        node["country"],
        "-",
        node["city"],
        "-",
        node["sector"]
    )

print()

print("="*90)
print("MISSÃƒÆ'O")
print("="*90)
print()

print("Medir continuamente")
print("a cobertura")
print("econÃƒÂ´mica")
print("da plataforma.")
print()

print("="*90)
print("CHEFE DE GABINETE")
print("="*90)
print()

print()

print("Bom dia, Presidente.")
print()

print("A InteligÃƒÂªncia de Cobertura")
print("passa a medir")
print("o avanÃƒÂ§o")
print("da ocupaÃƒÂ§ÃƒÂ£o")
print("dos mercados.")

print()

print("O Kernel")
print("priorizarÃƒÂ¡")
print("os territÃƒÂ³rios")
print("com menor")
print("cobertura.")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("Data :",datetime.now())
print()

print("COVERAGE INTELLIGENCE OPERACIONAL.")

