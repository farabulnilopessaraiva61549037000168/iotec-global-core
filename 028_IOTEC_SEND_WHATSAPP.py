import os
import subprocess
import sys

def preparar_e_disparar(numero_destino):
    js_code = f"""const {{ default: makeWASocket, useMultiFileAuthState }} = require('@whiskeysockets/baileys');

async function enviarApresentacao() {{
    const {{ state, saveCreds }} = await useMultiFileAuthState('C:/IOTEC/auth_info_baileys');
    const sock = makeWASocket({{
        auth: state,
        printQRInTerminal: false
    }});

    sock.ev.on('creds.update', saveCreds);

    sock.ev.on('connection.update', async (update) => {{
        const {{ connection }} = update;
        if (connection === 'open') {{
            const jid = '{numero_destino}@s.whatsapp.net';
            const mensagem = `*IOTEC GLOBAL — Usina Digital 24/7* 🚀\\n\\n` +
                `Prezado(a),\\n\\n` +
                `Apresentamos a *IOTEC*, uma infraestrutura de automação e inteligência B2B que opera no modelo *Follow-the-Sun* (24h/7d across fusos das Américas, Europa e Ásia/Oceania).\\n\\n` +
                `📌 *Destaques do Núcleo:*\\n` +
                `• Atendimento & Qualificação 24/7 na Sala Virtual.\\n` +
                `• Telemetria ao vivo de métricas e webhooks em Produção Real.\\n` +
                `• Resiliência de infraestrutura com persistência atômica.\\n\\n` +
                `📄 *Para interagir com a Sala Virtual, responda com:* */investor*\\n\\n` +
                `Atenciosamente,\\n` +
                `*Bruno — Founder & Core Developer*\\n` +
                `IOTEC (CNPJ: 61.549.037/0001-68)`;

            await sock.sendMessage(jid, {{ text: mensagem }});
            console.log('[OK] Mensagem de apresentacao enviada com sucesso!');
            process.exit(0);
        }}
    }});
}}

enviarApresentacao();
"""
    
    with open(r"C:\IOTEC\temp_dispatch.js", "w", encoding="utf-8") as f:
        f.write(js_code)
    
    print(f"[IOTEC] Disparando apresentação oficial para {numero_destino}...")
    subprocess.run(["node", r"C:\IOTEC\temp_dispatch.js"])

if __name__ == "__main__":
    num = sys.argv[1] if len(sys.argv) > 1 else "5588999999999"
    preparar_e_disparar(num)
