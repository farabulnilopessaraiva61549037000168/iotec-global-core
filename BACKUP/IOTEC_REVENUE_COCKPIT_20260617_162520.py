import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
import json
from datetime import datetime

DB_MARKET = r"C:\IOTEC\IOTEC_MARKET_INTELLIGENCE.db"
DB_OPP = r"C:\IOTEC\IOTEC_OPPORTUNITY.db"

market_conn = sqlite3.connect(DB_MARKET)
market_cur = market_conn.cursor()

opp_conn = sqlite3.connect(DB_OPP)
opp_cur = opp_conn.cursor()

segments = market_cur.execute("""
SELECT COUNT(*)
FROM segments
""").fetchone()[0]

opportunities = opp_cur.execute("""
SELECT COUNT(*)
FROM opportunities
""").fetchone()[0]

pipeline_total = opp_cur.execute("""
SELECT
COALESCE(SUM(estimated_value),0)
FROM opportunities
""").fetchone()[0]

pipeline_weighted = opp_cur.execute("""
SELECT
COALESCE(
SUM(
estimated_value * probability / 100.0
),
0
)
FROM opportunities
""").fetchone()[0]

prospeccao = opp_cur.execute("""
SELECT COUNT(*)
FROM opportunities
WHERE status='PROSPECCAO'
""").fetchone()[0]

qualificacao = opp_cur.execute("""
SELECT COUNT(*)
FROM opportunities
WHERE status='QUALIFICACAO'
""").fetchone()[0]

negociacao = opp_cur.execute("""
SELECT COUNT(*)
FROM opportunities
WHERE status='NEGOCIACAO'
""").fetchone()[0]

fechado = opp_cur.execute("""
SELECT COUNT(*)
FROM opportunities
WHERE status='FECHADO'
""").fetchone()[0]

top_segment = opp_cur.execute("""
SELECT
segment,
COUNT(*)
FROM opportunities
GROUP BY segment
ORDER BY COUNT(*) DESC
LIMIT 1
""").fetchone()

top_product = opp_cur.execute("""
SELECT
product,
COUNT(*)
FROM opportunities
GROUP BY product
ORDER BY COUNT(*) DESC
LIMIT 1
""").fetchone()

report = {

    "generated": str(datetime.now()),
    "segments": segments,
    "opportunities": opportunities,
    "pipeline_total": pipeline_total,
    "pipeline_weighted": pipeline_weighted,
    "prospeccao": prospeccao,
    "qualificacao": qualificacao,
    "negociacao": negociacao,
    "fechado": fechado,
    "top_segment": top_segment[0] if top_segment else "",
    "top_product": top_product[0] if top_product else ""

}

with open(
    r"C:\IOTEC\IOTEC_REVENUE_COCKPIT.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        report,
        f,
        indent=4,
        ensure_ascii=False
    )

with open(
    r"C:\IOTEC\IOTEC_REVENUE_COCKPIT.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write("\n")
    f.write("===================================\n")
    f.write("IOTEC REVENUE COCKPIT\n")
    f.write("===================================\n\n")

    f.write(f"SEGMENTOS: {segments}\n")
    f.write(f"OPORTUNIDADES: {opportunities}\n\n")

    f.write(f"PIPELINE BRUTO: R$ {pipeline_total:,.2f}\n")
    f.write(f"PIPELINE PONDERADO: R$ {pipeline_weighted:,.2f}\n\n")

    f.write(f"PROSPECCAO: {prospeccao}\n")
    f.write(f"QUALIFICACAO: {qualificacao}\n")
    f.write(f"NEGOCIACAO: {negociacao}\n")
    f.write(f"FECHADO: {fechado}\n\n")

    f.write(f"TOP SEGMENTO: {report['top_segment']}\n")
    f.write(f"TOP PRODUTO: {report['top_product']}\n")

print("")
print("===================================")
print("IOTEC REVENUE COCKPIT")
print("===================================")
print("")

print("SEGMENTOS:", segments)
print("OPORTUNIDADES:", opportunities)

print("")
print(f"PIPELINE BRUTO: R$ {pipeline_total:,.2f}")
print(f"PIPELINE PONDERADO: R$ {pipeline_weighted:,.2f}")

print("")
print("PROSPECCAO:", prospeccao)
print("QUALIFICACAO:", qualificacao)
print("NEGOCIACAO:", negociacao)
print("FECHADO:", fechado)

print("")
print("TOP SEGMENTO:", report["top_segment"])
print("TOP PRODUTO:", report["top_product"])

print("")
print("TXT:")
print(r"C:\IOTEC\IOTEC_REVENUE_COCKPIT.txt")

print("")
print("JSON:")
print(r"C:\IOTEC\IOTEC_REVENUE_COCKPIT.json")

market_conn.close()
opp_conn.close()


