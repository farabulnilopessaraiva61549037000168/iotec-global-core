$port = 8270
$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://localhost:$port/")

try {
    $listener.Start()
    Write-Host "`n=================================================================" -ForegroundColor Cyan
    Write-Host "     AGENTE INSTALADOR DE MÍDIAS IOTEC — CAFÉ COM ECONOMIA ATIVO ($port)" -ForegroundColor Green
    Write-Host "     Acesse a interface de luxo: http://localhost:$port/" -ForegroundColor Yellow
    Write-Host "=================================================================`n" -ForegroundColor Cyan
} catch {
    Write-Host "[ERRO] Porta $port ocupada ou indisponível." -ForegroundColor Red
    exit
}

while ($listener.IsListening) {
    $context = $listener.GetContext()
    $response = $context.Response

    $html = @"
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IOTEC — Café com Economia & Injeção de Mídia</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Plus+Jakarta+Sans:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body { background:#000; color:#FFF; font-family:'Plus Jakarta Sans',sans-serif; min-height:100vh; overflow-x:hidden; }

        /* CAMADA 1: VÍDEO ATMOSFÉRICO DE FUNDO INJETADO PELO AGENTE */
        .video-bg {
            position: fixed; top: 50%; left: 50%; min-width: 100%; min-height: 100%;
            z-index: -2; transform: translate(-50%, -50%);
            filter: grayscale(100%) contrast(125%) brightness(25%); object-fit: cover;
        }
        .overlay { position: fixed; top:0; left:0; width:100%; height:100%; background: rgba(5,5,8,0.85); z-index: -1; }

        .container { max-width: 1150px; margin: 0 auto; padding: 50px 20px; }

        .header-brand { text-align: center; margin-bottom: 40px; }
        .brand-title { font-family: 'Cinzel', serif; font-size: 34px; color: #E8D8C8; letter-spacing: 6px; }
        .brand-sub { font-size: 11px; color: #D4B886; letter-spacing: 3px; font-weight: 600; text-transform: uppercase; margin-top: 4px; }

        /* CAMADA 2: ESTRUTURA DE TRES CAMADAS VISUAIS EM VIDRO FOSCO */
        .grid-3-camadas { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-bottom: 40px; }
        
        .camada-card {
            background: rgba(15, 15, 20, 0.7);
            border: 1px solid rgba(232, 216, 200, 0.2);
            border-radius: 16px; padding: 25px;
            backdrop-filter: blur(15px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.8);
        }

        .camada-badge { font-family: 'Cinzel', serif; font-size: 10px; color: #D4B886; font-weight: 700; letter-spacing: 1px; margin-bottom: 8px; }
        .camada-title { font-size: 16px; font-weight: 700; color: #FFF; margin-bottom: 12px; }
        .camada-desc { font-size: 11.5px; color: #A1A1AA; line-height: 1.6; }

        /* CAMADA 3: PLANILHAS E GRÁFICOS INFORMATIVOS AUDITADOS */
        .panel-data {
            background: rgba(10, 10, 14, 0.85);
            border: 1px solid rgba(255,255,255,0.12);
            border-radius: 16px; padding: 30px 30px 50px 30px;
            margin-bottom: 40px;
        }

        .panel-header { font-family: 'Cinzel', serif; font-size: 18px; color: #E8D8C8; margin-bottom: 20px; display:flex; justify-content:space-between; align-items:center; }
        
        table { width: 100%; border-collapse: collapse; text-align: left; font-size: 12px; }
        th { background: rgba(232, 216, 200, 0.1); color: #D4B886; padding: 12px; font-weight: 600; text-transform: uppercase; font-size: 10px; letter-spacing: 1px; }
        td { padding: 14px 12px; border-bottom: 1px solid rgba(255,255,255,0.05); color: #E4E4E7; }
        .status-active { color: #10B981; font-weight: 700; }

        footer { text-align: center; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 25px; font-size: 11px; color: #71717A; line-height: 1.8; }
    </style>
</head>
<body>

    <video class="video-bg" autoplay loop muted playsinline>
        <source src="https://assets.mixkit.co/videos/preview/mixkit-abstract-fast-lines-of-light-31742-large.mp4" type="video/mp4">
    </video>
    <div class="overlay"></div>

    <div class="container">
        <div class="header-brand">
            <div class="brand-title">CAFÉ COM ECONOMIA</div>
            <div class="brand-sub">Programa Planejado por Software — IOTEC Enterprise</div>
        </div>

        <div class="grid-3-camadas">
            <div class="camada-card">
                <div class="camada-badge">CAMADA 01 — ATMOSFERA</div>
                <div class="camada-title">Instalador de Mídia Ativo</div>
                <div class="camada-desc">Injeção em tempo real de fundos P&B, vídeos institucionais em loop e fotografia de alto contraste.</div>
            </div>

            <div class="camada-card">
                <div class="camada-badge">CAMADA 02 — PROGRAMAÇÃO</div>
                <div class="camada-title">Mapeamento de Setores</div>
                <div class="camada-desc">Distribuição elegante das atrações internas: Gastronomia, Estética, Eventos e Cotas Orbitais.</div>
            </div>

            <div class="camada-card">
                <div class="camada-badge">CAMADA 03 — MÉTRICAS</div>
                <div class="camada-title">Gráficos & Planilhas</div>
                <div class="camada-desc">Exibição transparente do fluxo de faturamento, liquidação de ativos e travas de segurança.</div>
            </div>
        </div>

        <div class="panel-data">
            <div class="panel-header">
                <span>📊 PLANILHA INFORMATIVA DE OPERAÇÕES AUDITADAS</span>
                <span style="font-size:11px; color:#10B981;">● AGENTE INSTALADOR EM EXECUÇÃO</span>
            </div>

            <table>
                <thead>
                    <tr>
                        <th>Setor / Módulo</th>
                        <th>Atração / Recurso Visado</th>
                        <th>Nível de Capricho</th>
                        <th>Valoração Estimada</th>
                        <th>Status do Aplicador</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Café com Economia</strong></td>
                        <td>Apresentação Executiva de Cotas SAFE</td>
                        <td>Nível 4 — Ultra-Luxo</td>
                        <td>R$ 15.000,00</td>
                        <td><span class="status-active">INSTALADO</span></td>
                    </tr>
                    <tr>
                        <td><strong>Bronze da Lu — Estética</strong></td>
                        <td>Fundo P&B + Tabela de Sinal Agendado</td>
                        <td>Nível 2 — Corporativo</td>
                        <td>R$ 800,00</td>
                        <td><span class="status-active">INSTALADO</span></td>
                    </tr>
                    <tr>
                        <td><strong>Torre de Comando (War Room)</strong></td>
                        <td>Gráficos Telemétricos em Tempo Real</td>
                        <td>Nível 3 — Luxo Executivo</td>
                        <td>R$ 4.500,00</td>
                        <td><span class="status-active">INSTALADO</span></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <footer>
            <strong>IOTEC Enterprise Software & Financial Systems</strong><br>
            CNPJ: 61.549.037/0001-68 | Governança: Farabulini Lopes Saraiva (Bruno)<br>
            Contato Executivo: IOTEC.BL@proton.me | © 2026 IOTEC Global.
        </footer>
    </div>

</body>
</html>
"@

    $buffer = [System.Text.Encoding]::UTF8.GetBytes($html)
    $response.ContentLength64 = $buffer.Length
    $response.ContentType = "text/html; charset=utf-8"
    $response.OutputStream.Write($buffer, 0, $buffer.Length)
    $response.OutputStream.Close()
}

