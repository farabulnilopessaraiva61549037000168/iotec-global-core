with open("IOTEC_AUTOMATIC_PROSPECTION_ENGINE.py", "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Substitui qualquer contagem de placeholders incorreta por 5 valores
import re
content = re.sub(r'VALUES\s*\([^\)]+\)', 'VALUES (?, ?, ?, ?, ?)', content, flags=re.IGNORECASE)

with open("IOTEC_AUTOMATIC_PROSPECTION_ENGINE.py", "w", encoding="utf-8") as f:
    f.write(content)

print("[OK] Query SQL alinhada com sucesso!")
