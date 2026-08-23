import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
print("=" * 70)
print("X27 INTEGRATION REQUIREMENTS")
print("=" * 70)

print()

requisitos = [

    (
        "GOOGLE MAPS",
        "API KEY NECESSARIA",
        "EMPRESAS E ENDERECOS"
    ),

    (
        "GOOGLE PLACES",
        "API KEY NECESSARIA",
        "TELEFONES E SITES"
    ),

    (
        "EMAIL",
        "SMTP OU SERVICO",
        "ENVIO DE PROPOSTAS"
    ),

    (
        "WHATSAPP",
        "API NECESSARIA",
        "CONTATO COM CLIENTES"
    )

]

for r in requisitos:

    print("SERVICO :", r[0])
    print("REQUISITO:", r[1])
    print("FUNCAO   :", r[2])
    print("-" * 50)

print()
print("=" * 70)
print("CONCLUSAO")
print("=" * 70)

print("""
O nÃƒÂºcleo estÃƒÂ¡ operacional.

O prÃƒÂ³ximo avanÃƒÂ§o nÃƒÂ£o depende de mais bancos.

O prÃƒÂ³ximo avanÃƒÂ§o depende da conexÃƒÂ£o
com serviÃƒÂ§os externos.

Sem conectores o nÃƒÂºcleo apenas
organiza informaÃƒÂ§ÃƒÂµes.

Com conectores ele passa a descobrir,
comunicar e operar.
""")



