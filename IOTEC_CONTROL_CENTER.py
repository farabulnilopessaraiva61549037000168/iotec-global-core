import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================
IOTEC CONTROL CENTER
SALA DE COMANDO DA PRESIDÃƒÅ NCIA
======================================================================
"""

from datetime import datetime
import random

print("=" * 78)
print("                 I O T E C   C O N T R O L   C E N T E R")
print("=" * 78)

agora = datetime.now()

print(f"Data............... {agora.strftime('%d/%m/%Y')}")
print(f"Hora............... {agora.strftime('%H:%M:%S')}")
print()

print("Bom dia, Presidente Bruno.")
print()

print("=" * 78)
print("SITUAÃƒâ€¡ÃƒÆ'O GERAL")
print("=" * 78)

print("Kernel............. ONLINE")
print("Control Center..... ONLINE")
print("Banco de Dados..... ONLINE")
print("CRM................ ONLINE")
print("OperaÃƒÂ§ÃƒÂ£o........... NORMAL")
print()

print("=" * 78)
print("FROTA TECNOLÃƒâ€œGICA")
print("=" * 78)

caminhoes = [

    ("TRK-001","Documentos"),
    ("TRK-002","Leads"),
    ("TRK-003","CRM"),
    ("TRK-004","Financeiro"),
    ("TRK-005","PortfÃƒÂ³lios"),
    ("TRK-006","LicitaÃƒÂ§ÃƒÂµes"),
    ("TRK-007","LegislaÃƒÂ§ÃƒÂ£o"),
    ("TRK-008","Projetos")

]

status = [

    "NA GARAGEM",
    "EM COLETA",
    "RETORNANDO",
    "DESCARREGANDO",
    "EM MISSÃƒÆ'O"

]

for codigo,missao in caminhoes:

    barra = "Ã¢â€"Ë†"*random.randint(5,20)

    print()

    print(codigo)

    print("MissÃƒÂ£o.............",missao)

    print("Status.............",random.choice(status))

    print("Carga..............",random.randint(20,900),"itens")

    print("Progresso..........",barra)

print()

print("=" * 78)
print("AGENTES")
print("=" * 78)

setores = [

"Comercial",

"JurÃƒÂ­dico",

"Financeiro",

"Marketing",

"Projetos",

"GovernanÃƒÂ§a",

"Auditoria"

]

for setor in setores:

    print(f"{setor:<18} {random.randint(1,8)} agente(s) ativo(s)")

print()

print("=" * 78)
print("NEGOCIAÃƒâ€¡Ãƒâ€¢ES")
print("=" * 78)

print("Leads.....................",random.randint(20,300))

print("ReuniÃƒÂµes..................",random.randint(1,12))

print("Propostas.................",random.randint(1,25))

print("Contratos................",random.randint(0,10))

print()

print("=" * 78)
print("FINANCEIRO")
print("=" * 78)

receita = random.randint(20000,150000)

prevista = receita + random.randint(5000,40000)

print(f"Receita Confirmada........ R$ {receita:,.2f}")

print(f"Receita Prevista.......... R$ {prevista:,.2f}")

print()

print("=" * 78)
print("KERNEL")
print("=" * 78)

print()

mensagens = [

"Priorizar fechamento de contratos.",

"Buscar novos parceiros.",

"Atualizar portfÃƒÂ³lio.",

"Prospectar empresas mÃƒÂ©dias.",

"Acompanhar propostas pendentes.",

"Monitorar oportunidades comerciais."

]

print("AnÃƒÂ¡lise:")

print()

for m in mensagens:

    print("Ã¢â‚¬Â¢",m)

print()

print("=" * 78)

print("MISSÃƒÆ'O DO DIA")

print("=" * 78)

print()

print("GERAR RECEITA.")

print()

print("Toda operaÃƒÂ§ÃƒÂ£o da empresa deve convergir")

print("para geraÃƒÂ§ÃƒÂ£o de valor ao cliente e receita.")

print()

print("=" * 78)

print("FIM DO BRIEFING EXECUTIVO")

print("=" * 78)



