(function(){
    const output = document.getElementById("output");
    const mediaBox = document.getElementById("media-box");
    const mediaItems = window.IOTEC_MEDIA || [];
    let idx = 0;

    function setOutput(text){
        if(output){ output.textContent = text; }
    }

    function rotateMedia(){
        if(!mediaBox || mediaItems.length === 0) return;
        const item = mediaItems[idx % mediaItems.length];
        mediaBox.innerHTML = `
            <div class="media-title">${item.titulo || "Mensagem"}</div>
            <div class="media-text">${item.texto || ""}</div>
        `;
        idx += 1;
    }

    async function fetchJson(url, options){
        const res = await fetch(url, options || {});
        return await res.json();
    }

    window.rodarDiagnostico = async function(){
        setOutput("Executando diagnóstico...");
        try{
            const data = await fetchJson("/api/run-diagnostics");
            setOutput(JSON.stringify(data, null, 2));
        }catch(err){
            setOutput("Falha ao executar diagnóstico: " + err);
        }
    };

    window.abrirProtocolo = async function(categoria, descricao, camada){
        setOutput("Abrindo protocolo...");
        try{
            const data = await fetchJson("/api/open-ticket", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({
                    categoria: categoria,
                    descricao: descricao,
                    camada: camada
                })
            });
            setOutput(JSON.stringify(data, null, 2));
        }catch(err){
            setOutput("Falha ao abrir protocolo: " + err);
        }
    };

    rotateMedia();
    setInterval(rotateMedia, 5000);
})();
