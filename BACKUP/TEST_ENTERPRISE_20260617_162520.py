import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# TEST_ENTERPRISE.py

import requests

payload = {

    "name": "Bruno Lopes",
    "email": "bruno@globalenterprise.ai",
    "service": "Enterprise AI Automation",
    "message": "Operational automation and intelligent routing",
    "origin": "NETLIFY"

}

response = requests.post(

    "http://127.0.0.1:3000/new-lead",

    json=payload

)

print("\n================================================")
print(" TEST RESULT ")
print("================================================")
print(response.json())
print("================================================\n")


