import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================

# IOTEC GLOBAL ASSETS EXCHANGE

# EMPRESA: IOTEC

# MODO: INTERMEDIAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O INTELIGENTE DE ATIVOS

# PLATAFORMA: GLOBAL BROKER CORE

# ============================================================



from datetime import datetime

import uuid

import json

import random



# ============================================================

# IDENTIDADE CORPORATIVA

# ============================================================



EMPRESA = {



    "nome": "IOTEC GLOBAL ASSETS EXCHANGE",

    "cnpj": "00.000.000/0001-00",

    "email": "contato@iotecglobal.com",

    "suporte": "support@iotecglobal.com",

    "pais_base": "Brasil",

    "modo_operacional": "INTERMEDIAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O INTELIGENTE",

    "status": "ONLINE",

    "fundacao": str(datetime.utcnow())



}



# ============================================================

# SETORES OPERACIONAIS

# ============================================================



SETORES = [



    "IMOVEIS",

    "LEILOES_STORAGE",

    "ATIVOS_COMERCIAIS",

    "MAQUINARIO_AGRICOLA",

    "VEICULOS_ESPECIAIS",

    "GALPOES_LOGISTICOS",

    "TERRENOS",

    "ATIVOS_RURAIS"



]



# ============================================================

# TORRE DE CONTROLE

# ============================================================



TORRE_CONTROLE = {



    "clientes_ativos": 0,

    "ativos_monitorados": 0,

    "comissao_prevista": 0,

    "negocios_fechados": 0,

    "operacoes_em_andamento": 0,

    "regioes_monitoradas": []



}



# ============================================================

# BANCO DE CLIENTES

# ============================================================



CLIENTES = []



# ============================================================

# BANCO DE ATIVOS

# ============================================================



ATIVOS = []



# ============================================================

# BANCO DE LOGS

# ============================================================



LOGS = []



# ============================================================

# REGISTRAR LOG

# ============================================================



def registrar_log(evento):
    pass



    LOGS.append({



        "id": str(uuid.uuid4()),

        "timestamp": str(datetime.utcnow()),

        "evento": evento



    })



# ============================================================

# CADASTRO DE CLIENTE

# ============================================================



def cadastrar_cliente(nome, pais, perfil):
    pass



    cliente = {



        "id": str(uuid.uuid4()),

        "nome": nome,

        "pais": pais,

        "perfil": perfil,

        "data": str(datetime.utcnow())



    }



    CLIENTES.append(cliente)



    TORRE_CONTROLE["clientes_ativos"] += 1



    registrar_log(

        f"NOVO CLIENTE -> {nome}"

    )



# ============================================================

# CADASTRO DE ATIVO

# ============================================================



def cadastrar_ativo(



    tipo,

    titulo,

    localizacao,

    valor,

    setor



):



    ativo = {



        "id": str(uuid.uuid4()),

        "tipo": tipo,

        "titulo": titulo,

        "localizacao": localizacao,

        "valor": valor,

        "setor": setor,

        "status": "DISPONIVEL",

        "timestamp": str(datetime.utcnow())



    }



    ATIVOS.append(ativo)



    TORRE_CONTROLE["ativos_monitorados"] += 1



    registrar_log(

        f"ATIVO CADASTRADO -> {titulo}"

    )



# ============================================================

# MOTOR DE COMISSÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

# ============================================================



def calcular_comissao(valor):
    pass



    percentual = 0.05



    return valor * percentual



# ============================================================

# SIMULAR NEGÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"CIO

# ============================================================



def fechar_negocio(ativo_id, cliente_nome):
    pass



    for ativo in ATIVOS:
        pass



        if ativo["id"] == ativo_id:
            pass



            ativo["status"] = "NEGOCIADO"



            comissao = calcular_comissao(

                ativo["valor"]

            )



            TORRE_CONTROLE["comissao_prevista"] += comissao



            TORRE_CONTROLE["negocios_fechados"] += 1



            registrar_log(

                f"NEGOCIO FECHADO -> "

                f"{ativo['titulo']} | "

                f"CLIENTE: {cliente_nome}"

            )



            print("\n================================================")

            print(" NEGÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"CIO FECHADO")

            print("================================================")



            print(f"\nATIVO: {ativo['titulo']}")

            print(f"CLIENTE: {cliente_nome}")

            print(f"COMISSÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O: US$ {comissao:,.2f}")



# ============================================================

# TORRE EXECUTIVA

# ============================================================



def torre_executiva():
    pass



    print("\n================================================")

    print(" IOTEC GLOBAL BROKER CORE")

    print("================================================")



    print(f"\nEMPRESA: {EMPRESA['nome']}")

    print(f"CNPJ: {EMPRESA['cnpj']}")

    print(f"E-MAIL: {EMPRESA['email']}")



    print("\n================================================")

    print(" TORRE DE CONTROLE")

    print("================================================")



    print(

        f"\nCLIENTES ATIVOS: "

        f"{TORRE_CONTROLE['clientes_ativos']}"

    )



    print(

        f"ATIVOS MONITORADOS: "

        f"{TORRE_CONTROLE['ativos_monitorados']}"

    )



    print(

        f"NEGÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"CIOS FECHADOS: "

        f"{TORRE_CONTROLE['negocios_fechados']}"

    )



    print(

        f"COMISSÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O PREVISTA: "

        f"US$ {TORRE_CONTROLE['comissao_prevista']:,.2f}"

    )



# ============================================================

# RELATÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"RIO OPERACIONAL

# ============================================================



def exportar_relatorio():
    pass



    relatorio = {



        "empresa": EMPRESA,

        "torre_controle": TORRE_CONTROLE,

        "clientes": CLIENTES,

        "ativos": ATIVOS,

        "logs": LOGS



    }



    with open(



        "IOTEC_GLOBAL_BROKER_REPORT.json",

        "w",

        encoding="utf-8"



    ) as arquivo:



        json.dump(



            relatorio,

            arquivo,

            indent=4,

            ensure_ascii=False



        )



    print("\n================================================")

    print(" RELATÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"RIO EXPORTADO")

    print("================================================")



    print(

        "\nARQUIVO -> "

        "IOTEC_GLOBAL_BROKER_REPORT.json"

    )



# ============================================================

# DADOS INICIAIS

# ============================================================



def inicializar():
    pass



    cadastrar_cliente(



        "North Capital",

        "Estados Unidos",

        "INVESTIDOR"



    )



    cadastrar_cliente(



        "Florida Assets Group",

        "Estados Unidos",

        "CORRETORA"



    )



    cadastrar_ativo(



        "IMOVEL_COMERCIAL",

        "Shopping Plaza Miami",

        "Miami - Florida",

        2800000,

        "IMOVEIS"



    )



    cadastrar_ativo(



        "STORAGE_LEILAO",

        "Lote Premium Storage",

        "Texas",

        45000,

        "LEILOES_STORAGE"



    )



    cadastrar_ativo(



        "MAQUINARIO_AGRICOLA",

        "Trator Industrial X",

        "Kansas",

        180000,

        "MAQUINARIO_AGRICOLA"



    )



# ============================================================

# START

# ============================================================



if __name__ == "__main__":
    pass



    inicializar()



    torre_executiva()



    fechar_negocio(



        ATIVOS[0]["id"],

        "North Capital"



    )



    exportar_relatorio()



    print("\n================================================")

    print(" NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡CLEO FINALIZADO")

    print("================================================")




