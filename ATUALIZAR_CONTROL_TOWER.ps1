$path="C:\IOTEC_OMEGA_X\CONTROL_TOWER\index.html"

if(Test-Path $path){

Write-Host "Localizado CONTROL TOWER"

$content = Get-Content $path -Raw


$inserir = @"

<div id="iotec-monitor">

<h1>
IOTEC OMEGA X - CONTROL TOWER
</h1>

<h2>
PAINEL OPERACIONAL DO NÚCLEO
</h2>

<div>
Status:
<span id="status">
Aguardando núcleo...
</span>
</div>


<div>
Último evento:
<span id="evento">
Nenhum evento recebido
</span>
</div>


<div>
Alertas:
<span id="alerta">
Nenhum alerta
</span>
</div>


</div>


<script>

async function atualizarNucleo(){

try{

let resposta =
await fetch(
"http://192.168.0.102:5001/eventos"
);


let dados =
await resposta.json();


let eventos =
dados.eventos;


if(eventos.length>0){

let ultimo =
eventos[eventos.length-1];


document.getElementById("evento")
.innerHTML =
ultimo.descricao;


document.getElementById("alerta")
.innerHTML =
ultimo.prioridade;


document.getElementById("status")
.innerHTML =
"NÚCLEO ONLINE";

}


}

catch(e){

document.getElementById("status")
.innerHTML =
"NÚCLEO NÃO RESPONDENDO";

}


}


setInterval(
atualizarNucleo,
5000
);


atualizarNucleo();


</script>

"@


$content += $inserir


Set-Content `
$path `
$content `
-Encoding UTF8


Write-Host "CONTROL TOWER atualizada com sucesso"

}

else{

Write-Host "Arquivo CONTROL TOWER não encontrado"

}