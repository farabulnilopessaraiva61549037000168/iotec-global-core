import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from pathlib import Path

ROOT = Path(r"C:\IOTEC")

print("")
print("===================================")
print("IOTEC CUSTOMER JOURNEY AUDITOR")
print("===================================")

pontos = {

    "WAR_ROOM":
        ROOT / "IOTEC_WAR_ROOM_DATABASE.json",

    "REVENUE":
        ROOT / "IOTEC_REAL_REVENUE.json",

    "PAYPAL_SERVER":
        ROOT / "paypal_server.py",

    "PAYMENT_BRIDGE":
        ROOT / "IOTEC_PAYMENT_BRIDGE_ENGINE.py",

    "CORE_LOGIC":
        ROOT / "IOTEC_CORE_LOGIC.py"
}

print("")
print("COMPONENTES:")

ativos = 0

for nome, arquivo in pontos.items():
    pass

    status = arquivo.exists()

    if status:
        ativos += 1

    print(
        nome,
        "->",
        "ONLINE" if status else "OFFLINE"
    )

print("")
print("AUDITORIA DE JORNADA")

perguntas = [

    "ONDE O CLIENTE DESCREVE O PROBLEMA?",
    "ONDE O ORCAMENTO E GERADO?",
    "ONDE A FATURA E GERADA?",
    "ONDE O CLIENTE PAGA?",
    "ONDE O PAGAMENTO E CONFIRMADO?",
    "ONDE O SERVICO E LIBERADO?"
]

for item in perguntas:
    pass

    print("")
    print("[ ? ]", item)

print("")
print("ATIVOS:", ativos, "/", len(pontos))

print("")
print("CONCLUSAO:")
print(
    "VERIFICAR FRONTEND, FORMULARIOS E CAIXA"
)


