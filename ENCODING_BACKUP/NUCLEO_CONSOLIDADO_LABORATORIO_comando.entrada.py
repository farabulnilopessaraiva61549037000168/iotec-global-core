import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# modulo_ia.py
def processar_comando(entrada):
    entrada = entrada.lower()

    if 'abrir navegador' in entrada:
        return "Abrindo navegador..."
    elif 'executar diagnÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³stico' in entrada:
        return "Executando diagnÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³stico completo..."
    elif 'ligar modo stealth' in entrada:
        return "Modo furtivo ativado."
    elif 'desligar sistema' in entrada:
        return "Desligando sistema agora..."
    else:
        return f"Comando nÃƒÆ'Ã†â€™o reconhecido: {entrada}"


