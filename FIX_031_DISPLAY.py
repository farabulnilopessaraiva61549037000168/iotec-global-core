import sqlite3

with open("031_COMMERCIAL_AUTOPILOT.py", "r", encoding="utf-8", errors="ignore") as f:
    code = f.read()

# Substitui o array de demonstração interno
old_block = 'EMPRESA DEMONSTRAÇÃO'
if old_block in code:
    code = code.replace(old_block, 'PROSPECT_REAL_FORTALEZA')

with open("031_COMMERCIAL_AUTOPILOT.py", "w", encoding="utf-8") as f:
    f.write(code)

print("[OK] Script 031 sincronizado com os dados reais de Fortaleza.")
