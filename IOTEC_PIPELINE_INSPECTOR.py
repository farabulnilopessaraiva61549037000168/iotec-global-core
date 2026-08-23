import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json

ARQUIVO = "IOTEC_PIPELINE_DATABASE.json"

with open(
    ARQUIVO,
    "r",
    encoding="utf-8"
) as f:

    dados = json.load(f)

print("")
print("===================================")
print("IOTEC PIPELINE INSPECTOR")
print("===================================")

for lead in dados["leads"]:
    pass

    print("")
    print("-----------------------------------")
    print(lead["id"])
    print("-----------------------------------")

    propostas = [

        p for p in dados["propostas"]

        if p.get("lead_id")
        ==
        lead["id"]
    ]

    if not propostas:
        pass

        print("SEM PROPOSTA")
        continue

    for proposta in propostas:
        pass

        print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
        print(proposta["id"])

        contratos = [

            c for c in dados["contratos"]

            if c.get("proposta_id")
            ==
            proposta["id"]
        ]

        if not contratos:
            pass

            print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
            print("SEM CONTRATO")
            continue

        for contrato in contratos:
            pass

            print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
            print(contrato["id"])

            receitas = [

                r for r in dados["receita"]

                if r.get("contrato_id")
                ==
                contrato["id"]
            ]

            if not receitas:
                pass

                print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
                print("SEM RECEITA")
                continue

            for receita in receitas:
                pass

                print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
                print(receita["id"])

print("")
print("INSPECAO FINALIZADA")




