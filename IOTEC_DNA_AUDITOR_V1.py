# ==============================================================================
# IOTEC DNA AUDITOR V1
# Faz perguntas para a arquitetura da IOTEC
# ==============================================================================

from pathlib import Path
import os
import re
from collections import defaultdict

ROOT = Path.home() / "Documents" / "OMEGA_BASE"

EXT = {
    ".py",".md",".txt",".json",".yaml",".yml",
    ".ini",".cfg",".toml"
}

PERGUNTAS = {

    "IA":[
        "openai","llm","gpt","embedding",
        "ai","ia","machine learning","rag"
    ],

    "COMERCIAL":[
        "lead","crm","cliente","empresa",
        "negoci","proposal","proposta","venda"
    ],

    "DOCUMENTOS":[
        "pdf","docx","ocr","report",
        "relatorio","contrato"
    ],

    "EVENTOS":[
        "eventbus","queue","publish",
        "subscribe","event"
    ],

    "BANCO":[
        "sqlite","postgres","mysql",
        "database","db","sqlalchemy"
    ],

    "API":[
        "fastapi","flask","api",
        "@app.route","router"
    ],

    "DASHBOARD":[
        "dash","streamlit","gradio",
        "panel","dashboard"
    ],

    "AUTOMACAO":[
        "scheduler","cron",
        "thread","async","loop"
    ],

    "INSTINTOS":[
        "swarm","bee","crow","eagle",
        "falcon","heron","platypus",
        "instinct","behavior"
    ],

    "ANALISE":[
        "analytics","analysis",
        "estatistica","predict",
        "forecast"
    ]
}

resultado = defaultdict(list)

total = 0

for raiz,_,arquivos in os.walk(ROOT):

    for arquivo in arquivos:

        if Path(arquivo).suffix.lower() not in EXT:
            continue

        caminho = Path(raiz)/arquivo
        total += 1

        try:
            texto = caminho.read_text(
                encoding="utf8",
                errors="ignore"
            ).lower()
        except:
            continue

        for categoria,palavras in PERGUNTAS.items():

            score = 0

            for palavra in palavras:

                ocorrencias = len(
                    re.findall(
                        re.escape(palavra.lower()),
                        texto
                    )
                )

                score += ocorrencias

            if score:

                resultado[categoria].append({
                    "arquivo":str(caminho),
                    "score":score
                })

print("="*80)
print("IOTEC DNA AUDITOR")
print("="*80)

print()

print("Arquivos analisados:",total)

print()

for categoria in sorted(resultado):

    lista = sorted(
        resultado[categoria],
        key=lambda x:x["score"],
        reverse=True
    )

    print("-"*60)
    print(categoria)
    print("-"*60)

    print("Arquivos encontrados:",len(lista))

    print()

    for item in lista[:15]:

        print(
            f'{item["score"]:4d}  {item["arquivo"]}'
        )

    print()

print("="*80)

print("""
PERGUNTAS RESPONDIDAS

âœ" Existe IA?
âœ" Existe CRM?
âœ" Existe EventBus?
âœ" Existe Banco de Dados?
âœ" Existe Dashboard?
âœ" Existe API?
âœ" Existe AutomaÃ§Ã£o?
âœ" Existem Instintos?
âœ" Existe Motor AnalÃ­tico?
""")

