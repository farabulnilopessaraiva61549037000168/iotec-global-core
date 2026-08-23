import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def processar_interface(arq):
    nome = os.path.basename(arq)

    with open(arq, "r", encoding="utf-8") as f:
        conteudo = f.read()

    # =========================
    # INJEÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DO NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO (BACKDOOR CONTROLADO)
    # =========================
    injecao = """
<script>
document.addEventListener("DOMContentLoaded", function(){

    console.log("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Âµ IoTec nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo ativo");

    // Exemplo: interceptar botÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes
    document.querySelectorAll("button").forEach(btn => {
        btn.addEventListener("click", function(e){
            console.log("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Clique interceptado:", this.innerText);
        });
    });

    // Exemplo: aplicar estilo dinÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢mico
    document.body.style.transition = "0.3s";
    document.body.style.background = "#0D0D0D";
    document.body.style.color = "#F5F5F5";

});
</script>
"""

    # injeta antes de fechar o body
    if "</body>" in conteudo:
        conteudo = conteudo.replace("</body>", injecao + "\n</body>")

    # salva versÃƒÆ'Ã†â€™o modificada
    destino = os.path.join("C:\\IoTec", "oficina_" + nome)

    with open(destino, "w", encoding="utf-8") as f:
        f.write(conteudo)

    return destino


