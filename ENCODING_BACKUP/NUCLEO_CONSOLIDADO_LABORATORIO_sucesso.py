import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
if resultado["sucesso"]:
    abrir_portal_envio(resultado["dados"])



