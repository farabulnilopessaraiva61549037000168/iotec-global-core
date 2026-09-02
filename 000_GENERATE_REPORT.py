import sqlite3

conn = sqlite3.connect("C:\\IOTEC\\iotec_kernel.db")
cursor = conn.cursor()
cursor.execute("SELECT razao_social, cnpj, setor, score_potencial, gargalo_principal, status_qualificacao FROM empresas_qualificadas ORDER BY score_potencial DESC")
rows = cursor.fetchall()
conn.close()

html_rows = ""
for r in rows:
    html_rows += f"""
    <tr>
        <td style='font-weight: bold; color: #f8fafc;'>{r[0]}</td>
        <td>{r[1]}</td>
        <td>{r[2]}</td>
        <td><span style='background:#15803d; color:#fff; padding:3px 8px; border-radius:12px; font-weight:bold;'>{r[3]}/100</span></td>
        <td style='font-size: 8.5pt;'>{r[4]}</td>
        <td style='color: #4ade80; font-weight: bold;'>{r[5]}</td>
    </tr>
    """

html_full = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>IOTEC - Relatório Rover</title>
    <style>
        body {{ font-family: 'Segoe UI', sans-serif; background: #0f172a; color: #f8fafc; padding: 20px; }}
        .header {{ border-bottom: 2px solid #38bdf8; padding-bottom: 10px; margin-bottom: 20px; }}
        .title {{ font-size: 18pt; color: #38bdf8; font-weight: bold; }}
        table {{ width: 100%; border-collapse: collapse; background: #1e293b; border-radius: 6px; overflow: hidden; }}
        th {{ background: #334155; color: #38bdf8; padding: 10px; text-align: left; font-size: 9pt; }}
        td {{ padding: 10px; border-bottom: 1px solid #334155; font-size: 9pt; color: #cbd5e1; }}
    </style>
</head>
<body>
    <div class="header">
        <div class="title">IOTEC Enterprise — Relatório da Câmera Rover</div>
        <div>CNPJ: 61.549.037/0001-68 | Filtro: Score &gt; 80</div>
    </div>
    <table>
        <thead>
            <tr>
                <th>Razão Social</th>
                <th>CNPJ</th>
                <th>Setor</th>
                <th>Score</th>
                <th>Gargalo Principal</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
            {html_rows}
        </tbody>
    </table>
</body>
</html>"""

with open("C:\\IOTEC\\Relatorio_Rover_Calibragem.html", "w", encoding="utf-8") as f:
    f.write(html_full)

print("[OK] HTML gerado com sucesso!")
