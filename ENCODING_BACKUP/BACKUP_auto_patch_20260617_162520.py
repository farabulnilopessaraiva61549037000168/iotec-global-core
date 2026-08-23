import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os

ARQUIVO = "C:\\IOTEC\\CORE\\interface_profissional.html"

def substituir():
    pass

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        conteudo = f.read()

    antigo = "function enviar(){"
    novo = """async function enviar(){

  const dados = {
    nome: document.querySelector("input[placeholder='Nome completo ou responsÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡vel']").value,
    empresa: document.querySelector("input[placeholder='Empresa / InstituiÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o']").value,
    email: document.querySelector("input[type='email']").value,
    telefone: document.querySelector("input[placeholder='Telefone']").value,
    setor: document.querySelector("select").value,
    problema: document.querySelector("textarea").value
  };

  await fetch("http://127.0.0.1:5000/enviar", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(dados)
  });

  alert("SolicitaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o enviada para o nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo.");
}
"""

    if antigo in conteudo:
        conteudo = conteudo.replace(
            conteudo[conteudo.find(antigo):conteudo.find("}", conteudo.find(antigo))+1],
            novo
        )

        with open(ARQUIVO, "w", encoding="utf-8") as f:
            f.write(conteudo)

        print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Interface atualizada automaticamente")
    else:
        print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡  FunÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o nÃƒÆ'Ã†â€™o encontrada")

if __name__ == "__main__":
    substituir()


