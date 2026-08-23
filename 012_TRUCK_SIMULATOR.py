import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================
IOTEC
012_TRUCK_SIMULATOR.py
SIMULADOR DA FROTA TECNOLÃƒâ€œGICA
======================================================================
"""

import random
import time
from datetime import datetime


class CaminhaoTecnologico:

    def __init__(self, codigo, setor, missao):

        self.codigo = codigo
        self.setor = setor
        self.missao = missao

        self.status = "NA GARAGEM"

        self.progresso = 0

        self.carga = []


    def mostrar(self):

        print("=" * 70)

        print("CAMINHÃƒÆ'O:", self.codigo)

        print("SETOR:", self.setor)

        print("MISSÃƒÆ'O:", self.missao)

        print("STATUS:", self.status)

        print("PROGRESSO:", f"{self.progresso}%")

        print("=" * 70)


    def atualizar(self, status):

        self.status = status

        self.mostrar()


    def barra(self):

        blocos = int(self.progresso / 5)

        print("[" + "Ã¢â€"Ë†" * blocos + "-" * (20 - blocos) + "]",
              f"{self.progresso}%")



print("\n")
print("=" * 70)
print("IOTEC - CENTRAL LOGÃƒÂSTICA")
print("=" * 70)

caminhao = CaminhaoTecnologico(

    "TRK-002",

    "COMERCIAL",

    "Buscar Leads Empresariais"

)

caminhao.mostrar()

time.sleep(1)

etapas = [

    "SAINDO DA GARAGEM",

    "EM DESLOCAMENTO",

    "COLETANDO DADOS",

    "VALIDANDO MATERIAL",

    "RETORNANDO",

    "DESCARREGANDO",

    "MISSÃƒÆ'O FINALIZADA"

]

for etapa in etapas:

    caminhao.status = etapa

    caminhao.progresso += random.randint(10,20)

    if caminhao.progresso > 100:
        caminhao.progresso = 100

    print()

    print("STATUS:", etapa)

    caminhao.barra()

    time.sleep(1)


print()

print("=" * 70)
print("MATERIAL COLETADO")
print("=" * 70)

quantidade = random.randint(8,20)

for i in range(quantidade):

    empresa = {

        "empresa": f"Empresa_{i+1}",

        "cidade": random.choice(

            [

                "Fortaleza",

                "QuixadÃƒÂ¡",

                "Sobral",

                "Juazeiro",

                "Limoeiro"

            ]

        ),

        "segmento": random.choice(

            [

                "Contabilidade",

                "Advocacia",

                "IndÃƒÂºstria",

                "Hospital",

                "ClÃƒÂ­nica",

                "ConstruÃƒÂ§ÃƒÂ£o"

            ]

        )

    }

    caminhao.carga.append(empresa)

for empresa in caminhao.carga:

    print(

        empresa["empresa"],

        "-",

        empresa["segmento"],

        "-",

        empresa["cidade"]

    )


print()

print("=" * 70)
print("ENTREGA")
print("=" * 70)

print("Destino.............", caminhao.setor)

print("Carga entregue......", len(caminhao.carga), "registros")

print("HorÃƒÂ¡rio.............", datetime.now().strftime("%H:%M:%S"))

print()

print("Kernel atualizado com sucesso.")

print()

print("=" * 70)
print("MISSÃƒÆ'O CONCLUÃƒÂDA")
print("=" * 70)



