import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import time
import subprocess

print("?? NÃƒÆ'Ã…Â¡CLEO IOTEC INICIADO")

while True:
    pass

    print("?? Ciclo iniciado")

    subprocess.run(["python", "C:\\IOTEC\\CORE\\coletor_email.py"])
    subprocess.run(["python", "C:\\IOTEC\\CORE\\orquestrador.py"])
    subprocess.run(["python", "C:\\IOTEC\\CORE\\motor_producao.py"])

    print("? Ciclo finalizado")

    time.sleep(10)



