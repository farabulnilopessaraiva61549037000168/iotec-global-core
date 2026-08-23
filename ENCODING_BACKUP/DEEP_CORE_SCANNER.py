import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC - DEEP CORE SCANNER
# NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO DE ESCAVAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O E REVELAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O ESTRUTURAL
# EMPRESA: IOTEC
# MODO: ARQUEOLOGIA_TECNICA
# STATUS: ESCAVANDO
# ============================================================

import os
import json
from datetime import datetime
from collections import defaultdict

# ============================================================
# CONFIGURAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ============================================================

EMPRESA = "IOTEC"

PASTAS_ANALISE = [
    r"C:\IOTEC",
    r"C:\Users",
    r"D:\"
]

EXTENSOES_INTERESSE = [
    ".py",
    ".js",
    ".html",
    ".css",
    ".json",
    ".sql",
    ".txt",
    ".md",
    ".yml",
    ".yaml",
    ".tsx",
    ".jsx"
]

PALAVRAS_CHAVE = [
    "dashboard",
    "analytics",
    "juridico",
    "govtech",
    "financeiro",
    "api",
    "paypal",
    "stripe",
    "streamlit",
    "react",
    "intelligence",
    "automation",
    "pipeline",
    "lead",
    "enterprise",
    "monitor",
    "core",
    "engine",
    "render",
    "netlify",
    "database",
    "postgres",
    "mysql",
    "login",
    "auth",
    "admin"
]

# ============================================================
# ESTRUTURA CENTRAL
# ============================================================

NUCLEO = {
    "empresa": EMPRESA,
    "modo": "arqueologia_tecnica",
    "status": "escavando",
    "timestamp": str(datetime.now())
}

# ============================================================
# CONTADORES
# ============================================================

ativos = []
estatisticas = defaultdict(int)
setores_detectados = defaultdict(int)
tecnologias_detectadas = defaultdict(int)

# ============================================================
# DETECÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DE SETORES
# ============================================================

def detectar_setor(nome):
    pass

    nome = nome.lower()

    if "jurid" in nome:
        return "juridico"

    elif "gov" in nome:
        return "govtech"

    elif "finance" in nome:
        return "financeiro"

    elif "analytic" in nome:
        return "analytics"

    elif "import" in nome:
        return "importacao"

    elif "dashboard" in nome:
        return "dashboards"

    elif "admin" in nome:
        return "administracao"

    return "diversos"

# ============================================================
# DETECÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DE TECNOLOGIAS
# ============================================================

def detectar_tecnologias(conteudo):
    pass

    tecnologias = []

    conteudo = conteudo.lower()

    techs = {
        "streamlit": "streamlit",
        "react": "react",
        "flask": "flask",
        "fastapi": "fastapi",
        "paypal": "paypal",
        "stripe": "stripe",
        "postgres": "postgresql",
        "mysql": "mysql",
        "sqlite": "sqlite",
        "render": "render",
        "netlify": "netlify"
    }

    for chave, nome in techs.items():
        pass

        if chave in conteudo:
            tecnologias.append(nome)
            tecnologias_detectadas[nome] += 1

    return tecnologias

# ============================================================
# ESCAVAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O PROFUNDA
# ============================================================

print("\n======================================================")
print(" IOTEC - DEEP CORE SCANNER")
print("======================================================\n")

for raiz in PASTAS_ANALISE:
    pass

    print(f"[+] ESCAVANDO -> {raiz}")

    for pasta, subpastas, arquivos in os.walk(raiz):
        pass

        for arquivo in arquivos:
            pass

            try:
                pass

                caminho = os.path.join(pasta, arquivo)

                extensao = os.path.splitext(arquivo)[1].lower()

                if extensao not in EXTENSOES_INTERESSE:
                    continue

                tamanho = os.path.getsize(caminho)

                setor = detectar_setor(arquivo)

                estatisticas[extensao] += 1
                setores_detectados[setor] += 1

                palavras_detectadas = []

                tecnologias = []

                try:
                    pass

                    with open(caminho, "r", encoding="utf-8", errors="ignore") as f:
                        pass

                        conteudo = f.read(50000).lower()

                        tecnologias = detectar_tecnologias(conteudo)

                        for palavra in PALAVRAS_CHAVE:
                            pass

                            if palavra in conteudo:
                                palavras_detectadas.append(palavra)

                except:
                    pass

                ativos.append({
                    "arquivo": arquivo,
                    "caminho": caminho,
                    "extensao": extensao,
                    "tamanho_kb": round(tamanho / 1024, 2),
                    "setor_detectado": setor,
                    "palavras_detectadas": palavras_detectadas,
                    "tecnologias": tecnologias
                })

            except:
                pass

# ============================================================
# CONSOLIDAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ============================================================

relatorio = {
    "nucleo": NUCLEO,
    "ativos_detectados": len(ativos),
    "estatisticas_extensoes": dict(estatisticas),
    "setores_detectados": dict(setores_detectados),
    "tecnologias_detectadas": dict(tecnologias_detectadas),
    "ativos": ativos
}

# ============================================================
# EXPORTAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ============================================================

PASTA_EXPORT = r"C:\IOTEC_DEEP_CORE"

os.makedirs(PASTA_EXPORT, exist_ok=True)

JSON_PATH = os.path.join(PASTA_EXPORT, "deep_core_scan.json")
TXT_PATH = os.path.join(PASTA_EXPORT, "deep_core_relatorio.txt")

with open(JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(relatorio, f, indent=4, ensure_ascii=False)

# ============================================================
# RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO TXT
# ============================================================

with open(TXT_PATH, "w", encoding="utf-8") as f:
    pass

    f.write("=====================================================\n")
    f.write(" IOTEC - RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO DE ESCAVAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O PROFUNDA\n")
    f.write("=====================================================\n\n")

    f.write(f"ATIVOS DETECTADOS: {len(ativos)}\n\n")

    f.write("SETORIZAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O:\n")

    for setor, total in setores_detectados.items():
        f.write(f"- {setor}: {total}\n")

    f.write("\nTECNOLOGIAS:\n")

    for tech, total in tecnologias_detectadas.items():
        f.write(f"- {tech}: {total}\n")

    f.write("\nEXTENSÃƒÆ'Ã†â€™ES:\n")

    for ext, total in estatisticas.items():
        f.write(f"- {ext}: {total}\n")

# ============================================================
# RESULTADO FINAL
# ============================================================

print("\n======================================================")
print(" ESCAVAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O FINALIZADA")
print("======================================================\n")

print(f"ATIVOS DETECTADOS: {len(ativos)}\n")

print("SETORIZAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O:\n")

for setor, total in setores_detectados.items():
    print(f"{setor.upper()} -> {total}")

print("\nTECNOLOGIAS DETECTADAS:\n")

for tech, total in tecnologias_detectadas.items():
    print(f"{tech.upper()} -> {total}")

print(f"\nJSON -> {JSON_PATH}")
print(f"TXT  -> {TXT_PATH}")

print("\n======================================================")
print(" O NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO REVELOU AS CAMADAS ENCONTRADAS")
print("======================================================\n")


