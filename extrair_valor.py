import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def extrair_valor(corpo):
    pass



    import re



    match = re.search(r'\$ ?([\d,\.]+)', corpo)



    if match:
        pass

        return match.group(1)



    return None






