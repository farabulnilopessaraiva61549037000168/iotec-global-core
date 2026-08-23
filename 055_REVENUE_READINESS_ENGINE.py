# ==========================================================
# 055_REVENUE_READINESS_ENGINE.py
# IOTEC REVENUE READINESS ENGINE
# ==========================================================

import sqlite3

DB="iotec_kernel.db"

db=sqlite3.connect(DB, timeout=30)
cursor=db.cursor()

print("="*70)
print("IOTEC REVENUE READINESS ENGINE")
print("="*70)
print()

CHECKLIST=[

("GovernanÃƒÂ§a","ecosystems"),
("Protocolos","ecosystem_protocol"),
("Control Tower","control_tower"),
("ForÃƒÂ§a de Trabalho","workforce"),
("MissÃƒÂµes","missions"),
("Gateway de Leads","real_leads"),
("Fila de Clientes","client_queue"),
("Perguntas Executivas","executive_questions"),
("EvidÃƒÂªncias","executive_evidence")

]

prontos=0
total=len(CHECKLIST)

print("CHECKLIST EXECUTIVO")
print()

for nome,tabela in CHECKLIST:

    try:

        cursor.execute(f"SELECT COUNT(*) FROM {tabela}")

        qtd=cursor.fetchone()[0]

        status="OK"

        prontos+=1

    except:

        qtd=0

        status="FALTA"

    print(f"{status:<8}{nome:<30}{qtd}")

print()

print("="*70)

percentual=int((prontos/total)*100)

print("MATURIDADE OPERACIONAL")

print("="*70)

print()

print(f"Componentes encontrados : {prontos}/{total}")

print(f"ProntidÃƒÂ£o.............. : {percentual}%")

print()

# ---------------------------------------------------------

pendencias=[]

cursor.execute("SELECT COUNT(*) FROM real_leads")
if cursor.fetchone()[0]==0:
    pendencias.append("Nenhum lead real registrado.")

cursor.execute("SELECT COUNT(*) FROM missions")
if cursor.fetchone()[0]==0:
    pendencias.append("Nenhuma missÃƒÂ£o executada.")

cursor.execute("SELECT COUNT(*) FROM workforce")
if cursor.fetchone()[0]==0:
    pendencias.append("NÃƒÂ£o existe forÃƒÂ§a de trabalho.")

print("="*70)
print("GARGALOS")
print("="*70)
print()

if pendencias:

    for p in pendencias:

        print("[ ]",p)

else:

    print("Nenhum gargalo estrutural encontrado.")

print()

print("="*70)
print("PRÃƒâ€œXIMAS AÃƒâ€¡Ãƒâ€¢ES")
print("="*70)
print()

acoes=[

"Conectar Website",
"Conectar WhatsApp Business",
"Conectar LinkedIn",
"Cadastrar primeiro produto comercial",
"Receber primeiro lead real",
"Emitir primeira proposta",
"Receber primeiro pagamento"

]

for i,a in enumerate(acoes,1):

    print(f"{i:02d} - {a}")

print()

print("="*70)
print("MISSÃƒÆ'O DA PRESIDÃƒÅ NCIA")
print("="*70)
print()

print("A partir deste ponto,")
print("cada nova implementaÃƒÂ§ÃƒÂ£o")
print("deve aumentar a capacidade")
print("real de faturamento.")
print()

db.close()


