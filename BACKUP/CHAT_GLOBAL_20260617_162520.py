import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
function enviar(){

    let cmd = document.getElementById("cmd").value;



    fetch("http://localhost:5000/comando", {

        method:"POST",

        headers:{"Content-Type":"application/json"},

        body:JSON.stringify({comando:cmd})

    })

    .then(res => res.json())

    .then(data => {

        alert(data.resposta);

    });

}





