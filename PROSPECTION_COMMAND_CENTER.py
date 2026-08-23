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
TAXA_FECHAMENTO = 0.20
TAXA_QUALIFICACAO = 0.50

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

print("")
print("==================================================")
print("IOTEC PROSPECTION COMMAND CENTER")
print("==================================================")
print("")

# ==================================================
# DADOS ATUAIS
# ==================================================

rows = cur.execute("""

SELECT
    company,
    sector,
    estimated_value,
    lead_score,
    status

FROM commercial_opportunities

""").fetchall()

pipeline_total = 0
empresas = len(rows)

setores = {}

for r in rows:
    pass

    setor = r[1]
    valor = r[2]

    pipeline_total += valor

    setores[setor] = setores.get(setor, 0) + 1

ticket_medio = 0

if empresas > 0:
    ticket_medio = pipeline_total / empresas

# ==================================================
# META
# ==================================================

contratos = 0

if ticket_medio > 0:
    pass

    contratos = math.ceil(
        META_MENSAL / ticket_medio
    )

oportunidades = math.ceil(
    contratos / TAXA_FECHAMENTO
)

empresas_necessarias = math.ceil(
    oportunidades / TAXA_QUALIFICACAO
)

deficit = empresas_necessarias - empresas

if deficit < 0:
    deficit = 0

# ==================================================
# SETOR MAIS FORTE
# ==================================================

setor_prioritario = None
maior = 0

for setor, qtd in setores.items():
    pass

    if qtd > maior:
        maior = qtd
        setor_prioritario = setor

# ==================================================
# RECEITA POR STATUS
# ==================================================

negociacao = cur.execute("""

SELECT IFNULL(SUM(estimated_value),0)

FROM commercial_opportunities

WHERE status='NEGOCIACAO'

""").fetchone()[0]

pagamento = cur.execute("""

SELECT IFNULL(SUM(estimated_value),0)

FROM commercial_opportunities

WHERE status='PAGAMENTO_PENDENTE'

""").fetchone()[0]

# ==================================================
# PAINEL
# ==================================================

print("META MENSAL")
print(f"R$ {META_MENSAL:,.2f}")
print("")

print("PIPELINE")
print(f"R$ {pipeline_total:,.2f}")
print("")

print("TICKET MEDIO")
print(f"R$ {ticket_medio:,.2f}")
print("")

print("CONTRATOS NECESSARIOS")
print(contratos)
print("")

print("OPORTUNIDADES NECESSARIAS")
print(oportunidades)
print("")

print("EMPRESAS NECESSARIAS")
print(empresas_necessarias)
print("")

print("EMPRESAS ATUAIS")
print(empresas)
print("")

print("DEFICIT")
print(deficit)
print("")

print("==================================================")
print("SETOR PRIORITARIO")
print("==================================================")
print("")

print(setor_prioritario)
print("")

print("==================================================")
print("RECEITA QUENTE")
print("==================================================")
print("")

print(f"NEGOCIACAO: R$ {negociacao:,.2f}")
print(f"PAGAMENTO PENDENTE: R$ {pagamento:,.2f}")

print("")

receita_curto_prazo = negociacao + pagamento

print("RECEITA DE CURTO PRAZO")
print(f"R$ {receita_curto_prazo:,.2f}")

print("")

print("==================================================")
print("ORDEM OPERACIONAL")
print("==================================================")
print("")

if deficit == 0:
    pass

    print("RESERVATORIO SUFICIENTE")
    print("FOCO EM FECHAMENTO")

else:
    pass

    print(
        f"ADICIONAR {deficit} NOVAS EMPRESAS QUALIFICADAS"
    )

    print(
        f"PRIORIZAR SETOR: {setor_prioritario}"
    )

    print(
        f"FOCAR EM CONTRATOS DE R$ {ticket_medio:,.2f}"
    )

print("")
print("==================================================")

conn.close()




