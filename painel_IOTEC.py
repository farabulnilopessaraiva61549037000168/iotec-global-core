import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
<h1>Painel IOTEC</h1>



<button onclick="carregar()">Atualizar</button>



<h2>Pagamentos</h2>

<pre id="pagamentos"></pre>



<h2>Pedidos</h2>

<pre id="pedidos"></pre>



<script>

async function carregar() {

    try {

        let p = await fetch("file:///C:/IOTEC/financeiro/livro_caixa.json");

        let pagamentos = await p.text();

        document.getElementById("pagamentos").innerText = pagamentos;



        let ped = await fetch("file:///C:/IOTEC/pedidos/");

        document.getElementById("pedidos").innerText = "Veja pasta pedidos";



    } catch(e) {

        document.getElementById("pagamentos").innerText = "Erro ao carregar";

    }

}

</script>







