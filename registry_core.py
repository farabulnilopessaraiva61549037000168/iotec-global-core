import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
from pathlib import Path

REGISTRY = Path('REGISTRY/registry.json')


def load_registry():
    if not REGISTRY.exists():
        REGISTRY.parent.mkdir(parents=True, exist_ok=True)
        REGISTRY.write_text('{"lots": [], "ports": {}, "modules": {}}')

    return json.loads(REGISTRY.read_text())


def save_registry(data):
    REGISTRY.write_text(json.dumps(data, indent=2))


def register_lot(name, ports):
    data = load_registry()

    entry = {
        'name': name,
        'ports': ports,
        'status': 'active'
    }

    data['lots'].append(entry)




