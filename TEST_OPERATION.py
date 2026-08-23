import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# TEST_OPERATION.py

import requests

payload = {

    "company": "Global Enterprise",
    "contact": "Bruno Lopes",
    "email": "bruno@enterprise.ai",

    "demand": """

    Enterprise AI automation
    with analytics dashboard,
    operational monitoring
    and infrastructure integration

    """

}

response = requests.post(

    "http://127.0.0.1:3000/operation",

    json=payload

)

print(response.json())




