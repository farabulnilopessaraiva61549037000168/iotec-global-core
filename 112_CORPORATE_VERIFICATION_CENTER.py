import json
import os
from datetime import datetime

INPUT_FILE = "IOTEC_COMPANY_MASTER.json"
OUTPUT_FILE = "IOTEC_VERIFIED_COMPANIES.json"


def confidence(value):

    if value is None:
        return 0

    if isinstance(value, str):

        if value.strip() == "":
            return 0

    return 100


def verify_company(company):

    verified = {}

    verified["company_name"] = company.get("company_name", "")
    verified["segment"] = company.get("segmento", "")
    verified["city"] = company.get("city", "")
    verified["state"] = company.get("state", "")
    verified["country"] = company.get("country", "")

    verified["website"] = company.get("website", "")
    verified["email"] = company.get("email", "")
    verified["phone"] = company.get("phone", "")
    verified["whatsapp"] = company.get("whatsapp", "")
    verified["linkedin"] = company.get("linkedin", "")
    verified["instagram"] = company.get("instagram", "")
    verified["facebook"] = company.get("facebook", "")
    verified["youtube"] = company.get("youtube", "")

    verified["source"] = company.get("source", "")

    verified["confidence"] = {

        "company_name": confidence(verified["company_name"]),
        "segment": confidence(verified["segment"]),
        "city": confidence(verified["city"]),
        "website": confidence(verified["website"]),
        "email": confidence(verified["email"]),
        "phone": confidence(verified["phone"]),
        "whatsapp": confidence(verified["whatsapp"]),
        "linkedin": confidence(verified["linkedin"]),
        "instagram": confidence(verified["instagram"]),
        "facebook": confidence(verified["facebook"]),
        "youtube": confidence(verified["youtube"])

    }

    verified["verified_at"] = datetime.now().isoformat()

    return verified


def main():

    print("=" * 80)
    print("IOTEC CORPORATE VERIFICATION CENTER")
    print("=" * 80)
    print()

    if not os.path.exists(INPUT_FILE):

        print("Arquivo nÃƒÂ£o encontrado:")
        print(INPUT_FILE)
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:

        companies = json.load(f)

    verified_list = []

    for company in companies:

        verified_list.append(
            verify_company(company)
        )

    with open(

        OUTPUT_FILE,

        "w",

        encoding="utf-8"

    ) as f:

        json.dump(

            verified_list,

            f,

            indent=4,

            ensure_ascii=False

        )

    print("Empresas verificadas :", len(verified_list))
    print()

    print("=" * 80)
    print("TOP 5")
    print("=" * 80)
    print()

    for company in verified_list[:5]:

        print(company["company_name"])
        print("Cidade :", company["city"])
        print("ConfianÃƒÂ§a Nome :", company["confidence"]["company_name"])
        print("ConfianÃƒÂ§a Site :", company["confidence"]["website"])
        print()

    print("=" * 80)
    print("ARQUIVO GERADO")
    print("=" * 80)
    print()

    print(OUTPUT_FILE)

    print()

    print("STATUS")
    print("CORPORATE VERIFICATION READY")


if __name__ == "__main__":
    main()

