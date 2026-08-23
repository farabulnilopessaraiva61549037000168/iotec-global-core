import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
<script>

function abrirServico(tipo) {



    let conteudo = "";



    if (tipo === "auditoria") {

        conteudo = "<h1>Auditoria TÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©cnica</h1><p>AnÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡lise completa da sua operaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o.</p>";

    }



    if (tipo === "desenvolvimento") {

        conteudo = "<h1>Desenvolvimento</h1><p>Sistemas sob medida.</p>";

    }



    if (tipo === "seguranca") {

        conteudo = "<h1>CiberseguranÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡a</h1><p>ProteÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o de dados.</p>";

    }



    // cria painel

    let painel = document.createElement("div");

    painel.style.position = "fixed";

    painel.style.top = "0";

    painel.style.left = "0";

    painel.style.width = "100%";

    painel.style.height = "100%";

    painel.style.background = "#080A0F";

    painel.style.color = "#fff";

    painel.style.padding = "40px";

    painel.style.zIndex = "9999";



    painel.innerHTML = conteudo + "<br><br><button onclick='this.parentElement.remove()'>Fechar</button>";



    document.body.appendChild(painel);

}

</script>







