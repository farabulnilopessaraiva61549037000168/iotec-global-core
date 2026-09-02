import sys
import subprocess

IDIOMAS_PAIS = {
    "55": "pt", "1": "en", "44": "en", "49": "de", 
    "971": "ar", "81": "ja", "65": "en", "61": "en"
}

MENSAGENS = {
    "pt": {
        "titulo": "*IOTEC GLOBAL — Usina Digital 24/7* 🚀",
        "saudacao": "Prezado(a),",
        "intro": "Apresentamos a *IOTEC*, uma infraestrutura de automação e inteligência B2B que opera no modelo *Follow-the-Sun* (24h/7d cobrindo os fusos das Américas, Europa e Ásia/Oceania).",
        "destaques": "📌 *Destaques do Núcleo:*\n• Atendimento & Qualificação 24/7 na Sala Virtual.\n• Telemetria ao vivo de métricas e webhooks em Produção Real.\n• Resiliência de infraestrutura com persistência atômica.",
        "call": "📄 *Para interagir com a Sala Virtual, responda com:* */investor*",
        "ass": "Atenciosamente,\n*Bruno — Founder & Core Developer*\nIOTEC (CNPJ: 61.549.037/0001-68)"
    },
    "en": {
        "titulo": "*IOTEC GLOBAL — 24/7 Digital Engine* 🚀",
        "saudacao": "Dear Partner,",
        "intro": "Introducing *IOTEC*, a B2B automation and intelligence infrastructure operating under the *Follow-the-Sun* model (24/7 coverage across the Americas, Europe, and Asia/Oceania).",
        "destaques": "📌 *Core Highlights:*\n• 24/7 Lead Qualification in the Virtual Investor Room.\n• Live telemetry of real-time metrics and webhooks in Production Mode.\n• High-availability infrastructure with atomic database persistence.",
        "call": "📄 *To interact with our Virtual Room, reply with:* */investor*",
        "ass": "Best regards,\n*Bruno — Founder & Core Developer*\nIOTEC (CNPJ: 61.549.037/0001-68)"
    },
    "de": {
        "titulo": "*IOTEC GLOBAL — Digitales System 24/7* 🚀",
        "saudacao": "Sehr geehrte Damen und Herren,",
        "intro": "Wir präsentieren *IOTEC*, eine B2B-Automatisierungs- und Intelligenzinfrastruktur, die nach dem *Follow-the-Sun*-Modell arbeitet (24/7 Abdeckung über Amerika, Europa und Asien/Ozeanien).",
        "destaques": "📌 *Kern-Highlights:*\n• 24/7-Qualifizierung im Virtuellen Investorenraum.\n• Live-Telemetrie von Echtzeit-Metriken im Produktionsmodus.\n• Hochverfügbare Infrastruktur mit atomarer Datenpersistenz.",
        "call": "📄 *Antworten Sie mit folgendem Befehl, um zu starten:* */investor*",
        "ass": "Mit freundlichen Grüßen,\n*Bruno — Founder & Core Developer*\nIOTEC (CNPJ: 61.549.037/0001-68)"
    }
}

def obter_idioma_por_numero(numero):
    for ddi, lang in IDIOMAS_PAIS.items():
        if numero.startswith(ddi):
            return lang
    return "en"

def disparar_multilingue(numero_destino):
    lang = obter_idioma_por_numero(numero_destino)
    msg = MENSAGENS.get(lang, MENSAGENS["en"])
    texto_final = f"{msg['titulo']}\n\n{msg['saudacao']}\n\n{msg['intro']}\n\n{msg['destaques']}\n\n{msg['call']}\n\n{msg['ass']}"
    
    js_code = f"""const {{ default: makeWASocket, useMultiFileAuthState, DisconnectReason }} = require('@whiskeysockets/baileys');
const pino = require('pino');

async function enviar() {{
    const {{ state, saveCreds }} = await useMultiFileAuthState('C:/IOTEC/auth_info_baileys');
    const sock = makeWASocket({{
        auth: state,
        logger: pino({{ level: 'silent' }}),
        printQRInTerminal: false
    }});

    sock.ev.on('creds.update', saveCreds);

    sock.ev.on('connection.update', async (update) => {{
        const {{ connection, lastDisconnect }} = update;
        if (connection === 'open') {{
            const jid = '{numero_destino}@s.whatsapp.net';
            await sock.sendMessage(jid, {{ text: `{texto_final}` }});
            console.log('[OK] Mensagem entregue com sucesso em {lang.upper()} para {numero_destino}');
            process.exit(0);
        }} else if (connection === 'close') {{
            const shouldReconnect = (lastDisconnect?.error)?.output?.statusCode !== DisconnectReason.loggedOut;
            if (shouldReconnect) {{
                enviar();
            }}
        }}
    }});
}}
enviar();
"""
    with open(r"C:\IOTEC\temp_dispatch_multilang.js", "w", encoding="utf-8") as f:
        f.write(js_code)
    
    print(f"[IOTEC MULTILANG] Idioma detectado: {lang.upper()} | Disparando para {numero_destino}...")
    subprocess.run(["node", r"C:\IOTEC\temp_dispatch_multilang.js"])

if __name__ == "__main__":
    num = sys.argv[1] if len(sys.argv) > 1 else "5588999999999"
    disparar_multilingue(num)
