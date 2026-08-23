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
    "service": "AI Automation",
    "message": "Teste",
    "origin": "LOCAL_TEST"
}

try:
    pass

    r = requests.post(
        "http://127.0.0.1:3000/new-lead",
        json=payload,
        timeout=10
    )

    print("")
    print("STATUS:", r.status_code)
    print("")
    print(r.text)

except Exception as e:
    pass

    print("")
    print("ERROR:")
    print(e)


