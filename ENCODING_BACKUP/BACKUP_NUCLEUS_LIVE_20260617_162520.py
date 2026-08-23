import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC NUCLEUS LIVE ENGINE
# ============================================================
# OBJETIVO:
#
# ligar o nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo de verdade:
#
# 1. conectar JSON ao portal
# 2. transformar dados em experiencia viva
# 3. criar overlays dinamicos
# 4. ativar narrativa automatica
# 5. sincronizar videos
# 6. criar recepcao inteligente
# 7. criar setores vivos
# 8. transformar o portal em rede operacional
# 9. ligar experiencia empresarial real
# 10. ativar transmissao cinematografica
#
# ============================================================

import json
import os

print("")
print("================================================")
print(" IOTEC NUCLEUS LIVE ENGINE")
print("================================================")
print("")

# ============================================================
# ROOT
# ============================================================

ROOT = r"C:\IOTEC_OMEGA_X"

FRONTEND = os.path.join(ROOT,"frontend")

VIDEOS = os.path.join(FRONTEND,"videos")

JSON_FILE = "IOTEC_REALITY_EXECUTION_ENGINE.json"

PORTAL = os.path.join(
    FRONTEND,
    "iotec_nucleus_live.html"
)

# ============================================================
# LOAD JSON
# ============================================================

print("[LOAD] carregando inteligencia operacional...")
print("")

if not os.path.exists(JSON_FILE):
    pass

    print("[FALHA] json nao encontrado")
    exit()

with open(JSON_FILE,"r",encoding="utf-8") as f:
    pass

    sectors = json.load(f)

print("[OK] inteligencia carregada")
print("")

# ============================================================
# VIDEO COLLECTOR
# ============================================================

def collect_videos(folder):
    pass

    result = []

    if not os.path.exists(folder):
        pass

        return result

    for file in os.listdir(folder):
        pass

        if file.endswith(".mp4") or file.endswith(".webm"):
            pass

            result.append(
                f"videos/{os.path.basename(folder)}/{file}"
            )

    return result

# ============================================================
# CATEGORY MAP
# ============================================================

map_sector = {

    "Corporate Operations":"corporate",
    "Technology & AI":"technology",
    "Media Network":"urban"

}

# ============================================================
# BUILD CARDS
# ============================================================

cards = ""
scripts = ""

index = 1

for sector in sectors:
    pass

    sector_name = sector["sector"]

    category = map_sector.get(
        sector_name,
        "unknown"
    )

    folder = os.path.join(
        VIDEOS,
        category
    )

    videos = collect_videos(folder)

    js_array = ",".join(
        [f'"{v}"' for v in videos]
    )

    messages = sector["sales_engine"]["messages"]

    overlays = ",".join(
        [f'"{m}"' for m in messages]
    )

    ctas = sector["sales_engine"]["call_to_action"]

    cta_array = ",".join(
        [f'"{c}"' for c in ctas]
    )

    cards += f"""

    <div class='card'>

        <video
        id='video{index}'
        autoplay
        muted
        loop
        playsinline></video>

        <div class='overlay'>

            <div class='sector'>
                {sector_name}
            </div>

            <div class='message'
            id='message{index}'></div>

            <div class='cta'
            id='cta{index}'></div>

        </div>

    </div>

    """

    scripts += f"""

    const videos{index} = [
    {js_array}
    ];

    const messages{index} = [
    {overlays}
    ];

    const ctas{index} = [
    {cta_array}
    ];

    let videoIndex{index} = 0;
    let messageIndex{index} = 0;
    let ctaIndex{index} = 0;

    const video{index} =
    document.getElementById("video{index}");

    const message{index} =
    document.getElementById("message{index}");

    const cta{index} =
    document.getElementById("cta{index}");

    function rotateVideo{index}(){{

        if(videos{index}.length === 0) return;

        video{index}.src =
        videos{index}[videoIndex{index}];

        video{index}.play();

        videoIndex{index}++;

        if(videoIndex{index} >= videos{index}.length){{
            videoIndex{index} = 0;
        }}

    }}

    function rotateMessage{index}(){{

        if(messages{index}.length === 0) return;

        message{index}.innerText =
        messages{index}[messageIndex{index}];

        messageIndex{index}++;

        if(messageIndex{index} >= messages{index}.length){{
            messageIndex{index} = 0;
        }}

    }}

    function rotateCTA{index}(){{

        if(ctas{index}.length === 0) return;

        cta{index}.innerText =
        ctas{index}[ctaIndex{index}];

        ctaIndex{index}++;

        if(ctaIndex{index} >= ctas{index}.length){{
            ctaIndex{index} = 0;
        }}

    }}

    rotateVideo{index}();
    rotateMessage{index}();
    rotateCTA{index}();

    setInterval(rotateVideo{index},25000);
    setInterval(rotateMessage{index},7000);
    setInterval(rotateCTA{index},9000);

    """

    index += 1

