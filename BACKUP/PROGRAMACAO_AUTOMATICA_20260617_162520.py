import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================

# IOTEC MEDIA ENGINE

# PROGRAMACAO AUTOMATICA

# ============================================================



Clear-Host



Write-Host ""

Write-Host "===================================================="

Write-Host " IOTEC MEDIA ENGINE"

Write-Host "===================================================="

Write-Host ""



# ============================================================

# ROOT

# ============================================================



$ROOT = "C:\IOTEC_OMEGA_X"



$MEDIA = "$ROOT\media_core"



$FRONT = "$ROOT\frontend"



$VIDEOS = "$MEDIA\videos"



$PLAYLIST = "$MEDIA\playlist"



# ============================================================

# PASTAS

# ============================================================



New-Item `

-ItemType Directory `

-Force `

-Path $VIDEOS | Out-Null



New-Item `

-ItemType Directory `

-Force `

-Path $PLAYLIST | Out-Null



Write-Host "[OK] estrutura criada"



# ============================================================

# BUSCA VIDEOS

# ============================================================



Write-Host ""

Write-Host "[CHECK] procurando videos..."



$search = Get-ChildItem `

"$HOME\Downloads",

"$HOME\Desktop",

"$HOME\Videos" `

-Recurse `

-Include *.mp4 `

-ErrorAction SilentlyContinue



if($search.Count -eq 0){



    Write-Host ""

    Write-Host "[ERRO] nenhum video encontrado"

    Pause

    Exit



}



Write-Host ""

Write-Host "VIDEOS LOCALIZADOS:"

Write-Host ""



$i = 1



foreach($v in $search){



    Write-Host "[$i] $($v.Name)"



    $dest = "$VIDEOS\video$i.mp4"



    Copy-Item `

    $v.FullName `

    $dest `

    -Force `

    -ErrorAction SilentlyContinue



    $i++



}



# ============================================================

# CRIA PLAYLIST

# ============================================================



Write-Host ""

Write-Host "[BUILD] criando programacao..."



$playlist = ""



$j = 1



foreach($v in Get-ChildItem $VIDEOS -Filter *.mp4){



$playlist += @"



<div class='video-card'>



<video autoplay muted loop playsinline>



<source src='../media_core/videos/video$j.mp4' type='video/mp4'>



</video>



</div>



"@



$j++



}



# ============================================================

# PORTAL TV

# ============================================================



$html = @"



<!DOCTYPE html>



<html>



<head>



<meta charset='UTF-8'>



<title>IOTEC GLOBAL STREAM</title>



<style>



body{



margin:0;

padding:0;

background:black;

color:white;

font-family:Arial;



}



.hero{



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

flex-direction:column;

justify-content:center;

align-items:center;



text-align:center;



}



.hero h1{



font-size:80px;

letter-spacing:8px;



}



.hero p{



font-size:22px;

width:60%;

opacity:0.8;



}



.stream{



padding:40px;



display:grid;



grid-template-columns:

repeat(2,1fr);



gap:25px;



}



.video-card{



overflow:hidden;

border-radius:20px;

background:#111;



}



video{



width:100%;

height:100%;

object-fit:cover;



}



.info{



padding:40px;

line-height:35px;

font-size:20px;



}



.footer{



padding:50px;

text-align:center;

opacity:0.6;



}



</style>



</head>



<body>



<section class='hero'>



<h1>IOTEC</h1>



<p>



Global Operations,

Economy,

Energy,

Streaming,

Enterprise Intelligence,

Geopolitics,

Urbanism,

Technology



</p>



</section>



<section class='info'>



<h2>GLOBAL PROGRAMMING</h2>



<p>ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ Economia global</p>

<p>ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ Energia e petrÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³leo</p>

<p>ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ GeopolÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­tica internacional</p>

<p>ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ Urbanismo inteligente</p>

<p>ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ Centros financeiros</p>

<p>ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ Tecnologia e IA</p>



</section>



<section class='stream'>



$playlist



</section>



<section class='footer'>



<p>



CONTACT:

iotec.bl@proton.me



</p>



</section>



</body>



</html>



"@



# ============================================================

# SALVA

# ============================================================



Set-Content `

"$FRONT\global_stream.html" `

$html `

-Encoding UTF8



Write-Host ""

Write-Host "[OK] portal televisionado criado"



# ============================================================

# ABRIR

# ============================================================



Start-Process `

"$FRONT\global_stream.html"



# ============================================================

# FINAL

# ============================================================



Write-Host ""

Write-Host "===================================================="

Write-Host " PROGRAMACAO INICIADA"

Write-Host "===================================================="

Write-Host ""



Write-Host "[+] Videos integrados"

Write-Host "[+] Programacao criada"

Write-Host "[+] Stream criado"

Write-Host "[+] Portal televisionado ativo"

Write-Host "[+] Acervo operacional"



Write-Host ""

Pause





