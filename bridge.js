// bridge.js

async function sendEvent() {

    const payload = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        service: document.getElementById("service").value,
        message: document.getElementById("message").value
    };

    const response = await fetch(
        "http://127.0.0.1:3000/new-event",
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
        "EVENT SENT TO CONTROL TOWER\nPROTOCOL: "
        + result.protocol
    );
}