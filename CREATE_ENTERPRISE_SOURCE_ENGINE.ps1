# ==========================================================
# CREATE_ENTERPRISE_SOURCE_ENGINE.ps1
# IOTEC
# ==========================================================

$destino = "C:\IOTEC\enterprise"

if (!(Test-Path $destino)) {
    New-Item -ItemType Directory -Path $destino -Force | Out-Null
}

$python = @'
# ==========================================================
# IOTEC ENTERPRISE SOURCE ENGINE
# ==========================================================

import requests

from WEBSITE_FINDER import search as find_website
from CONTACT_EXTRACTOR import extract


class EnterpriseSourceEngine:

    HEADERS = {
        "User-Agent":"IOTEC Enterprise"
    }

    @staticmethod
    def clean(company):

        remover = [

            "Brasil",
            "Ceará",
            "Fortaleza",
            "Região Nordeste",
            "Centro",
            "Pici",
            "Paupina"

        ]

        nome = company

        for item in remover:

            nome = nome.replace(item,"")

        return nome.split(",")[0].strip()

    @staticmethod
    def openstreetmap(company):

        try:

            r = requests.get(

                "https://nominatim.openstreetmap.org/search",

                params={

                    "q":EnterpriseSourceEngine.clean(company),

                    "format":"jsonv2",

                    "limit":1

                },

                headers=EnterpriseSourceEngine.HEADERS,

                timeout=20

            )

            if r.status_code != 200:

                return {}

            dados = r.json()

            if not dados:

                return {}

            d = dados[0]

            return {

                "display_name":d.get("display_name",""),

                "latitude":d.get("lat",""),

                "longitude":d.get("lon",""),

                "osm_class":d.get("class",""),

                "osm_type":d.get("type","")

            }

        except:

            return {}

'@

$arquivo = Join-Path $destino "source_engine.py"

Set-Content `
    -Path $arquivo `
    -Value $python `
    -Encoding UTF8

Write-Host ""
Write-Host "==============================================="
Write-Host " ENTERPRISE SOURCE ENGINE CRIADO"
Write-Host "==============================================="
Write-Host ""
Write-Host $arquivo
Write-Host ""