# ==========================================================
# 095_PRODUCTION_PLANNING_AND_CONTROL.py
# IOTEC PRODUCTION PLANNING AND CONTROL
# PCP DIGITAL
# ==========================================================

from datetime import datetime

print("="*90)
print("IOTEC PRODUCTION PLANNING AND CONTROL")
print("PLANEJAMENTO E CONTROLE DA PRODUÃƒâ€¡ÃƒÆ'O DIGITAL")
print("="*90)
print()

print("Inicializando PCP Digital...")
print()

# ==========================================================
# ORDENS DE PRODUÃƒâ€¡ÃƒÆ'O
# ==========================================================

OPS = [

("OP-000001","Executive Skin","ALTA","EM PRODUÃƒâ€¡ÃƒÆ'O"),

("OP-000002","Google Maps","ALTA","AGUARDANDO"),

("OP-000003","WhatsApp Business","ALTA","EM IMPLANTAÃƒâ€¡ÃƒÆ'O"),

("OP-000004","LinkedIn","MÃƒâ€°DIA","PLANEJAMENTO"),

("OP-000005","Portal Comercial","ALTA","EM PRODUÃƒâ€¡ÃƒÆ'O"),

("OP-000006","Knowledge Library","MÃƒâ€°DIA","EM PRODUÃƒâ€¡ÃƒÆ'O"),

("OP-000007","Visual Genome","CONCLUÃƒÂDA","FINALIZADA"),

("OP-000008","Experience Warehouse","CONCLUÃƒÂDA","FINALIZADA")

]

print("="*90)
print("ORDENS DE PRODUÃƒâ€¡ÃƒÆ'O")
print("="*90)
print()

for numero,produto,prioridade,status in OPS:

    print(numero)
    print("Produto.....",produto)
    print("Prioridade..",prioridade)
    print("Status......",status)
    print()

# ==========================================================
# FÃƒÂBRICAS
# ==========================================================

FABRICAS=[

("Knowledge Factory","Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"â€˜","95%"),

("HTML Factory","Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†","100%"),

("Commercial Factory","Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜","74%"),

("Campaign Factory","Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜","69%"),

("API Factory","Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜","48%"),

("Quality Factory","Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜","82%"),

("Deployment Factory","Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜","63%"),

("Revenue Factory","Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"Ë†Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜Ã¢â€"â€˜","22%")

]

print("="*90)
print("LINHAS INDUSTRIAIS")
print("="*90)
print()

for nome,barra,p in FABRICAS:

    print(nome.ljust(28),barra,p)

print()

# ==========================================================
# CAPACIDADES
# ==========================================================

CAPACIDADES=[

"Descoberta de Empresas",

"CRM",

"Executive Skin",

"Experience Warehouse",

"Visual Genome",

"Google Maps",

"Render",

"Netlify",

"PayPal",

"Campanhas",

"Produtos",

"DocumentaÃƒÂ§ÃƒÂ£o",

"IA",

"Monitoramento",

"Infraestrutura"

]

print("="*90)
print("CAPACIDADES INDUSTRIAIS")
print("="*90)
print()

for c in CAPACIDADES:

    print("Ã¢Å"â€œ",c)

print()

# ==========================================================
# GARGALOS
# ==========================================================

print("="*90)
print("GARGALOS DETECTADOS")
print("="*90)
print()

GARGALOS=[

"Google Maps pendente.",

"LinkedIn aguardando implantaÃƒÂ§ÃƒÂ£o.",

"WhatsApp Business em implantaÃƒÂ§ÃƒÂ£o.",

"Revenue Factory aguardando novos clientes."

]

for g in GARGALOS:

    print("Ã¢Å¡Â ",g)

print()

# ==========================================================
# ENGENHOSIDADE
# ==========================================================

print("="*90)
print("ÃƒÂNDICE DE ENGENHOSIDADE")
print("="*90)
print()

print("Conhecimento.............. 96")
print("Arquitetura............... 95")
print("ReutilizaÃƒÂ§ÃƒÂ£o.............. 91")
print("IntegraÃƒÂ§ÃƒÂ£o................ 82")
print("AutomaÃƒÂ§ÃƒÂ£o................. 86")
print("ProduÃƒÂ§ÃƒÂ£o.................. 88")
print()

indice=(96+95+91+82+86+88)/6

print("ÃƒÂNDICE GERAL.............. %.1f"%indice)
print()

# ==========================================================
# CHEFE DE GABINETE
# ==========================================================

print("="*90)
print("CHEFE DE GABINETE")
print("="*90)
print()

print("Boa noite, Presidente.")
print()

print("O Planejamento Industrial")
print("estÃƒÂ¡ coordenando todas")
print("as ordens de produÃƒÂ§ÃƒÂ£o.")
print()

print("As fÃƒÂ¡bricas trabalham")
print("em paralelo, mantendo")
print("o fluxo contÃƒÂ­nuo.")
print()

print("Os principais gargalos")
print("foram identificados e")
print("estÃƒÂ£o sendo acompanhados.")
print()

print("O prÃƒÂ³ximo objetivo")
print("ÃƒÂ© ampliar a Revenue Factory")
print("atravÃƒÂ©s da implantaÃƒÂ§ÃƒÂ£o")
print("das integraÃƒÂ§ÃƒÂµes comerciais.")
print()

# ==========================================================
# FILOSOFIA
# ==========================================================

print("="*90)
print("FILOSOFIA DO PCP")
print("="*90)
print()

print("Nenhuma capacidade")
print("permanece ociosa.")
print()

print("Nenhuma ordem")
print("permanece esquecida.")
print()

print("Todo conhecimento")
print("deve entrar")
print("na linha de produÃƒÂ§ÃƒÂ£o.")
print()

print("Toda produÃƒÂ§ÃƒÂ£o")
print("deve gerar")
print("valor ao cliente.")
print()

print("Todo valor")
print("deve fortalecer")
print("a sustentabilidade")
print("da IOTEC.")
print()

# ==========================================================
# STATUS
# ==========================================================

print("="*90)
print("STATUS")
print("="*90)
print()

print("Ordens de ProduÃƒÂ§ÃƒÂ£o.......",len(OPS))
print("FÃƒÂ¡bricas.................",len(FABRICAS))
print("Capacidades..............",len(CAPACIDADES))
print("Data.....................",datetime.now().strftime("%d/%m/%Y %H:%M"))
print()

print("PLANEJAMENTO E CONTROLE DA PRODUÃƒâ€¡ÃƒÆ'O OPERACIONAL.")