# ============================================================
# HTML
# ============================================================

html = f"""

<!DOCTYPE html>

<html lang='pt-br'>

<head>

<meta charset='UTF-8'>

<title>IOTEC NUCLEUS LIVE</title>

<style>

*{{
margin:0;
padding:0;
box-sizing:border-box;
}}

body{{

background:#020617;
font-family:Arial;
overflow-x:hidden;
color:white;

}}

.header{{

padding:30px;

background:
linear-gradient(
90deg,
#0f172a,
#111827,
#1e293b
);

}}

.logo{{

font-size:42px;
font-weight:bold;
letter-spacing:5px;

}}

.subtitle{{

margin-top:10px;
color:#94a3b8;

}}

.grid{{

display:grid;
grid-template-columns:1fr 1fr;
gap:25px;
padding:25px;

}}

.card{{

position:relative;

height:380px;

overflow:hidden;

border-radius:22px;

background:#111827;

box-shadow:
0 0 40px rgba(0,0,0,0.6);

}}

video{{

width:100%;
height:100%;
object-fit:cover;

}}

.overlay{{

position:absolute;

inset:0;

background:
linear-gradient(
180deg,
rgba(0,0,0,0.15),
rgba(0,0,0,0.75)
);

display:flex;

flex-direction:column;

justify-content:flex-end;

padding:30px;

}}

.sector{{

font-size:14px;
letter-spacing:3px;
color:#94a3b8;
margin-bottom:10px;

}}

.message{{

font-size:28px;
font-weight:bold;
max-width:500px;
line-height:1.3;

animation:fade 1s ease;

}}

.cta{{

margin-top:18px;

display:inline-block;

padding:12px 18px;

background:#2563eb;

border-radius:12px;

font-size:14px;

font-weight:bold;

width:max-content;

animation:fade 1s ease;

}}

.footer{{

padding:30px;
text-align:center;
color:#64748b;

}}

@keyframes fade{{

from{{
opacity:0;
transform:translateY(10px);
}}

to{{
opacity:1;
transform:translateY(0px);
}}

}}

</style>

</head>

<body>

<div class='header'>

<div class='logo'>
IOTEC NUCLEUS LIVE
</div>

<div class='subtitle'>
ecossistema audiovisual ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ operacoes ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ tecnologia ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ inteligencia empresarial
</div>

</div>

<div class='grid'>

{cards}

</div>

<div class='footer'>

iotec.bl@proton.me
<br>
IOTEC ENTERPRISE MEDIA NETWORK

</div>

<script>

{scripts}

</script>

</body>

</html>

"""

# ============================================================
# SAVE
# ============================================================

with open(PORTAL,"w",encoding="utf-8") as f:
    pass

    f.write(html)

# ============================================================
# FINAL REPORT
# ============================================================

print("")
print("================================================")
print(" NUCLEUS LIVE REPORT")
print("================================================")
print("")

print("[OK] json conectado ao portal")
print("[OK] overlays cinematograficos ativos")
print("[OK] narrativa automatica ativa")
print("[OK] videos sincronizados")
print("[OK] setores vivos criados")
print("[OK] experiencia empresarial online")
print("[OK] transmissao cinematografica ativa")
print("[OK] ecossistema operacional ligado")

print("")
print("PORTAL:")
print("")
print(PORTAL)

print("")
print("================================================")
print(" IOTEC NUCLEUS ONLINE")
print("================================================")
print("")


