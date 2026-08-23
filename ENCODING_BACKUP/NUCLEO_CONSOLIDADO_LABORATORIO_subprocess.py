import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import subprocess

# Abre CMD como administrador e executa um comando
subprocess.run(["cmd", "/k", "echo Sistema Iniciado && dir"], shell=True)

# Abre PowerShell e executa script
subprocess.run(["powershell", "-Command", "Write-Output 'Ignicao Ativada'"], shell=True)



