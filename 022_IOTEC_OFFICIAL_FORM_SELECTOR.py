import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from pathlib import Path
import json

ROOT = Path(r"C:\IOTEC")

print("="*70)
print("IOTEC OFFICIAL FORM SELECTOR")
print("="*70)

IGNORAR = [
    "BACKUP",
    "LABORATORIO",
    "DUPLICADOS",
    "ENCODING_BACKUP",
    "__pycache__",
    "venv",
    "node_modules"
]

PALAVRAS = {
    "payment":10,
    "paypal":10,
    "pix":10,
    "checkout":10,
    "form":6,
    "email":6,
    "whatsapp":6,
    "api":6,
    "database":6,
    "sql":5,
    "json":4,
    "lead":5,
    "cliente":5,
    "cpf":3,
    "cnpj":3,
    "telefone":3,
    "empresa":3,
    "produto":4
}

formularios=[]

print()
print("LOCALIZANDO FORMULÃƒÂRIOS...")
print()

for arquivo in ROOT.rglob("*"):

    if arquivo.suffix.lower() not in [".html",".htm",".py"]:
        continue

    caminho=str(arquivo).upper()

    if any(i in caminho for i in IGNORAR):
        continue

    nome=arquivo.name.lower()

    if not any(x in nome for x in [
        "form",
        "lead",
        "checkout",
        "cliente",
        "cadastro",
        "landing"
    ]):
        continue

    score=0

    try:
        texto=arquivo.read_text(
            encoding="utf-8",
            errors="ignore"
        ).lower()
    except:
        texto=""

    for palavra,pontos in PALAVRAS.items():

        if palavra in texto:
            score+=pontos

    if "paypal" in texto:
        score+=15

    if "checkout" in texto:
        score+=15

    if "button" in texto or "<button" in texto:
        score+=5

    if "<form" in texto:
        score+=10

    formularios.append({

        "arquivo":str(arquivo),
        "score":score

    })

formularios.sort(
    key=lambda x:x["score"],
    reverse=True
)

print("="*70)
print("RANKING")
print("="*70)
print()

for i,item in enumerate(formularios[:20],1):

    print(f"{i:02d}  Score {item['score']:03d}")

    print(item["arquivo"])

    print()

if not formularios:

    print("Nenhum formulÃƒÂ¡rio localizado.")
    exit()

escolhido=formularios[0]

print("="*70)
print("FORMULÃƒÂRIO OFICIAL")
print("="*70)
print()

print(escolhido["arquivo"])
print()

print("Score :",escolhido["score"])
print()

print("="*70)
print("JUSTIFICATIVA")
print("="*70)
print()

print("O nÃƒÂºcleo analisou automaticamente todos")
print("os formulÃƒÂ¡rios encontrados.")

print()

print("O formulÃƒÂ¡rio escolhido apresentou")
print("o maior score operacional.")

print()

print("A decisÃƒÂ£o considerou:")

print("Ã¢Å"â€œ Estrutura HTML")
print("Ã¢Å"â€œ PresenÃƒÂ§a de Checkout")
print("Ã¢Å"â€œ IntegraÃƒÂ§ÃƒÂ£o PayPal")
print("Ã¢Å"â€œ APIs")
print("Ã¢Å"â€œ Email")
print("Ã¢Å"â€œ Banco")
print("Ã¢Å"â€œ Componentes comerciais")

print()

print("Os demais permanecerÃƒÂ£o")
print("como patrimÃƒÂ´nio tÃƒÂ©cnico.")

print()

relatorio={

    "formulario_oficial":escolhido,

    "top20":formularios[:20]

}

with open(

    "IOTEC_FORMULARIO_OFICIAL.json",

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
print("MISSÃƒÆ'O CONCLUÃƒÂDA")
print("="*70)

print()

print("Arquivo salvo:")

print("IOTEC_FORMULARIO_OFICIAL.json")



