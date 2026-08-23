from xhtml2pdf import pisa

html_content = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Plano de Ativação Comercial e Go-Live IoTec</title>
    <style>
        @page { size: a4 portrait; margin: 1.5cm; }
        body { font-family: Helvetica, Arial, sans-serif; color: #1e293b; font-size: 10pt; line-height: 1.4; }
        .header { border-bottom: 2px solid #0284c7; padding-bottom: 10px; margin-bottom: 15px; }
        .header h1 { color: #0284c7; font-size: 18pt; margin: 0 0 5px 0; text-transform: uppercase; }
        .header .subtitle { color: #64748b; font-size: 10pt; font-weight: bold; }
        .badge { background-color: #0284c7; color: #ffffff; padding: 4px 8px; font-size: 8pt; font-weight: bold; margin-top: 6px; display: inline-block; }
        h2 { color: #0f172a; font-size: 12pt; border-left: 4px solid #0284c7; padding-left: 8px; margin-top: 18px; margin-bottom: 10px; }
        p { margin: 0 0 8px 0; color: #334155; }
        table { width: 100%; border-collapse: collapse; margin: 12px 0; }
        th { background-color: #0f172a; color: #38bdf8; text-align: left; padding: 6px 8px; font-size: 9pt; }
        td { padding: 7px 8px; border-bottom: 1px solid #cbd5e1; color: #334155; font-size: 9pt; }
        .callout { background-color: #f1f5f9; border-left: 4px solid #10b981; padding: 10px 12px; margin: 14px 0; }
        .callout-title { color: #059669; font-weight: bold; font-size: 10pt; margin-bottom: 3px; }
        .step-item { background-color: #f8fafc; border: 1px solid #e2e8f0; padding: 8px 10px; margin-bottom: 6px; }
        .step-number { color: #0284c7; font-weight: bold; }
        .footer { margin-top: 25px; border-top: 1px solid #cbd5e1; padding-top: 8px; font-size: 8pt; color: #94a3b8; text-align: center; }
    </style>
</head>
<body>

    <div class="header">
        <h1>Plano de Abertura &amp; Go-Live Comercial</h1>
        <div class="subtitle">Plataforma IoTec — Módulo de Operação Autônoma via IA</div>
        <div class="badge">Status: Autorizado para Ativação</div>
    </div>

    <p>Este documento estabelece o protocolo de entrada em produção para a plataforma <strong>IoTec</strong>. Com a arquitetura de negócios totalmente mapeada e as regras operacionais integradas à Inteligência Artificial, o sistema inicia a fase de <strong>Monetização Direta</strong>.</p>

    <div class="callout">
        <div class="callout-title">Diretriz Operacional Pronta</div>
        A IA atuará como operadora autônoma de fluxo contínuo. A intervenção humana fica restrita à auditoria financeira de alto nível e calibração de parâmetros em tempo real.
    </div>

    <h2>1. Matriz de Ativação dos Módulos Principais</h2>
    <table>
        <thead>
            <tr>
                <th>Módulo do Sistema</th>
                <th>Função na Monetização</th>
                <th>Ação Imediata de Go-Live</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>015_PAYMENT_GATEWAY_ENGINE</strong></td>
                <td>Processamento central de pagamentos e liquidação.</td>
                <td>Virar chaves de Sandbox para Produção.</td>
            </tr>
            <tr>
                <td><strong>099H_PAYPAL_PIX_GATEWAY</strong></td>
                <td>Emissão de Pix instantâneo e suporte PayPal.</td>
                <td>Validar webhooks de confirmação imediata.</td>
            </tr>
            <tr>
                <td><strong>015_AUDIT_ENGINE</strong></td>
                <td>Auditoria e conciliação em tempo real.</td>
                <td>Ativar logs de segurança e prevenção de vazamento.</td>
            </tr>
            <tr>
                <td><strong>ENTERPRISE_WEB_CORE</strong></td>
                <td>Interface de captação e checkout dos clientes.</td>
                <td>Liberar domínio comercial e rotas de venda.</td>
            </tr>
        </tbody>
    </table>

    <h2>2. Roteiro Prático de Execução (Próximas Horas)</h2>
    <div class="step-item">
        <span class="step-number">Passo 01:</span> <strong>Virada de Chaves de API</strong>
        <p>Inserção dos tokens e segredos reais dos provedores bancários e gateways diretamente nas variáveis de ambiente da IA.</p>
    </div>
    <div class="step-item">
        <span class="step-number">Passo 02:</span> <strong>Injeção da Carga Inicial de Teste Sintético</strong>
        <p>Execução de 1 transação real de baixo valor (R$ 1,00) via Pix para homologação ponta a ponta do fluxo de notificação.</p>
    </div>
    <div class="step-item">
        <span class="step-number">Passo 03:</span> <strong>Abertura Comercial para Beta Pago</strong>
        <p>Liberação de acesso para o primeiro grupo de clientes selecionados/primeira esteira de venda ativa.</p>
    </div>
    <div class="step-item">
        <span class="step-number">Passo 04:</span> <strong>Monitoramento de Consistência e Ajustes</strong>
        <p>Calibração dos tempos de resposta da IA e confirmações de recebimento pelo motor de auditoria.</p>
    </div>

    <h2>3. Visão de Escala Financeira</h2>
    <p>Com o sistema rodando de forma autônoma, cada transação processada retroalimenta o motor de inteligência e valida a tese comercial da IoTec.</p>

    <div class="footer">
        IoTec Business &amp; Technology Platform — Documento Gerado para Ativação de Produção
    </div>

</body>
</html>
"""

pdf_path = "Plano_de_Ativacao_IoTec.pdf"

with open(pdf_path, "wb") as pdf_file:
    pisa_status = pisa.CreatePDF(html_content, dest=pdf_file)

if not pisa_status.err:
    print(f"PDF gerado com sucesso em: {pdf_path}")
else:
    print("Ocorreu um erro ao gerar o PDF.")
