async function sendOrder(data){

    try{

        const response = await fetch(

            "http://127.0.0.1:8000/api/orders",

            {

                method:"POST",

                headers:{
                    "Content-Type":"application/json"
                },

                body:JSON.stringify(data)

            }

        );

        const result = await response.json();

        console.log(
            "IOTEC ORDER SENT",
            result
        );

        alert(
            "Solicitação enviada para a Central IOTEC"
        );

    }

    catch(error){

        console.error(
            "ERRO CORE",
            error
        );

        alert(
            "Falha ao conectar com núcleo operacional"
        );

    }

}