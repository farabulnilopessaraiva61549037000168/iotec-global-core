// NETLIFY_REAL_BRIDGE.js

async function sendLead() {

    const payload = {

        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        service: document.getElementById("service").value,
        message: document.getElementById("message").value,
        origin: "NETLIFY"

    };

    try {

        const response = await fetch(

            "https://SEU_RENDER_URL.onrender.com/new-lead",

            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(payload)
            }
        );

        const result = await response.json();

        console.log(result);

        alert(

            "REQUEST RECEIVED\n\n" +
            "PROTOCOL: " + result.protocol + "\n" +
            "SECTOR: " + result.sector + "\n" +
            "SCORE: " + result.score

        );

        document.getElementById("name").value = "";
        document.getElementById("email").value = "";
        document.getElementById("service").value = "";
        document.getElementById("message").value = "";

    } catch(error) {

        console.error(error);

        alert(
            "CONNECTION ERROR WITH CONTROL TOWER"
        );
    }
}