import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def should_invest(cost, expected_return):

    roi = ((expected_return - cost) / cost) * 100

    if roi >= 300:
        return "INVESTIMENTO MUITO RECOMENDADO"

    if roi >= 150:
        return "RECOMENDADO"

    if roi >= 50:
        return "ANALISAR"

    return "NÃƒÆ'O INVESTIR"



