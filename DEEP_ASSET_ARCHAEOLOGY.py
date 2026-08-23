import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# DEEP_ASSET_ARCHAEOLOGY.py
# Auditoria Profunda de Ativos TecnolÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³gicos IOTEC

import os
from pathlib import Path
from collections import defaultdict
from datetime import datetime

ROOT = r"C:\IOTEC_OMEGA_X"

OUT = os.path.join(
    ROOT,
    "REPORTS",
    "ARQUEOLOGIA_ATIVOS_IOTEC.txt"
)

CATEGORIAS = {

    "CRM":[
        "crm",
        "lead",
        "opportunity",
        "pipeline",
        "client",
        "proposal"
    ],

    "MONETIZACAO":[
        "payment",
        "invoice",
        "billing",
        "monetization",
        "pricing",
        "price"
    ],

    "AUTOMACAO":[
        "automation",
        "engine",
        "agent",
        "robot",
        "workflow"
    ],

    "INTELIGENCIA":[
        "ai",
        "analytics",
        "data",
        "score",
        "predict",
        "forecast"
    ],

    "TORRE_COMANDO":[
        "tower",
        "dashboard",
        "command",
        "operations",
        "executive"
    ],

    "OBSERVABILIDADE":[
        "monitor",
        "observability",
        "audit",
        "watchdog",
        "telemetry"
    ],

    "STREAMING":[
        "stream",
        "video",
        "broadcast",
        "media"
    ],

    "INFRAESTRUTURA":[
        "server",
        "api",
        "backend",
        "frontend",
        "core"
    ]
}

ativos = defaultdict(list)

arquivos_total = 0
linhas_total = 0

for raiz, dirs, files in os.walk(ROOT):
    pass

    for nome in files:
        pass

        arquivos_total += 1

        caminho = os.path.join(raiz, nome)

        try:
            pass

            ext = Path(nome).suffix.lower()

            if ext not in [
                ".py",
                ".js",
                ".html",
                ".css",
                ".json"
            ]:
                continue

            try:
                pass

                with open(
                    caminho,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as f:

                    conteudo = f.read()

                    linhas = len(
                        conteudo.splitlines()
                    )

                    linhas_total += linhas

            except:
                conteudo = ""
                linhas = 0

            nome_lower = nome.lower()

            for categoria, palavras in CATEGORIAS.items():
                pass

                score = 0

                for p in palavras:
                    pass

                    if p in nome_lower:
                        score += 5

                    if p in conteudo.lower():
                        score += 1

                if score > 0:
                    pass

                    ativos[categoria].append({

                        "arquivo": caminho,
                        "linhas": linhas,
                        "score": score

                    })

        except:
            pass

# ====================================================
# VALOR ESTIMADO
# ====================================================

valor_total = 0

for categoria in ativos:
    pass

    for item in ativos[categoria]:
        pass

        valor_total += (
            item["linhas"] * 0.8
            +
            item["score"] * 120
        )

valor_usd = round(valor_total,2)
valor_brl = round(valor_usd * 5.5,2)

# ====================================================
# RELATORIO
# ====================================================

os.makedirs(
    os.path.dirname(OUT),
    exist_ok=True
)

with open(
    OUT,
    "w",
    encoding="utf-8"
) as r:

    r.write("\n")
    r.write("="*70 + "\n")
    r.write("ARQUEOLOGIA DE ATIVOS IOTEC\n")
    r.write("="*70 + "\n\n")

    r.write(
        f"DATA: {datetime.now()}\n\n"
    )

    r.write(
        f"ARQUIVOS ANALISADOS: {arquivos_total}\n"
    )

    r.write(
        f"LINHAS ANALISADAS: {linhas_total}\n\n"
    )

    for categoria in sorted(ativos.keys()):
        pass

        r.write(
            "\n" + "="*50 + "\n"
        )

        r.write(
            categoria + "\n"
        )

        r.write(
            "="*50 + "\n"
        )

        total_cat = 0

        ativos[categoria].sort(
            key=lambda x: x["score"],
            reverse=True
        )

        for item in ativos[categoria][:50]:
            pass

            total_cat += item["score"]

            r.write(
                f"[{item['score']:03}] "
                f"{item['linhas']:06} linhas | "
                f"{item['arquivo']}\n"
            )

        r.write(
            f"\nSCORE DA CATEGORIA: {total_cat}\n"
        )

    r.write("\n")
    r.write("="*70 + "\n")
    r.write("ESTIMATIVA TECNOLOGICA\n")
    r.write("="*70 + "\n\n")

    r.write(
        f"VALOR TECNICO USD: ${valor_usd:,.2f}\n"
    )

    r.write(
        f"VALOR TECNICO BRL: R$ {valor_brl:,.2f}\n"
    )

    r.write("\n")
    r.write("="*70 + "\n")
    r.write("FIM DA ARQUEOLOGIA\n")
    r.write("="*70 + "\n")

print("")
print("="*60)
print("ARQUEOLOGIA DE ATIVOS CONCLUIDA")
print("="*60)
print(OUT)
print("")




