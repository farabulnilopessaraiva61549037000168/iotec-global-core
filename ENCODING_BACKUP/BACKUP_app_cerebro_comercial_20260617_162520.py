import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
from flask import Flask, request, jsonify
from openai import OpenAI

# =========================
# CONFIGURAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# =========================

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# memÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³ria simples em RAM (MVP)
SESSIONS = {}

# =========================
# PROMPT MESTRE DO VENDEDOR IA
# =========================

SYSTEM_PROMPT = """
You are a Global Sales Agent AI.

You are NOT support. You are a HIGH-CONVERSION SALES CLOSER.

Your job:
- qualify leads
- identify sector
- identify company size
- detect urgency
- recommend ONE offer
- push toward closing

Rules:
- ask one question at a time
- always move toward closing
- never give too many options
- always end with CTA
- be concise and commercial
- if enterprise ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ suggest human handoff

Offer logic:
- small ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Starter Plan
- medium ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Business Plan
- large ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Enterprise Plan
"""

# =========================
# MOTOR DE OFERTAS
# =========================

def get_offer(size):
    if size == "small":
        return {
            "plan": "Starter Plan",
            "price": "$29 - $99/month",
            "value": "basic automation + chatbot + dashboard"
        }
    elif size == "medium":
        return {
            "plan": "Business Plan",
            "price": "$99 - $299/month",
            "value": "CRM + automation + integrations"
        }
    else:
        return {
            "plan": "Enterprise Plan",
            "price": "$500+/month",
            "value": "custom AI + APIs + dedicated support"
        }

# =========================
# AGENTE IA
# =========================

def run_agent(message, history):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    for h in history:
        messages.append(h)

    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.6
    )

    return response.choices[0].message.content


# =========================
# EXTRATOR SIMPLES DE PERFIL (MVP)
# =========================

def extract_profile(text):
    text = text.lower()

    # heurÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­stica simples (pode evoluir depois)
    size = "small"
    sector = "unknown"

    if "empresa grande" in text or "enterprise" in text:
        size = "large"
    elif "empresa mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©dia" in text or "medium" in text:
        size = "medium"

    if "educaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o" in text:
        sector = "education"
    elif "saÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºde" in text:
        sector = "health"
    elif "indÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºstria" in text:
        sector = "industry"

    return {"size": size, "sector": sector}


# =========================
# CHAT PRINCIPAL
# =========================

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    session_id = data.get("session_id")
    message = data.get("message")

    if session_id not in SESSIONS:
        SESSIONS[session_id] = []

    history = SESSIONS[session_id]

    # roda agente
    reply = run_agent(message, history)

    # salva memÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³ria
    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": reply})

    return jsonify({
        "reply": reply
    })


# =========================
# OFERTA FINAL
# =========================

@app.route("/offer", methods=["POST"])
def offer():
    data = request.json
    message = data.get("message")

    profile = extract_profile(message)
    offer = get_offer(profile["size"])

    return jsonify({
        "profile": profile,
        "offer": offer
    })


# =========================
# CHECKOUT SIMULADO
# =========================

@app.route("/checkout", methods=["POST"])
def checkout():
    return jsonify({
        "status": "success",
        "checkout_url": "https://checkout.stripe.com/mock"
    })


# =========================
# START SERVER
# =========================

if __name__ == "__main__":
    app.run(port=5000, debug=False, use_reloader=False)



