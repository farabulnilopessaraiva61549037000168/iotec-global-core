import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =========================================================

# IOTEC PORT GUARD

# VERIFICADOR AUTOMATICO DE PORTAS

# =========================================================



import socket



# =========================================================

# PORTAS BLOQUEADAS PELO NAVEGADOR

# =========================================================



PORTAS_RESTRITAS = [



    1,

    7,

    9,

    11,

    13,

    15,

    17,

    19,

    20,

    21,

    22,

    23,

    25,

    37,

    42,

    43,

    53,

    69,

    77,

    79,

    87,

    95,

    101,

    102,

    103,

    104,

    109,

    110,

    111,

    113,

    115,

    117,

    119,

    123,

    135,

    137,

    139,

    143,

    161,

    179,

    389,

    427,

    465,

    512,

    513,

    514,

    515,

    526,

    530,

    531,

    532,

    540,

    548,

    554,

    556,

    563,

    587,

    601,

    636,

    993,

    995,

    1719,

    1720,

    1723,

    2049,

    3659,

    4045,

    5060,

    5061,

    6000,

    6566,

    6665,

    6666,

    6667,

    6668,

    6669

]



# =========================================================

# VERIFICAR PORTA OCUPADA

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

# BUSCAR PORTA SEGURA

# =========================================================



def buscar_porta_segura():
    pass



    print("")

    print("=" * 50)

    print(" IOTEC PORT GUARD ")

    print("=" * 50)

    print("")



    for porta in range(5000, 9000):
        pass



        # IGNORA PORTAS RESTRITAS

        if porta in PORTAS_RESTRITAS:
            pass

            continue



        # IGNORA PORTAS OCUPADAS

        if porta_ocupada(porta):
            pass

            continue



        print("")

        print(f"PORTA SEGURA ENCONTRADA: {porta}")

        print("")



        return porta



    print("")

    print("NENHUMA PORTA LIVRE ENCONTRADA")

    print("")



    return None



# =========================================================

# EXECUCAO

# =========================================================



if __name__ == '__main__':
    pass



    buscar_porta_segura()






