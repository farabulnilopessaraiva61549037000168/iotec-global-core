import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os

import re



def periciar_interface(conteudo):
    pass

    relatorio = []



    if "<button" in conteudo:
        pass

        relatorio.append("Possui botÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âµes")



    if "onclick" in conteudo:
        pass

        relatorio.append("Possui eventos de clique")



    if "<form" in conteudo:
        pass

        relatorio.append("Possui formulÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡rios")



    if "http" in conteudo:
        pass

        relatorio.append("Possui links externos")



    return relatorio





def reconstruir_interface(conteudo):
    pass

    # remove chamadas externas

    conteudo = re.sub(r'onclick=".*?"', 'onclick="ativarNucleo()"', conteudo)



    # remove links externos

    conteudo = re.sub(r'href="http.*?"', 'href="#"', conteudo)



    return conteudo





def processar_interface(arq):
    pass

    nome = os.path.basename(arq)



    with open(arq, "r", encoding="utf-8") as f:
        pass

        conteudo = f.read()



    # ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â PERÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂCIA

    relatorio = periciar_interface(conteudo)

    print(f"ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â PerÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­cia ({nome}):", relatorio)



    # ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ'Ã¢â‚¬Å¡ RECONSTRUÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

    conteudo = reconstruir_interface(conteudo)



    # ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã¢â‚¬Å¡  INJEÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O DO NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡CLEO

    injecao = """

<script>

function ativarNucleo(){

    alert("IoTec nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleo ativado");

}

</script>

"""



    if "</body>" in conteudo:
        pass

        conteudo = conteudo.replace("</body>", injecao + "\n</body>")



    destino = os.path.join("C:\\IoTec", "oficina_" + nome)



    with open(destino, "w", encoding="utf-8") as f:
        pass

        f.write(conteudo)



    return destino






