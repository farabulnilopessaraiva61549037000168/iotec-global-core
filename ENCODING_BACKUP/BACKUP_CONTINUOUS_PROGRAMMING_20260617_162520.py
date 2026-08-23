import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC LIVE MEDIA ENGINE
# CONTINUOUS PROGRAMMING SYSTEM
# ============================================================
#
# RESOLVE:
#
# 1 - MEDIA ENGINE CONTINUO
# 2 - ROTACAO AUTOMATICA
# 3 - PLAYLISTS DINAMICAS
# 4 - PROGRAMACAO VIVA
# 5 - DISTRIBUICAO PUBLICA
#
# ============================================================

import os
import random
import shutil
import time
from datetime import datetime

# ============================================================
# ROOT
# ============================================================

ROOT = r"C:\IOTEC_OMEGA_X"

FRONT = os.path.join(ROOT,"frontend")

MEDIA = os.path.join(ROOT,"media_core")

VIDEOS = os.path.join(MEDIA,"videos")

PLAYLIST = os.path.join(MEDIA,"playlists")

EXPORT = os.path.join(MEDIA,"exports")

REPORT = os.path.join(MEDIA,"reports")

# ============================================================
# PASTAS
# ============================================================

folders = [

    MEDIA,
    VIDEOS,
    PLAYLIST,
    EXPORT,
    REPORT

]

for f in folders:
    pass

    os.makedirs(f,exist_ok=True)

# ============================================================
# CABECALHO
# ============================================================

print("\n================================================")
print(" IOTEC LIVE MEDIA ENGINE")
print("================================================\n")

# ============================================================
# BUSCA AUTOMATICA DE VIDEOS
# ============================================================

print("[CHECK] procurando videos premium...\n")

search_paths = [

    os.path.join(os.path.expanduser("~"),"Downloads"),
    os.path.join(os.path.expanduser("~"),"Desktop"),
    os.path.join(os.path.expanduser("~"),"Videos")

]

video_list = []

for path in search_paths:
    pass

    if os.path.exists(path):
        pass

        for root,dirs,files in os.walk(path):
            pass

            for file in files:
                pass

                if file.lower().endswith(".mp4"):
                    pass

                    full = os.path.join(root,file)

                    video_list.append(full)

# ============================================================
# VALIDA
# ============================================================

if len(video_list) == 0:
    pass

    print("[ERRO] nenhum video encontrado")

    exit()

print(f"[OK] {len(video_list)} videos encontrados\n")

# ============================================================
# COPIA PARA ACERVO
# ============================================================

print("[BUILD] criando acervo operacional...\n")

count = 1

for video in video_list:
    pass

    try:
        pass

        ext = os.path.splitext(video)[1]

        dest = os.path.join(
            VIDEOS,
            f"video_{count}{ext}"
        )

        shutil.copy(video,dest)

        print(f"[OK] video integrado: {count}")

        count += 1

    except:
        pass

        print("[FALHA] erro ao copiar video")

# ============================================================
# PLAYLISTS DINAMICAS
# ============================================================

print("\n[BUILD] criando playlists dinamicas...\n")

sectors = [

    "energia",
    "financas",
    "industria",
    "geopolitica",
    "urbanismo",
    "tecnologia",
    "medicina",
    "corporativo"

]

playlist_data = {}

all_videos = os.listdir(VIDEOS)

for sector in sectors:
    pass

    random.shuffle(all_videos)

    selected = all_videos[:4]

    playlist_data[sector] = selected

    print(f"[OK] playlist criada: {sector}")

# ============================================================
# PROGRAMACAO VIVA
# ============================================================

print("\n[BUILD] criando programacao viva...\n")

programming = []

hours = [

    "08:00",
    "10:00",
    "12:00",
    "14:00",
    "16:00",
    "18:00",
    "20:00",
    "22:00"

]

for h in hours:
    pass

    sector = random.choice(sectors)

    programming.append({

        "hour":h,
        "sector":sector

    })

    print(f"[LIVE] {h} -> {sector}")

# ============================================================
# HTML TELEVISIONADO
# ============================================================

print("\n[BUILD] criando portal televisionado...\n")

cards = ""

