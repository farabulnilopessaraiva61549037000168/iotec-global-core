$base = "C:\IOTEC\IOTEC_RENDER_READY"

Write-Host "🚀 ATIVANDO MOTOR INTELIGENTE" -ForegroundColor Cyan

# =========================
# ATIVAR FORMULÁRIOS
# =========================

Get-ChildItem "$base\static" -Filter *.html | ForEach-Object {

    $c = Get-Content $_.FullName -Raw

    if ($c -match "<form" -and $c -notmatch "action=") {
        $c = $c -replace "<form", '<form action="/enviar" method="post"'
        Write-Host "✔ Form ativado: $($_.Name)"
    }

    Set-Content $_.FullName $c
}

# =========================
# BACKEND
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

    print("NOVO CLIENTE:", nome, email, mensagem)

    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
"@

$app | Out-File "$base\app.py" -Encoding UTF8

"flask" | Out-File "$base\requirements.txt"

Write-Host "✅ MOTOR ATIVADO" -ForegroundColor Green
