import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import requests



payload = {



    "name": "Bruno",

    "email": "bruno@test.com",

    "service": "AI Operations",

    "message": "First real operational test",

    "origin": "NETLIFY"



}



response = requests.post(

    "http://127.0.0.1:3000/new-lead",

    json=payload

)



print(response.json())




