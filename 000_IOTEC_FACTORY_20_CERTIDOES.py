# ==============================================================================
# IOTEC ENTERPRISE - FABRICA AUTOMÁTICA DE 20 CERTIDÕES OFICIAIS
# CNPJ: 61.549.037/0001-68
# ==============================================================================

import os
import subprocess
from datetime import datetime

# Dicionário dos 20 Tipos de Certidões e Suas Identidades Visuais
TIPOS_CERTIDOES = {
    1: {"titulo": "CERTIDÃO NEGATIVA DE INADIMPLÊNCIA B2B", "cor": "#064e3b", "nivel": "Nível 1: Regularidade Financeira", "watermark": "FINANCIAL CLEARANCE"},
    2: {"titulo": "CERTIDÃO DE HOMOLOGAÇÃO DE CONCILIAÇÃO PIX", "cor": "#0284c7", "nivel": "Nível 2: Integração Tecnológica", "watermark": "PIX CONCILIATED"},
    3: {"titulo": "CERTIDÃO DE AUDITORIA DE BALANÇO E RECURSOS", "cor": "#9f1239", "nivel": "Nível 3: Governança & Compliance", "watermark": "AUDITED & CONFIDENTIAL"},
    4: {"titulo": "CERTIDÃO DE LICENCIAMENTO & OUTORGA ENTERPRISE", "cor": "#b45309", "nivel": "Nível 4: Outorga Global", "watermark": "ENTERPRISE SEAL"},
    5: {"titulo": "CERTIDÃO DE ISENÇÃO DE GARGALOS OPERACIONAIS", "cor": "#0f172a", "nivel": "Nível 1: Eficiência Operacional", "watermark": "OPERATIONAL VERIFIED"},
    6: {"titulo": "CERTIDÃO DE QUITAÇÃO DE RECORRÊNCIA MENSAL", "cor": "#059669", "nivel": "Nível 2: Adimplência Recorrente", "watermark": "RECURRENCE CLEARANCE"},
    7: {"titulo": "CERTIDÃO DE REGULARIDADE CADASTRAL B2B", "cor": "#0284c7", "nivel": "Nível 1: Cadastro Unificado", "watermark": "CADASTRO AUDITADO"},
    8: {"titulo": "CERTIDÃO DE CAPACIDADE TÉCNICA EM AUTOMAÇÃO", "cor": "#b45309", "nivel": "Nível 4: Capacidade Técnica", "watermark": "TECHNICAL CAPACITY"},
    9: {"titulo": "CERTIDÃO DE HIGIDEZ BANCÁRIA E LIQUIDEZ", "cor": "#064e3b", "nivel": "Nível 3: Liquidez Garantida", "watermark": "BANKING CLEARANCE"},
    10: {"titulo": "CERTIDÃO DE CONFORMIDADE LGPD E SIGILO DADOS", "cor": "#9f1239", "nivel": "Nível 3: Conformidade LGPD", "watermark": "DATA PROTECTION"},
    11: {"titulo": "CERTIDÃO DE VALIDAÇÃO DE CONTRATO SOCIAL", "cor": "#0f172a", "nivel": "Nível 1: Validação Jurídica", "watermark": "JURIDICAL VERIFIED"},
    12: {"titulo": "CERTIDÃO DE ADESÃO AO ECOSSISTEMA IOTEC", "cor": "#b45309", "nivel": "Nível 4: Filiação Global", "watermark": "ECOSYSTEM MEMBER"},
    13: {"titulo": "CERTIDÃO DE AUTENTICIDADE DE NOTAS E EMISSÕES", "cor": "#059669", "nivel": "Nível 2: Emissão Fiscal", "watermark": "FISCAL CLEARANCE"},
    14: {"titulo": "CERTIDÃO DE ISENÇÃO DE RETENÇÃO BANCÁRIA", "cor": "#064e3b", "nivel": "Nível 2: Isenção de Trava", "watermark": "UNLOCKED FUNDS"},
    15: {"titulo": "CERTIDÃO DE CONFRONTAÇÃO DE PAGAMENTOS ASAAS", "cor": "#0284c7", "nivel": "Nível 2: Gateway Auditado", "watermark": "GATEWAY AUDITED"},
    16: {"titulo": "CERTIDÃO DE RESTRUTAÇÃO DE DÍVIDAS B2B", "cor": "#9f1239", "nivel": "Nível 3: Acordo Homologado", "watermark": "RESTRUCTURED DEBT"},
    17: {"titulo": "CERTIDÃO DE PONTUALIDADE EM FATURAMENTO", "cor": "#059669", "nivel": "Nível 1: Pontualidade Gold", "watermark": "PUNCTUALITY SEAL"},
    18: {"titulo": "CERTIDÃO DE CONTRATAÇÃO DE LICENÇA ANUAL", "cor": "#b45309", "nivel": "Nível 4: Contrato Anual", "watermark": "ANNUAL CONTRACT"},
    19: {"titulo": "CERTIDÃO DE ATIVIDADE COMERCIAL VERIFICADA", "cor": "#0f172a", "nivel": "Nível 1: Status Ativo", "watermark": "ACTIVE STATUS"},
    20: {"titulo": "CERTIDÃO SUPREMA DE QUITAÇÃO E INTEGRALIZAÇÃO", "cor": "#b45309", "nivel": "Nível 4: Quitação Suprema", "watermark": "SUPREME CLEARANCE"}
}

