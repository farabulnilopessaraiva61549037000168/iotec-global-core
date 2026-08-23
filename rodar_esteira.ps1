Set-Location C:\IOTEC
Write-Host '===> [1/2] Minerando E-mails (Operario 2)...' -ForegroundColor Cyan
python C:\IOTEC\operario_2_minerador.py

Write-Host '===> [2/2] Enviando Propostas (Operario 3)...' -ForegroundColor Cyan
python C:\IOTEC\operario_3_contatador.py

Write-Host '===> [OK] Ciclo de automação concluído!' -ForegroundColor Green