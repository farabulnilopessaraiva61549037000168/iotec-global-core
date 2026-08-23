import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
from datetime import datetime

CAMPAIGN_DB = r"C:\IOTEC\IOTEC_CAMPAIGNS.db"
LEADS_DB = r"C:\IOTEC\IOTEC_REAL_LEADS.db"

print("=" * 70)
print("X27 DISCOVERY MISSION CENTER")
print("=" * 70)
print()

camp_conn = sqlite3.connect(CAMPAIGN_DB)
camp_cur = camp_conn.cursor()

lead_conn = sqlite3.connect(LEADS_DB)
lead_cur = lead_conn.cursor()

camp_cur.execute("""
SELECT
campaign_name,
segment,
target_companies
FROM campaigns
WHERE status='ATIVA'
""")

campanhas = camp_cur.fetchall()

total_faltante = 0

for campanha in campanhas:

    nome = campanha[0]
    segmento = campanha[1]
    meta = campanha[2]

    lead_cur.execute("""
    SELECT COUNT(*)
    FROM real_leads
    WHERE UPPER(segment)=UPPER(?)
    """, (segmento,))

    atual = lead_cur.fetchone()[0]

    faltam = max(0, meta - atual)

    total_faltante += faltam

    print("=" * 70)
    print("CAMPANHA :", nome)
    print("SEGMENTO :", segmento)
    print("META     :", meta)
    print("ATUAL    :", atual)
    print("FALTAM   :", faltam)
    print()

    if faltam > 0:

        print("BUSCAS NECESSARIAS")

        for i in range(1, min(faltam, 10) + 1):

            print(
                f"[ ] {segmento} BRASIL - OPORTUNIDADE {i}"
            )

        if faltam > 10:
            print(f"... + {faltam - 10} oportunidades")

    print()

print("=" * 70)
print("CENTRO DE MISSOES")
print("=" * 70)

print()
print("DATA:", datetime.now())
print()
print("TOTAL DE EMPRESAS NECESSARIAS:", total_faltante)
print()

print("PRIORIDADE OPERACIONAL")

camp_cur.execute("""
SELECT
segment,
SUM(target_revenue)
FROM campaigns
GROUP BY segment
ORDER BY SUM(target_revenue) DESC
""")

for row in camp_cur.fetchall():

    print(
        f"{row[0]:15} "
        f"R$ {row[1]:,.2f}"
    )

print()
print("=" * 70)
print("STATUS")
print("=" * 70)

print("""
O NUCLEO ESTA PRONTO PARA RECEBER
EMPRESAS REAIS.

PROXIMA ETAPA:

1 - CONECTAR FONTE EXTERNA
2 - IMPORTAR EMPRESAS
3 - QUALIFICAR
4 - GERAR PROPOSTAS
5 - CONVERTER CONTRATOS
""")

camp_conn.close()
lead_conn.close()



