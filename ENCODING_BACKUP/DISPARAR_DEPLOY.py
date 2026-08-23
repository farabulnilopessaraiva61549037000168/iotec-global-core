import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC - DEPLOY READINESS SYSTEM
# ============================================================

import os, subprocess, sys
from datetime import datetime

REQUIRED_ENV = [
    "NETLIFY_AUTH_TOKEN",
    "NETLIFY_SITE_ID",
    "BACKEND_URL"
]

def log(msg):
    print(f"[{datetime.now()}] {msg}")

def check_env():
    missing = [k for k in REQUIRED_ENV if not os.getenv(k)]
    if missing:
        log(f"Credenciais faltando: {missing}")
        return False
    log("Credenciais OK")
    return True

def build_frontend():
    log("Build do frontend...")
    # ajuste para seu projeto (ex: npm)
    subprocess.run(["cmd", "/c", "npm run build"], check=False)

def test_backend():
    log("Testando backend (ping simples)...")
    # substitua por teste real
    return True

def qa_checks():
    log("Executando QA bÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡sico...")
    # plugue aqui seus checks (UI/API)
    return True

def ready():
    return check_env() and test_backend() and qa_checks()

def deploy_netlify():
    log("Deploy no Netlify...")
    # requer CLI do Netlify instalada
    subprocess.run([
        "cmd","/c",
        "npx netlify deploy --prod --dir=dist "
        f"--auth={os.getenv('NETLIFY_AUTH_TOKEN')} "
        f"--site={os.getenv('NETLIFY_SITE_ID')}"
    ], check=False)

def deploy_backend():
    log("Backend jÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ deve estar publicado (Render/Railway).")
    # vocÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª pode integrar CLI/API da sua plataforma aqui

def main():
    build_frontend()

    if not ready():
        log("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ Locomotiva pronta, aguardando credenciais/liberaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o.")
        input("Quando estiver tudo liberado, pressione ENTER para deploy...")

    if ready():
        deploy_netlify()
        deploy_backend()
        log("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Deploy concluÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­do.")
    else:
        log("ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Ainda faltam requisitos.")

if __name__ == "__main__":
    main()


