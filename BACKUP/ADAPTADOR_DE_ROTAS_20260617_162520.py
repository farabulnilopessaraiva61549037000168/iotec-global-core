import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
// ===============================

// IOTEC ADAPTADOR DE ROTAS

// ===============================



// intercepta todos os links

document.querySelectorAll('a').forEach(link => {

  link.addEventListener('click', function(e) {

    const href = this.getAttribute('href');



    if (!href) return;



    // sÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³ intercepta rotas do Replit

    if (href.startsWith('http') && href.includes('replit')) {

      e.preventDefault();



      if (href.includes('/servicos')) {

        window.location.href = 'servicos.html';

      }



      else if (href.includes('/diagnostico')) {

        window.location.href = 'diagnostico.html';

      }



      else if (href.includes('/portais')) {

        window.location.href = 'portais.html';

      }



      else {

        window.location.href = 'index.html';

      }

    }

  });

});





// ===============================

// SIMULAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O DO NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡CLEO

// ===============================

const NUCLEO = {

  diagnostico: function(texto) {

    return "DiagnÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³stico processado pelo nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleo IOTEC";

  }

};





// ===============================

// LIGAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O COM O TEXTAREA

// ===============================

const textarea = document.getElementById("diagTexto");

const resultado = document.getElementById("diagResults");



if (textarea && resultado) {

  textarea.addEventListener("blur", () => {

    const resposta = NUCLEO.diagnostico(textarea.value);

    resultado.innerHTML = `<div style="padding:10px">${resposta}</div>`;

  });

}





