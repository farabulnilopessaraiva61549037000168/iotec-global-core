import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def calculate_value(score):
    pass

    if score < 100:
        return 5000

    elif score < 500:
        return 25000

    elif score < 1500:
        return 100000

    elif score < 5000:
        return 500000

    return 1000000




