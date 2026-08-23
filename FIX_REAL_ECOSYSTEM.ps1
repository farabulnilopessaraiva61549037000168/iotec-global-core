Write-Host ""
Write-Host "================================================"
Write-Host " REAL ECOSYSTEM AUTO FIX"
Write-Host "================================================"
Write-Host ""

$BASE = "C:\IOTEC"

Set-Location $BASE

# ============================================================
# REMOVE ARQUIVO QUEBRADO
# ============================================================

if (Test-Path "$BASE\REAL_ECOSYSTEM.py") {

    Remove-Item "$BASE\REAL_ECOSYSTEM.py" -Force
}

Write-Host "[OK] ARQUIVO ANTIGO REMOVIDO"
Write-Host ""

# ============================================================
# CRIA PYTHON LIMPO
# ============================================================

$PY = @'
import os
import time

BASES = [

    r"C:\IOTEC",
    r"C:\IOTEC_OMEGA_X"
]

REAL_STATE = {

    "interfaces":0,
    "html":0,
    "python":0,
    "videos":0,
    "socketio":0,
    "paypal":0,
    "forms":0,
    "logs":0
}

def scan():

    global REAL_STATE

    REAL_STATE = {

        "interfaces":0,
        "html":0,
        "python":0,
        "videos":0,
        "socketio":0,
        "paypal":0,
        "forms":0,
        "logs":0
    }

    for BASE in BASES:

        if not os.path.exists(BASE):
            continue

        for root, dirs, files in os.walk(BASE):

            for file in files:

                full = os.path.join(root, file)

                lower = file.lower()

                # HTML
                if lower.endswith(".html"):

                    REAL_STATE["interfaces"] += 1
                    REAL_STATE["html"] += 1

                    try:

                        content = open(
                            full,
                            "r",
                            encoding="utf-8",
                            errors="ignore"
                        ).read().lower()

                    except:
                        continue

                    if "socket.io" in content:

                        REAL_STATE["socketio"] += 1

                    if "paypal" in content:

                        REAL_STATE["paypal"] += 1

                    if "<form" in content:

                        REAL_STATE["forms"] += 1

                # PYTHON
                elif lower.endswith(".py"):

                    REAL_STATE["python"] += 1

                # VIDEOS
                elif lower.endswith((
                    ".mp4",
                    ".mov",
                    ".webm"
                )):

                    REAL_STATE["videos"] += 1

                # LOGS
                elif lower.endswith(".log"):

                    REAL_STATE["logs"] += 1

scan()

print("")
print("================================================")
print(" IOTEC REAL ECOSYSTEM")
print("================================================")
print("")

print("INTERFACES:", REAL_STATE["interfaces"])
print("HTML:", REAL_STATE["html"])
print("PYTHON:", REAL_STATE["python"])
print("VIDEOS:", REAL_STATE["videos"])
print("SOCKETIO:", REAL_STATE["socketio"])
print("PAYPAL:", REAL_STATE["paypal"])
print("FORMS:", REAL_STATE["forms"])
print("LOGS:", REAL_STATE["logs"])

print("")
print("================================================")
print(" REAL ECOSYSTEM ONLINE")
print("================================================")
print("")
'@

Set-Content `
    -Path "$BASE\REAL_ECOSYSTEM.py" `
    -Value $PY `
    -Encoding UTF8

Write-Host "[OK] REAL_ECOSYSTEM.py RECONSTRUÍDO"
Write-Host ""

python -m py_compile "$BASE\REAL_ECOSYSTEM.py"

if ($LASTEXITCODE -ne 0) {

    Write-Host "[ERRO] PYTHON INVALIDO"
    exit
}

Write-Host "[OK] PYTHON VALIDADO"
Write-Host ""

python "$BASE\REAL_ECOSYSTEM.py"

Write-Host ""
Write-Host "================================================"
Write-Host " REAL ECOSYSTEM FINALIZADO"
Write-Host "================================================"
Write-Host ""