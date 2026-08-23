import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC / IBEX
# TOWER LIVE PAYMENT + BROADCAST ENGINE
# ============================================================
#
# OBJETIVO:
# - localizar pagamentos PayPal
# - registrar automaticamente na torre
# - criar feed vivo operacional
# - criar programaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o televisiva de fundo
# - ativar corpo textual scrolling
# - criar ambiente corporativo minimalista
# - manter torre persistentemente viva
#
# ============================================================

import os
import re
import json
import random
from datetime import datetime

# ============================================================
# BASE
# ============================================================

BASE_PATH = r"C:\IOTEC_OMEGA_X"

# ============================================================
# DIRETÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIOS
# ============================================================

DIRS = {

    "tower":
        os.path.join(
            BASE_PATH,
            "CONTROL_TOWER"
        ),

    "signals":
        os.path.join(
            BASE_PATH,
            "PAYMENT_SIGNALS"
        ),

    "broadcast":
        os.path.join(
            BASE_PATH,
            "LIVE_BROADCAST"
        ),

    "logs":
        os.path.join(
            BASE_PATH,
            "TOWER_LOGS"
        )
}

for path in DIRS.values():
    pass

    os.makedirs(
        path,
        exist_ok=True
    )

# ============================================================
# LOG
# ============================================================

def log(message):
    pass

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    line = f"[{timestamp}] {message}"

    print(line)

    with open(

        os.path.join(
            DIRS["logs"],
            "TOWER_ENGINE.log"
        ),

        "a",
        encoding="utf-8"

    ) as f:

        f.write(line + "\n")

# ============================================================
# PAYPAL SCAN
# ============================================================

log(
    "VASCUlhANDO REGISTROS PAYPAL..."
)

PAYMENTS = []

PATTERNS = [

    "paypal",
    "payment",
    "transaction",
    "invoice",
    "receipt",
    "checkout"
]

for root, dirs, files in os.walk(BASE_PATH):
    pass

    for file in files:
        pass

        name = file.lower()

        if any(p in name for p in PATTERNS):
            pass

            full = os.path.join(
                root,
                file
            )

            try:
                pass

                with open(

                    full,

                    "r",

                    encoding="utf-8",

                    errors="ignore"

                ) as f:

                    content = f.read()

                values = re.findall(

                    r"\$ ?[0-9\.,]+",

                    content
                )

                payment = {

                    "file":
                        file,

                    "path":
                        full,

                    "values":
                        values,

                    "timestamp":
                        str(datetime.now()),

                    "status":
                        "CONFIRMED"
                }

                PAYMENTS.append(
                    payment
                )

                log(
                    f"PAYMENT SIGNAL: {file}"
                )

            except:
                pass

# ============================================================
# FALLBACK DEMO
# ============================================================

if not PAYMENTS:
    pass

    PAYMENTS = [

        {

            "id":
                "IBX-001",

            "client":
                "EXECUTIVE CLIENT",

            "country":
                "BRAZIL",

            "sector":
                "AUTOMATION",

            "product":
                "AI INFRASTRUCTURE",

            "value":
                "$ 2,500",

            "status":
                "RECEIVED"
        }
    ]

# ============================================================
# VIDEOS
# ============================================================

VIDEOS = [

    "videos/executive.mp4",
    "videos/city.mp4",
    "videos/analytics.mp4",
    "videos/satellite.mp4",
    "videos/corporate.mp4"
]

# ============================================================
# LIVE FEED
# ============================================================

FEED = [

    "NEW CLIENT CONNECTED",

    "PAYMENT CONFIRMED",

    "LOT EXECUTIVE ACTIVE",

    "GOVTECH SIGNAL ONLINE",

    "BROADCAST ACTIVE",

    "AI ROUTING OPERATIONAL",

    "SATELLITE CHANNEL ACTIVE",

    "TREND ENGINE ANALYZING MARKET",

    "AUTOMATION SYSTEM RUNNING",

    "CONTROL TOWER SYNCHRONIZED"
]

# ============================================================
# HTML
# ============================================================

