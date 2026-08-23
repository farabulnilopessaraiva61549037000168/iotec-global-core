import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
IOTEC ENGINEERING CONSOLE
VersÃƒÂ£o 1.0

Objetivo:
Enviar uma missÃƒÂ£o ao NÃƒÂºcleo e registrar a resposta.
"""

import datetime

print("=" * 70)
print("IOTEC ENGINEERING CONSOLE")
print("=" * 70)

mission = input("\nMISSÃƒÆ'O: ")

print("\nEnviando missÃƒÂ£o ao NÃƒÂºcleo...\n")

# =====================================================
# Aqui vocÃƒÂª substitui pela chamada real do seu NÃƒÂºcleo.
# Por enquanto ÃƒÂ© apenas um ponto de integraÃƒÂ§ÃƒÂ£o.
# =====================================================

response = """
NÃƒÅ¡CLEO:
MissÃƒÂ£o recebida.

Analisando...

Status:
AGUARDANDO IMPLEMENTAÃƒâ€¡ÃƒÆ'O DA INTEGRAÃƒâ€¡ÃƒÆ'O.
"""

print(response)

log = f"""
====================================================
DATA: {datetime.datetime.now()}

MISSÃƒÆ'O

{mission}

RESPOSTA

{response}
====================================================
"""

with open("MISSION_LOG.txt", "a", encoding="utf-8") as f:
    f.write(log)

print("\nLog salvo em MISSION_LOG.txt")



