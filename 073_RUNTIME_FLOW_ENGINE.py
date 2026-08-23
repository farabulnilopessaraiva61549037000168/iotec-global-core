# ==========================================================
# 073_RUNTIME_FLOW_ENGINE.py
# IOTEC RUNTIME FLOW ENGINE
# ==========================================================

import os
from collections import defaultdict

ROOT = r"C:\IOTEC"

IGNORE = {
    "venv",
    "__pycache__",
    "BACKUP",
    "ENCODING_BACKUP",
    "LABORATORIO",
    "DUPLICADOS",
    "FROZEN"
}

PADROES = {

    "SQLITE_WRITE":[
        "cursor.execute(",
        "insert into",
        "update ",
        "delete from",
        "create table"
    ],

    "SQLITE_READ":[
        "select ",
        "fetchone",
        "fetchall"
    ],

    "SUBPROCESS":[
        "subprocess.run",
        "subprocess.call",
        "subprocess.Popen",
        "os.system("
    ],

    "FLASK_ROUTE":[
        "@app.route",
        "Flask(",
        "Blueprint("
    ],

    "HTTP_REQUEST":[
        "requests.get",
        "requests.post",
        "requests.put",
        "requests.delete"
    ],

    "JSON":[
        "json.load",
        "json.dump",
        "json.loads",
        "json.dumps"
    ],

    "EMAIL":[
        "smtplib",
        "imaplib",
        "email.message",
        "SMTP("
    ],

    "PAYPAL":[
        "paypal",
        "checkout",
        "capture",
        "webhook"
    ],

    "WHATSAPP":[
        "whatsapp",
        "wa.me",
        "graph.facebook"
    ],

    "GOOGLE_MAPS":[
        "googlemaps",
        "maps.googleapis",
        "places",
        "geocode"
    ]
}

resultado = defaultdict(list)

print("="*70)
print("IOTEC RUNTIME FLOW ENGINE")
print("="*70)
print()

arquivos = 0

for raiz, pastas, files in os.walk(ROOT):

    pastas[:] = [p for p in pastas if p not in IGNORE]

    for arq in files:

        if not arq.endswith(".py"):
            continue

        arquivos += 1

        caminho = os.path.join(raiz, arq)

        try:

            texto = open(
                caminho,
                encoding="utf-8",
                errors="ignore"
            ).read().lower()

        except:

            continue

        for grupo, palavras in PADROES.items():

            total = 0

            for p in palavras:

                total += texto.count(p.lower())

            if total:

                resultado[grupo].append((total, arq, caminho))

print("Arquivos analisados :", arquivos)
print()

for grupo in PADROES:

    print("="*70)
    print(grupo)
    print("="*70)

    ranking = sorted(
        resultado[grupo],
        reverse=True
    )

    if not ranking:

        print("Nenhuma ocorrÃƒÂªncia.")
        print()
        continue

    total = sum(x[0] for x in ranking)

    print("OcorrÃƒÂªncias :", total)
    print()

    print("TOP 15")

    print()

    for score, arq, caminho in ranking[:15]:

        print(f"{score:4}  {arq}")

    print()

print("="*70)
print("MATRIZ OPERACIONAL")
print("="*70)
print()

for grupo in PADROES:

    print(f"{grupo:<20} {len(resultado[grupo]):>5} mÃƒÂ³dulos")

print()

print("="*70)
print("MISSÃƒÆ'O")
print("="*70)
print()

print("O Kernel identificou")
print("os mecanismos")
print("reais de execuÃƒÂ§ÃƒÂ£o")
print("da plataforma.")

print()

print("A PresidÃƒÂªncia agora")
print("conhece quem")
print("grava banco,")
print("abre rotas,")
print("executa processos")
print("e conversa")
print("com sistemas externos.")


