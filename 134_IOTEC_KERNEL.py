import subprocess
from datetime import datetime

MODULES = [

    "126_COMMERCIAL_COMMAND_CENTER.py",

    "127_OPERATIONAL_AUDITOR.py",

    "128_CONTROL_TOWER.py",

    "129_MISSION_ORCHESTRATOR.py",

    "130_AGENT_EXECUTION_ENGINE.py",

    "131_MISSION_COMPLETION_ENGINE.py",

    "132_EVENT_BUS_ENGINE.py",

    "133_KERNEL_EVENT_DISPATCHER.py"

]

print("="*90)
print("IOTEC KERNEL")
print("="*90)
print()

print("Inicializando Centros...")
print()

for module in MODULES:

    print(f"> Executando {module}")

    subprocess.run(
        ["python", module],
        check=False
    )

print()
print("="*90)
print("KERNEL FINALIZADO")
print("="*90)
print()

print("Data:", datetime.now())
print()

print("Todos os Centros foram sincronizados.")

