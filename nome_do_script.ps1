$arquivo = "C:\IOTEC\enterprise\source_engine.py"

if (!(Test-Path $arquivo)) {
    Write-Host "ERRO: Arquivo não encontrado."
    exit
}

Copy-Item $arquivo "$arquivo.bak_part2" -Force

$codigo = @'

    # =====================================================
    # ENRICH
    # =====================================================

    @staticmethod
    def enrich(company):

        resultado = {

            "company_name": company,

            "website": "",

            "email": "",

            "phone": "",

            "linkedin": "",

            "instagram": "",

            "facebook": "",

            "youtube": ""

        }

        osm = EnterpriseSourceEngine.openstreetmap(company)

        if osm:

            resultado.update(osm)

        try:

            website = find_website(company)

        except Exception:

            website = ""

        resultado["website"] = website

        if website:

            contatos = extract(website)

            emails = contatos.get("emails", [])

            phones = contatos.get("phones", [])

            if emails:

                resultado["email"] = emails[0]

            telefones = []

            foreach_phone = phones

            for p in foreach_phone:

                numero = "".join(c for c in p if c.isdigit())

                if len(numero) >= 10:

                    telefones.append(numero)

            if telefones:

                resultado["phone"] = telefones[0]

            resultado["linkedin"] = contatos.get("linkedin","")

            resultado["instagram"] = contatos.get("instagram","")

            resultado["facebook"] = contatos.get("facebook","")

            resultado["youtube"] = contatos.get("youtube","")

        return resultado


if __name__ == "__main__":

    empresa = "Makro Engenharia"

    print("="*70)
    print("IOTEC ENTERPRISE SOURCE ENGINE")
    print("="*70)
    print()

    dados = EnterpriseSourceEngine.enrich(empresa)

    for k,v in dados.items():

        print(f"{k:18}",v)

'@

Add-Content -Path $arquivo -Value $codigo -Encoding UTF8

Write-Host ""
Write-Host "========================================"
Write-Host " PARTE 2 ADICIONADA"
Write-Host "========================================"
Write-Host ""
Write-Host "Execute:"
Write-Host "python C:\IOTEC\enterprise\source_engine.py"