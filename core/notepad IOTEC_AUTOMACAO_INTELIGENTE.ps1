$base = "C:\IOTEC\IOTEC_RENDER_READY"

Write-Host "🚀 ATIVANDO MOTOR INTELIGENTE" -ForegroundColor Cyan

# =========================
# 1. ATIVAR FORMULÁRIOS
# =========================

Get-ChildItem "$base\static" -Filter *.html | ForEach-Object {

    $c = Get-Content $_.FullName -Raw

    # adiciona action apenas se não existir
    if ($c -match "<form" -and $c -notmatch "action=") {
        $c = $c -replace "<form", '<form action="/enviar" method="post"'
        Write-Host "✔ Formulário ativado em: $($_.Name)"
    }

    Set-Content $_.FullName $c
}

# =========================
# 2. CRIAR BACKEND (MOTOR)
# =========================

$app = @"
from flask import Flask, request, send_from_directory

app = Flask(__name__, static_folder="static")

@app.route("/")
def home():
    return send_from_directory("static", "index.html")

@app.route("/<path:path>")
def arquivos(path):
    return send_from_directory("static", path)

@app.route("/enviar", methods=["POST"])
def enviar():
    nome = request.form.get("nome")
    email = request.form.get("email")
    mensagem = request.form.get("mensagem")

    print("=== NOVO CLIENTE ===")
    print(nome, email, mensagem)

    return "Recebido com sucesso"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
"@

$app | Out-File "$base\app.py" -Encoding UTF8

# =========================
# 3. REQUIREMENTS
# =========================

"flask" | Out-File "$base\requirements.txt"

Write-Host "✅ MOTOR ATIVADO SEM ALTERAR VISUAL" -ForegroundColor Green