# ==========================================================
# 048_INTERECOSYSTEM_PROTOCOL_ENGINE.py
# IOTEC INTERECOSYSTEM PROTOCOL
# ==========================================================

import sqlite3

DB="iotec_kernel.db"

db=sqlite3.connect(DB, timeout=30)
cursor=db.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS ecosystem_protocol(

id INTEGER PRIMARY KEY AUTOINCREMENT,

origem TEXT,

destino TEXT,

operacao TEXT,

prioridade TEXT,

status TEXT,

autorizacao TEXT,

observacao TEXT

)

""")

db.commit()

PROTOCOLOS=[

("COMERCIAL","FINANCEIRO",
"Solicitar Recebimento",
"ALTA",
"ATIVO",
"PRESIDÃƒÅ NCIA",
"Cliente efetuou pedido"),

("FINANCEIRO","COMERCIAL",
"Pagamento Confirmado",
"ALTA",
"ATIVO",
"AUTOMÃƒÂTICA",
"Pagamento aprovado"),

("FINANCEIRO","PRODUÃƒâ€¡ÃƒÆ'O",
"Liberar ProduÃƒÂ§ÃƒÂ£o",
"ALTA",
"ATIVO",
"AUTOMÃƒÂTICA",
"Pagamento confirmado"),

("PRODUÃƒâ€¡ÃƒÆ'O","QUALIDADE",
"Solicitar ValidaÃƒÂ§ÃƒÂ£o",
"MÃƒâ€°DIA",
"ATIVO",
"AUTOMÃƒÂTICA",
"Produto concluÃƒÂ­do"),

("QUALIDADE","COMERCIAL",
"Produto Liberado",
"MÃƒâ€°DIA",
"ATIVO",
"AUTOMÃƒÂTICA",
"Entrega autorizada"),

("COMERCIAL","CRM",
"Registrar Cliente",
"MÃƒâ€°DIA",
"ATIVO",
"AUTOMÃƒÂTICA",
"Novo cliente"),

("CRM","INTELIGÃƒÅ NCIA",
"Atualizar Perfil",
"BAIXA",
"ATIVO",
"AUTOMÃƒÂTICA",
"Aprendizado"),

("INTELIGÃƒÅ NCIA","PRESIDÃƒÅ NCIA",
"Enviar Indicadores",
"ALTA",
"ATIVO",
"AUTOMÃƒÂTICA",
"RelatÃƒÂ³rio diÃƒÂ¡rio"),

("IA","COMERCIAL",
"Sugerir Oportunidade",
"MÃƒâ€°DIA",
"ATIVO",
"AUTOMÃƒÂTICA",
"Lead encontrado"),

("ARQUITETURA","PRESIDÃƒÅ NCIA",
"Solicitar MudanÃƒÂ§a Estrutural",
"ALTA",
"ATIVO",
"MANUAL",
"NecessÃƒÂ¡ria aprovaÃƒÂ§ÃƒÂ£o")

]

novos=0

for protocolo in PROTOCOLOS:

    cursor.execute("""

    SELECT id

    FROM ecosystem_protocol

    WHERE origem=?
    AND destino=?
    AND operacao=?

    """,(protocolo[0],protocolo[1],protocolo[2]))

    if cursor.fetchone() is None:

        cursor.execute("""

        INSERT INTO ecosystem_protocol(

        origem,

        destino,

        operacao,

        prioridade,

        status,

        autorizacao,

        observacao

        )

        VALUES(?,?,?,?,?,?,?)

        """,protocolo)

        novos+=1

db.commit()

print("="*70)
print("IOTEC INTERECOSYSTEM PROTOCOL")
print("="*70)
print()

cursor.execute("""

SELECT

origem,

destino,

operacao,

prioridade

FROM ecosystem_protocol

ORDER BY prioridade DESC,origem

""")

for origem,destino,operacao,prioridade in cursor.fetchall():

    print(f"{origem:15} ---> {destino:15}")
    print("OperaÃƒÂ§ÃƒÂ£o :",operacao)
    print("Prioridade :",prioridade)
    print("-"*60)

print()

print("="*70)
print("RESUMO")
print("="*70)
print()

cursor.execute("SELECT COUNT(*) FROM ecosystem_protocol")

print("Protocolos registrados :",cursor.fetchone()[0])

print()

print("A comunicaÃƒÂ§ÃƒÂ£o entre")
print("os ecossistemas agora")
print("possui regras oficiais.")

print()

print("PrÃƒÂ³xima missÃƒÂ£o:")

print()

print("Criar os Agentes de Fronteira")
print("que executarÃƒÂ£o estes protocolos.")

db.close()


