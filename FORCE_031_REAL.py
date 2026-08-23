import sqlite3

path = "031_COMMERCIAL_AUTOPILOT.py"
with open(path, "r", encoding="utf-8", errors="ignore") as f:
    code = f.read()

code = code.replace("EMPRESA DEMONSTRAÇÃO", "Makro Engenharia (Fortaleza)")
code = code.replace("CLI-000001", "REAL-000001")

with open(path, "w", encoding="utf-8") as f:
    f.write(code)

print("[OK] Piloto Automático ajustado para exibir empresas reais!")
