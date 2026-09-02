# ==============================================================================
# IOTEC ENTERPRISE - GERADOR DE CERTIDÃO OFICIAL (NÍVEL ENTERPRISE)
# CNPJ: 61.549.037/0001-68
# ==============================================================================

import os
from datetime import datetime

def gerar_certidao_nivel_enterprise():
    data_extenso = datetime.now().strftime("%d de %B de %Y")
    
    html_template = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Certidão Oficial IOTEC Enterprise</title>
    <style>
        @page {{
            size: A4;
            margin: 0;
        }}
        body {{
            font-family: 'Georgia', 'Times New Roman', serif;
            background-color: #0f172a;
            padding: 30px;
            display: flex;
            justify-content: center;
        }}
        .cert-container {{
            background: #ffffff;
            width: 100%;
            max-width: 800px;
            padding: 50px;
            border: 12px double #b45309;
            box-shadow: 0 20px 50px rgba(0,0,0,0.5);
            position: relative;
            overflow: hidden;
        }}
        /* Marca d'Água Translucida */
        .watermark {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) rotate(-30deg);
            font-size: 42pt;
            font-weight: bold;
            color: rgba(180, 83, 9, 0.06);
            white-space: nowrap;
            pointer-events: none;
            letter-spacing: 4px;
            text-transform: uppercase;
        }}
        .header {{
            text-align: center;
            border-bottom: 2px solid #b45309;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }}
        .republica {{
            font-size: 9pt;
            font-weight: bold;
            letter-spacing: 2px;
            color: #78350f;
            text-transform: uppercase;
        }}
        .company-title {{
            font-size: 22pt;
            font-weight: bold;
            color: #0f172a;
            letter-spacing: 1.5px;
            margin: 5px 0;
        }}
        .cnpj-tag {{
            font-size: 9.5pt;
            color: #475569;
            font-family: monospace;
        }}
        .badge-level {{
            display: inline-block;
            background: #78350f;
            color: #fef3c7;
            padding: 4px 15px;
            border-radius: 3px;
            font-size: 8pt;
            font-weight: bold;
            letter-spacing: 1.5px;
            margin-top: 10px;
            text-transform: uppercase;
        }}
        .cert-title {{
            text-align: center;
            font-size: 15pt;
            font-weight: bold;
            color: #0f172a;
            margin: 30px 0 25px 0;
            text-decoration: underline;
            letter-spacing: 0.5px;
        }}
        .body-text {{
            font-size: 11.5pt;
            line-height: 1.8;
            color: #1e293b;
            text-align: justify;
            text-indent: 30px;
        }}
        .data-card {{
            background: #fffbeb;
            border: 1px solid #fde68a;
            border-left: 5px solid #b45309;
            padding: 20px;
            margin: 25px 0;
            font-family: monospace;
            font-size: 10pt;
            color: #451a03;
        }}
        .data-row {{
            margin-bottom: 6px;
        }}
        .security-footer {{
            margin-top: 40px;
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            border-top: 1px solid #cbd5e1;
            padding-top: 20px;
        }}
        .qr-placeholder {{
            width: 90px;
            height: 90px;
            border: 2px solid #b45309;
            padding: 4px;
            background: #fff;
            text-align: center;
        }}
        .signature-box {{
            text-align: center;
        }}
        .signature-line {{
            width: 260px;
            border-top: 1px solid #0f172a;
            margin-bottom: 5px;
        }}
        .legal-notice {{
            font-size: 7.5pt;
            color: #64748b;
            text-align: center;
            margin-top: 25px;
        }}
    </style>
</head>
<body>
    <div class="cert-container">
        <div class="watermark">IOTEC ENTERPRISE SEAL</div>

        <div class="header">
            <div class="republica">República Federativa do Brasil — Governança Digital</div>
            <div class="company-title">IOTEC ENTERPRISE SYSTEMS</div>
            <div class="cnpj-tag">CNPJ REGISTRADO: 61.549.037/0001-68</div>
            <div class="badge-level">Nível 4: Licenciamento & Outorga Enterprise</div>
        </div>

        <div class="cert-title">
            CERTIDÃO DE AUTORIZAÇÃO E REGULARIDADE OPERACIONAL
        </div>

        <div class="body-text">
            <strong>CERTIFICAMOS</strong>, para os devidos fins de direito, comprovação institucional e livre circulação de negócios junto a órgãos públicos e privados, que a empresa abaixo qualificada concluiu com êxito todas as etapas de verificação de segurança e encontra-se plenamente <strong>LICENCIADA E HOMOLOGADA</strong> pela infraestrutura tecnológica da IOTEC Enterprise.
        </div>

        <div class="data-card">
            <div class="data-row"><strong>RAZÃO SOCIAL:</strong> ATACADISTA & DISTRIBUIDORA B2B LTDA</div>
            <div class="data-row"><strong>CNPJ:</strong> 12.345.678/0001-90</div>
            <div class="data-row"><strong>STATUS DE HOMOLOGAÇÃO:</strong> CONCILIADO & INTEGRADO (PIX/ASAAS)</div>
            <div class="data-row"><strong>HASH DE SEGURANÇA:</strong> SHA256-89A02F99B12C78E411029384</div>
            <div class="data-row"><strong>CÓDIGO DE AUTENTICIDADE:</strong> IOTEC-2026-ENT-9941-X</div>
        </div>

        <div class="body-text">
            A presente Certidão atesta a higidez fiscal e a integração com liquidação automática de recebíveis via Pix/Asaas, possuindo validade jurídica em todo o território nacional pelo prazo de 90 (noventa) dias a contar de sua emissão.
        </div>

        <div class="security-footer">
            <div class="qr-placeholder">
                <img src="https://api.qrserver.com/v1/create-qr-code/?size=85x85&data=https://deft-choux-097d84.netlify.app/validar?code=IOTEC-2026-ENT-9941-X" alt="QR Code" width="85" height="85">
            </div>

            <div class="signature-box">
                <div class="signature-line"></div>
                <div style="font-weight: bold; font-size: 9.5pt; color: #0f172a;">DEPARTAMENTO DE AUDITORIA E CONFORMIDADE</div>
                <div style="font-size: 8pt; color: #475569;">IOTEC Enterprise Global Core</div>
                <div style="font-size: 8.5pt; color: #78350f; font-weight: bold; margin-top: 4px;">Quixadá - CE, {data_extenso}</div>
            </div>
        </div>

        <div class="legal-notice">
            Documento emitido eletronicamente pela IOTEC Enterprise Systems (CNPJ 61.549.037/0001-68). Sua autenticidade pode ser confirmada via QR Code ou no portal https://deft-choux-097d84.netlify.app/ . Amparo legal: MP nº 2.200-2/2001.
        </div>
    </div>
</body>
</html>"""

    output_html = r"C:\IOTEC\Certidao_Oficial_Enterprise.html"
    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html_template)

    print(f"[OK] Certidão Nível Enterprise gerada em: {output_html}")

if __name__ == "__main__":
    gerar_certidao_nivel_enterprise()
