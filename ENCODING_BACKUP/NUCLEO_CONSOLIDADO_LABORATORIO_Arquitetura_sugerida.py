import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
[Tablets (navegador)] <----WebSocket (Socket.IO)----> [Servidor Web (Flask + Flask-SocketIO / FastAPI + websockets)]
                                               \
                                                -> [Banco/JSON local para histÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rico e copiloto]
                                                -> [Dashboard (Dash/Plotly) para sua mesa]



