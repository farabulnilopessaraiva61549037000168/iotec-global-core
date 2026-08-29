import os

token_correto = input("Cole a sua chave de API do Asaas e aperte ENTER: ").strip()

with open(r"C:\IOTEC\token.txt", "w", encoding="utf-8") as f:
    f.write(token_correto)

print("\n [✔] Token gravado com 100% de precisão no arquivo token.txt!")
