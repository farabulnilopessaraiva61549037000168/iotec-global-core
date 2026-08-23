import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
<select onchange="trocarIdioma(this.value)">
  <option value="pt">ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â· PT</option>
  <option value="en">ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂºÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¸ EN</option>
</select>

<script>
let idiomaAtual = "pt";

const textos = {
  pt: {
    painel: "Painel Central",
    pedidos: "Pedidos",
    enviar: "Enviar"
  },
  en: {
    painel: "Dashboard",
    pedidos: "Orders",
    enviar: "Send"
  }
};

function trocarIdioma(idioma){
  idiomaAtual = idioma;
  document.getElementById("titulo").innerText = textos[idioma].painel;
}
</script>



