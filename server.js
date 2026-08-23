const express = require('express');
const path = require('path');
require('dotenv').config();

const app = express();
app.use(express.json());
app.use(express.static(path.join(__dirname)));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Rota de captura e entrega automática do Token de Dados
app.post('/api/orders/capture', (req, res) => {
    const { orderID, customerDetails } = req.body;
    const dataAccessToken = "DATA-GLOBAL-" + Math.random().toString(36).substring(2, 10).toUpperCase();

    console.log("\n========================================");
    console.log("✅ TRANSACÃO INTERNACIONAL APROVADA!");
    console.log("🆔 Order ID PayPal: " + orderID);
    console.log("🔑 Token de Acesso Gerado: " + dataAccessToken);
    console.log("========================================\n");

    res.json({
        success: true,
        message: "Pagamento aprovado e dados liberados!",
        orderID: orderID,
        token: dataAccessToken
    });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log('🚀 Locomotiva rodando em http://localhost:' + PORT));
