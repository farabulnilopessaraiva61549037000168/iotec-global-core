import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =========================================================

# IOTEC AUTO PORT CONFIG

# CONFIGURADOR AUTOMATICO DE PORTAS

# =========================================================



import socket

import os

import re



# =========================================================

# PORTAS RESTRITAS

# =========================================================



PORTAS_RESTRITAS = [



    20,

    21,

    22,

    23,

    25,

    53,

    110,

    111,

    135,

    139,

    143,

    389,

    443,

    445,

    465,

    587,

    993,

    995,

    1723,

    5060,

    5061,

    6000,

    6665,

    6666,

    6667,

    6668,

    6669

]



# =========================================================

# VERIFICAR PORTA

# =========================================================



def porta_ocupada(porta):
    pass



    sock = socket.socket(

        socket.AF_INET,

        socket.SOCK_STREAM

    )



    resultado = sock.connect_ex(

        ('127.0.0.1', porta)

    )



    sock.close()



    return resultado == 0



# =========================================================

# BUSCAR PORTA LIVRE

# =========================================================



def buscar_porta():
    pass



    for porta in range(5000, 9000):
        pass



        if porta in PORTAS_RESTRITAS:
            pass

            continue



        if porta_ocupada(porta):
            pass

            continue



        return porta



    return None



# =========================================================

# ALTERAR PORTA AUTOMATICAMENTE

# =========================================================



def alterar_porta_arquivo(



    arquivo_py



):



    if not os.path.exists(arquivo_py):
        pass



        print("")

        print(f"ARQUIVO NAO ENCONTRADO:")

        print(arquivo_py)

        print("")



        return



    porta_segura = buscar_porta()



    if not porta_segura:
        pass



        print("")

        print("NENHUMA PORTA LIVRE")

        print("")



        return



    with open(



        arquivo_py,



        "r",



        encoding="utf-8"



    ) as f:



        conteudo = f.read()



    # PROCURA app.run(port=XXXX)

    conteudo = re.sub(



        r'port\s*=\s*\d+',



        f'port={porta_segura}',



        conteudo

    )



    with open(



        arquivo_py,



        "w",



        encoding="utf-8"



    ) as f:



        f.write(conteudo)



    print("")

    print("=" * 50)

    print(" PORTA ALTERADA AUTOMATICAMENTE ")

    print("=" * 50)

    print("")



    print(f"ARQUIVO: {arquivo_py}")

    print(f"NOVA PORTA: {porta_segura}")

    print("")



# =========================================================

# EXECUCAO

# =========================================================



if __name__ == '__main__':
    pass



    print("")

    print("=" * 50)

    print(" IOTEC AUTO PORT CONFIG ")

    print("=" * 50)

    print("")



    arquivo = input(



        "DIGITE O NOME DO ARQUIVO PY: "

    )



    alterar_porta_arquivo(arquivo)






