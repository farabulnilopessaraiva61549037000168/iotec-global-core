
async function sendLead() {

    const payload = {

        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        company: document.getElementById("company").value,
        whatsapp: document.getElementById("whatsapp").value,
        service: document.getElementById("service").value,
        message: document.getElementById("message").value,
        origin: "NETLIFY"

    };

    const response = await fetch(

        "https://YOUR-RENDER-URL.onrender.com/new-lead",

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

        "OPERATION RECEIVED\n\n" +
        "PROTOCOL: " + result.protocol + "\n" +
        "PIPELINE: " + result.pipeline + "\n" +
        "PRIORITY: " + result.priority

    );

}

