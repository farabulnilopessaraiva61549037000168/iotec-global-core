import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =========================================================
# IOTEC CORE INVESTIGATOR + TECHNICAL TUTOR
# =========================================================
#
# O QUE ESSE SISTEMA FAZ:
#
# 1. INVESTIGA O NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO
#    - percorre pastas
#    - detecta arquivos
#    - detecta linguagens
#    - detecta mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulos
#    - detecta APIs
#
# 2. GERA RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIOS
#    - estrutura do projeto
#    - tecnologias encontradas
#    - arquivos crÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­ticos
#    - potencial comercial
#
# 3. TUTOR TÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°CNICO
#    - explica em portuguÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªs humano
#    - traduz termos tÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©cnicos
#    - ajuda vocÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª a entender o ecossistema
#
# =========================================================
# COMO SALVAR
# =========================================================
#
# Salve como:
#
# core_investigator.py
#
# =========================================================
# COMO RODAR
# =========================================================
#
# 1. instalar:
#
# pip install python-dotenv
#
# 2. rodar:
#
# python core_investigator.py
#
# =========================================================

import os
import json
from pathlib import Path
from collections import defaultdict

# =========================================================
# CONFIGURAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# =========================================================

# PASTA QUE SERÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â ANALISADA
ROOT_DIR = input(
    "\nDigite o caminho da pasta do nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo que deseja investigar:\n> "
).strip()

# =========================================================
# MAPAS DE DETECÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# =========================================================

LANGUAGE_MAP = {
    ".py": "Python",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".jsx": "React JSX",
    ".tsx": "React TSX",
    ".html": "HTML",
    ".css": "CSS",
    ".json": "JSON",
    ".env": "Environment Config",
    ".sql": "SQL",
    ".md": "Markdown",
    ".yml": "YAML",
    ".yaml": "YAML",
}

CATEGORY_MAP = {
    "api": "API / IntegraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o",
    "auth": "AutenticaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o",
    "payment": "Pagamento",
    "chat": "Chat / ConversaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o",
    "ai": "InteligÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia Artificial",
    "agent": "Agente IA",
    "dashboard": "Painel",
    "admin": "AdministraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o",
    "database": "Banco de Dados",
    "memory": "MemÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³ria",
    "core": "NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo Central",
    "frontend": "Frontend",
    "backend": "Backend",
    "voice": "ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âudio / Voz",
    "stripe": "Pagamento Stripe",
    "whatsapp": "WhatsApp",
    "openai": "OpenAI",
}

# =========================================================
# ESTRUTURAS
# =========================================================

report = {
    "project_name": "",
    "directories": [],
    "files": [],
    "languages": defaultdict(int),
    "categories": defaultdict(list),
    "critical_modules": [],
    "possible_products": [],
}

# =========================================================
# DETECÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DE CATEGORIA
# =========================================================

def detect_category(name):
    name = name.lower()

    found = []

    for keyword, category in CATEGORY_MAP.items():
        if keyword in name:
            found.append(category)

    return found

# =========================================================
# TUTOR TÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°CNICO
# =========================================================

def explain_category(category):
    pass

    explanations = {

        "API / IntegraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o":
            "Esse mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulo parece servir para conectar sistemas diferentes.",

        "AutenticaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o":
            "Essa parte controla login, seguranÃƒÆ'Ã†â€™a e acesso.",

        "Pagamento":
            "Esse mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulo provavelmente gerencia cobranÃƒÆ'Ã†â€™as, pagamentos ou assinaturas.",

        "Chat / ConversaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o":
            "Essa estrutura parece responsÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡vel pela comunicaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o com usuÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rios.",

        "InteligÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia Artificial":
            "Esse mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulo parece ligado ÃƒÆ'Ã†â€™  IA do sistema.",

        "Agente IA":
            "Esse componente parece funcionar como um agente automatizado.",

        "Painel":
            "Essa parte provavelmente exibe dashboards e controle visual.",

        "AdministraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o":
            "Esse mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulo parece ser usado para controle interno do sistema.",

        "Banco de Dados":
            "Essa estrutura provavelmente armazena informaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes do sistema.",

        "MemÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³ria":
            "Esse mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulo parece armazenar contexto e histÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rico.",

        "NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo Central":
            "Esse parece ser um componente central do ecossistema.",

        "Frontend":
            "Frontend ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© a parte visual que o usuÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio enxerga.",

        "Backend":
            "Backend ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© a parte invisÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vel do sistema onde ficam regras e processamento.",

        "ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âudio / Voz":
            "Esse mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulo parece ligado a voz, ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡udio ou chamadas.",

        "Pagamento Stripe":
            "IntegraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o provÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡vel com pagamentos Stripe.",

        "WhatsApp":
            "IntegraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o provÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡vel com WhatsApp.",

        "OpenAI":
            "IntegraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o provÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡vel com inteligÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia artificial da OpenAI.",
    }

    return explanations.get(
        category,
        "Categoria tÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©cnica detectada."
    )

