import re

with open("031_COMMERCIAL_AUTOPILOT.py", "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Substitui a referencia ao arquivo json de demo por iotec.db na classe do autopilot
content = content.replace("EMPRESA DEMONSTRAÇÃO", "PROSPECT REAL FORTALEZA")
content = content.replace("clientes.json", "iotec.db")

with open("031_COMMERCIAL_AUTOPILOT.py", "w", encoding="utf-8") as f:
    f.write(content)

print("[OK] 031_COMMERCIAL_AUTOPILOT reconfigurado para a base iotec.db!")
