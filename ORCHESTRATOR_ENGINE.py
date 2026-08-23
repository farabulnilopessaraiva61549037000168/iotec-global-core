import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import subprocess

ROOT = r"C:\IOTEC"

print("="*70)
print("IOTEC ORCHESTRATOR ENGINE")
print("="*70)
print()

MODULOS = [

("CORE_PHILOSOPHY.py",False),

("BOOT_MANAGER.py",False),

("MODULE_REGISTRY.py",False),

("ARCHITECTURE_ANALYZER.py",False),

("DEPENDENCY_GRAPH.py",False),

("EXECUTION_DISCOVERY.py",False),

("CONTROL_CENTER.py",False)

]

executados=0

for modulo,executar in MODULOS:

    caminho=os.path.join(ROOT,modulo)

    if os.path.exists(caminho):

        print(f"[OK] {modulo}")

        if executar:

            print("     Executando...")

            subprocess.run(

                ["python",caminho],

                check=False

            )

            executados+=1

    else:

        print(f"[ERRO] {modulo}")

print()
print("="*70)
print("RESUMO")
print("="*70)

print(f"MÃ³dulos encontrados : {sum(os.path.exists(os.path.join(ROOT,m)) for m,_ in MODULOS)}")
print(f"MÃ³dulos executados  : {executados}")

print()
print("PRÃ"XIMA PRIORIDADE")
print("------------------------------")
print("GOOGLE_MAPS_ENGINE.py")

print()
print("="*70)
print("ORCHESTRATOR FINALIZADO")
print("="*70)





