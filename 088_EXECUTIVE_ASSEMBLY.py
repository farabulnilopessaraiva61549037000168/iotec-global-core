# ==========================================================
# 088_EXECUTIVE_ASSEMBLY.py
# IOTEC EXECUTIVE ASSEMBLY
# ==========================================================

from datetime import datetime

print("="*80)
print("IOTEC EXECUTIVE ASSEMBLY")
print("="*80)
print()

print("Convocando todos os departamentos...")
print()

DEPARTAMENTOS = [

("PresidÃƒÂªncia","ONLINE"),
("Chief of Staff","ONLINE"),
("Executive Skin","ONLINE"),
("Executive Cockpit","ONLINE"),
("Knowledge Kernel","ONLINE"),
("Infrastructure Command Center","ONLINE"),
("Discovery Center","ONLINE"),
("Campaign Center","ONLINE"),
("Commercial Intelligence","ONLINE"),
("CRM","ONLINE"),
("Operation Center","ONLINE"),
("Experience Warehouse","ONLINE"),
("Visual Genome","ONLINE"),
("Official Assets","ONLINE"),
("Financeiro","ONLINE"),
("Render","ONLINE"),
("Netlify","ONLINE"),
("PayPal","ONLINE"),
("Proton Mail","ONLINE"),
("Google Maps","PENDENTE"),
("WhatsApp Business","EM IMPLANTAÃƒâ€¡ÃƒÆ'O"),
("LinkedIn","PENDENTE"),
("OpenAI","PENDENTE")

]

online = 0
pendentes = 0

print("="*80)
print("DEPARTAMENTOS")
print("="*80)
print()

for nome,status in DEPARTAMENTOS:

    if status == "ONLINE":
        icone = "Ã°Å¸Å¸Â¢"
        online += 1
    elif status == "PENDENTE":
        icone = "Ã°Å¸â€Â´"
        pendentes += 1
    else:
        icone = "Ã°Å¸Å¸Â¡"
        pendentes += 1

    print(f"{icone} {nome:<35}{status}")

print()

print("="*80)
print("RESUMO EXECUTIVO")
print("="*80)
print()

print(f"Data........................ {datetime.now().strftime('%d/%m/%Y %H:%M')}")
print(f"Departamentos Online....... {online}")
print(f"ImplantaÃƒÂ§ÃƒÂµes Pendentes..... {pendentes}")

indice = int((online / len(DEPARTAMENTOS)) * 100)

print(f"ÃƒÂndice Geral............... {indice}%")

print()

print("="*80)
print("CHEFE DE GABINETE")
print("="*80)
print()

print("Bom dia, Presidente.")
print()

print("Toda a estrutura principal da empresa foi convocada.")
print()

if pendentes == 0:

    print("Todos os departamentos encontram-se operacionais.")

else:

    print("Existem departamentos estratÃƒÂ©gicos aguardando implantaÃƒÂ§ÃƒÂ£o.")
    print()
    print("Prioridades:")
    print("- Google Maps")
    print("- WhatsApp Business")
    print("- LinkedIn")
    print("- OpenAI")

print()

print("="*80)
print("MISSÃƒÆ'O")
print("="*80)
print()

print("A Executive Assembly passa a representar")
print("a reuniÃƒÂ£o oficial de todos os departamentos")
print("antes do inÃƒÂ­cio das operaÃƒÂ§ÃƒÂµes.")

print()

print("="*80)
print("STATUS")
print("="*80)
print()

print("EXECUTIVE ASSEMBLY CONCLUÃƒÂDA.")


