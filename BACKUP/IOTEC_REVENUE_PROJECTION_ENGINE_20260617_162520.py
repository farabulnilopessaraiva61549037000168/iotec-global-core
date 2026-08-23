import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC REVENUE PROJECTION ENGINE
# PROJETA RECEITA FUTURA
# ==========================================================

import json
from datetime import datetime

TRACTION = r"C:\IOTEC\IOTEC_TRACTION_REPORT.json"

OUTPUT_JSON = r"C:\IOTEC\IOTEC_REVENUE_PROJECTION_REPORT.json"
OUTPUT_TXT  = r"C:\IOTEC\IOTEC_REVENUE_PROJECTION_REPORT.txt"

# ==========================================================
# CONFIGURAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ==========================================================

AVERAGE_TICKET = 5000

# ==========================================================
# CARREGA
# ==========================================================

with open(
    TRACTION,
    "r",
    encoding="utf-8"
) as f:

    traction = json.load(f)

current_clients = traction["current"]["clients"]

target_clients = traction["targets_30_days"]["clients"]

# ==========================================================
# RECEITA ATUAL
# ==========================================================

current_revenue = (
    current_clients *
    AVERAGE_TICKET
)

# ==========================================================
# PROJEÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ==========================================================

revenue_30 = (
    target_clients *
    AVERAGE_TICKET
)

revenue_90 = (
    target_clients *
    3 *
    AVERAGE_TICKET
)

gap_revenue = (
    revenue_30 -
    current_revenue
)

# ==========================================================
# STATUS
# ==========================================================

if revenue_30 >= 50000:
    pass

    status = "ESCALA"

elif revenue_30 >= 20000:
    pass

    status = "CRESCIMENTO"

else:
    pass

    status = "INICIAL"

# ==========================================================
# RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO
# ==========================================================

report = {

    "generated": str(datetime.now()),

    "average_ticket": AVERAGE_TICKET,

    "current_clients": current_clients,

    "target_clients": target_clients,

    "current_revenue": current_revenue,

    "revenue_projection_30_days": revenue_30,

    "revenue_projection_90_days": revenue_90,

    "gap_revenue": gap_revenue,

    "status": status
}

# ==========================================================
# JSON
# ==========================================================

with open(
    OUTPUT_JSON,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        report,
        f,
        indent=4,
        ensure_ascii=False
    )

# ==========================================================
# TXT
# ==========================================================

with open(
    OUTPUT_TXT,
    "w",
    encoding="utf-8"
) as f:

    f.write("\n")
    f.write("===================================\n")
    f.write("IOTEC REVENUE PROJECTION ENGINE\n")
    f.write("===================================\n\n")

    f.write(
        f"TICKET MEDIO: R$ {AVERAGE_TICKET:,.2f}\n"
    )

    f.write(
        f"CLIENTES ATUAIS: {current_clients}\n"
    )

    f.write(
        f"CLIENTES META: {target_clients}\n\n"
    )

    f.write(
        f"RECEITA ATUAL: R$ {current_revenue:,.2f}\n"
    )

    f.write(
        f"PROJECAO 30 DIAS: R$ {revenue_30:,.2f}\n"
    )

    f.write(
        f"PROJECAO 90 DIAS: R$ {revenue_90:,.2f}\n"
    )

    f.write(
        f"GAP FINANCEIRO: R$ {gap_revenue:,.2f}\n\n"
    )

    f.write(
        f"STATUS: {status}\n"
    )

# ==========================================================
# CONSOLE
# ==========================================================

print("")
print("===================================")
print("IOTEC REVENUE PROJECTION ENGINE")
print("===================================")

print("")
print(
    "RECEITA ATUAL: R$",
    current_revenue
)

print(
    "PROJECAO 30 DIAS: R$",
    revenue_30
)

print(
    "PROJECAO 90 DIAS: R$",
    revenue_90
)

print(
    "GAP FINANCEIRO: R$",
    gap_revenue
)

print("")
print(
    "STATUS:",
    status
)

print("")
print("TXT:")
print(OUTPUT_TXT)

print("")
print("JSON:")
print(OUTPUT_JSON)

print("")
print("CONCLUIDO")


