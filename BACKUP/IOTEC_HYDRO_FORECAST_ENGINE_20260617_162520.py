import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
from datetime import datetime

HYDRO_REPORT = r"C:\IOTEC\IOTEC_HYDROECONOMIC_REPORT.json"

try:
    pass

    with open(
        HYDRO_REPORT,
        "r",
        encoding="utf-8"
    ) as f:

        hydro = json.load(f)

except:
    pass

    print("")
    print("RELATORIO NAO ENCONTRADO")
    print(HYDRO_REPORT)
    raise SystemExit

reservoir = hydro.get(
    "reservoir",
    0
)

contracts = hydro.get(
    "contracts",
    0
)

revenue = hydro.get(
    "revenue",
    0
)

power_index = hydro.get(
    "power_index",
    0
)

print("")
print("===================================")
print("IOTEC HYDRO FORECAST ENGINE")
print("===================================")
print("")

print(
    f"RESERVATORIO ATUAL: {reservoir}"
)

print(
    f"CONTRATOS ATUAIS: {contracts}"
)

print(
    f"RECEITA ATUAL: R$ {revenue:,.2f}"
)

print("")
print("SIMULACOES")
print("")

levels = [

    10,
    25,
    50,
    100,
    250,
    500,
    1000

]

forecast = []

for level in levels:
    pass

    growth_factor = level / max(
        reservoir,
        1
    )

    future_contracts = round(
        contracts *
        growth_factor
    )

    future_revenue = (
        revenue *
        growth_factor
    )

    forecast.append({

        "reservoir": level,

        "contracts": future_contracts,

        "revenue": future_revenue

    })

    print(
        f"RESERVATORIO {level}"
    )

    print(
        f"CONTRATOS PREVISTOS: "
        f"{future_contracts}"
    )

    print(
        f"RECEITA PREVISTA: "
        f"R$ {future_revenue:,.2f}"
    )

    print("")

report = {

    "generated": str(
        datetime.now()
    ),

    "current_reservoir":
        reservoir,

    "current_contracts":
        contracts,

    "current_revenue":
        revenue,

    "power_index":
        power_index,

    "forecast":
        forecast

}

OUTPUT = (
    r"C:\IOTEC\IOTEC_HYDRO_FORECAST_REPORT.json"
)

with open(
    OUTPUT,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        report,
        f,
        indent=4,
        ensure_ascii=False
    )

print("")
print("JSON:")
print(OUTPUT)

print("")
print("CONCLUIDO")


