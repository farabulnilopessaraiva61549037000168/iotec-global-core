import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import sqlite3
import requests
from datetime import datetime

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"
PAYPAL = "http://127.0.0.1:5001/health"

def status(ok):
    return "[OK]" if ok else "[ERRO]"

print("=" * 70)
print("                 IOTEC CONTROL CENTER")
print("=" * 70)
print()

# Data
print("DATA:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
print()

# Banco
db_ok = os.path.exists(DB)
print(f"{status(db_ok)} Banco SQLite")

# Pipeline
if db_ok:
    try:
        conn = sqlite3.connect(DB)
        cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

        total = cur.execute("SELECT COUNT(*) FROM pipeline").fetchone()[0]

        pendentes = cur.execute("""
            SELECT COUNT(*)
            FROM pipeline
            WHERE payment_status='AGUARDANDO_PAGAMENTO'
        """).fetchone()[0]

        ativos = cur.execute("""
            SELECT COUNT(*)
            FROM pipeline
            WHERE status='CLIENTE_ATIVO'
        """).fetchone()[0]

        conn.close()

        print(f"{status(True)} Pipeline")
        print(f"     Registros : {total}")
        print(f"     Pendentes : {pendentes}")
        print(f"     Ativos    : {ativos}")

    except Exception as e:
        print(f"{status(False)} Pipeline")
        print("     ", e)

print()

# PayPal
try:
    r = requests.get(PAYPAL, timeout=5)

    if r.status_code == 200:
        print(f"{status(True)} PayPal Server")
    else:
        print(f"{status(False)} PayPal Server")

except:
    print(f"{status(False)} PayPal Server")

print()

# IntegraÃ§Ãµes
print("INTEGRAÃ‡Ã•ES")
print("---------------------------------------------")
print("[OK] PayPal")
print("[EM DESENVOLVIMENTO] Google Maps")
print("[PENDENTE] LinkedIn")
print("[PENDENTE] Instagram")
print("[PENDENTE] YouTube")
print("[PENDENTE] WhatsApp Business")

print()

print("META DO MÃŠS")
print("---------------------------------------------")
print("Receita.............R$ 50.000")
print("Empresas............5.000")
print("Contratos...........15")

print()

print("FUNDO ESTRATÃ‰GICO")
print("---------------------------------------------")
print("Saldo...............R$ 200,00")

print()
print("=" * 70)
print("CONTROL CENTER OPERACIONAL")
print("=" * 70)


print()
print("=" * 70)
print("HEALTH CHECK")
print("=" * 70)

modulos = [
    ("PAYMENT_ENGINE.py", r"C:\IOTEC\PAYMENT_ENGINE.py"),
    ("paypal_server.py", r"C:\IOTEC\paypal_server.py"),
    ("CORE_PHILOSOPHY.py", r"C:\IOTEC\CORE_PHILOSOPHY.py"),
    ("CONFIRM_PAYMENT.py", r"C:\IOTEC\CONFIRM_PAYMENT.py"),
    ("PAYPAL_CONFIRM_ENGINE.py", r"C:\IOTEC\PAYPAL_CONFIRM_ENGINE.py")
]

for nome, caminho in modulos:

    if os.path.exists(caminho):
        print(f"[OK] {nome}")
    else:
        print(f"[ERRO] {nome}")

print()
print("=" * 70)
print("SERVIÃ‡OS")
print("=" * 70)

servicos = [
    ("PayPal Local", "http://127.0.0.1:5001/health"),
]

for nome, url in servicos:

    try:
        r = requests.get(url, timeout=3)

        if r.status_code == 200:
            print(f"[ONLINE] {nome}")
        else:
            print(f"[OFFLINE] {nome}")

    except Exception:
        print(f"[OFFLINE] {nome}")

print()
print("=" * 70)
print("FIM DA VERIFICAÃ‡ÃƒO")
print("=" * 70)

print()
print("=" * 70)
print("MISSION CONTROL")
print("=" * 70)

META = 50000.00

try:

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

    receita = cur.execute("""

        SELECT IFNULL(SUM(proposal_value),0)

        FROM pipeline

        WHERE status='CLIENTE_ATIVO'

    """).fetchone()[0]

    oportunidades = cur.execute("""

        SELECT COUNT(*)

        FROM pipeline

    """).fetchone()[0]

    pendentes = cur.execute("""

        SELECT COUNT(*)

        FROM pipeline

        WHERE payment_status='AGUARDANDO_PAGAMENTO'

    """).fetchone()[0]

    conn.close()

    falta = META - float(receita)

    if falta < 0:
        falta = 0

    print(f"Receita realizada.... R$ {receita:,.2f}")
    print(f"Meta do mÃªs.......... R$ {META:,.2f}")
    print(f"Falta................ R$ {falta:,.2f}")
    print()
    print(f"Oportunidades........ {oportunidades}")
    print(f"Pagamentos pendentes. {pendentes}")

except Exception as erro:

    print("[ERRO]", erro)

print()
print("=" * 70)
print("PRÃ"XIMA MISSÃƒO")
print("=" * 70)

print("1 - Finalizar Google Maps")
print("2 - Integrar LinkedIn")
print("3 - Integrar Proton Mail")
print("4 - Integrar Instagram")
print("5 - Criar Discovery Engine")
print("6 - Automatizar Follow-up")
print("7 - Iniciar captaÃ§Ã£o de clientes")

print()
print("=" * 70)
print("NÃšCLEO EM EVOLUÃ‡ÃƒO")
print("=" * 70)


print()
print("=" * 70)
print("DECISION ENGINE")
print("=" * 70)

acoes = []

try:

    if pendentes > 0:
        acoes.append(f"Existem {pendentes} pagamentos aguardando confirmaÃ§Ã£o.")

    if oportunidades < 100:
        acoes.append("Pipeline pequeno. Recomenda-se intensificar a prospecÃ§Ã£o.")

    if receita < META * 0.30:
        acoes.append("Receita abaixo de 30% da meta mensal.")

    if falta > 0:
        acoes.append(f"Faltam R$ {falta:,.2f} para atingir a meta.")

except:
    pass

integracoes = [
    ("Google Maps", False),
    ("LinkedIn", False),
    ("Instagram", False),
    ("YouTube", False),
    ("WhatsApp", False),
    ("Proton Mail", False)
]

for nome, ativo in integracoes:

    if not ativo:
        acoes.append(f"IntegraÃ§Ã£o pendente: {nome}")

print()

if len(acoes)==0:

    print("[OK] Nenhuma recomendaÃ§Ã£o.")

else:

    for i,item in enumerate(acoes,1):

        print(f"{i}. {item}")

print()

print("=" * 70)
print("ROI ENGINE")
print("=" * 70)

FUNDO = 200

investimentos = [

("Google Maps API",200,12000),

("LinkedIn Automation",0,5000),

("Instagram",0,3000)

]

for nome,custo,retorno in investimentos:

    if custo>0:

        roi=((retorno-custo)/custo)*100

    else:

        roi=999999

    print(f"{nome:25} ROI estimado: {roi:8.1f}%")

print()

print("=" * 70)
print("ETAPA 4 CONCLUÃDA")
print("=" * 70)


import glob

print()
print("=" * 70)
print("AUTO DISCOVERY ENGINE")
print("=" * 70)

PASTA = r"C:\IOTEC"

arquivos = sorted(glob.glob(PASTA + "\\*.py"))

print()
print(f"MÃ³dulos encontrados: {len(arquivos)}")
print()

categorias = {
    "CORE": [],
    "ENGINE": [],
    "SERVER": [],
    "AUDITOR": [],
    "DISCOVERY": [],
    "PAYMENT": [],
    "CONTROL": [],
    "OUTROS": []
}

for arq in arquivos:

    nome = os.path.basename(arq)

    nome_upper = nome.upper()

    if "CORE" in nome_upper:
        categorias["CORE"].append(nome)

    elif "ENGINE" in nome_upper:
        categorias["ENGINE"].append(nome)

    elif "SERVER" in nome_upper:
        categorias["SERVER"].append(nome)

    elif "AUDITOR" in nome_upper:
        categorias["AUDITOR"].append(nome)

    elif "DISCOVERY" in nome_upper:
        categorias["DISCOVERY"].append(nome)

    elif "PAYMENT" in nome_upper:
        categorias["PAYMENT"].append(nome)

    elif "CONTROL" in nome_upper:
        categorias["CONTROL"].append(nome)

    else:
        categorias["OUTROS"].append(nome)

for categoria, lista in categorias.items():

    print()
    print(f"{categoria} ({len(lista)})")

    for item in lista[:10]:
        print("   â€¢", item)

    if len(lista) > 10:
        print(f"   ... +{len(lista)-10} mÃ³dulos")

print()
print("=" * 70)
print("ESTATÃSTICAS")
print("=" * 70)

total = len(arquivos)

engines = len(categorias["ENGINE"])
servers = len(categorias["SERVER"])
core = len(categorias["CORE"])

print(f"Total de mÃ³dulos........ {total}")
print(f"Engines................. {engines}")
print(f"Servers................. {servers}")
print(f"Core.................... {core}")

print()
print("=" * 70)
print("AUTO DISCOVERY FINALIZADO")
print("=" * 70)





