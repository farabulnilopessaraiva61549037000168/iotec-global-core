import json
import os
from datetime import datetime

INPUT_FILE = "IOTEC_VERIFIED_COMPANIES.json"
OUTPUT_FILE = "IOTEC_CORPORATE_GRAPH.json"


# ==========================================================
# Inicializa estrutura de enriquecimento
# ==========================================================

def enrichment_structure():

    return {

        "website": {
            "value": "",
            "status": "PENDING",
            "confidence": 0,
            "source": ""
        },

        "email": {
            "value": "",
            "status": "PENDING",
            "confidence": 0,
            "source": ""
        },

        "phone": {
            "value": "",
            "status": "PENDING",
            "confidence": 0,
            "source": ""
        },

        "whatsapp": {
            "value": "",
            "status": "PENDING",
            "confidence": 0,
            "source": ""
        },

        "linkedin": {
            "value": "",
            "status": "PENDING",
            "confidence": 0,
            "source": ""
        },

        "instagram": {
            "value": "",
            "status": "PENDING",
            "confidence": 0,
            "source": ""
        },

        "facebook": {
            "value": "",
            "status": "PENDING",
            "confidence": 0,
            "source": ""
        },

        "youtube": {
            "value": "",
            "status": "PENDING",
            "confidence": 0,
            "source": ""
        }

    }


# ==========================================================
# Calcula completude
# ==========================================================

def completion(data):

    total = len(data)
    ok = 0

    for item in data.values():

        if item["status"] == "VERIFIED":
            ok += 1

    return round((ok / total) * 100, 2)


# ==========================================================
# Principal
# ==========================================================

def main():

    print("=" * 90)
    print("IOTEC CORPORATE ENRICHMENT ENGINE")
    print("=" * 90)
    print()

    if not os.path.exists(INPUT_FILE):

        print("Arquivo inexistente:")
        print(INPUT_FILE)
        return

    with open(
        INPUT_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        companies = json.load(f)

    graph = []

    for company in companies:

        enrich = enrichment_structure()

        graph.append({

            "company_name": company.get("company_name", ""),

            "segment": company.get("segment", ""),

            "city": company.get("city", ""),

            "state": company.get("state", ""),

            "country": company.get("country", ""),

            "market_score": company.get("market_score", 0),

            "enrichment": enrich,

            "completion": completion(enrich),

            "created_at": datetime.now().isoformat()

        })

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            graph,
            f,
            indent=4,
            ensure_ascii=False
        )

    print("Empresas processadas :", len(graph))
    print()

    print("=" * 90)
    print("TOP 5")
    print("=" * 90)
    print()

    for item in graph[:5]:

        print(item["company_name"])
        print("Segmento :", item["segment"])
        print("Completude :", f"{item['completion']}%")
        print()

    print("=" * 90)
    print("ARQUIVO GERADO")
    print("=" * 90)
    print()

    print(OUTPUT_FILE)
    print()

    print("STATUS")
    print("CORPORATE GRAPH READY")


if __name__ == "__main__":
    main()

