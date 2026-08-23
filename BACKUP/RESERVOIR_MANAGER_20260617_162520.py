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
print("===================================")
print("RESERVOIR MANAGER")
print("===================================")
print("")

# ==========================================
# LEITURA DO FUNIL
# ==========================================

rows = cur.execute("""

SELECT
    estimated_value,
    status

FROM commercial_opportunities

""").fetchall()

pipeline_total = 0

for r in rows:
    pipeline_total += r[0]

qtd_oportunidades = len(rows)

# ==========================================
# TICKET MEDIO
# ==========================================

ticket_medio = 0

if qtd_oportunidades > 0:
    ticket_medio = pipeline_total / qtd_oportunidades

# ==========================================
# PARAMETROS
# ==========================================

taxa_fechamento = 0.20
taxa_qualificacao = 0.50

# ==========================================
# CALCULOS
# ==========================================

contratos_necessarios = 0

if ticket_medio > 0:
    pass

    contratos_necessarios = math.ceil(
        META_MENSAL / ticket_medio
    )

oportunidades_necessarias = math.ceil(
    contratos_necessarios / taxa_fechamento
)

empresas_necessarias = math.ceil(
    oportunidades_necessarias / taxa_qualificacao
)

# ==========================================
# RESERVATORIO ATUAL
# ==========================================

empresas_atuais = cur.execute("""

SELECT COUNT(*)

FROM commercial_opportunities

""").fetchone()[0]

# ==========================================
# DEFICIT
# ==========================================

faltam_empresas = (
    empresas_necessarias -
    empresas_atuais
)

if faltam_empresas < 0:
    faltam_empresas = 0

# ==========================================
# ANALISE
# ==========================================

print("META MENSAL")
print(f"R$ {META_MENSAL:,.2f}")
print("")

print("PIPELINE TOTAL")
print(f"R$ {pipeline_total:,.2f}")
print("")

print("TICKET MEDIO")
print(f"R$ {ticket_medio:,.2f}")
print("")

print("CONTRATOS NECESSARIOS")
print(contratos_necessarios)
print("")

print("OPORTUNIDADES NECESSARIAS")
print(oportunidades_necessarias)
print("")

print("EMPRESAS NECESSARIAS")
print(empresas_necessarias)
print("")

print("EMPRESAS NO RESERVATORIO")
print(empresas_atuais)
print("")

print("DEFICIT")
print(faltam_empresas)
print("")

# ==========================================
# ACAO
# ==========================================

if faltam_empresas == 0:
    pass

    print("STATUS")
    print("RESERVATORIO ADEQUADO")

else:
    pass

    print("STATUS")
    print("REABASTECIMENTO NECESSARIO")

    print("")
    print("ACAO SUGERIDA")

    print(
        f"CAPTAR MAIS "
        f"{faltam_empresas} "
        f"EMPRESAS QUALIFICADAS"
    )

print("")
print("===================================")

conn.close()


