# ==========================================================
# 076_EXECUTIVE_SKIN.py
# IOTEC EXECUTIVE SKIN
# ==========================================================

import time
import os

os.system("cls" if os.name == "nt" else "clear")

def linha():
    print("=" * 80)

def pausa(seg=1):
    time.sleep(seg)

linha()
print("IOTEC ENTERPRISE OPERATING SYSTEM".center(80))
print("EXECUTIVE SKIN".center(80))
linha()
print()

print("Inicializando Empresa...")
pausa(0.8)

etapas = [

"Ativando Executive Skin",
"Conectando Cockpit",
"Verificando Presidencia",
"Carregando Ecossistemas",
"Ativando Monitoramento",
"Inicializando Discovery Center",
"Sincronizando Campanhas",
"Preparando Experience Centers",
"Carregando Executive Voice",
"Empresa pronta"

]

for etapa in etapas:

    print(f"[OK] {etapa}")
    pausa(0.35)

print()

linha()
print("BEM-VINDO".center(80))
linha()
print()

print("Bom dia, Presidente.")
print()
print("A IOTEC encontra-se operacional.")
print()

print("Todas as torres estao online.")
print("Nenhum incidente critico encontrado.")
print()

linha()

print("VISAO GERAL")

linha()

status = [

("Executive Skin","ONLINE"),

("Executive Cockpit","ONLINE"),

("Discovery Center","ONLINE"),

("Campaign Center","ONLINE"),

("Operation Center","ONLINE"),

("Knowledge Kernel","ONLINE"),

("Executive Voice","AGUARDANDO"),

("Experience Warehouse","AGUARDANDO"),

("Experience Centers","AGUARDANDO")

]

for nome,estado in status:

    print(f"{nome:<35} {estado}")

print()

linha()
print("MISSAO DO DIA")
linha()
print()

print("- Descobrir novas oportunidades.")
print("- Acompanhar campanhas.")
print("- Atender clientes.")
print("- Aprender continuamente.")
print("- Fortalecer a empresa.")

print()

linha()
print("PAINEL DA PRESIDENCIA")
linha()

print()

print("[1] Executive Cockpit")
print("[2] Discovery Center")
print("[3] Campaign Center")
print("[4] Operation Center")
print("[5] Experience Centers")
print("[6] Experience Warehouse")
print("[7] Knowledge Kernel")
print("[8] Configuracoes")
print("[9] Encerrar")

print()

linha()

print("A Executive Skin passa a representar")
print("a face oficial da IOTEC.")

print()

print("O PowerShell continua existindo.")
print("O Python continua existindo.")
print()

print("Mas a Presidencia passa")
print("a enxergar uma EMPRESA.")

print()

linha()
print("STATUS")
linha()

print()

print("EXECUTIVE SKIN INICIADA COM SUCESSO.")
print("FASE III EM EXECUCAO.")


