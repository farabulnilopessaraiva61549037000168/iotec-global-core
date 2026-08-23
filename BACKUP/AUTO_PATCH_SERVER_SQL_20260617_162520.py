import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from pathlib import Path

arquivo = Path(r"C:\IOTEC_OMEGA_X\backend\server.py")

codigo = arquivo.read_text(encoding="utf-8")

antigo = """

    INSERT INTO leads(

    company,
    email,
    sector,
    message,
    created

    )

    VALUES(?,?,?,?,?)

"""

novo = """

    INSERT INTO leads(

    company,
    email,
    sector,
    message,
    created,

    phone,
    city,

    employees,
    users_expected,

    urgency,
    current_system,

    budget_estimate,
    desired_deadline

    )

    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)

"""

codigo = codigo.replace(antigo, novo)

antigo2 = """

    company,
    email,
    sector,
    message,
    created

    ))

"""

novo2 = """

    company,
    email,
    sector,
    message,
    created,

    phone,
    city,

    employees,
    users_expected,

    urgency,
    current_system,

    budget_estimate,
    desired_deadline

    ))

"""

codigo = codigo.replace(antigo2, novo2)

arquivo.write_text(codigo, encoding="utf-8")

print("")
print("===================================")
print("SERVER SQL PATCH APLICADO")
print("===================================")
print("")


