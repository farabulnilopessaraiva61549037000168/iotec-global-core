from pprint import pprint
from GOOGLE_MAPS_CONNECTOR import pesquisar_empresas

print("=" * 70)
print("IOTEC GOOGLE MAPS TEST")
print("=" * 70)
print()

consulta = "engenharia Fortaleza"

print("Pesquisando:", consulta)
print()

empresas = pesquisar_empresas(consulta)

print("Empresas encontradas:", len(empresas))
print()

for empresa in empresas[:5]:

    pprint(empresa)

    print("-" * 70)


