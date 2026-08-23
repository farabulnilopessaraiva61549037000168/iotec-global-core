import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from __future__ import annotations
from pathlib import Path
from typing import Any, Dict, List

from common.helpers import (
    save_json,
    score_asset,
    classify_asset,
    copy_to_quarantine,
)


class MinerNucleus:
    def __init__(self, base_dir: Path, config: Dict[str, Any]) -> None:
        self.base_dir = base_dir
        self.config = config
        self.out_dir = base_dir / config["paths"]["miner_dir"]
        self.quarantine_dir = base_dir / config["paths"]["miner_quarantine_dir"]
        self.ranking_dir = base_dir / config["paths"]["miner_ranking_dir"]
        self.catalog_dir = base_dir / config["paths"]["miner_catalog_dir"]

    def _scan_reservoir(self, base: Path, limit: int = 400) -> List[Dict[str, Any]]:
        out: List[Dict[str, Any]] = []
        if not base.exists():
            return out

        count = 0
        for item in base.rglob("*"):
            if count >= limit:
                break
            try:
                if item.is_file():
                    rel = item.relative_to(base)
                    depth = len(rel.parts)
                    out.append({
                        "name": item.name,
                        "path": str(item),
                        "size": item.stat().st_size,
                        "suffix": item.suffix.lower(),
                        "reservoir": str(base),
                        "depth": depth
                    })
                    count += 1
            except Exception:
                continue
        return out

    def execute(self, envelope: Dict[str, Any], compressed_complexity: float) -> Dict[str, Any]:
        reservoirs = [Path(p) for p in self.config.get("reservoirs", [])]
        scanned: List[Dict[str, Any]] = []

        for reservoir in reservoirs:
            scanned.extend(self._scan_reservoir(reservoir))

        selected: List[Dict[str, Any]] = []
        rejects: List[Dict[str, Any]] = []
        ranking: List[Dict[str, Any]] = []

        for item in scanned:
            category = classify_asset(item)
            item["category"] = category
            item["score"] = score_asset(item)

            if category == "reject":
                quarantine_path = copy_to_quarantine(item["path"], self.quarantine_dir)
                item["quarantine_copy"] = quarantine_path
                rejects.append(item)
            else:
                selected.append(item)

            ranking.append(item)

        ranking = sorted(ranking, key=lambda x: x.get("score", 0), reverse=True)

        catalog = {
            "visual": [x for x in selected if x["category"] == "visual"][:100],
            "corporate": [x for x in selected if x["category"] == "corporate"][:100],
            "hybrid": [x for x in selected if x["category"] == "hybrid"][:100]
        }

        payload = {
            "status": "ok",
            "kind": "miner",
            "objective": envelope.get("objective"),
            "compressed_complexity": compressed_complexity,
            "assets_scanned": len(scanned),
            "assets_selected": len(selected),
            "assets_rejected": len(rejects),
            "top_ranked_assets": ranking[:50],
            "selected_assets": selected[:200],
            "rejects_preview": rejects[:50]
        }

        save_json(self.out_dir / "miner_output.json", payload)
        save_json(self.ranking_dir / "asset_ranking.json", {"ranking": ranking[:200]})
        save_json(self.catalog_dir / "asset_catalog.json", catalog)
        return payload


