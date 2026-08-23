# ==============================================================================
# 119_REVENUE_FACTORY.py
# IOTEC REVENUE FACTORY
# FÃƒÂBRICA DE RECEITA
# ==============================================================================

import json
from datetime import datetime
from collections import Counter

print("="*90)
print("IOTEC REVENUE FACTORY")
print("FÃƒÂBRICA DE GERAÃƒâ€¡ÃƒÆ'O DE RECEITA")
print("="*90)
print()

ARQUIVO="IOTEC_OPPORTUNITY_DATABASE.json"

try:

    with open(ARQUIVO,"r",encoding="utf8") as f:

        banco=json.load(f)

except:

    print("Banco de oportunidades nÃƒÂ£o encontrado.")
    raise SystemExit()

oportunidades = banco.get("oportunidades", [])

PIPELINE=[]

print("="*90)
print("PIPELINE COMERCIAL")
print("="*90)
print()

for i,item in enumerate(oportunidades,1):

    empresa=item["empresa"]

    ordem={

        "id":i,

        "empresa":empresa,

        "fase":"PROSPECÃƒâ€¡ÃƒÆ'O",

        "responsÃƒÂ¡vel":"COMMERCIAL_AGENT",

        "status":"AGUARDANDO",

        "prÃƒÂ³xima_aÃƒÂ§ÃƒÂ£o":"Pesquisar contato"

    }

    PIPELINE.append(ordem)

    print("="*70)
    print(empresa)
    print()
    print("FASE............. PROSPECÃƒâ€¡ÃƒÆ'O")
    print("RESPONSÃƒÂVEL...... COMMERCIAL_AGENT")
    print("PRÃƒâ€œXIMA AÃƒâ€¡ÃƒÆ'O..... Pesquisar contato")
    print()

print("="*90)
print("ESTÃƒÂGIOS DO PIPELINE")
print("="*90)
print()

ETAPAS=[

"PROSPECÃƒâ€¡ÃƒÆ'O",

"QUALIFICAÃƒâ€¡ÃƒÆ'O",

"CONTATO",

"APRESENTAÃƒâ€¡ÃƒÆ'O",

"PROPOSTA",

"NEGOCIAÃƒâ€¡ÃƒÆ'O",

"CONTRATO",

"IMPLANTAÃƒâ€¡ÃƒÆ'O",

"SUCESSO DO CLIENTE"

]

for etapa in ETAPAS:

    print("Ã¢Å"â€œ",etapa)

print()

print("="*90)
print("RESUMO")
print("="*90)
print()

print("Empresas...........",len(PIPELINE))
print("Pipeline...........",len(PIPELINE))
print("Receita Atual...... R$ 0,00")
print("Meta Inicial....... 10 clientes")

saida={

    "generated_at":datetime.now().isoformat(),

    "pipeline":PIPELINE,

    "etapas":ETAPAS

}

with open(

    "IOTEC_REVENUE_PIPELINE.json",

    "w",

    encoding="utf8"

) as f:

    json.dump(

        saida,

        f,

        indent=4,

        ensure_ascii=False

    )

print()

print("="*90)
print("MISSÃƒÆ'O")
print("="*90)
print()

print("Toda oportunidade")
print("deve entrar")
print("no Pipeline Comercial.")
print()

print("Nenhuma oportunidade")
print("permanece esquecida.")
print()

print("Toda negociaÃƒÂ§ÃƒÂ£o")
print("ÃƒÂ© acompanhada")
print("atÃƒÂ© gerar")
print("cliente.")
print()

print("="*90)
print("ARQUIVO GERADO")
print("="*90)
print()

print("IOTEC_REVENUE_PIPELINE.json")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("REVENUE FACTORY OPERACIONAL.")


