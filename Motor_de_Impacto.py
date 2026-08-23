import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def calculate_impact_score(
    pessoas_afetadas,
    prejuizo_estimado,
    criticidade
):

    score = 0

    score += pessoas_afetadas * 0.01

    score += prejuizo_estimado / 10000

    score += criticidade * 100

    return round(score, 2)




