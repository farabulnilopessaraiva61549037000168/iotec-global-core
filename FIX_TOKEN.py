import sys

print("\n=== REGISTRO DIRETO DE CHAVE ASAAS ===")
token = input("Cole sua chave Asaas completa aqui e pressione ENTER: ").strip()

with open(r"C:\IOTEC\token.txt", "wb") as f:
    f.write(token.encode("utf-8"))

print(" [✔] Token gravado direto da memória no token.txt sem alteração do terminal!")
