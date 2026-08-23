import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
import socket
from datetime import datetime
from pathlib import Path
import requests

BASE = Path(r"C:\IOTEC")
PP = BASE / "PAYMENTS" / "PAYPAL"
SAN = PP / "SANEAMENTO"
CFG = PP / "CONFIG"
OUT = PP / "SAIDAS"

STATUS_JSON = SAN / "STATUS_SANEAMENTO_PAYPAL.json"
HIST_JSON = SAN / "HISTORICO_CORRECOES_PAYPAL.json"
AUD_JSON = SAN / "AUDITORIA_FLUXO_PAYPAL.json"
REL_TXT = OUT / "RELATORIO_DIAGNOSTICO_PAYPAL.txt"
CFG_JSON = CFG / "paypal_local_config.json"

def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def load_json(path, default):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default

def save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def add_history(hist, etapa, status, detalhe):
    hist.append({
        "timestamp": now(),
        "etapa": etapa,
        "status": status,
        "detalhe": detalhe
    })

def check_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.5)
    try:
        s.connect((host, port))
        return True
    except Exception:
        return False
    finally:
        try:
            s.close()
        except Exception:
            pass

def main():
    cfg = load_json(CFG_JSON, {})
    status = load_json(STATUS_JSON, {"paypal": {}})
    hist = load_json(HIST_JSON, [])
    auditoria = {"ultima_execucao": now(), "etapas": []}
    rel = []

    env = str(cfg.get("environment", "sandbox")).strip().lower()
    client_id = str(cfg.get("client_id", "")).strip()
    client_secret = str(cfg.get("client_secret", "")).strip()
    currency = str(cfg.get("currency_code", "BRL")).strip()
    amount = str(cfg.get("test_amount", "29.90")).strip()
    webhook_public_url = str(cfg.get("webhook_public_url", "")).strip()
    local_host = str(cfg.get("local_webhook_host", "127.0.0.1")).strip()
    local_port = int(cfg.get("local_webhook_port", 8787))

    api_base = "https://api-m.paypal.com" if env == "live" else "https://api-m.sandbox.paypal.com"

    rel.append("IOTEC PAYPAL - RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO DE DIAGNÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œSTICO")
    rel.append("=" * 70)
    rel.append(f"ExecuÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o: {now()}")
    rel.append(f"Base oficial: {BASE}")
    rel.append(f"Ambiente: {env}")
    rel.append("")

    if client_id and client_secret:
        status["paypal"]["credenciais"] = "ok"
        auditoria["etapas"].append({"etapa": "credenciais", "status": "ok"})
        add_history(hist, "credenciais", "ok", "Credenciais locais encontradas.")
        rel.append("[OK] Credenciais locais encontradas.")
    else:
        status["paypal"]["credenciais"] = "erro"
        auditoria["etapas"].append({"etapa": "credenciais", "status": "erro"})
        add_history(hist, "credenciais", "erro", "Credenciais ausentes.")
        rel.append("[ERRO] Credenciais ausentes em paypal_local_config.json.")

    rota_local_ok = check_port(local_host, local_port)
    if rota_local_ok:
        status["paypal"]["rota_local"] = "ok"
        auditoria["etapas"].append({"etapa": "rota_local", "status": "ok"})
        add_history(hist, "rota_local", "ok", f"Rota local aberta em {local_host}:{local_port}.")
        rel.append(f"[OK] Rota local aberta em {local_host}:{local_port}.")
    else:
        status["paypal"]["rota_local"] = "erro"
        auditoria["etapas"].append({"etapa": "rota_local", "status": "erro"})
        add_history(hist, "rota_local", "erro", f"Rota local fechada em {local_host}:{local_port}.")
        rel.append(f"[ERRO] Rota local fechada em {local_host}:{local_port}.")

    if webhook_public_url.startswith("https://"):
        status["paypal"]["webhook_url_publica"] = "ok"
        rel.append(f"[OK] Webhook pÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºblica configurada: {webhook_public_url}")
    else:
        status["paypal"]["webhook_url_publica"] = "erro"
        rel.append("[ERRO] Webhook pÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºblica ausente ou sem HTTPS.")

    access_token = None
    if status["paypal"]["credenciais"] == "ok":
        try:
            r = requests.post(
                f"{api_base}/v1/oauth2/token",
                headers={"Accept": "application/json", "Accept-Language": "en_US"},
                data={"grant_type": "client_credentials"},
                auth=(client_id, client_secret),
                timeout=25
            )
            oauth_body = r.json() if r.text else {}
            auditoria["etapas"].append({"etapa": "oauth", "http_status": r.status_code, "body": oauth_body})
            if r.ok and "access_token" in oauth_body:
                access_token = oauth_body["access_token"]
                status["paypal"]["oauth"] = "ok"
                add_history(hist, "oauth", "ok", f"OAuth OK. HTTP {r.status_code}.")
                rel.append(f"[OK] OAuth validado. HTTP {r.status_code}.")
            else:
                status["paypal"]["oauth"] = "erro"
                add_history(hist, "oauth", "erro", f"Falha OAuth. HTTP {r.status_code}.")
                rel.append(f"[ERRO] OAuth falhou. HTTP {r.status_code}.")
        except Exception as e:
            status["paypal"]["oauth"] = "erro"
            rel.append(f"[ERRO] ExceÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o no OAuth: {e}")
    else:
        status["paypal"]["oauth"] = "erro"
        rel.append("[ERRO] OAuth nÃƒÆ'Ã†â€™o testado porque credenciais falharam.")

    if access_token:
        payload = {
            "intent": "CAPTURE",
            "purchase_units": [
                {
                    "amount": {
                        "currency_code": currency,
                        "value": amount
                    },
                    "description": "IOTEC TESTE DE FLUXO PAYPAL"
                }
            ]
        }
        try:
            r = requests.post(
                f"{api_base}/v2/checkout/orders",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {access_token}"
                },
                json=payload,
                timeout=25
            )
            body = r.json() if r.text else {}
            auditoria["etapas"].append({"etapa": "orders_create", "http_status": r.status_code, "body": body})
            if r.ok and body.get("id"):
                status["paypal"]["orders"] = "ok"
                add_history(hist, "orders_create", "ok", f"Order criada. HTTP {r.status_code}.")
                rel.append(f"[OK] Order criada. ID: {body.get('id')} | HTTP {r.status_code}")
            else:
                status["paypal"]["orders"] = "erro"
                add_history(hist, "orders_create", "erro", f"Order falhou. HTTP {r.status_code}.")
                rel.append(f"[ERRO] Falha ao criar order. HTTP {r.status_code}")
        except Exception as e:
            status["paypal"]["orders"] = "erro"
            rel.append(f"[ERRO] ExceÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o ao criar order: {e}")
    else:
        status["paypal"]["orders"] = "erro"
        rel.append("[ERRO] Orders nÃƒÆ'Ã†â€™o testado porque OAuth falhou.")

    todos_ok = all([
        status["paypal"].get("credenciais") == "ok",
        status["paypal"].get("oauth") == "ok",
        status["paypal"].get("orders") == "ok"
    ])

    status["paypal"]["ambiente"] = env
    status["paypal"]["fluxo"] = "aberto_parcial" if todos_ok else "fechado"

    if todos_ok:
        rel.append("")
        rel.append("[OK] NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo conseguiu autenticar e criar pedido.")
        rel.append("Fluxo parcial aberto. Falta webhook pÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºblica HTTPS para o ciclo completo.")
    else:
        rel.append("")
        rel.append("[ERRO] Fluxo ainda fechado. Verificar etapas com falha.")

    save_json(STATUS_JSON, status)
    save_json(HIST_JSON, hist)
    save_json(AUD_JSON, auditoria)
    REL_TXT.write_text("\\n".join(rel), encoding="utf-8")
    print("\\n".join(rel))

if __name__ == "__main__":
    main()