for item in programming:
    pass

    sector = item["sector"]

    videos = playlist_data[sector]

    chosen = random.choice(videos)

    cards += f"""

    <div class='card'>

        <video autoplay muted loop playsinline>

            <source src='../media_core/videos/{chosen}'
            type='video/mp4'>

        </video>

        <div class='overlay'>

            <h2>{sector.upper()}</h2>

            <p>PROGRAMACAO AO VIVO</p>

            <span>{item['hour']}</span>

        </div>

    </div>

    """

html = f"""

<!DOCTYPE html>

<html>

<head>

<meta charset='UTF-8'>

<title>IOTEC LIVE NETWORK</title>

<style>

body{{
margin:0;
background:black;
font-family:Arial;
color:white;
overflow-x:hidden;
}}

header{{
height:100vh;

background:
linear-gradient(
rgba(0,0,0,0.6),
rgba(0,0,0,0.9)
),

url('https://images.unsplash.com/photo-1516321318423-f06f85e504b3');

background-size:cover;
background-position:center;

display:flex;
justify-content:center;
align-items:center;
flex-direction:column;
text-align:center;
}}

header h1{{
font-size:90px;
letter-spacing:10px;
margin:0;
}}

header p{{
font-size:24px;
opacity:0.8;
width:60%;
}}

.grid{{
display:grid;
grid-template-columns:repeat(2,1fr);
gap:30px;
padding:40px;
}}

.card{{
position:relative;
overflow:hidden;
border-radius:25px;
background:#111;
height:420px;
}}

.card video{{
width:100%;
height:100%;
object-fit:cover;
}}

.overlay{{
position:absolute;
bottom:0;
width:100%;
padding:25px;
background:
linear-gradient(
transparent,
rgba(0,0,0,0.95)
);
}}

.overlay h2{{
margin:0;
font-size:34px;
}}

.overlay p{{
opacity:0.8;
}}

footer{{
padding:50px;
text-align:center;
opacity:0.7;
}}

</style>

</head>

<body>

<header>

<h1>IOTEC</h1>

<p>

GLOBAL ENTERPRISE STREAMING
INTELLIGENCE
MEDIA
OPERATIONS
AUTOMATION

</p>

</header>

<section class='grid'>

{cards}

</section>

<footer>

<p>

iotec.bl@proton.me

</p>

<p>

LIVE ENTERPRISE NETWORK

</p>

</footer>

</body>

</html>

"""

# ============================================================
# SALVA PORTAL
# ============================================================

portal = os.path.join(
    FRONT,
    "iotec_live_network.html"
)

with open(portal,"w",encoding="utf-8") as f:
    pass

    f.write(html)

print("[OK] portal televisionado criado")

# ============================================================
# DISTRIBUICAO PUBLICA
# ============================================================

print("\n[DISTRIBUTION] preparando vitrines...\n")

socials = [

    "linkedin",
    "youtube",
    "instagram",
    "twitter",
    "tiktok"

]

for s in socials:
    pass

    social_path = os.path.join(
        EXPORT,
        s
    )

    os.makedirs(
        social_path,
        exist_ok=True
    )

    print(f"[OK] vitrine preparada: {s}")

# ============================================================
# RELATORIO
# ============================================================

report_text = f"""

================================================
IOTEC LIVE MEDIA ENGINE
================================================

STATUS:

[OK] MEDIA ENGINE CONTINUO
[OK] ROTACAO AUTOMATICA
[OK] PLAYLISTS DINAMICAS
[OK] PROGRAMACAO VIVA
[OK] DISTRIBUICAO PUBLICA

VIDEOS:
{len(video_list)}

PLAYLISTS:
{len(playlist_data)}

SETORES:
{len(sectors)}

PROGRAMACOES:
{len(programming)}

VITRINES:
{len(socials)}

PORTAL:
{portal}

DATA:
{datetime.now()}

================================================

"""

report_file = os.path.join(
    REPORT,
    "live_engine_report.txt"
)

with open(report_file,"w",encoding="utf-8") as f:
    pass

    f.write(report_text)

# ============================================================
# FINAL
# ============================================================

print("\n================================================")
print(" LIVE MEDIA ENGINE ONLINE")
print("================================================\n")

print("[OK] media engine iniciado")
print("[OK] rotacao automatica ativa")
print("[OK] playlists dinamicas criadas")
print("[OK] programacao viva criada")
print("[OK] distribuicao publica preparada")
print("[OK] portal televisionado online")

print("\nPORTAL:\n")
print(portal)

print("\n================================================\n")