def obter_data_pt_br():
    meses = {
        1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
        5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
        9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }
    hoje = datetime.now()
    return f"{hoje.day} de {meses[hoje.month]} de {hoje.year}"

def emitir_certidao_oficial(tipo_id, nome_solicitante, doc_solicitante, codigo_hash="IOTEC-2026-X89"):
    cert_info = TIPOS_CERTIDOES.get(tipo_id, TIPOS_CERTIDOES[1])
    data_extenso = obter_data_pt_br()
    
    html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <style>
        @page {{ size: A4; margin: 0; }}
        body {{ font-family: 'Georgia', serif; background: #fff; margin: 0; padding: 40px; color: #0f172a; }}
        .cert-container {{ border: 10px double {cert_info['cor']}; padding: 40px; position: relative; height: 920px; box-sizing: border-box; }}
        .watermark {{ position: absolute; top: 45%; left: 10%; right: 10%; text-align: center; transform: rotate(-30deg); font-size: 34pt; font-weight: bold; color: rgba(15, 23, 42, 0.04); text-transform: uppercase; letter-spacing: 4px; pointer-events: none; }}
        .header {{ text-align: center; border-bottom: 2px solid {cert_info['cor']}; padding-bottom: 12px; margin-bottom: 20px; }}
        .republica {{ font-size: 8pt; font-weight: bold; letter-spacing: 2px; color: #475569; text-transform: uppercase; }}
        .company-title {{ font-size: 20pt; font-weight: bold; color: #0f172a; margin: 4px 0 2px 0; }}
        .cnpj-tag {{ font-size: 8.5pt; color: #475569; font-family: monospace; margin-bottom: 8px; }}
        .badge-level {{ display: inline-block; background: {cert_info['cor']}; color: #ffffff; padding: 3px 14px; font-size: 7.5pt; font-weight: bold; text-transform: uppercase; border-radius: 2px; }}
        .cert-title {{ text-align: center; font-size: 13.5pt; font-weight: bold; margin: 25px 0 20px 0; text-decoration: underline; color: #0f172a; }}
        .body-text {{ font-size: 11pt; line-height: 1.75; text-align: justify; text-indent: 30px; color: #1e293b; }}
        .data-card {{ background: #f8fafc; border: 1px solid #e2e8f0; border-left: 5px solid {cert_info['cor']}; padding: 16px; margin: 20px 0; font-family: monospace; font-size: 9.5pt; }}
        .security-footer {{ position: absolute; bottom: 40px; left: 40px; right: 40px; display: flex; justify-content: space-between; align-items: flex-end; border-top: 1px solid #cbd5e1; padding-top: 15px; }}
        .signature-box {{ text-align: center; }}
        .signature-line {{ width: 250px; border-top: 1px solid #0f172a; margin-bottom: 4px; }}
        .legal-notice {{ position: absolute; bottom: 15px; left: 40px; right: 40px; font-size: 7pt; color: #64748b; text-align: center; }}
    </style>
</head>
<body>
    <div class="cert-container">
        <div class="watermark">{cert_info['watermark']}</div>
        <div class="header">
            <div class="republica">República Federativa do Brasil — Governança Digital</div>
            <div class="company-title">IOTEC ENTERPRISE SYSTEMS</div>
            <div class="cnpj-tag">CNPJ REGISTRADO: 61.549.037/0001-68</div>
            <div class="badge-level">{cert_info['nivel']}</div>
        </div>
        
        <div class="cert-title">{cert_info['titulo']}</div>
        
        <div class="body-text">
            <strong>CERTIFICAMOS</strong>, para os devidos fins de direito, fé pública e comprovação institucional junto a órgãos competentes, que a entidade/solicitante abaixo especificado cumpriu rigorosamente todos os requisitos formais e encontra-se devidamente registrado e homologado na infraestrutura da IOTEC Enterprise.
        </div>
        
        <div class="data-card">
            <strong>NOME DO SOLICITANTE / RAZÃO SOCIAL:</strong> {nome_solicitante.upper()}<br>
            <strong>CPF / CNPJ DO TITULAR:</strong> {doc_solicitante}<br>
            <strong>STATUS DA CERTIDÃO:</strong> REGULAR E AUTÊNTICO<br>
            <strong>HASH DE SEGURANÇA:</strong> SHA256-IOTEC-{codigo_hash}<br>
            <strong>CÓDIGO DE VALIDAÇÃO:</strong> {codigo_hash}
        </div>
        
        <div class="body-text">
            A presente Certidão atesta a veracidade das informações prestadas e possui eficácia jurídica plena em todo o território nacional pelo prazo de 90 (noventa) dias a contar da data de sua emissão.
        </div>
        
        <div class="security-footer">
            <div>
                <img src="https://api.qrserver.com/v1/create-qr-code/?size=80x80&data=https://deft-choux-097d84.netlify.app/validar?code={codigo_hash}" width="80" height="80">
            </div>
            <div class="signature-box">
                <div class="signature-line"></div>
                <div style="font-weight: bold; font-size: 8.5pt;">DEPARTAMENTO DE AUDITORIA E CONFORMIDADE</div>
                <div style="font-size: 7.5pt; color: #475569;">IOTEC Enterprise Global Core</div>
                <div style="font-size: 8pt; color: {cert_info['cor']}; font-weight: bold; margin-top: 3px;">Quixadá - CE, {data_extenso}</div>
            </div>
        </div>
        
        <div class="legal-notice">
            Documento emitido eletronicamente pela IOTEC Enterprise Systems (CNPJ 61.549.037/0001-68). Autenticidade verificável via QR Code ou no portal https://deft-choux-097d84.netlify.app/ | Amparo legal: MP nº 2.200-2/2001.
        </div>
    </div>
</body>
</html>"""

    temp_html = r"C:\IOTEC\temp_factory.html"
    nome_sanitizado = "".join(x for x in nome_solicitante if x.isalnum() or x in " _-").strip().replace(" ", "_")
    output_pdf = f"C:\\IOTEC\\Certidao_Modelo_{tipo_id}_{nome_sanitizado}.pdf"

    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html_content)

    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    browser_bin = chrome_path if os.path.exists(chrome_path) else edge_path

    if os.path.exists(browser_bin):
        cmd = [browser_bin, "--headless", "--disable-gpu", f"--print-to-pdf={output_pdf}", temp_html]
        subprocess.run(cmd, check=True)
        print(f"[OK] Certidão Tipo #{tipo_id} gerada para {nome_solicitante} em: {output_pdf}")
        return output_pdf
    else:
        print("[ERRO] Navegador Chrome/Edge não localizado.")
        return None

if __name__ == "__main__":
    # Teste de emissão do Modelo #1 (Certidão Negativa) para um solicitante
    emitir_certidao_oficial(
        tipo_id=1, 
        nome_solicitante="Atacadista & Distribuidora B2B LTDA", 
        doc_solicitante="12.345.678/0001-90",
        codigo_hash="IOTEC-2026-NEG-8821-X"
    )
