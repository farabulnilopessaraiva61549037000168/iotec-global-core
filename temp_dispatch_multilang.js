const { default: makeWASocket, useMultiFileAuthState, DisconnectReason } = require('@whiskeysockets/baileys');
const pino = require('pino');

async function enviar() {
    const { state, saveCreds } = await useMultiFileAuthState('C:/IOTEC/auth_info_baileys');
    const sock = makeWASocket({
        auth: state,
        logger: pino({ level: 'silent' }),
        printQRInTerminal: false
    });

    sock.ev.on('creds.update', saveCreds);

    sock.ev.on('connection.update', async (update) => {
        const { connection, lastDisconnect } = update;
        if (connection === 'open') {
            const jid = '49301234567@s.whatsapp.net';
            await sock.sendMessage(jid, { text: `*IOTEC GLOBAL — Digitales System 24/7* 🚀

Sehr geehrte Damen und Herren,

Wir präsentieren *IOTEC*, eine B2B-Automatisierungs- und Intelligenzinfrastruktur, die nach dem *Follow-the-Sun*-Modell arbeitet (24/7 Abdeckung über Amerika, Europa und Asien/Ozeanien).

📌 *Kern-Highlights:*
• 24/7-Qualifizierung im Virtuellen Investorenraum.
• Live-Telemetrie von Echtzeit-Metriken im Produktionsmodus.
• Hochverfügbare Infrastruktur mit atomarer Datenpersistenz.

📄 *Antworten Sie mit folgendem Befehl, um zu starten:* */investor*

Mit freundlichen Grüßen,
*Bruno — Founder & Core Developer*
IOTEC (CNPJ: 61.549.037/0001-68)` });
            console.log('[OK] Mensagem entregue com sucesso em DE para 49301234567');
            process.exit(0);
        } else if (connection === 'close') {
            const shouldReconnect = (lastDisconnect?.error)?.output?.statusCode !== DisconnectReason.loggedOut;
            if (shouldReconnect) {
                enviar();
            }
        }
    });
}
enviar();
