import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

CAMPAIGN_DB = r"C:\IOTEC\IOTEC_CAMPAIGNS.db"
LEADS_DB = r"C:\IOTEC\IOTEC_REAL_LEADS.db"

print("=" * 70)
print("X27 CAMPAIGN STATUS")
print("=" * 70)
print()

# CAMPANHAS
camp_conn = sqlite3.connect(CAMPAIGN_DB)
camp_cur = camp_conn.cursor()

lead_conn = sqlite3.connect(LEADS_DB)
lead_cur = lead_conn.cursor()

camp_cur.execute("""
SELECT
campaign_name,
segment,
target_companies,
target_proposals,
target_contracts,
target_revenue,
status
FROM campaigns
ORDER BY campaign_name
""")

campanhas = camp_cur.fetchall()

if not campanhas:
    print("NENHUMA CAMPANHA ENCONTRADA")
else:

    for c in campanhas:

        nome = c[0]
        segmento = c[1]
        meta_empresas = c[2]
        meta_propostas = c[3]
        meta_contratos = c[4]
        meta_receita = c[5]
        status = c[6]

        lead_cur.execute("""
        SELECT COUNT(*)
        FROM real_leads
        WHERE UPPER(segment)=UPPER(?)
        """, (segmento,))

        encontrados = lead_cur.fetchone()[0]

        lead_cur.execute("""
        SELECT COALESCE(SUM(estimated_value),0)
        FROM real_leads
        WHERE UPPER(segment)=UPPER(?)
        """, (segmento,))

        pipeline = lead_cur.fetchone()[0]

        percentual = 0

        if meta_empresas > 0:
            percentual = round(
                (encontrados / meta_empresas) * 100,
                2
            )

        print("=" * 70)
        print("CAMPANHA :", nome)
        print("SEGMENTO :", segmento)
        print("STATUS   :", status)
        print()
        print("META EMPRESAS......", meta_empresas)
        print("ENCONTRADAS........", encontrados)
        print("PROGRESSO..........", f"{percentual}%")
        print()
        print("META PROPOSTAS.....", meta_propostas)
        print("META CONTRATOS.....", meta_contratos)
        print("META RECEITA.......", f"R$ {meta_receita:,.2f}")
        print("PIPELINE REAL......", f"R$ {pipeline:,.2f}")
        print()

print("=" * 70)

lead_cur.execute("""
SELECT COUNT(*)
FROM real_leads
""")

total_leads = lead_cur.fetchone()[0]

lead_cur.execute("""
SELECT COALESCE(SUM(estimated_value),0)
FROM real_leads
""")

total_pipeline = lead_cur.fetchone()[0]

print("RESUMO GERAL")
print()
print("LEADS..............", total_leads)
print("PIPELINE...........", f"R$ {total_pipeline:,.2f}")

print()
print("MISSAO")
print("1 - Localizar empresas reais")
print("2 - Registrar contatos")
print("3 - Qualificar oportunidades")
print("4 - Gerar propostas")
print("5 - Converter contratos")
print("6 - Registrar receita")

print()
print("=" * 70)
print("STATUS FINALIZADO")
print("=" * 70)

camp_conn.close()
lead_conn.close()



