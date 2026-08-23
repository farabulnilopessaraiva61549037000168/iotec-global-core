import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from __future__ import annotations
import json
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import urlparse

BASE_DIR = Path(__file__).resolve().parents[2]
ROUTER_DIR = BASE_DIR / "CORE" / "router"
MODULES_DIR = BASE_DIR / "MODULES"
CONFIG_PATH = BASE_DIR / "CONFIG" / "iotec_config.json"

sys.path.insert(0, str(ROUTER_DIR))
sys.path.insert(0, str(MODULES_DIR))

from common.helpers import load_json
from visible_core_router import SuperIllusionVisibleCore


class Handler(BaseHTTPRequestHandler):
    core = SuperIllusionVisibleCore()
    config = load_json(CONFIG_PATH)

    def _send(self, code: int, payload: dict) -> None:
        data = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/api/status":
            self._send(200, {
                "status": "ok",
                "service": "IOTEC Visible Core API V2",
                "architecture": self.config.get("architecture_name"),
                "version": self.config.get("version")
            })
            return
        if parsed.path == "/api/describe":
            self._send(200, self.core.describe())
            return
        self._send(404, {"status": "not_found", "path": parsed.path})

    def do_POST(self):
        parsed = urlparse(self.path)
        if parsed.path != "/api/dispatch":
            self._send(404, {"status": "not_found", "path": parsed.path})
            return

        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length).decode("utf-8") if length > 0 else "{}"

        try:
            payload = json.loads(body)
        except Exception:
            self._send(400, {"status": "bad_request", "message": "JSON invÃƒÆ'Ã‚Â¡lido."})
            return

        self._send(200, self.core.dispatch(payload))


def main() -> None:
    config = load_json(CONFIG_PATH)
    host = config.get("host", "127.0.0.1")
    port = int(config.get("port", 8787))
    server = HTTPServer((host, port), Handler)
    print(f"IOTEC Visible Core API V2 em http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    main()


