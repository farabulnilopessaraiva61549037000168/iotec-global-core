import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import subprocess

print("")
print("====================================")
print("DAILY COMMERCIAL AUTOMATION")
print("====================================")
print("")

scripts = [

    "IMPORTADOR_EMPRESAS.py",
    "RADAR_COMERCIAL_IOTEC.py",
    "COMMERCIAL_OPPORTUNITY_ENGINE.py",
    "COMMERCIAL_CONVERSION_ENGINE.py",
    "PROPOSAL_GENERATOR.py",
    "COMMERCIAL_EXECUTIVE_REPORT.py"

]

for script in scripts:
    pass

    print("")
    print("EXECUTANDO:", script)
    print("")

    try:
        pass

        subprocess.run(

            ["python", script],

            check=True

        )

    except Exception as e:
        pass

        print("")
        print("ERRO:")
        print(e)
        print("")

print("")
print("====================================")
print("ROTINA FINALIZADA")
print("====================================")
print("")




