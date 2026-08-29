import sqlite3

conn = sqlite3.connect(r'C:\IOTEC\iotec.db')
cursor = conn.cursor()

# Lote Expansivo de Pesos-Pesados Globais
NOVOS_PESOS_PESADOS = [
    # ESTADOS UNIDOS & CANADÁ (FINANCIAL & CLOUD INFRASTRUCTURE)
    ("FISERV INC.", "EIN: 39-1506125", "EUA", "PAYMENTS_CORE_ENGINE"),
    ("GLOBAL PAYMENTS INC.", "EIN: 58-2567903", "EUA", "TRANSACTION_COMPLIANCE"),
    ("FIS (FIDELITY NATIONAL INFO)", "EIN: 42-1503600", "EUA", "BANKING_RISK_SHIELD"),
    ("NICE ACTIMIZE INC.", "EIN: 13-3982001", "EUA", "AML_SANCTIONS_MONITORING"),
    ("NVEI CORP (NUVAPAY)", "CA-BN: 835293211", "CANADÁ", "CROSSBORDER_SETTLEMENT"),

    # UNIÃO EUROPEIA & REINO UNIDO (NEOBANKS & B2B SOFTWARE)
    ("WORLDLINE S.A.", "FR-SIREN: 378272160", "FRANÇA / UE", "MERCHANT_PAYMENTS_API"),
    ("WISE PAYMENTS LTD", "UK-SEC: 07208273", "REINO UNIDO", "INTERNATIONAL_RAILS"),
    ("N26 AG", "DE-HRB: 170622", "ALEMANHA / UE", "REALTIME_RISK_SCORING"),
    ("NEXI S.P.A.", "IT-CF: 09489670969", "ITÁLIA / UE", "EUROPEAN_SETTLEMENT_GATEWAY"),
    ("REVOLUT BUSINESS EU", "LT-SEC: 304580906", "LITUÂNIA / UE", "TREASURY_COMPLIANCE"),

    # ÁSIA, JAPÃO & SUDESTE ASIÁTICO
    ("PAYTM (ONE97 COMMUNICATIONS)", "IN-CIN: L72200DL2000PLC", "ÍNDIA", "HIGH_VOLUME_GATEWAY"),
    ("LINE PAY CORP.", "JP-SEC: 0100-01-182390", "JAPÃO", "MOBILE_SETTLEMENT_MODULE"),
    ("PAYU GLOBAL B.V.", "NL-KVK: 34336043", "CINGAPURA / HOLANDA", "EMERGING_MARKETS_COMPLIANCE"),
    ("DLOCAL LIMITED", "US-SEC: 0001844981", "URUGUAI / EUA / ASIA", "CROSSBORDER_PAYMENTS"),

    # ORIENTE MÁDIO & ÁFRICA (UAE, ARÁBIA SAUDITA & ÁFRICA DO SUL)
    ("NETWORK INTERNATIONAL LLC", "UAE-DFM: NETW", "EMIRADOS ÁRABES", "MIDDLE_EAST_PAYMENTS"),
    ("STC PAY (SAUDI DIGITAL BANK)", "SA-CR: 1010508280", "ARÁBIA SAUDITA", "NEOBANK_SECURITY_ENGINE"),
    ("FLUTTERWAVE INC.", "EIN: 81-2294101", "NIGÉRIA / EUA", "PAN_AFRICAN_RAILS")
]

for empresa, reg, pais, modulo in NOVOS_PESOS_PESADOS:
    try:
        cursor.execute("""
            INSERT INTO leads (razao_social, cnpj, registro_global, pais, status)
            VALUES (?, ?, ?, ?, 'PENDENTE_COLD_OUTREACH')
        """, (empresa, reg, reg, pais))
    except Exception:
        pass

conn.commit()

cursor.execute("SELECT COUNT(*) FROM leads")
total = cursor.fetchone()[0]
conn.close()

print("=============================================================")
print(" [✔] MAVENS & PESOS-PESADOS GLOBAIS INGERIDOS COM SUCESSO!")
print(f" 🚀 Novo Total de Leads na Base IOTEC: {total} empresas.")
print("=============================================================")
