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


class ValidationNucleus:
    def __init__(self, base_dir: Path, config: Dict[str, Any]) -> None:
        self.base_dir = base_dir
        self.config = config
        self.out_dir = base_dir / config["paths"]["results_dir"]

    def execute(self, envelope: Dict[str, Any], compressed_complexity: float) -> Dict[str, Any]:
        checks: List[Dict[str, Any]] = envelope.get("metadata", {}).get("checks", [])
        passed = True
        failed = []

        for check in checks:
            if not check.get("ok", False):
                passed = False
                failed.append(check.get("name", "unknown"))

        payload = {
            "status": "ok" if passed else "blocked",
            "kind": "validation",
            "objective": envelope.get("objective"),
            "compressed_complexity": compressed_complexity,
            "checks_count": len(checks),
            "passed": passed,
            "failed_reasons": failed
        }
        save_json(self.out_dir / "validation_output.json", payload)
        return payload


