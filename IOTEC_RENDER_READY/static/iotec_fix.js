document.addEventListener("DOMContentLoaded", function() {

    console.log("IOTEC MOTOR ATIVO");

    // Corrigir botões que não fazem nada
    document.querySelectorAll("button").forEach(btn => {
        btn.addEventListener("click", function() {
            console.log("Botão clicado:", btn.innerText);
        });
    });

    // Corrigir links mortos
    document.querySelectorAll("a").forEach(link => {
        if (link.getAttribute("href") === "#") {
            link.setAttribute("href", "/");
        }
    });

});

