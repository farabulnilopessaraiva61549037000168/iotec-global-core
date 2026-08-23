// FRONT_BRIDGE.js

async function sendLead() {

    const payload = {

        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        service: document.getElementById("service").value,
        message: document.getElementById("message").value,
        origin: "NETLIFY"

    };

    const response = await fetch(

        "http://127.0.0.1:3000/new-lead",

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

        "REQUEST RECEIVED\n" +
        "PROTOCOL: " + result.protocol + "\n" +
        "SECTOR: " + result.sector + "\n" +
        "SCORE: " + result.score

    );
}