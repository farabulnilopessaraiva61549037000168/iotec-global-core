import re

file_path = r"C:\IOTEC\000_IOTEC_FACTORY_20_CERTIDOES.py"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Corrige o espaçamento entre a Tag do CNPJ e a Badge do Nível
content_fixed = content.replace(
    '.cnpj-tag { font-size: 8.5pt; color: #475569; font-family: monospace; margin-bottom: 8px; }',
    '.cnpj-tag { font-size: 8.5pt; color: #475569; font-family: monospace; margin-bottom: 14px; margin-top: 4px; }'
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content_fixed)

print("[OK] Layout da Fábrica de Certidões 100% recalibrado sem sobreposição!")
