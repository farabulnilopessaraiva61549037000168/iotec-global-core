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


class VisualNucleus:
    def __init__(self, base_dir: Path, config: Dict[str, Any]) -> None:
        self.base_dir = base_dir
        self.config = config
        self.out_dir = base_dir / config["paths"]["visual_dir"]

    def execute(self, envelope: Dict[str, Any], compressed_complexity: float) -> Dict[str, Any]:
        selected_assets = envelope.get("metadata", {}).get("selected_assets", [])
        visual_assets: List[Dict[str, Any]] = []

        for item in selected_assets:
            if item.get("category") in {"visual", "hybrid"}:
                visual_assets.append(item)

        blueprint = {
            "rotational_slides": True,
            "special_effects": True,
            "channel_atmosphere": True,
            "narrative": [
                "escaneando solo digital",
                "descendo na mina",
                "veia digital encontrada",
                "cascalho valioso selecionado",
                "composiÃƒÆ'Ã‚Â§ÃƒÆ'Ã‚Â£o visual em andamento"
            ]
        }

        payload = {
            "status": "ok",
            "kind": "visual",
            "objective": envelope.get("objective"),
            "compressed_complexity": compressed_complexity,
            "visual_assets_routed": len(visual_assets),
            "visual_assets_preview": visual_assets[:80],
            "showcase_blueprint": blueprint
        }
        save_json(self.out_dir / "visual_output.json", payload)
        return payload


