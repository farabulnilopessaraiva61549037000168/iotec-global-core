import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def trigger_blackout():
    print("[Blackout Shell] Dissolvendo superfÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­cie do sistema...")
    # Remove todas as rotas externas temporariamente
    disable_surface_interfaces()

def disable_surface_interfaces():
    print("[Blackout Shell] Interfaces externas desativadas.")



