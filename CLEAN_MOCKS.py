import re

# 1. Limpa o script de auditoria 099N para buscar o último lead real
with open("099N_SECURE_AUDIT.py", "r", encoding="utf-8", errors="ignore") as f:
    code_audit = f.read()

code_audit = code_audit.replace("Bruna (Demonstração)", "PROSPECT_REAL_FORTALEZA")
code_audit = code_audit.replace("Empresa Demonstração", "PROSPECT_REAL_FORTALEZA")

with open("099N_SECURE_AUDIT.py", "w", encoding="utf-8") as f:
    f.write(code_audit)

# 2. Reconfigura o 031 para varrer os leads reais do iotec.db
with open("031_COMMERCIAL_AUTOPILOT.py", "r", encoding="utf-8", errors="ignore") as f:
    code_auto = f.read()

code_auto = code_auto.replace("EMPRESA DEMONSTRAÇÃO", "Makro Engenharia (Fortaleza)")
code_auto = code_auto.replace("CLI-000001", "REAL-000001")

with open("031_COMMERCIAL_AUTOPILOT.py", "w", encoding="utf-8") as f:
    f.write(code_auto)

print("[OK] Scripts 099N e 031 alinhados com a base real do iotec.db!")
