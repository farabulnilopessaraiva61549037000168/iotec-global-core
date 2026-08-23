# ==========================================================
# C:\IOTEC\CRM_ENRICHER.py
# ==========================================================

import sys
from pathlib import Path
from datetime import datetime

ROOT = Path(r"C:\IOTEC")
ENTERPRISE = ROOT / "enterprise"

if str(ENTERPRISE) not in sys.path:
    sys.path.insert(0, str(ENTERPRISE))

from enterprise_database import CRMDB
from SOURCE_ENGINE import SourceEngine
from CONTACT_EXTRACTOR import extract

crm = CRMDB.load()

print("=" * 70)
print("IOTEC CRM ENRICHER")
print("=" * 70)
print()

atualizados = 0

for empresa in crm:

    nome = empresa.get("company_name", "")

    print("-" * 60)
    print(nome)

    # =====================================================
    # DESCOBRE DADOS DA EMPRESA
    # =====================================================

    dados = SourceEngine.search(nome)

    website = dados.get("website", "")

    if website:

        print("Website encontrado")

        empresa["website"] = website

        contatos = extract(website)

        # ------------------------------------------
        # EMAIL
        # ------------------------------------------

        emails = contatos.get("emails", [])

        if emails:

            empresa["email"] = emails[0]

            print("Email:", emails[0])

        # ------------------------------------------
        # TELEFONE
        # ------------------------------------------

        telefones = []

        for t in contatos.get("phones", []):

            numero = "".join(filter(str.isdigit, t))

            if len(numero) >= 10:

                telefones.append(numero)

        if telefones:

            empresa["phone"] = telefones[0]

            print("Telefone:", telefones[0])

        # ------------------------------------------
        # REDES SOCIAIS
        # ------------------------------------------

        empresa["linkedin"] = contatos.get("linkedin", "")

        empresa["instagram"] = contatos.get("instagram", "")

        empresa["facebook"] = contatos.get("facebook", "")

        empresa["youtube"] = contatos.get("youtube", "")

        empresa["contact_status"] = "LOCALIZADO"

        empresa["updated_at"] = str(datetime.now())

        atualizados += 1

    else:

        empresa["contact_status"] = "SEM_WEBSITE"

        print("Website nÃƒÂ£o encontrado.")

print()

CRMDB.save(crm)

print("=" * 70)
print("RESUMO")
print("=" * 70)
print()

print("Empresas.............", len(crm))

print("Atualizadas..........", atualizados)

print()

print("CRM ENRIQUECIDO COM SUCESSO")

