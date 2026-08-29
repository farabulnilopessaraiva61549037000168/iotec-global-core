const wppconnect = require('@wppconnect-team/wppconnect');
const express = require('express');
const app = express();

// Aumenta limite do body para aceitar PDFs em Base64 grandes
app.use(express.json({ limit: '50mb' }));

let clientGlobal = null;
const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

wppconnect.create({
  session: 'iotec-session',
  autoClose: false,
  puppeteerOptions: {
    executablePath: chromePath,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  }
})
.then((client) => {
  clientGlobal = client;
  console.log('\n[✔] WPPCONNECT LOCAL ONLINE — PRONTO PARA DISPAROS!\n');
})
.catch((erro) => console.log('Erro ao inicializar WPPConnect:', erro));

// Função utilitária para tratamento e resolução de número
async function resolveNumber(phone) {
  let cleanPhone = phone.toString().replace(/\D/g, '');
  if (!cleanPhone.startsWith('55') && cleanPhone.length <= 11) {
    cleanPhone = '55' + cleanPhone;
  }
  let targetId = `${cleanPhone}@c.us`;
  try {
    const profile = await clientGlobal.checkNumberStatus(targetId);
    if (profile && profile.numberExists) {
      return profile.id._serialized || targetId;
    }
  } catch (e) {}
  return targetId;
}

// 1. Rota de Envio de Mensagem de Texto
app.post('/send-message', async (req, res) => {
  const { phone, message } = req.body;
  if (!clientGlobal) return res.status(503).json({ status: 'error', message: 'WhatsApp offline.' });

  try {
    const targetId = await resolveNumber(phone);
    const response = await clientGlobal.sendText(targetId, message);
    return res.status(200).json({ status: 'success', id: response.id, response });
  } catch (error) {
    return res.status(500).json({ status: 'error', error: error.toString() });
  }
});

// 2. Rota de Envio de Boletos e Documentos (PDF / Imagens / Base64)
app.post('/send-file', async (req, res) => {
  const { phone, filePath, filename, caption } = req.body;
  if (!clientGlobal) return res.status(503).json({ status: 'error', message: 'WhatsApp offline.' });

  try {
    const targetId = await resolveNumber(phone);
    // filePath pode ser um caminho local ("C:\\faturas\\boleto.pdf") ou Base64 ("data:application/pdf;base64,...")
    const response = await clientGlobal.sendFile(targetId, filePath, filename || 'documento.pdf', caption || '');
    return res.status(200).json({ status: 'success', id: response.id, response });
  } catch (error) {
    return res.status(500).json({ status: 'error', error: error.toString() });
  }
});

app.listen(21465, () => console.log('[🚀] API IOTEC WPPConnect rodando na porta 21465'));