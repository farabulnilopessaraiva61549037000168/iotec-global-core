const { default: makeWASocket, useMultiFileAuthState, DisconnectReason } = require('@whiskeysockets/baileys');
const sqlite3 = require('sqlite3').verbose();
const qrcode = require('qrcode-terminal');

const db = new sqlite3.Database('C:\\IOTEC\\iotec_kernel.db');

async function iniciarNodeJonas() {
    const { state, saveCreds } = await useMultiFileAuthState('C:\\IOTEC\\auth_info_baileys');

    const sock = makeWASocket({
        auth: state
    });

    sock.ev.on('creds.update', saveCreds);

    sock.ev.on('connection.update', (update) => {
        const { connection, lastDisconnect, qr } = update;

        if (qr) {
            console.log('\n==================================================================');
            console.log(' [NODE-JONAS] ESCANEIE O QR CODE ABAIXO PARA CONECTAR O WHATSAPP');
            console.log('==================================================================\n');
            qrcode.generate(qr, { small: true });
        }

        if (connection === 'open') {
            console.log('\n[NODE-JONAS] SUCESSO: WhatsApp Conectado e Sessão Salva com Sucesso!');
            console.log('[NODE-JONAS] A sessão ficará permanente em C:\\IOTEC\\auth_info_baileys\n');
            iniciarFilaAgendada(sock);
        } else if (connection === 'close') {
            const status = lastDisconnect?.error?.output?.statusCode;
            console.log(`[NODE-JONAS] Conexão encerrada (Status: ${status}). Reconectando...`);
            iniciarNodeJonas();
        }
    });
}

function iniciarFilaAgendada(sock) {
    setInterval(async () => {
        const agora = new Date();
        const hora = agora.getHours();
        const diaSemana = agora.getDay();

        // Horário comercial: Segunda a Sexta (08h-11h30 e 14h-17h)
        const horarioValido = (diaSemana >= 1 && diaSemana <= 5) && 
                              ((hora >= 8 && hora < 12) || (hora >= 14 && hora < 17));

        if (!horarioValido) {
            console.log('[NODE-JONAS] Fora do expediente comercial. Disparos agendados em espera.');
            return;
        }

        db.get(`SELECT * FROM empresas_qualificadas WHERE status_qualificacao = 'APROVADO_PARA_DISPARO' LIMIT 1`, async (err, empresa) => {
            if (err || !empresa) return;

            db.run(`UPDATE empresas_qualificadas SET status_qualificacao = 'EM_PROCESSAMENTO' WHERE id = ?`, [empresa.id]);

            const numeroJid = `${empresa.cnpj.replace(/\D/g, '')}@s.whatsapp.net`;
            const mensagem = `Olá! Aqui é a Camila, da IOTEC. Mapeamos um gargalo na conciliação de recebíveis da ${empresa.razao_social}. Com quem eu conseguiria validar 2 minutos sobre isso por aqui?`;

            try {
                console.log(`[DISPARO] Enviando abordagem para: ${empresa.razao_social}...`);
                await sock.sendMessage(numeroJid, { text: mensagem });
                db.run(`UPDATE empresas_qualificadas SET status_qualificacao = 'ABORDADO' WHERE id = ?`, [empresa.id]);
                console.log(`[SUCESSO] Abordagem entregue para ${empresa.razao_social}.`);
            } catch (error) {
                console.log(`[ERRO] Falha no disparo para ${empresa.razao_social}:`, error);
                db.run(`UPDATE empresas_qualificadas SET status_qualificacao = 'FALHA_ENVIO' WHERE id = ?`, [empresa.id]);
            }
        });

    }, Math.floor(Math.random() * (120000 - 45000 + 1)) + 45000);
}

iniciarNodeJonas();
