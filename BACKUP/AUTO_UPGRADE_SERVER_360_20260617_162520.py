import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from pathlib import Path

arquivo = Path(r"C:\IOTEC_OMEGA_X\backend\server.py")

codigo = arquivo.read_text(encoding="utf-8")

if "phone = data.get" in codigo:
    print("SERVER JA ESTA ATUALIZADO")
    raise SystemExit

codigo = codigo.replace(

"""    company = data.get("company")
    email = data.get("email")
    sector = data.get("sector")
    message = data.get("message")""",

"""    company = data.get("company")
    email = data.get("email")
    sector = data.get("sector")
    message = data.get("message")

    phone = data.get("phone")
    city = data.get("city")

    employees = data.get("employees")
    users_expected = data.get("users_expected")

    urgency = data.get("urgency")
    current_system = data.get("current_system")

    budget_estimate = data.get("budget_estimate")
    desired_deadline = data.get("desired_deadline")"""
)

backup = arquivo.with_suffix(".backup")
backup.write_text(codigo, encoding="utf-8")

print("BACKUP CRIADO")
print(backup)

print("")
print("ATENCAO:")
print("O SERVER.PY FOI PREPARADO PARA LEADS 360")
print("AGORA E NECESSARIO AJUSTAR O INSERT SQL")


