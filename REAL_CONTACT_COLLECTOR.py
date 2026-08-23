# ==========================================================
# C:\IOTEC\REAL_CONTACT_COLLECTOR.py
# IOTEC REAL CONTACT COLLECTOR v1
# ==========================================================

import sys
import json
import time
import requests

from pathlib import Path
from datetime import datetime

ROOT = Path(r"C:\IOTEC")
ENTERPRISE = ROOT / "enterprise"

if str(ENTERPRISE) not in sys.path:
    sys.path.insert(0, str(ENTERPRISE))

from enterprise_database import CRMDB

HEADERS = {

    "User-Agent":
    "IOTEC Contact Discovery Engine 1.0"

}

crm = CRMDB.load()

print("="*70)
print("IOTEC REAL CONTACT COLLECTOR")
print("="*70)
print()

atualizados = 0

# ---------------------------------------------------------

def pesquisar_empresa(nome):

    url = "https://nominatim.openstreetmap.org/search"

    params = {

        "q": nome,

        "format": "jsonv2",

        "limit": 1,

        "addressdetails": 1

    }

    try:

        r = requests.get(

            url,

            params=params,

            headers=HEADERS,

            timeout=30

        )

        if r.status_code != 200:

            return None

        dados = r.json()

        if not dados:

            return None

        return dados[0]

    except:

        return None

# ---------------------------------------------------------

for empresa in crm:

    if empresa.get("website") not in ("", "PENDENTE", None):

        continue

    nome = empresa["company_name"]

    print("--------------------------------------------")
    print(nome)

    resultado = pesquisar_empresa(nome)

    if resultado is None:

        print("Sem resultado.")

        continue

    empresa["osm_display_name"] = resultado.get(

        "display_name",

        ""

    )

    empresa["latitude"] = resultado.get(

        "lat",

        ""

    )

    empresa["longitude"] = resultado.get(

        "lon",

        ""

    )

    empresa["osm_type"] = resultado.get(

        "type",

        ""

    )

    empresa["osm_class"] = resultado.get(

        "class",

        ""

    )

    empresa["contact_status"] = "LOCALIZADO"

    empresa["updated_at"] = str(datetime.now())

    atualizados += 1

    print("Localizado.")

    time.sleep(1)

CRMDB.save(crm)

print()
print("="*70)
print("RESUMO")
print("="*70)
print()

print("Empresas........",len(crm))
print("Atualizadas.....",atualizados)

print()

print("COLETA FINALIZADA.")

