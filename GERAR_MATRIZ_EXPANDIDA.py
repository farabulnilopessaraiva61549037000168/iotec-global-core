import os

html_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>IOTEC - Matriz Mestre de Inteligência Setorial Expandida</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #0b0f19; color: #e2e8f0; padding: 20px; }
        h1 { color: #60a5fa; border-bottom: 2px solid #3b82f6; padding-bottom: 10px; }
        h2 { color: #38bdf8; margin-top: 20px; }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        th, td { border: 1px solid #1e293b; padding: 10px; text-align: left; }
        th { background-color: #1e293b; color: #38bdf8; }
        tr:nth-child(even) { background-color: #111827; }
        .highlight { color: #4ade80; font-weight: bold; }
    </style>
</head>
<body>
    <h1>IOTEC GLOBAL CORE | SECTOR INTELLIGENCE DESK (+350%)</h1>
    <p><strong>CNPJ PJ:</strong> 61.549.037/0001-68 | <strong>Projeto REGULUS</strong></p>
    
    <h2>1. Matriz Ampliada de Setores Econômicos & Beneficiamento</h2>
    <table>
        <thead>
            <tr>
                <th>Setor Econômico</th>
                <th>Mapeamento Setorial Potencializado</th>
                <th>Mecanismo de Conversão IOTEC</th>
                <th>Ganhos de Escala</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Agro, Cadeias Proteicas & Alimentos</strong></td>
                <td>Soja, Milho, Trigo, Café, Frutas, Laticínios, Ovinos, Caprinos, Suínos, Avicultura, Piscicultura</td>
                <td>Automação de recebíveis de cooperativas e conciliação de insumos agrícolas via Asaas.</td>
                <td><span class="highlight">+350% de Densidade</span></td>
            </tr>
            <tr>
                <td><strong>Energia, Mineração & BRICS</strong></td>
                <td>Petróleo, Gás, Terras Raras, Usinas, Energias Limpas, Mineração & Trade Global</td>
                <td>Hub de liquidação financeira e câmbio internacional (USD/EUR) via Remessa Online.</td>
                <td><span class="highlight">Liquidação Transfronteiriça</span></td>
            </tr>
            <tr>
                <td><strong>Engenharia, Saúde & Biotecnologia</strong></td>
                <td>Prototipagem, Modelagem, Bioengenharia, Biomedicina, Arquitetura, Elétrica e Construção Civil</td>
                <td>Licenciamento de software SaaS com cobrança recorrente e gestão de direitos digitais.</td>
                <td><span class="highlight">Contratos High-Ticket</span></td>
            </tr>
            <tr>
                <td><strong>Logística, Varejo & Serviços</strong></td>
                <td>Atacado, Compras Online, Moda, Turismo, Pesca, Educação, Marketing, Gestão Pública</td>
                <td>Cobrança preditiva via PIX, redução de tarifas bancárias e régua omnichannel.</td>
                <td><span class="highlight">Zero Fricção de Caixa</span></td>
            </tr>
        </tbody>
    </table>
</body>
</html>
"""

with open("MATRIZ_INTELIGENCIA_SETORIAL.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ Arquivo 'MATRIZ_INTELIGENCIA_SETORIAL.html' gerado com sucesso!")
