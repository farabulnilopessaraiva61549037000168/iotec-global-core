import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
print(json.dumps(sistema.gerar_manifesto_operacional(), indent=2, ensure_ascii=False))



