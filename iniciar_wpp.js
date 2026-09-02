const wppconnect = require('@wppconnect-team/wppconnect');
const express = require('express');

let wppClient = null;

wppconnect.create({
    session: 'iotec-session',
    autoClose: false,
    headless: false,
    statusFind: false,
    puppeteerOptions: {
        executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    },
    logQR: true
})
.then((client) => {
    console.log('==================================================');
    console.log('✅ CONEXAO CONCLUIDA! PRONTO PARA ENVIOS');
    console.log('==================================================');
    wppClient = client;
})
.catch((erro) => {
    console.error('❌ Erro WPPConnect:', erro);
});

const app = express();
app.use(express.json());

app.post('/send-message', async (req, res) => {
    if (!wppClient) {
        return res.status(503).json({ status: 'error', message: 'Cliente aguardando inicializacao.' });
    }

    try {
        const { phone, message } = req.body;
        if (!phone || !message) {
            return res.status(400).json({ status: 'error', message: 'Campos phone e message sao obrigatorios.' });
        }

        const formattedPhone = phone.includes('@c.us') ? phone : phone + '@c.us';
        await wppClient.sendText(formattedPhone, message);
        return res.json({ status: 'success', message: 'Mensagem enviada com sucesso!' });
    } catch (error) {
        return res.status(500).json({ status: 'error', message: error.toString() });
    }
});

app.listen(21465, () => {
    console.log('🚀 Servidor HTTP rodando na porta 21465 (POST /send-message)');
});
