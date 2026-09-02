const { default: makeWASocket, useMultiFileAuthState } = require('@whiskeysockets/baileys');

async function enviarApresentacao() {
    const { state, saveCreds } = await useMultiFileAuthState('C:/IOTEC/auth_info_baileys');
    const sock = makeWASocket({
        auth: state,
        printQRInTerminal: false
    });

    sock.ev.on('creds.update', saveCreds);

    sock.ev.on('connection.update', async (update) => {
        const { connection } = update;
        if (connection === 'open') {
            const jid = '5588999999999@s.whatsapp.net';
            const mensagem = `*IOTEC GLOBAL — Usina Digital 24/7* 🚀\n\n` +
                `Prezado(a),\n\n` +
                `Apresentamos a *IOTEC*, uma infraestrutura de automação e inteligência B2B que opera no modelo *Follow-the-Sun* (24h/7d across fusos das Américas, Europa e Ásia/Oceania).\n\n` +
                `📌 *Destaques do Núcleo:*\n` +
                `• Atendimento & Qualificação 24/7 na Sala Virtual.\n` +
                `• Telemetria ao vivo de métricas e webhooks em Produção Real.\n` +
                `• Resiliência de infraestrutura com persistência atômica.\n\n` +
                `📄 *Para interagir com a Sala Virtual, responda com:* */investor*\n\n` +
                `Atenciosamente,\n` +
                `*Bruno — Founder & Core Developer*\n` +
                `IOTEC (CNPJ: 61.549.037/0001-68)`;

            await sock.sendMessage(jid, { text: mensagem });
            console.log('[OK] Mensagem de apresentacao enviada com sucesso!');
            process.exit(0);
        }
    });
}

enviarApresentacao();
