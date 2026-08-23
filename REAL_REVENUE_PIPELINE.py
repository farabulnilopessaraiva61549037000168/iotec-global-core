# REAL_REVENUE_PIPELINE.py

import json
from pathlib import Path
from datetime import datetime


ROOT = Path(r"C:\IOTEC")

COMPANY_DB = ROOT / "company_database.json"
CRM_DB = ROOT / "crm_database.json"

OUTPUT = ROOT / "enterprise" / "revenue"
OUTPUT.mkdir(parents=True, exist_ok=True)


PIPELINE = [
    "NOVO",
    "CONTATO",
    "QUALIFICADO",
    "PROPOSTA",
    "NEGOCIACAO",
    "CONTRATO",
    "CLIENTE"
]


def load_json(file):

    if not file.exists():
        return []

    with open(file, encoding="utf-8") as f:
        return json.load(f)


def save_json(file, data):

    with open(file, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )


companies = load_json(COMPANY_DB)
crm = load_json(CRM_DB)

crm_index = {}

for item in crm:

    crm_index[item["company_name"]] = item


new_records = 0
updated = 0

for company in companies:

    name = company.get("company_name", "")

    if not name:
        continue

    if name not in crm_index:

        lead = {

            "company_name": name,

            "country": company.get("country"),

            "state": company.get("state"),

            "city": company.get("city"),

            "segment": company.get("segmento"),

            "score": company.get("market_score", 0),

            "website": "",

            "email": "",

            "phone": "",

            "linkedin": "",

            "contact_person": "",

            "product": company.get("produto_iotec"),

            "pipeline": PIPELINE[0],

            "proposal_sent": False,

            "contract_signed": False,

            "client": False,

            "estimated_value": 8500,

            "created_at": str(datetime.now()),

            "updated_at": str(datetime.now())

        }

        crm.append(lead)

        crm_index[name] = lead

        new_records += 1

    else:

        crm_index[name]["updated_at"] = str(datetime.now())

        updated += 1


save_json(CRM_DB, crm)


dashboard = {

    "generated_at": str(datetime.now()),

    "companies": len(companies),

    "crm_records": len(crm),

    "new_records": new_records,

    "updated": updated,

    "contacts_found": len([
        x for x in crm
        if x["email"] or x["phone"]
    ]),

    "proposals": len([
        x for x in crm
        if x["proposal_sent"]
    ]),

    "contracts": len([
        x for x in crm
        if x["contract_signed"]
    ]),

    "clients": len([
        x for x in crm
        if x["client"]
    ])

}


save_json(
    OUTPUT / "real_revenue_dashboard.json",
    dashboard
)


print("=" * 70)
print("REAL REVENUE PIPELINE")
print("=" * 70)
print()

print("Empresas.............", dashboard["companies"])
print("CRM..................", dashboard["crm_records"])
print("Novos Leads..........", dashboard["new_records"])
print("Atualizados..........", dashboard["updated"])
print("Contatos Encontrados.", dashboard["contacts_found"])
print("Propostas............", dashboard["proposals"])
print("Contratos............", dashboard["contracts"])
print("Clientes.............", dashboard["clients"])
print()

print("Dashboard salvo em:")
print(OUTPUT / "real_revenue_dashboard.json")

