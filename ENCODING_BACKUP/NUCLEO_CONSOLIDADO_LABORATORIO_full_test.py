import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import subprocess
import sys

def run(cmd):
    print(f"\n=== TESTANDO: {cmd} ===")
    try:
        subprocess.run(cmd, shell=True, check=True)
        print("OK")
    except:
        print("FALHOU")

print("=== TESTE COMPLETO DO N?CLEO ===")

# 1. Verificar lacre
run("python C:/IOTEC/CORE/security/seal_guard.py verify")

# 2. Rodar ciclo completo
run("python C:/IOTEC/CORE/runtime/run_demo_cycle.py")

print("\n=== TESTE FINALIZADO ===")


