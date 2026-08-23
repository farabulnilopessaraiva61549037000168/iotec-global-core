import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================

# IOTEC GLOBAL REALTY

# GLOBAL FINANCIAL CORE ENGINE

# VERSAO: 1.0

# ============================================================



from datetime import datetime

import uuid

import json



# ============================================================

# EMPRESA

# ============================================================



EMPRESA = {



    "nome": "IOTEC GLOBAL REALTY",

    "holding": "IOTEC",

    "cnpj": "61.549.037/0001-68",

    "email": "iotec.bl@proton.me",

    "status": "ONLINE",

    "fundacao": str(datetime.utcnow())



}



# ============================================================

# CONVERSAO MONETARIA

# ============================================================



MOEDAS = {



    "USD": 1.00,

    "BRL": 5.42,

    "EUR": 0.92,

    "GBP": 0.78,

    "CAD": 1.37



}



# ============================================================

# PESO OPERACIONAL POR PAIS

# ============================================================



PESO_PAIS = {



    "Estados Unidos": 1.8,

    "Brasil": 0.7,

    "Europa": 1.6,

    "CanadÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡": 1.4,

    "Reino Unido": 1.7



}



# ============================================================

# CATEGORIAS

# ============================================================



CATEGORIAS = [



    "IMOVEIS",

    "LUXURY",

    "GALPOES",

    "PORTOS",

    "DOCAS",

    "ALUGUEL",

    "COMERCIAL",

    "RURAL"



]



# ============================================================

# DATABASES

# ============================================================



CLIENTES = []

SERVICOS = []

TICKETS = []

LOGS = []



# ============================================================

# LOG

# ============================================================



def registrar_log(evento):
    pass



    LOGS.append({



        "id": str(uuid.uuid4()),

        "timestamp": str(datetime.utcnow()),

        "evento": evento



    })



# ============================================================

# CADASTRO CLIENTE

# ============================================================



def cadastrar_cliente(



    nome,

    pais,

    email,

    categoria



):



    cliente = {



        "id": f"IOT-{uuid.uuid4().hex[:8].upper()}",

        "nome": nome,

        "pais": pais,

        "email": email,

        "categoria": categoria,

        "timestamp": str(datetime.utcnow())



    }



    CLIENTES.append(cliente)



    registrar_log(

        f"CLIENTE CADASTRADO -> {nome}"

    )



    return cliente



# ============================================================

# CALCULO TICKET

# ============================================================



def calcular_ticket(



    valor_base,

    complexidade,

    pais,

    risco,

    mercado



):



    peso = PESO_PAIS.get(pais, 1.0)



    ticket = (

        valor_base

        * complexidade

        * peso

        * risco

        * mercado

    )



    return round(ticket, 2)



# ============================================================

# CONVERSAO

# ============================================================



def converter_moeda(



    valor_usd,

    moeda



):



    taxa = MOEDAS.get(moeda, 1)



    return round(valor_usd * taxa, 2)



# ============================================================

# GERAR SERVICO

# ============================================================



def gerar_servico(



    cliente,

    categoria,

    descricao,

    valor_base,

    complexidade,

    risco,

    mercado,

    moeda



):



    ticket_usd = calcular_ticket(



        valor_base,

        complexidade,

        cliente["pais"],

        risco,

        mercado



    )



    ticket_local = converter_moeda(



        ticket_usd,

        moeda



    )



    servico = {



        "id": f"SV-{uuid.uuid4().hex[:10].upper()}",

        "cliente": cliente["nome"],

        "pais": cliente["pais"],

        "categoria": categoria,

        "descricao": descricao,



        "ticket_usd": ticket_usd,

        "moeda_local": moeda,

        "ticket_local": ticket_local,



        "status": "EM ANALISE",



        "timestamp": str(datetime.utcnow())



    }



    SERVICOS.append(servico)



    TICKETS.append(ticket_usd)



    registrar_log(

        f"SERVICO GERADO -> {servico['id']}"

    )



    return servico



# ============================================================

# DASHBOARD

# ============================================================



def dashboard():
    pass



    receita_total = sum(TICKETS)



    print()

    print("===================================================")

    print(" IOTEC GLOBAL REALTY")

    print(" GLOBAL FINANCIAL CORE")

    print("===================================================")



    print()

    print(f"EMPRESA: {EMPRESA['nome']}")

    print(f"CNPJ: {EMPRESA['cnpj']}")

    print(f"EMAIL: {EMPRESA['email']}")



    print()

    print("===================================================")

    print(" OPERACOES")

    print("===================================================")



    print()

    print(f"CLIENTES: {len(CLIENTES)}")

    print(f"SERVICOS: {len(SERVICOS)}")



    print()

    print(

        f"RECEITA GLOBAL CONSOLIDADA: "

        f"US$ {receita_total:,.2f}"

    )



    print()

    print("===================================================")

    print(" SERVICOS")

    print("===================================================")



    for servico in SERVICOS:
        pass



        print()

        print(f"ID: {servico['id']}")

        print(f"CLIENTE: {servico['cliente']}")

        print(f"PAIS: {servico['pais']}")

        print(f"CATEGORIA: {servico['categoria']}")



        print(

            f"TICKET USD: "

            f"US$ {servico['ticket_usd']:,.2f}"

        )



        print(

            f"TICKET LOCAL: "

            f"{servico['ticket_local']:,.2f} "

            f"{servico['moeda_local']}"

        )



# ============================================================

# EXPORTAR

# ============================================================



def exportar():
    pass



    relatorio = {



        "empresa": EMPRESA,

        "clientes": CLIENTES,

        "servicos": SERVICOS,

        "logs": LOGS



    }



    with open(



        "IOTEC_GLOBAL_FINANCIAL_CORE.json",

        "w",

        encoding="utf-8"



    ) as arquivo:



        json.dump(



            relatorio,

            arquivo,

            indent=4,

            ensure_ascii=False



        )



    print()

    print("===================================================")

    print(" EXPORTACAO")

    print("===================================================")



    print()

    print(

        "ARQUIVO -> "

        "IOTEC_GLOBAL_FINANCIAL_CORE.json"

    )



# ============================================================

# SIMULACAO

# ============================================================



cliente1 = cadastrar_cliente(



    "Fagner Saraiva Realty",

    "Estados Unidos",

    "fagner@realty.com",

    "LUXURY"



)



cliente2 = cadastrar_cliente(



    "North Port Logistics",

    "Europa",

    "north@ports.com",

    "PORTOS"



)



servico1 = gerar_servico(



    cliente1,

    "LUXURY",

    "Sistema premium imobiliario",

    5000,

    1.8,

    1.4,

    1.5,

    "USD"



)



servico2 = gerar_servico(



    cliente2,

    "PORTOS",

    "Analytics logistico portuario",

    12000,

    2.2,

    1.7,

    1.8,

    "EUR"



)



# ============================================================

# EXECUCAO

# ============================================================



dashboard()



exportar()



print()

print("===================================================")

print(" NUCLEO FINALIZADO")

print("===================================================")





