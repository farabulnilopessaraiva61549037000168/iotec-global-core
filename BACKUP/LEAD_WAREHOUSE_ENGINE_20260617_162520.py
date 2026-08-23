import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

CAPACIDADE_MAXIMA = 1000
LIMITE_CRITICO = 20
LIMITE_ATENCAO = 50

conn = sqlite3.connect(DB)
cur = conn.cursor()

print("")
print("==================================================")
print("IOTEC LEAD WAREHOUSE ENGINE")
print("==================================================")
print("")

# ==================================================
# ESTOQUE
# ==================================================

total = cur.execute("""

SELECT COUNT(*)

FROM commercial_opportunities

""").fetchone()[0]

# ==================================================
# STATUS
# ==================================================

ocupacao = 0

if CAPACIDADE_MAXIMA > 0:
    pass

    ocupacao = (
        total / CAPACIDADE_MAXIMA
    ) * 100

if ocupacao < LIMITE_CRITICO:
    pass

    nivel = "CRITICO"

elif ocupacao < LIMITE_ATENCAO:
    pass

    nivel = "ATENCAO"

else:
    pass

    nivel = "SAUDAVEL"

# ==================================================
# CLASSIFICACAO
# ==================================================

novas = cur.execute("""

SELECT COUNT(*)

FROM commercial_opportunities

WHERE status='NOVA'

""").fetchone()[0]

analise = cur.execute("""

SELECT COUNT(*)

FROM commercial_opportunities

WHERE status='EM_ANALISE'

""").fetchone()[0]

proposta = cur.execute("""

SELECT COUNT(*)

FROM commercial_opportunities

WHERE status='PROPOSTA_ENVIADA'

""").fetchone()[0]

negociacao = cur.execute("""

SELECT COUNT(*)

FROM commercial_opportunities

WHERE status='NEGOCIACAO'

""").fetchone()[0]

pagamento = cur.execute("""

SELECT COUNT(*)

FROM commercial_opportunities

WHERE status='PAGAMENTO_PENDENTE'

""").fetchone()[0]

ativos = cur.execute("""

SELECT COUNT(*)

FROM commercial_opportunities

WHERE status='CLIENTE_ATIVO'

""").fetchone()[0]

# ==================================================
# TOP LEADS
# ==================================================

top = cur.execute("""

SELECT

company,
sector,
estimated_value,
status

FROM commercial_opportunities

ORDER BY estimated_value DESC

LIMIT 10

""").fetchall()

# ==================================================
# ALERTAS
# ==================================================

alertas = []

if ocupacao < LIMITE_CRITICO:
    pass

    alertas.append(
        "RESERVATORIO ABAIXO DE 20%"
    )

if total < 50:
    pass

    alertas.append(
        "ESTOQUE COMERCIAL MUITO BAIXO"
    )

if negociacao == 0:
    pass

    alertas.append(
        "SEM NEGOCIACOES ATIVAS"
    )

if pagamento == 0:
    pass

    alertas.append(
        "SEM PAGAMENTOS PENDENTES"
    )

# ==================================================
# PAINEL
# ==================================================

print("CAPACIDADE MAXIMA")
print(CAPACIDADE_MAXIMA)

print("")

print("EMPRESAS")
print(total)

print("")

print("OCUPACAO")
print(f"{ocupacao:.2f}%")

print("")

print("NIVEL")
print(nivel)

print("")

print("==================================================")
print("DISTRIBUICAO")
print("==================================================")
print("")

print("NOVA:", novas)
print("EM_ANALISE:", analise)
print("PROPOSTA:", proposta)
print("NEGOCIACAO:", negociacao)
print("PAGAMENTO:", pagamento)
print("CLIENTE:", ativos)

print("")

print("==================================================")
print("TOP LEADS")
print("==================================================")
print("")

for t in top:
    pass

    print(
        f"{t[0]} | "
        f"{t[1]} | "
        f"R$ {t[2]:,.2f} | "
        f"{t[3]}"
    )

print("")

print("==================================================")
print("ALERTAS")
print("==================================================")
print("")

if len(alertas) == 0:
    pass

    print("SEM ALERTAS")

else:
    pass

    for alerta in alertas:
        pass

        print(alerta)

print("")

print("==================================================")
print("RESUMO EXECUTIVO")
print("==================================================")
print("")

print(
    f"CAPACIDADE LIVRE: "
    f"{CAPACIDADE_MAXIMA - total}"
)

print(
    f"OCUPACAO: "
    f"{ocupacao:.2f}%"
)

print(
    f"ALERTAS: "
    f"{len(alertas)}"
)

print("")

print("==================================================")

conn.close()