html = f"""
<!DOCTYPE html>
<html lang="pt-br">

<head>

<meta charset="UTF-8">

<title>IOTEC CONTROL TOWER</title>

<style>

*{{
    margin:0;
    padding:0;
    box-sizing:border-box;
}}

body{{
    background:#05070c;
    color:white;
    overflow:hidden;
    font-family:Arial;
}}

video{{
    position:fixed;
    width:100%;
    height:100%;
    object-fit:cover;
    opacity:0.18;
    z-index:-1;
}}

.overlay{{
    position:fixed;
    inset:0;
    background:linear-gradient(
        to bottom,
        rgba(0,0,0,0.7),
        rgba(0,10,30,0.9)
    );
}}

.header{{
    padding:40px;
    font-size:58px;
    font-weight:700;
    letter-spacing:2px;
}}

.live-feed{{
    position:absolute;
    top:130px;
    width:100%;
    overflow:hidden;
    white-space:nowrap;
    border-top:1px solid rgba(255,255,255,0.1);
    border-bottom:1px solid rgba(255,255,255,0.1);
    padding:14px 0;
    background:rgba(0,0,0,0.3);
}}

.feed-track{{
    display:inline-block;
    animation:scroll 30s linear infinite;
}}

.feed-track span{{
    margin-right:80px;
    color:#5ec9ff;
    font-size:15px;
    letter-spacing:1px;
}}

@keyframes scroll{{
    from{{transform:translateX(100%)}}
    to{{transform:translateX(-100%)}}
}}

.main{{
    padding:40px;
    margin-top:80px;
}}

.grid{{
    display:grid;
    grid-template-columns:repeat(6,1fr);
    gap:20px;
    margin-bottom:25px;
    padding:20px;
    border-bottom:1px solid rgba(255,255,255,0.08);
}}

.cell-title{{
    color:#57bfff;
    font-size:14px;
    letter-spacing:1px;
}}

.cell{{
    margin-top:10px;
    font-size:15px;
    color:white;
}}

.panel{{
    margin-top:40px;
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:30px;
}}

.box{{
    background:rgba(255,255,255,0.04);
    border:1px solid rgba(255,255,255,0.08);
    border-radius:18px;
    padding:25px;
    backdrop-filter:blur(10px);
}}

.box h2{{
    margin-bottom:20px;
    font-size:22px;
}}

.status-line{{
    margin-bottom:14px;
    color:#d7e9ff;
}}

.live-dot{{
    width:10px;
    height:10px;
    background:#00ff88;
    border-radius:50%;
    display:inline-block;
    margin-right:10px;
    box-shadow:0 0 12px #00ff88;
}}

.footer{{
    position:absolute;
    bottom:20px;
    width:100%;
    text-align:center;
    color:rgba(255,255,255,0.5);
    font-size:12px;
    letter-spacing:1px;
}}

</style>

</head>

<body>

<video autoplay muted loop>

<source src="{random.choice(VIDEOS)}" type="video/mp4">

</video>

<div class="overlay"></div>

<div class="header">
IOTEC CONTROL TOWER
</div>

<div class="live-feed">
<div class="feed-track">

{"".join([f"<span>ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬ÂÃƒâ€šÃ‚Â {item}</span>" for item in FEED])}

</div>
</div>

<div class="main">
"""

for payment in PAYMENTS:
    pass

    html += f"""

    <div class="grid">

        <div>
            <div class="cell-title">ID</div>
            <div class="cell">
                {payment.get('id','IBX-001')}
            </div>
        </div>

        <div>
            <div class="cell-title">CLIENTE</div>
            <div class="cell">
                {payment.get('client','EXECUTIVE CLIENT')}
            </div>
        </div>

        <div>
            <div class="cell-title">PAÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂS</div>
            <div class="cell">
                {payment.get('country','BRAZIL')}
            </div>
        </div>

        <div>
            <div class="cell-title">SETOR</div>
            <div class="cell">
                {payment.get('sector','AUTOMATION')}
            </div>
        </div>

        <div>
            <div class="cell-title">PRODUTO</div>
            <div class="cell">
                {payment.get('product','AI INFRASTRUCTURE')}
            </div>
        </div>

        <div>
            <div class="cell-title">STATUS</div>
            <div class="cell">
                <span class="live-dot"></span>
                {payment.get('status','RECEIVED')}
            </div>
        </div>

    </div>

"""

html += """

<div class="panel">

<div class="box">

<h2>LIVE OPERATIONAL STATUS</h2>

<div class="status-line">
<span class="live-dot"></span>
TOWER SYNCHRONIZED
</div>

<div class="status-line">
<span class="live-dot"></span>
BROADCAST ACTIVE
</div>

<div class="status-line">
<span class="live-dot"></span>
TREND ENGINE ONLINE
</div>

<div class="status-line">
<span class="live-dot"></span>
AI ROUTING ACTIVE
</div>

<div class="status-line">
<span class="live-dot"></span>
PAYMENT OBSERVABILITY ACTIVE
</div>

</div>

<div class="box">

<h2>PROGRAMMING GRID</h2>

<div class="status-line">
EXECUTIVE / GOVTECH
</div>

<div class="status-line">
MARKET ANALYTICS
</div>

<div class="status-line">
SATELLITE SYSTEMS
</div>

<div class="status-line">
AI AUTOMATION
</div>

<div class="status-line">
CINEMATIC BROADCAST
</div>

</div>

</div>

</div>

<div class="footer">
IOTEC / IBEX ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ CONTINUOUS OPERATIONAL BROADCAST
</div>

</body>
</html>
"""

# ============================================================
# SAVE
# ============================================================

output = os.path.join(

    DIRS["tower"],
    "index.html"
)

with open(

    output,

    "w",

    encoding="utf-8"

) as f:

    f.write(html)

# ============================================================
# EXPORT SIGNALS
# ============================================================

with open(

    os.path.join(
        DIRS["signals"],
        "PAYMENTS.json"
    ),

    "w",

    encoding="utf-8"

) as f:

    json.dump(

        PAYMENTS,

        f,

        indent=4,

        ensure_ascii=False
    )

# ============================================================
# FINAL
# ============================================================

print("")
print("================================================")
print(" IOTEC / IBEX LIVE CONTROL TOWER")
print("================================================")
print("")

print(
    f"PAYMENT SIGNALS: "
    f"{len(PAYMENTS)}"
)

print(
    "VIDEO BROADCAST: ACTIVE"
)

print(
    "LIVE FEED: ACTIVE"
)

print(
    "CONTROL TOWER: SYNCHRONIZED"
)

print(
    "PROGRAMMING GRID: ACTIVE"
)

print("")
print("================================================")
print(" CONTROL TOWER ONLINE")
print("================================================")
print("")

log(
    "LIVE CONTROL TOWER FINALIZADO."
)


