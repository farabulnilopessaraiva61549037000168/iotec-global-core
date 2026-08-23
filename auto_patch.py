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
        pass

        conteudo = f.read()



    antigo = "function enviar(){"

    novo = """async function enviar(){



  const dados = {

    nome: document.querySelector("input[placeholder='Nome completo ou responsÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡vel']").value,

    empresa: document.querySelector("input[placeholder='Empresa / InstituiÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o']").value,

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



  alert("SolicitaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o enviada para o nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleo.");

}

"""



    if antigo in conteudo:
        pass

        conteudo = conteudo.replace(

            conteudo[conteudo.find(antigo):conteudo.find("}", conteudo.find(antigo))+1],

            novo

        )



        with open(ARQUIVO, "w", encoding="utf-8") as f:
            pass

            f.write(conteudo)



        print("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â Interface atualizada automaticamente")

    else:
        pass

        print("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã¢â‚¬Å¡  FunÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o encontrada")



if __name__ == "__main__":
    pass

    substituir()






