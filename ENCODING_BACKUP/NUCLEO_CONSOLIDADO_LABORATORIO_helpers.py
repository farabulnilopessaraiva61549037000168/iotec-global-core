import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from __future__ import annotations
import json
import math
import os
import shutil
import traceback
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def ensure_dir(path: str | Path) -> Path:
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def load_json(path: str | Path, default: Dict[str, Any] | None = None) -> Dict[str, Any]:
    p = Path(path)
    if not p.exists():
        return default if default is not None else {}
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: str | Path, data: Dict[str, Any]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def append_log(log_path: str | Path, level: str, message: str) -> None:
    p = Path(log_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8") as f:
        f.write(f"[{now_iso()}] [{level.upper()}] {message}\n")


def write_snapshot(snapshot_dir: str | Path, prefix: str, payload: Dict[str, Any]) -> str:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out = Path(snapshot_dir) / f"{ts}_{prefix}.json"
    save_json(out, payload)
    return str(out)


def bounded(value: float, minimum: float = 0.0, maximum: float = 1.0) -> float:
    return max(minimum, min(maximum, value))


def reliability_score(criteria: Dict[str, float]) -> float:
    vals: List[float] = []
    for _, v in criteria.items():
        try:
            vals.append(float(v))
        except Exception:
            vals.append(0.0)
    if not vals:
        return 0.0
    return bounded(sum(vals) / len(vals))


def compress_complexity_logarithmically(value: float) -> float:
    if value <= 0:
        return 0.0
    return round(math.log(value + 1, 10), 6)


def safe_exception_payload(exc: Exception) -> Dict[str, Any]:
    return {
        "type": exc.__class__.__name__,
        "message": str(exc),
        "traceback": traceback.format_exc()
    }


def env_info() -> Dict[str, Any]:
    return {
        "cwd": os.getcwd(),
        "username": os.environ.get("USERNAME", ""),
        "computername": os.environ.get("COMPUTERNAME", "")
    }


def score_asset(item: Dict[str, Any]) -> float:
    ext = item.get("suffix", "").lower()
    size = float(item.get("size", 0))
    depth = float(item.get("depth", 0))
    base = 0.25

    visual_ext = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg", ".mp4", ".mp3", ".wav", ".html", ".htm"}
    corp_ext = {".pdf", ".doc", ".docx", ".xlsx", ".csv", ".json", ".txt", ".md", ".py", ".ps1", ".js", ".ts"}

    if ext in visual_ext:
        base += 0.35
    if ext in corp_ext:
        base += 0.35

    if 1024 <= size <= 25_000_000:
        base += 0.20
    elif size > 25_000_000:
        base += 0.05

    if depth <= 6:
        base += 0.10

    return bounded(round(base, 4))


def classify_asset(item: Dict[str, Any]) -> str:
    ext = item.get("suffix", "").lower()
    visual_ext = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg", ".mp4", ".mp3", ".wav", ".html", ".htm"}
    corp_ext = {".pdf", ".doc", ".docx", ".xlsx", ".csv", ".json", ".txt", ".md", ".py", ".ps1", ".js", ".ts"}

    if ext in visual_ext and ext in corp_ext:
        return "hybrid"
    if ext in visual_ext:
        return "visual"
    if ext in corp_ext:
        return "corporate"
    return "reject"


def copy_to_quarantine(src: str | Path, quarantine_dir: str | Path) -> str | None:
    try:
        s = Path(src)
        if not s.exists() or not s.is_file():
            return None
        q = ensure_dir(quarantine_dir)
        target = q / s.name
        if target.exists():
            stem = target.stem
            suff = target.suffix
            target = q / f"{stem}_{datetime.now().strftime('%Y%m%d_%H%M%S')}{suff}"
        shutil.copy2(s, target)
        return str(target)
    except Exception:
        return None


