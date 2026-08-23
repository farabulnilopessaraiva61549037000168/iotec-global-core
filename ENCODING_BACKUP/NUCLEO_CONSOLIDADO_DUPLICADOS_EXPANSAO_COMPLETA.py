import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import time
import random
import webbrowser

BASE = "C:\\IoTec"

def listar_interfaces():
    locais = [
        "C:\\IoTec\\interfaces_origem",
        os.path.join(os.environ["USERPROFILE"], "Desktop", "OFICINA_IOTEC")
    ]

    arquivos = []

    for local in locais:
        if os.path.exists(local):
            for root, dirs, files in os.walk(local):
                for file in files:
                    if file.endswith((".html", ".htm")):
                        arquivos.append(os.path.join(root, file))

    print(f"{len(arquivos)} interfaces disponÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­veis")
    return arquivos




def exibir_interface(caminho):
    try:
        url = "file:///" + caminho.replace("\", "/")
        webbrowser.open(url)
    except:
        pass


def log_iotec(msg):
    with open("C:\\IoTec\\log_rotacao.txt", "a", encoding="utf-8") as f:
        f.write(msg + "\n")


def modo_rotacao():
    print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â½Ãƒâ€šÃ‚Â¬ Modo rotaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o ativado\n")

    while True:
        interfaces = listar_interfaces()

        if not interfaces:
            print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Nenhuma interface disponÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vel")
            time.sleep(5)
            continue

        escolhida = escolher_inteligente(interfaces)

        print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â½Ãƒâ€šÃ‚Â¯ Interface ativa: {os.path.basename(escolhida)}")

        processar_interface(escolhida)
        exibir_interface(escolhida)
        log_iotec(escolhida)

        time.sleep(10)

return destino


if __name__ == "__main__":
    modo_rotacao()


def processar_interface(arq):
    import os

    nome = os.path.basename(arq)

    with open(arq, "r", encoding="utf-8") as f:
        conteudo = f.read()

    injecao = """<script>console.log("IoTec ativo");</script>"""

    if "</body>" in conteudo:
        conteudo = conteudo.replace("</body>", injecao + "\n</body>")

    destino = os.path.join("C:\\IoTec", "oficina_" + nome)

    with open(destino, "w", encoding="utf-8") as f:
        f.write(conteudo)

    return destino




