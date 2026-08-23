import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"
META = 50000

conn = sqlite3.connect(DB)
cur = conn.cursor()

print("")
print("==================================================")
print("IOTEC WAR ROOM ENGINE")
print("==================================================")
print("")

# ==================================================
# RECEITA
# ==================================================

receita_recebida = cur.execute("""

SELECT IFNULL(
SUM(amount),0
)

FROM financial_ledger

WHERE status='PAGO'

""").fetchone()[0]

pipeline = cur.execute("""

SELECT IFNULL(
SUM(estimated_value),0
)

FROM commercial_opportunities

WHERE status <> 'CLIENTE_ATIVO'

""").fetchone()[0]

clientes = cur.execute("""

SELECT COUNT(*)

FROM client_projects

""").fetchone()[0]

projetos_entregues = cur.execute("""

SELECT COUNT(*)

FROM client_projects

WHERE status='ENTREGUE'

""").fetchone()[0]

deficit = max(
    0,
    META - receita_recebida
)

# ==================================================
# MISSOES
# ==================================================

oportunidades = cur.execute("""

SELECT

company,
status,
estimated_value,
lead_score

FROM commercial_opportunities

WHERE status <> 'CLIENTE_ATIVO'

ORDER BY

estimated_value DESC,
lead_score DESC

""").fetchall()

print("PAINEL EXECUTIVO")
print("")

print(
    f"META: R$ {META:,.2f}"
)

print(
    f"RECEITA RECEBIDA: "
    f"R$ {receita_recebida:,.2f}"
)

print(
    f"DEFICIT: "
    f"R$ {deficit:,.2f}"
)

print(
    f"PIPELINE: "
    f"R$ {pipeline:,.2f}"
)

print(
    f"CLIENTES: "
    f"{clientes}"
)

print(
    f"PROJETOS ENTREGUES: "
    f"{projetos_entregues}"
)

print("")
print("==================================================")
print("MISSAO DO DIA")
print("==================================================")
print("")

missoes = []

for empresa, status, valor, score in oportunidades:
    pass

    if status == "NEGOCIACAO":
        pass

        prioridade = 100
        acao = "REUNIAO EXECUTIVA"

    elif status == "PAGAMENTO_PENDENTE":
        pass

        prioridade = 95
        acao = "COBRANCA"

    elif status == "PROPOSTA_ENVIADA":
        pass

        prioridade = 85
        acao = "FOLLOWUP"

    elif status == "EM_ANALISE":
        pass

        prioridade = 70
        acao = "DIAGNOSTICO"

    else:
        pass

        prioridade = score
        acao = "QUALIFICACAO"

    missoes.append(

        (
            prioridade,
            empresa,
            status,
            valor,
            acao
        )

    )

missoes.sort(
    reverse=True
)

for idx, m in enumerate(
    missoes[:5],
    start=1
):

    print(
        f"{idx}. "
        f"{m[1]} | "
        f"{m[2]} | "
        f"R$ {m[3]:,.2f} | "
        f"{m[4]}"
    )

# ==================================================
# COBERTURA DA META
# ==================================================

print("")
print("==================================================")
print("ANALISE DE META")
print("==================================================")
print("")

cobertura = receita_recebida + pipeline

print(
    f"COBERTURA TOTAL: "
    f"R$ {cobertura:,.2f}"
)

if cobertura >= META:
    pass

    print(
        "META COBERTA PELO ECOSSISTEMA"
    )

    excedente = cobertura - META

    print(
        f"EXCEDENTE: "
        f"R$ {excedente:,.2f}"
    )

else:
    pass

    faltam = META - cobertura

    print(
        f"FALTAM: "
        f"R$ {faltam:,.2f}"
    )

# ==================================================
# RISCO
# ==================================================

print("")
print("==================================================")
print("RISCO EXECUTIVO")
print("==================================================")
print("")

if pipeline >= deficit:
    pass

    risco = "BAIXO"

elif pipeline >= deficit * 0.7:
    pass

    risco = "MEDIO"

else:
    pass

    risco = "ALTO"

print(
    f"RISCO DA META: {risco}"
)

if risco == "BAIXO":
    pass

    prob = 95

elif risco == "MEDIO":
    pass

    prob = 70

else:
    pass

    prob = 40

print(
    f"PROBABILIDADE ESTIMADA: "
    f"{prob}%"
)

print("")
print("==================================================")
print("DECISAO EXECUTIVA")
print("==================================================")
print("")

if risco == "BAIXO":
    pass

    print(
        "FOCAR EM CONVERSAO"
    )

elif risco == "MEDIO":
    pass

    print(
        "AUMENTAR PROSPECCAO"
    )

else:
    pass

    print(
        "REABASTECER RESERVATORIO"
    )

print("")
print("==================================================")

conn.close()


