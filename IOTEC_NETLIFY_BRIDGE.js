async function sendLead(event) {

    event.preventDefault();

    const payload = {

        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        company: document.getElementById("company").value,
        service: document.getElementById("service").value,
        message: document.getElementById("message").value,
        origin: "NETLIFY"

    };

    try {

        const response = await fetch(
            "https://SEU-BACKEND-RENDER.onrender.com/new-lead",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(payload)
            }
        );

        const result = await response.json();

        alert(
            "SOLICITAÇÃO RECEBIDA\n\n" +
            "PROTOCOLO: " + result.protocol + "\n" +
            "SETOR: " + result.sector + "\n" +
            "PRIORIDADE: " + result.priority
        );

    }
    catch(error){

        console.error(error);

        alert(
            "Falha ao enviar solicitação."
        );

    }

}