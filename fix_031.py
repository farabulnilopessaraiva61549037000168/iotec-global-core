with open('031_COMMERCIAL_AUTOPILOT.py', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Substitui o bloco de variáveis soltas por valores padrão de execução autônoma
content = content.replace('prioridade,', 'prioridade = "ALTA"')

with open('031_COMMERCIAL_AUTOPILOT.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch de prioridade aplicado com sucesso!")
