function enviar(){
let entrada = document.getElementById("input").value;

fetch("http://localhost:5000/processar", {
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({pedido:entrada})
})
.then(res=>res.json())
.then(data=>{
document.getElementById("resposta").innerText=data.resposta;
});
}

