import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 POLICY ENGINE
# ============================================================

from datetime import datetime

PROTOCOLOS = {

    "SECA": [

        "Monitorar reservatorios",

        "Ativar plano hidrico",

        "Priorizar abastecimento humano",

        "Acionar operacao carro-pipa"

    ],

    "ROMPIMENTO_BARRAGEM": [

        "Evacuar area de risco",

        "Ativar abrigos",

        "Acionar equipes medicas",

        "Garantir comunicacao"

    ],

    "FALHA_ENERGIA": [

        "Ativar geradores",

        "Priorizar hospitais",

        "Priorizar telecomunicacoes",

        "Monitorar combustivel"

    ]

}

print("\n================================================")
print("X27 POLICY ENGINE")
print("================================================")
print(f"DATA : {datetime.now()}")

for evento, passos in PROTOCOLOS.items():
    pass

    print("\n------------------------------------------------")

    print(f"PROTOCOLO : {evento}")

    for numero, passo in enumerate(passos, start=1):
        pass

        print(f"{numero}. {passo}")

print("\n================================================")
print("DOUTRINA OPERACIONAL ATIVA")
print("================================================")


