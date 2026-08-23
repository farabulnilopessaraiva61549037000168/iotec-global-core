import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import json
import time

# DiretÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio onde os registros serÃƒÆ'Ã†â€™o armazenados
registro_path = "C:/Users/Bruno Lopes/Desktop/Neo_System_Core/conversa_log.json"

# FunÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o para registrar interaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes no sistema
def registrar_interacao(mensagem):
    data_hora = time.strftime('%Y-%m-%d %H:%M:%S')
    novo_registro = {"data_hora": data_hora, "mensagem": mensagem}

    # Carregar registros anteriores, se existirem
    if os.path.exists(registro_path):
        with open(registro_path, "r") as arquivo:
            registros = json.load(arquivo)
    else:
        registros = []

    registros.append(novo_registro)

    # Salvar novamente no arquivo JSON
    with open(registro_path, "w") as arquivo:
        json.dump(registros, arquivo, indent=4)

# FunÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o para revisar e organizar os registros
def revisar_pendencias():
    if not os.path.exists(registro_path):
        print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â¨ Nenhuma interaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o registrada ainda.\n")
        return

    with open(registro_path, "r") as arquivo:
        registros = json.load(arquivo)

    print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â **Revisando InteraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes e PendÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncias:**\n")
    for reg in registros:
        print(f"[{reg['data_hora']}] {reg['mensagem']}")

    print("\nÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ RevisÃƒÆ'Ã†â€™o concluÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­da! Tudo organizado.\n")

# Registrar novas interaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes
registrar_interacao("Sistema de monitoramento iniciado e verificando pendÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncias.")

# Revisar registros existentes
revisar_pendencias()


