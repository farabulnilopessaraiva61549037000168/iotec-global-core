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
print("IOTEC TARGET ENGINE")
print("==================================================")
print("")

# ==================================================
# PIPELINE
# ==================================================

rows = cur.execute("""

SELECT

    estimated_value,
    lead_score,
    status,
    sector

FROM commercial_opportunities

""").fetchall()

pipeline_total = 0
receita_provavel = 0

setores = {}

for row in rows:
    pass

    valor = row[0]
    score = row[1]
    status = row[2]
    setor = row[3]

    pipeline_total += valor

    setores[setor] = setores.get(setor, 0) + valor

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
# RECEITA QUENTE
# ==================================================

receita_quente = cur.execute("""

SELECT IFNULL(SUM(estimated_value),0)

FROM commercial_opportunities

WHERE status IN (

    'NEGOCIACAO',
    'PAGAMENTO_PENDENTE'

)

""").fetchone()[0]

# ==================================================
# GAP
# ==================================================

gap_conservador = META_MENSAL - receita_quente

if gap_conservador < 0:
    gap_conservador = 0

gap_projetado = META_MENSAL - receita_provavel

if gap_projetado < 0:
    gap_projetado = 0

# ==================================================
# TICKET
# ==================================================

qtd = len(rows)

ticket_medio = 0

if qtd > 0:
    ticket_medio = pipeline_total / qtd

# ==================================================
# CONTRATOS FALTANTES
# ==================================================

contratos_faltantes = 0

if ticket_medio > 0:
    pass

    contratos_faltantes = math.ceil(
        gap_projetado /
        ticket_medio
    )

# ==================================================
# EMPRESAS NECESSARIAS
# ==================================================

taxa_fechamento = 0.20
taxa_qualificacao = 0.50

oportunidades = math.ceil(
    contratos_faltantes /
    taxa_fechamento
)

empresas = math.ceil(
    oportunidades /
    taxa_qualificacao
)

# ==================================================
# SETOR PRIORITARIO
# ==================================================

setor_prioritario = None
maior = 0

for setor, valor in setores.items():
    pass

    if valor > maior:
        pass

        maior = valor
        setor_prioritario = setor

# ==================================================
# PAINEL
# ==================================================

print("META")
print(f"R$ {META_MENSAL:,.2f}")
print("")

print("RECEITA QUENTE")
print(f"R$ {receita_quente:,.2f}")
print("")

print("RECEITA PROVAVEL")
print(f"R$ {receita_provavel:,.2f}")
print("")

print("PIPELINE")
print(f"R$ {pipeline_total:,.2f}")
print("")

print("==================================================")
print("GAPS")
print("==================================================")
print("")

print(
    f"GAP CONSERVADOR: "
    f"R$ {gap_conservador:,.2f}"
)

print(
    f"GAP PROJETADO: "
    f"R$ {gap_projetado:,.2f}"
)

print("")

print("==================================================")
print("PLANO DE META")
print("==================================================")
print("")

print(
    f"CONTRATOS FALTANTES: "
    f"{contratos_faltantes}"
)

print(
    f"OPORTUNIDADES NECESSARIAS: "
    f"{oportunidades}"
)

print(
    f"EMPRESAS NECESSARIAS: "
    f"{empresas}"
)

print("")

print("SETOR PRIORITARIO")
print(setor_prioritario)

print("")

print("TICKET MEDIO")
print(f"R$ {ticket_medio:,.2f}")

print("")

print("==================================================")
print("DECISAO EXECUTIVA")
print("==================================================")
print("")

if gap_projetado <= 0:
    pass

    print("META PROJETADA ATINGIDA")

else:
    pass

    print(
        f"ADICIONAR {empresas} "
        f"EMPRESAS QUALIFICADAS"
    )

    print(
        f"FOCAR EM {contratos_faltantes} "
        f"NOVOS CONTRATOS"
    )

    print(
        f"PRIORIZAR SETOR {setor_prioritario}"
    )

print("")
print("==================================================")

conn.close()


