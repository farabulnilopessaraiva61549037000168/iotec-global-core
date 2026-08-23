import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    pass

    return """

    <html>

    <head>

    <title>IOTEC CONTROL TOWER</title>

    <style>

    body{
        background:#05070d;
        color:white;
        font-family:Arial;
        padding:40px;
    }

    h1{
        font-size:48px;
        color:#58c8ff;
    }

    .box{
        margin-top:30px;
        padding:20px;
        border-radius:16px;
        background:rgba(255,255,255,0.05);
        border:1px solid rgba(255,255,255,0.1);
    }

    </style>

    </head>

    <body>

    <h1>IOTEC CONTROL TOWER</h1>

    <div class="box">

    REALTIME OPERATIONAL CORE ACTIVE

    </div>

    </body>

    </html>

    """

print("")
print("================================================")
print(" IOTEC CONTROL TOWER")
print("================================================")
print("")
print("OPEN:")
print("http://127.0.0.1:3000")
print("")

app.run(
    host="127.0.0.1",
    port=3000,
    debug=True
)


