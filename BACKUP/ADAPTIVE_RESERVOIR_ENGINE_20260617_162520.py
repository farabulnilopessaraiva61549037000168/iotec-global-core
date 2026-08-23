import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
import math

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

META_MENSAL = 50000

conn = sqlite3.connect(DB)
cur = conn.cursor()

print("")
print("==================================================")
print("IOTEC ADAPTIVE RESERVOIR ENGINE")
print("==================================================")
print("")

# ==================================================
# DADOS DO PIPELINE
# ==================================================

rows = cur.execute("""

SELECT

    estimated_value,
    lead_score,
    status

FROM commercial_opportunities

""").fetchall()

pipeline_total = 0
receita_provavel = 0

for row in rows:
    pass

    valor = row[0]
    score = row[1]
    status = row[2]

    pipeline_total += valor

    chance = score

    if status == "NEGOCIACAO":
        chance += 30

    elif status == "PAGAMENTO_PENDENTE":
        chance += 40

    elif status == "PROPOSTA_ENVIADA":
        chance += 20

    elif status == "EM_ANALISE":
        chance += 10

    if chance > 100:
        chance = 100

    receita_provavel += valor * (chance / 100)

# ==================================================
# EMPRESAS ATUAIS
# ==================================================

empresas_atuais = cur.execute("""

SELECT COUNT(*)

FROM commercial_opportunities

""").fetchone()[0]

# ==================================================
# TICKET MEDIO
# ==================================================

ticket_medio = 0

if empresas_atuais > 0:
    ticket_medio = pipeline_total / empresas_atuais

# ==================================================
# CALCULO ADAPTATIVO
# ==================================================

taxa_fechamento = 0.20
taxa_qualificacao = 0.50

if ticket_medio > 0:
    pass

    contratos_necessarios = math.ceil(
        META_MENSAL / ticket_medio
    )

else:
    pass

    contratos_necessarios = 0

oportunidades_necessarias = math.ceil(
    contratos_necessarios / taxa_fechamento
)

reservatorio_operacional = math.ceil(
    oportunidades_necessarias / taxa_qualificacao
)

reservatorio_tatico = reservatorio_operacional * 3

reservatorio_estrategico = reservatorio_operacional * 12

# ==================================================
# STATUS
# ==================================================

if empresas_atuais < reservatorio_operacional:
    pass

    nivel = "VERMELHO"

elif empresas_atuais < reservatorio_tatico:
    pass

    nivel = "AMARELO"

elif empresas_atuais < reservatorio_estrategico:
    pass

    nivel = "VERDE"

else:
    pass

    nivel = "EXCELENTE"

# ==================================================
# DEFICITS
# ==================================================

deficit_operacional = max(
    0,
    reservatorio_operacional - empresas_atuais
)

deficit_tatico = max(
    0,
    reservatorio_tatico - empresas_atuais
)

deficit_estrategico = max(
    0,
    reservatorio_estrategico - empresas_atuais
)

# ==================================================
# PAINEL
# ==================================================

print("META")
print(f"R$ {META_MENSAL:,.2f}")
print("")

print("PIPELINE")
print(f"R$ {pipeline_total:,.2f}")
print("")

print("RECEITA PROVAVEL")
print(f"R$ {receita_provavel:,.2f}")
print("")

print("TICKET MEDIO")
print(f"R$ {ticket_medio:,.2f}")
print("")

print("==================================================")
print("RESERVATORIOS")
print("==================================================")
print("")

print(
    f"OPERACIONAL: {reservatorio_operacional}"
)

print(
    f"TATICO: {reservatorio_tatico}"
)

print(
    f"ESTRATEGICO: {reservatorio_estrategico}"
)

print("")

print("EMPRESAS ATUAIS")
print(empresas_atuais)

print("")

print("NIVEL")
print(nivel)

print("")

print("==================================================")
print("DEFICITS")
print("==================================================")
print("")

print(
    f"OPERACIONAL: {deficit_operacional}"
)

print(
    f"TATICO: {deficit_tatico}"
)

print(
    f"ESTRATEGICO: {deficit_estrategico}"
)

print("")

print("==================================================")
print("ORDEM EXECUTIVA")
print("==================================================")
print("")

if nivel == "VERMELHO":
    pass

    print(
        f"ADICIONAR {deficit_operacional} EMPRESAS IMEDIATAMENTE"
    )

elif nivel == "AMARELO":
    pass

    print(
        f"ADICIONAR {deficit_tatico} EMPRESAS"
    )

elif nivel == "VERDE":
    pass

    print(
        "RESERVATORIO SAUDAVEL"
    )

else:
    pass

    print(
        "RESERVATORIO EXCELENTE"
    )

print("")
print("==================================================")

conn.close()


