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
    pass

    locais = [

        "C:\\IoTec\\interfaces_origem",

        os.path.join(os.environ["USERPROFILE"], "Desktop", "OFICINA_IOTEC")

    ]



    arquivos = []



    for local in locais:
        pass

        if os.path.exists(local):
            pass

            for root, dirs, files in os.walk(local):
                pass

                for file in files:
                    pass

                    if file.endswith((".html", ".htm")):
                        pass

                        arquivos.append(os.path.join(root, file))



    print(f"{len(arquivos)} interfaces disponÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­veis")

    return arquivos









def exibir_interface(caminho):
    pass

    try:
        pass

        url = "file:///" + caminho.replace("\", "/")

        webbrowser.open(url)

    except:
        pass

        pass





def log_iotec(msg):
    pass

    with open("C:\\IoTec\\log_rotacao.txt", "a", encoding="utf-8") as f:
        pass

        f.write(msg + "\n")





def modo_rotacao():
    pass

    print("\nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â½ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ Modo rotaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o ativado\n")



    while True:
        pass

        interfaces = listar_interfaces()



        if not interfaces:
            pass

            print("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã¢â‚¬Å¡ ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¯ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â Nenhuma interface disponÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­vel")

            time.sleep(5)

            continue



        escolhida = escolher_inteligente(interfaces)



        print(f"ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â½ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¯ Interface ativa: {os.path.basename(escolhida)}")



        processar_interface(escolhida)

        exibir_interface(escolhida)

        log_iotec(escolhida)



        time.sleep(10)



return destino





if __name__ == "__main__":
    pass

    modo_rotacao()





def processar_interface(arq):
    pass

    import os



    nome = os.path.basename(arq)



    with open(arq, "r", encoding="utf-8") as f:
        pass

        conteudo = f.read()



    injecao = """<script>console.log("IoTec ativo");</script>"""



    if "</body>" in conteudo:
        pass

        conteudo = conteudo.replace("</body>", injecao + "\n</body>")



    destino = os.path.join("C:\\IoTec", "oficina_" + nome)



    with open(destino, "w", encoding="utf-8") as f:
        pass

        f.write(conteudo)



    return destino










