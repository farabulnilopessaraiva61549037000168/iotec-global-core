import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import re

def periciar_interface(conteudo):
    relatorio = []

    if "<button" in conteudo:
        relatorio.append("Possui botÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes")

    if "onclick" in conteudo:
        relatorio.append("Possui eventos de clique")

    if "<form" in conteudo:
        relatorio.append("Possui formulÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rios")

    if "http" in conteudo:
        relatorio.append("Possui links externos")

    return relatorio


def reconstruir_interface(conteudo):
    # remove chamadas externas
    conteudo = re.sub(r'onclick=".*?"', 'onclick="ativarNucleo()"', conteudo)

    # remove links externos
    conteudo = re.sub(r'href="http.*?"', 'href="#"', conteudo)

    return conteudo


def processar_interface(arq):
    nome = os.path.basename(arq)

    with open(arq, "r", encoding="utf-8") as f:
        conteudo = f.read()

    # ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â PERÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂCIA
    relatorio = periciar_interface(conteudo)
    print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â PerÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­cia ({nome}):", relatorio)

    # ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â RECONSTRUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
    conteudo = reconstruir_interface(conteudo)

    # ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  INJEÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DO NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO
    injecao = """
<script>
function ativarNucleo(){
    alert("IoTec nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo ativado");
}
</script>
"""

    if "</body>" in conteudo:
        conteudo = conteudo.replace("</body>", injecao + "\n</body>")

    destino = os.path.join("C:\\IoTec", "oficina_" + nome)

    with open(destino, "w", encoding="utf-8") as f:
        f.write(conteudo)

    return destino