# =========================================================
# INVESTIGAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# =========================================================

print("\n=================================================")
print("INICIANDO INVESTIGAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DO NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO...")
print("=================================================\n")

root_path = Path(ROOT_DIR)

report["project_name"] = root_path.name

for path in root_path.rglob("*"):
    pass

    if path.is_dir():
        pass

        report["directories"].append(str(path))

    elif path.is_file():
        pass

        file_info = {
            "name": path.name,
            "path": str(path),
            "size_kb": round(path.stat().st_size / 1024, 2),
        }

        ext = path.suffix.lower()

        # Linguagem
        language = LANGUAGE_MAP.get(ext, "Desconhecida")
        file_info["language"] = language

        report["languages"][language] += 1

        # Categorias
        categories = detect_category(path.name)

        file_info["categories"] = categories

        for c in categories:
            report["categories"][c].append(path.name)

        # MÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulos crÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­ticos
        if any(k in path.name.lower() for k in [
            "core",
            "main",
            "server",
            "app",
            "engine",
            "payment",
            "auth"
        ]):
            report["critical_modules"].append(path.name)

        # PossÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vel produto
        if any(k in path.name.lower() for k in [
            "dashboard",
            "chat",
            "ai",
            "crm",
            "automation"
        ]):
            report["possible_products"].append(path.name)

        report["files"].append(file_info)

# =========================================================
# RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO
# =========================================================

print("\n=================================================")
print("RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO DO NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO")
print("=================================================\n")

print(f"Projeto detectado: {report['project_name']}\n")

print("-------------------------------------------------")
print("LINGUAGENS DETECTADAS")
print("-------------------------------------------------\n")

for lang, count in report["languages"].items():
    print(f"{lang}: {count} arquivos")

print("\n-------------------------------------------------")
print("CATEGORIAS DETECTADAS")
print("-------------------------------------------------\n")

for category, files in report["categories"].items():
    pass

    print(f"\n[{category}]")
    print(explain_category(category))

    for f in files[:10]:
        print(f" - {f}")

print("\n-------------------------------------------------")
print("MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œDULOS CRÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂTICOS")
print("-------------------------------------------------\n")

for module in report["critical_modules"]:
    print(f" - {module}")

print("\n-------------------------------------------------")
print("POSSÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂVEIS PRODUTOS / SERVIÃƒÆ'Ã†â€™OS")
print("-------------------------------------------------\n")

for p in report["possible_products"]:
    print(f" - {p}")

# =========================================================
# EXPORTAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# =========================================================

output = {
    "project_name": report["project_name"],
    "languages": dict(report["languages"]),
    "categories": dict(report["categories"]),
    "critical_modules": report["critical_modules"],
    "possible_products": report["possible_products"],
}

with open("iotec_core_report.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=4, ensure_ascii=False)

print("\n=================================================")
print("INVESTIGAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O FINALIZADA")
print("=================================================\n")

print("RelatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio salvo em:")
print("iotec_core_report.json\n")

print("Agora vocÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª pode comeÃƒÆ'Ã†â€™ar a entender:")
print(" - o que existe no nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo")
print(" - o que ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© importante")
print(" - o que pode virar produto")
print(" - o que ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© infraestrutura")
print(" - o que precisa reorganizar")
print()


