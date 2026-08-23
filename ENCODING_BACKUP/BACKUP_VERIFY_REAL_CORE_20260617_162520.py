import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
from collections import defaultdict

ROOT = input("Digite a pasta raiz do nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo:\n> ").strip()

IGNORE = {
    'node_modules',
    '.git',
    '__pycache__',
    'dist',
    'build',
    '.next',
    '.cache',
    'venv',
    '.venv'
}

# ======================================================
# ASSINATURAS
# ======================================================

SIGNATURES = {

    "IA_SYSTEM": [
        "openai",
        "langchain",
        "gpt",
        "agent",
        "embedding",
        "rag",
        "realtime"
    ],

    "CHAT_SYSTEM": [
        "chat",
        "conversation",
        "whatsapp",
        "telegram",
        "discord",
        "message"
    ],

    "PAYMENT_SYSTEM": [
        "stripe",
        "payment",
        "checkout",
        "paypal",
        "mercadopago"
    ],

    "CRM_SYSTEM": [
        "crm",
        "lead",
        "pipeline",
        "sales",
        "customer"
    ],

    "AUTH_SYSTEM": [
        "auth",
        "login",
        "jwt",
        "token",
        "session"
    ],

    "API_SYSTEM": [
        "api",
        "endpoint",
        "router",
        "fastapi",
        "flask",
        "express"
    ],

    "DASHBOARD_SYSTEM": [
        "dashboard",
        "panel",
        "admin",
        "analytics",
        "metrics"
    ],

    "AUTOMATION_SYSTEM": [
        "automation",
        "workflow",
        "trigger",
        "schedule",
        "cron"
    ],

    "ENGINE_SYSTEM": [
        "engine",
        "core",
        "processor",
        "runtime",
        "executor"
    ],

    "DATABASE_SYSTEM": [
        "mongodb",
        "postgres",
        "mysql",
        "sqlite",
        "redis",
        "database"
    ],

    "FRONTEND_SYSTEM": [
        "react",
        "next",
        "vue",
        "frontend",
        "component"
    ],

    "BACKEND_SYSTEM": [
        "backend",
        "server",
        "service",
        "controller"
    ]
}

# ======================================================
# RESULTADOS
# ======================================================

results = defaultdict(list)

file_count = 0

# ======================================================
# VARREDURA
# ======================================================

for root, dirs, files in os.walk(ROOT):
    pass

    dirs[:] = [d for d in dirs if d not in IGNORE]

    for file in files:
        pass

        file_count += 1

        path = os.path.join(root, file)

        lower = file.lower()

        for system_name, patterns in SIGNATURES.items():
            pass

            for pattern in patterns:
                pass

                if pattern in lower:
                    results[system_name].append(path)
                    break

# ======================================================
# RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO
# ======================================================

lines = []

lines.append("====================================")
lines.append("IOTEC VERIFIED CORE REPORT")
lines.append("====================================\n")

lines.append(f"Projeto: {ROOT}")
lines.append(f"Arquivos analisados: {file_count}\n")

for system_name, items in results.items():
    pass

    unique = list(set(items))

    lines.append("====================================")
    lines.append(system_name)
    lines.append("====================================")

    lines.append(f"OCORRÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â NCIAS: {len(unique)}\n")

    for item in unique[:20]:
        lines.append(item)

    lines.append("")

# ======================================================
# DIAGNÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œSTICO FINAL
# ======================================================

lines.append("====================================")
lines.append("DIAGNÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œSTICO FINAL")
lines.append("====================================\n")

for system_name, items in results.items():
    pass

    total = len(set(items))

    if total > 100:
        level = "MUITO FORTE"

    elif total > 40:
        level = "FORTE"

    elif total > 10:
        level = "MODERADO"

    elif total > 0:
        level = "EXISTE"

    else:
        level = "NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DETECTADO"

    lines.append(f"{system_name} -> {level} ({total})")

# ======================================================
# SALVAR
# ======================================================

output = "VERIFIED_CORE_REPORT.txt"

with open(output, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("\n====================================")
print("VERIFICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O CONCLUÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂDA")
print("====================================\n")

print(f"RelatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio salvo em: {output}")


