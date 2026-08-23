import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
<script>
// ===============================
// CONTEÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡DO REAL DOS SERVIÃƒÆ'Ã†â€™OS
// ===============================

function abrirServico(nome) {

    let conteudo = "";

    if (nome.includes("auditoria")) {
        conteudo = `
        <h1>Auditoria TecnolÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³gica</h1>
        <p>DiagnÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³stico completo da infraestrutura digital.</p>
        <ul>
            <li>AnÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise de sistemas</li>
            <li>Mapeamento de falhas</li>
            <li>Plano de otimizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o</li>
        </ul>
        `;
    }

    else if (nome.includes("pericia")) {
        conteudo = `
        <h1>PerÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­cia TÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©cnica Judicial</h1>
        <p>Laudos tÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©cnicos para processos judiciais.</p>
        `;
    }

    else if (nome.includes("desenvol")) {
        conteudo = `
        <h1>Desenvolvimento Sob Medida</h1>
        <p>Sistemas personalizados para sua empresa.</p>
        `;
    }

    else if (nome.includes("seguran")) {
        conteudo = `
        <h1>SeguranÃƒÆ'Ã†â€™a da InformaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o</h1>
        <p>ProteÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o completa de dados e sistemas.</p>
        `;
    }

    else if (nome.includes("dados") || nome.includes("business")) {
        conteudo = `
        <h1>Business Intelligence</h1>
        <p>AnÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise estratÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©gica de dados.</p>
        `;
    }

    abrirPainel(conteudo);
}

// ATIVA TODOS OS "SAIBA MAIS"
document.querySelectorAll("a, button").forEach(el => {

    el.addEventListener("click", function(e) {

        let texto = (this.innerText || "").toLowerCase();

        if (texto.includes("saiba")) {
            e.preventDefault();
            abrirServico(texto);
        }

    });

});
</script>



