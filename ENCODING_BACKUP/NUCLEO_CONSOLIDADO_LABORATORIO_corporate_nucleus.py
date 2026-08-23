import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from __future__ import annotations
from pathlib import Path
from typing import Any, Dict, List

from common.helpers import save_json


class CorporateNucleus:
    def __init__(self, base_dir: Path, config: Dict[str, Any]) -> None:
        self.base_dir = base_dir
        self.config = config
        self.out_dir = base_dir / config["paths"]["corporate_dir"]

    def execute(self, envelope: Dict[str, Any], compressed_complexity: float) -> Dict[str, Any]:
        selected_assets = envelope.get("metadata", {}).get("selected_assets", [])
        docs: List[Dict[str, Any]] = []

        for item in selected_assets:
            if item.get("category") in {"corporate", "hybrid"}:
                docs.append(item)

        payload = {
            "status": "ok",
            "kind": "corporate",
            "objective": envelope.get("objective"),
            "compressed_complexity": compressed_complexity,
            "documents_routed": len(docs),
            "documents_preview": docs[:80],
            "tracks": {
                "analise": True,
                "auditoria": True,
                "pericia_documental": True,
                "autopsia_documental": True
            }
        }
        save_json(self.out_dir / "corporate_output.json", payload)
        return payload


