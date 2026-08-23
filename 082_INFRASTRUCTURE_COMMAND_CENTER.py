# ==========================================================
# 082_INFRASTRUCTURE_COMMAND_CENTER.py
# IOTEC INFRASTRUCTURE COMMAND CENTER
# ==========================================================

from datetime import datetime

print("="*80)
print("IOTEC INFRASTRUCTURE COMMAND CENTER")
print("="*80)
print()

print("Inicializando Centro de Infraestrutura...")
print()

NUVENS = [

("Render",
"Backend Ã¢â‚¬Â¢ APIs Ã¢â‚¬Â¢ Kernel Ã¢â‚¬Â¢ Agentes",
"ONLINE"),

("Netlify",
"Portais Ã¢â‚¬Â¢ Landing Pages Ã¢â‚¬Â¢ CatÃƒÂ¡logo",
"ONLINE"),

("GitHub",
"RepositÃƒÂ³rios Oficiais",
"SINCRONIZAÃƒâ€¡ÃƒÆ'O")

]

INTEGRACOES = [

("Google Maps API","PENDENTE"),
("LinkedIn","PENDENTE"),
("WhatsApp Business API","PENDENTE"),
("Proton Mail","ONLINE"),
("PayPal","ONLINE"),
("Google OAuth","PENDENTE"),
("OpenAI","PENDENTE")

]

print("="*80)
print("NUVENS")
print("="*80)
print()

for nome,descricao,status in NUVENS:

    cor="Ã°Å¸Å¸Â¢"

    if status!="ONLINE":
        cor="Ã°Å¸Å¸Â¡"

    print(f"{cor} {nome}")
    print(f"    {descricao}")
    print(f"    Status : {status}")
    print()

print("="*80)
print("INTEGRAÃƒâ€¡Ãƒâ€¢ES")
print("="*80)
print()

for nome,status in INTEGRACOES:

    if status=="ONLINE":
        icone="Ã°Å¸Å¸Â¢"
    else:
        icone="Ã°Å¸â€Â´"

    print(f"{icone} {nome:<30}{status}")

print()

print("="*80)
print("TÃƒÅ¡NEIS OPERACIONAIS")
print("="*80)
print()

TUNEIS=[

("Kernel","Render","LIBERADO",100),

("Kernel","Netlify","LIBERADO",100),

("Kernel","Google Maps","PENDENTE",20),

("Kernel","LinkedIn","PENDENTE",15),

("Kernel","WhatsApp","EM IMPLANTAÃƒâ€¡ÃƒÆ'O",40),

("Kernel","PayPal","LIBERADO",100),

("Kernel","Proton Mail","LIBERADO",100)

]

for origem,destino,status,percentual in TUNEIS:

    barra=int(percentual/5)

    print(f"{origem}  <=====>  {destino}")
    print("Ã¢â€"Ë†"*barra+"Ã¢â€"â€˜"*(20-barra))
    print(status)
    print()

print("="*80)
print("CAPACIDADES LIBERADAS")
print("="*80)
print()

CAPACIDADES=[

("Portais PÃƒÂºblicos","ATIVO"),

("Deploy ContÃƒÂ­nuo","ATIVO"),

("Recebimento PayPal","ATIVO"),

("Correio Corporativo","ATIVO"),

("Descoberta de Empresas","AGUARDANDO"),

("Mensageria WhatsApp","AGUARDANDO"),

("Relacionamento LinkedIn","AGUARDANDO")

]

for nome,status in CAPACIDADES:

    print(f"{nome:<35}{status}")

print()

print("="*80)
print("MONETIZAÃƒâ€¡ÃƒÆ'O")
print("="*80)
print()

ativos=sum(1 for _,status in CAPACIDADES if status=="ATIVO")
pendentes=len(CAPACIDADES)-ativos

indice=int((ativos/len(CAPACIDADES))*100)

print(f"Canais ativos............. {ativos}")
print(f"Canais pendentes......... {pendentes}")
print(f"ÃƒÂndice operacional....... {indice}%")

print()

print("="*80)
print("CHEFE DE GABINETE")
print("="*80)
print()

print("Bom dia, Presidente.")
print()

print("Resumo Executivo")

print(f"- Data............. {datetime.now().strftime('%d/%m/%Y %H:%M')}")
print(f"- Infraestrutura... EstÃƒÂ¡vel")
print(f"- TÃƒÂºneis ativos.... {ativos}")
print(f"- PendÃƒÂªncias....... {pendentes}")

print()

print("PrÃƒÂ³ximas prioridades:")

print()

print("1. Concluir Google Maps")
print("2. Concluir WhatsApp Business")
print("3. Concluir LinkedIn")
print("4. Liberar sensores comerciais")
print("5. Iniciar campanhas reais")

print()

print("="*80)
print("MISSÃƒÆ'O")
print("="*80)
print()

print("Cada tÃƒÂºnel liberado")
print("ativa novas capacidades")
print("da plataforma.")

print()

print("Cada capacidade")
print("ativa novas")
print("estratÃƒÂ©gias de")
print("monetizaÃƒÂ§ÃƒÂ£o.")

print()

print("="*80)
print("STATUS")
print("="*80)
print()

print("CENTRO DE INFRAESTRUTURA OPERACIONAL.")


