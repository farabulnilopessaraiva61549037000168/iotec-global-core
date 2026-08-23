Write-Host ""
Write-Host "================================================"
Write-Host " IOTEC / IBEX LIVE SOCKET RECOVERY"
Write-Host "================================================"
Write-Host ""

$BASE = "C:\IOTEC"

Set-Location $BASE

$TARGET = "$BASE\LIVE_SOCKET_TOWER.py"

if (!(Test-Path $TARGET)) {

```
Write-Host "[ERRO] LIVE_SOCKET_TOWER.py NÃO ENCONTRADO"
exit
```

}

$PORT = 3000

$CONTENT = Get-Content $TARGET -Raw

$CONTENT = $CONTENT -replace "async_mode='eventlet'", "async_mode='threading'"

$CONTENT = $CONTENT -replace "port=\d+", "port=$PORT"

$CONTENT = $CONTENT -replace "host='0.0.0.0'", "host='127.0.0.1'"

$CONTENT = $CONTENT -replace "socketio.run(", "socketio.run("

if ($CONTENT -notmatch "allow_unsafe_werkzeug") {

```
$CONTENT = $CONTENT -replace "\)\s*$", @"

,

allow_unsafe_werkzeug=True,

debug=True,

use_reloader=False
```

)
"@
}

Set-Content `    -Path $TARGET`
-Value $CONTENT `
-Encoding UTF8

Write-Host "[OK] LIVE_SOCKET_TOWER.py CORRIGIDO"

python -m py_compile $TARGET

if ($LASTEXITCODE -ne 0) {

```
Write-Host "[ERRO] PYTHON INVÁLIDO"
exit
```

}

Write-Host "[OK] PYTHON VALIDADO"

Start-Process cmd.exe `
-ArgumentList "/k cd /d $BASE && python LIVE_SOCKET_TOWER.py"

Start-Sleep -Seconds 5

Start-Process "[http://127.0.0.1:$PORT](http://127.0.0.1:$PORT)"

Write-Host ""
Write-Host "================================================"
Write-Host " LIVE SOCKET TOWER ONLINE"
Write-Host "================================================"
Write-Host ""
