document.addEventListener("DOMContentLoaded", function () {

    console.log("🔥 IOTEC ADAPTADOR ATIVO");

    let elementos = document.querySelectorAll("button, a, div");

    elementos.forEach(el => {

        el.addEventListener("click", function () {

            let texto = el.innerText || el.value || "ação desconhecida";

            let corpo = `
Origem: OFICINA_IOTEC
Ação: ${texto}
Hora: ${new Date().toLocaleString()}
`;

            window.location.href =
                "mailto:iotec.bl@proton.me?subject=INTERFACE_IOTEC&body=" + encodeURIComponent(corpo);

        });

    });

});
