import os
import subprocess
from datetime import datetime

# 1. Gerar o HTML da Certidão Oficial
data_extenso = datetime.now().strftime("%d de %B de %Y")

html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <style>
        @page {{ size: A4; margin: 0; }}
        body {{ font-family: 'Georgia', serif; background: #fff; margin: 0; padding: 40px; color: #0f172a; }}
        .cert-container {{ border: 10px double #b45309; padding: 40px; position: relative; height: 900px; box-sizing: border-box; }}
        .watermark {{ position: absolute; top: 45%; left: 15%; transform: rotate(-30deg); font-size: 38pt; font-weight: bold; color: rgba(180, 83, 9, 0.05); text-transform: uppercase; letter-spacing: 4px; }}
        .header {{ text-align: center; border-bottom: 2px solid #b45309; padding-bottom: 15px; margin-bottom: 25px; }}
        .republica {{ font-size: 8pt; font-weight: bold; letter-spacing: 2px; color: #78350f; text-transform: uppercase; }}
        .company-title {{ font-size: 20pt; font-weight: bold; color: #0f172a; margin: 5px 0; }}
        .cnpj-tag {{ font-size: 9pt; color: #475569; font-family: monospace; }}
        .badge-level {{ display: inline-block; background: #78350f; color: #fef3c7; padding: 3px 12px; font-size: 8pt; font-weight: bold; margin-top: 8px; text-transform: uppercase; }}
        .cert-title {{ text-align: center; font-size: 14pt; font-weight: bold; margin: 25px 0; text-decoration: underline; }}
        .body-text {{ font-size: 11pt; line-height: 1.7; text-align: justify; text-indent: 25px; }}
        .data-card {{ background: #fffbeb; border: 1px solid #fde68a; border-left: 5px solid #b45309; padding: 15px; margin: 20px 0; font-family: monospace; font-size: 9.5pt; }}
        .security-footer {{ position: absolute; bottom: 40px; left: 40px; right: 40px; display: flex; justify-content: space-between; align-items: flex-end; border-top: 1px solid #cbd5e1; padding-top: 15px; }}
        .signature-box {{ text-align: center; }}
        .signature-line {{ width: 240px; border-top: 1px solid #0f172a; margin-bottom: 5px; }}
        .legal-notice {{ position: absolute; bottom: 15px; left: 40px; right: 40px; font-size: 7pt; color: #64748b; text-align: center; }}
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
        <div class="cert-title">CERTIDÃO DE AUTORIZAÇÃO E REGULARIDADE OPERACIONAL</div>
        <div class="body-text">
            <strong>CERTIFICAMOS</strong>, para os devidos fins de direito e comprovação institucional, que a empresa abaixo qualificada concluiu com êxito todas as etapas de verificação de segurança e encontra-se plenamente <strong>LICENCIADA E HOMOLOGADA</strong> pela infraestrutura tecnológica da IOTEC Enterprise.
        </div>
        <div class="data-card">
            <strong>RAZÃO SOCIAL:</strong> ATACADISTA & DISTRIBUIDORA B2B LTDA<br>
            <strong>CNPJ:</strong> 12.345.678/0001-90<br>
            <strong>STATUS DE HOMOLOGAÇÃO:</strong> CONCILIADO & INTEGRADO (PIX/ASAAS)<br>
            <strong>HASH DE SEGURANÇA:</strong> SHA256-89A02F99B12C78E411029384<br>
            <strong>CÓDIGO DE AUTENTICIDADE:</strong> IOTEC-2026-ENT-9941-X
        </div>
        <div class="body-text">
            A presente Certidão atesta a higidez fiscal e a integração com liquidação automatizada de recebíveis via Pix/Asaas, possuindo validade jurídica em todo o território nacional pelo prazo de 90 (noventa) dias.
        </div>
        <div class="security-footer">
            <div>
                <img src="https://api.qrserver.com/v1/create-qr-code/?size=80x80&data=https://deft-choux-097d84.netlify.app/validar?code=IOTEC-2026-ENT-9941-X" width="80" height="80">
            </div>
            <div class="signature-box">
                <div class="signature-line"></div>
                <div style="font-weight: bold; font-size: 9pt;">DEPARTAMENTO DE AUDITORIA E CONFORMIDADE</div>
                <div style="font-size: 8pt; color: #475569;">IOTEC Enterprise Global Core</div>
                <div style="font-size: 8pt; color: #78350f; font-weight: bold; margin-top: 3px;">Quixadá - CE, {data_extenso}</div>
            </div>
        </div>
        <div class="legal-notice">
            Documento emitido eletronicamente pela IOTEC Enterprise Systems (CNPJ 61.549.037/0001-68). Autenticidade verificável em https://deft-choux-097d84.netlify.app/ | Amparo legal: MP nº 2.200-2/2001.
        </div>
    </div>
</body>
</html>"""

html_path = r"C:\IOTEC\temp_certidao.html"
pdf_path = r"C:\IOTEC\Certidao_Oficial_Enterprise.pdf"

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

# 2. Localizar o navegador para conversão Headless em PDF
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

browser_bin = chrome_path if os.path.exists(chrome_path) else edge_path

if os.path.exists(browser_bin):
    cmd = [
        browser_bin,
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]
    subprocess.run(cmd, check=True)
    print(f"[OK] PDF Oficial gerado com sucesso em: {pdf_path}")
else:
    print("[ERRO] Navegador Chrome/Edge não encontrado para converter em PDF.")
