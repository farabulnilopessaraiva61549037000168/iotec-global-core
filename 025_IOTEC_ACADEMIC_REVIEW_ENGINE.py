import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from pathlib import Path
import hashlib
import json
from datetime import datetime

ROOT = Path(r"C:\IOTEC")

IGNORAR = [
    "BACKUP",
    "LABORATORIO",
    "DUPLICADOS",
    "ENCODING_BACKUP",
    "__pycache__",
    "node_modules",
    "venv",
    ".git",
    "MINERADORA_BRUTA",
    "_SANITIZADA",
    "site-packages"
]

print("="*70)
print("IOTEC ACADEMIC REVIEW ENGINE")
print("="*70)
print()

algoritmos=[]

for arquivo in ROOT.rglob("*.py"):

    caminho=str(arquivo)

    if any(x.lower() in caminho.lower() for x in IGNORAR):
        continue

    try:
        texto=arquivo.read_text(
            encoding="utf-8",
            errors="ignore"
        )
    except:
        continue

    linhas=len(texto.splitlines())

    texto_lower=texto.lower()

    # -----------------------------
    # BANCA MATEMÃƒÂTICA
    # -----------------------------

    nota_matematica=100

    if "eval(" in texto_lower:
        nota_matematica-=20

    if "except:" in texto_lower:
        nota_matematica-=10

    # -----------------------------
    # BANCA ENGENHARIA
    # -----------------------------

    nota_engenharia=100

    if linhas>1500:
        nota_engenharia-=10

    if "todo" in texto_lower:
        nota_engenharia-=5

    # -----------------------------
    # BANCA IA
    # -----------------------------

    nota_ia=100

    if "score" in texto_lower and "justific" not in texto_lower:
        nota_ia-=25

    if "random" in texto_lower:
        nota_ia-=20

    # -----------------------------
    # BANCA COMERCIAL
    # -----------------------------

    nota_comercial=70

    if "paypal" in texto_lower:
        nota_comercial+=10

    if "checkout" in texto_lower:
        nota_comercial+=10

    if "payment" in texto_lower:
        nota_comercial+=10

    # -----------------------------
    # BANCA SEGURANÃƒâ€¡A
    # -----------------------------

    nota_seguranca=100

    if "os.remove" in texto_lower:
        nota_seguranca-=20

    if "shutil.rmtree" in texto_lower:
        nota_seguranca-=30

    # -----------------------------
    # BANCA UX
    # -----------------------------

    nota_ux=70

    if "html" in texto_lower:
        nota_ux+=10

    if "bootstrap" in texto_lower:
        nota_ux+=10

    if "css" in texto_lower:
        nota_ux+=10

    # -----------------------------
    # NOTA FINAL
    # -----------------------------

    nota_final=round(

        (
            nota_matematica+
            nota_engenharia+
            nota_ia+
            nota_comercial+
            nota_seguranca+
            nota_ux

        )/6,1

    )

    if nota_final>=90:
        parecer="APROVADO"

    elif nota_final>=75:
        parecer="REVISÃƒÆ'O"

    else:
        parecer="REPROVADO"

    assinatura=hashlib.md5(
        texto.encode(errors="ignore")
    ).hexdigest()

    algoritmos.append({

        "arquivo":caminho,

        "linhas":linhas,

        "matematica":nota_matematica,

        "engenharia":nota_engenharia,

        "ia":nota_ia,

        "comercial":nota_comercial,

        "seguranca":nota_seguranca,

        "ux":nota_ux,

        "nota_final":nota_final,

        "parecer":parecer,

        "assinatura":assinatura

    })

algoritmos.sort(

    key=lambda x:x["nota_final"],

    reverse=True

)

print()

print("ALGORITMOS ANALISADOS:",len(algoritmos))

print()

for a in algoritmos[:20]:

    print("="*70)

    print(a["arquivo"])

    print()

    print("MATEMÃƒÂTICA :",a["matematica"])

    print("ENGENHARIA :",a["engenharia"])

    print("IA         :",a["ia"])

    print("COMERCIAL  :",a["comercial"])

    print("SEGURANÃƒâ€¡A  :",a["seguranca"])

    print("UX         :",a["ux"])

    print()

    print("NOTA FINAL :",a["nota_final"])

    print("PARECER    :",a["parecer"])

    print()

relatorio={

    "data":str(datetime.now()),

    "algoritmos":algoritmos

}

with open(

    "IOTEC_ACADEMIC_REVIEW.json",

    "w",

    encoding="utf-8"

) as f:

    json.dump(

        relatorio,

        f,

        indent=4,

        ensure_ascii=False

    )

print("="*70)

print("BANCA ACADÃƒÅ MICA FINALIZADA")

print("="*70)

print()

print("Arquivo gerado:")

print("IOTEC_ACADEMIC_REVIEW.json")



