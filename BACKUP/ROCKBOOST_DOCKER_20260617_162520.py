import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================

# IOTEC ROCKBOOST DOCKER ENGINE

# CONTAINERIZED GOVERNANCE SYSTEM

# ============================================================



from pathlib import Path



# ============================================================

# BASE

# ============================================================



BASE = Path(

    "C:/IOTEC_DOCKER_CORE"

)



BASE.mkdir(

    parents=True,

    exist_ok=True

)



# ============================================================

# PASTAS

# ============================================================



PASTAS = [



    "acropole",

    "ia_engine",

    "analytics",

    "streaming",

    "governance"



]



for pasta in PASTAS:
    pass



    (

        BASE / pasta

    ).mkdir(



        parents=True,

        exist_ok=True



    )



# ============================================================

# DOCKER COMPOSE

# ============================================================



DOCKER = """

version: '3.9'



services:



  acropole:



    image: python:3.11



    container_name:

      iotec_acropole



    working_dir:

      /app



    volumes:

      - ./acropole:/app



    command:

      python app.py



    ports:

      - "9001:9001"



  ia_engine:



    image: python:3.11



    container_name:

      iotec_ia_engine



    working_dir:

      /app



    volumes:

      - ./ia_engine:/app



    command:

      python app.py



    ports:

      - "9002:9002"



  analytics:



    image: python:3.11



    container_name:

      iotec_analytics



    working_dir:

      /app



    volumes:

      - ./analytics:/app



    command:

      python app.py



    ports:

      - "9003:9003"



  streaming:



    image: python:3.11



    container_name:

      iotec_streaming



    working_dir:

      /app



    volumes:

      - ./streaming:/app



    command:

      python app.py



    ports:

      - "9004:9004"



  governance:



    image: python:3.11



    container_name:

      iotec_governance



    working_dir:

      /app



    volumes:

      - ./governance:/app



    command:

      python app.py



    ports:

      - "9005:9005"

"""



# ============================================================

# APPS

# ============================================================



APP = """

from http.server import HTTPServer

from http.server import SimpleHTTPRequestHandler



PORT = 9000



print()

print("===================================")

print(" IOTEC CONTAINER ONLINE")

print("===================================")



server = HTTPServer(

    ('0.0.0.0', PORT),

    SimpleHTTPRequestHandler

)



server.serve_forever()

"""



# ============================================================

# EXPORTAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

# ============================================================



with open(



    BASE / "docker-compose.yml",



    "w",

    encoding="utf-8"



) as f:



    f.write(DOCKER)



for pasta in PASTAS:
    pass



    with open(



        BASE / pasta / "app.py",



        "w",

        encoding="utf-8"



    ) as f:



        f.write(APP)



# ============================================================

# POWERSHELL

# ============================================================



PS1 = f'''

cd "{BASE}"



docker compose up

'''



with open(



    BASE / "INICIAR_DOCKER.ps1",



    "w",

    encoding="utf-8"



) as f:



    f.write(PS1)



# ============================================================

# FINAL

# ============================================================



print()

print("===================================================")

print(" IOTEC ROCKBOOST DOCKER ENGINE")

print("===================================================")



print()

print(f"BASE -> {BASE}")



print()

print("CONTAINERS:")



for pasta in PASTAS:
    pass



    print(f" [+] {pasta}")



print()

print("ARQUIVOS:")



print(" [+] docker-compose.yml")

print(" [+] INICIAR_DOCKER.ps1")



print()

print("===================================================")

print(" EXECUÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O")

print("===================================================")



print()

print("1. INSTALAR DOCKER DESKTOP")



print()

print("2. ABRIR POWERSHELL")



print()

print("3. EXECUTAR")



print()

print("./INICIAR_DOCKER.ps1")



print()

print("===================================================")

print(" GOVERNANÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡A CONTAINERIZADA")

print("===================================================")





