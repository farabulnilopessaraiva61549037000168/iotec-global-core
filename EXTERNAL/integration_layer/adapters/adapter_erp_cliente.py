import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from __future__ import annotations

import json

from pathlib import Path

from typing import Any, Dict





class ERPClientAdapter:
    pass

    def __init__(self, contract_path: str, mapping_path: str) -> None:
        pass

        self.contract = json.loads(Path(contract_path).read_text(encoding="utf-8"))

        self.mapping = json.loads(Path(mapping_path).read_text(encoding="utf-8"))



    def transform(self, source_payload: Dict[str, Any]) -> Dict[str, Any]:
        pass

        output: Dict[str, Any] = {}

        for field in self.mapping.get("fields", []):
            pass

            src = field.get("from")

            dst = field.get("to")

            output[dst] = self._extract(source_payload, src)

        return output



    def _extract(self, data: Dict[str, Any], dotted_path: str) -> Any:
        pass

        current: Any = data

        for part in dotted_path.split("."):
            pass

            if not isinstance(current, dict):
                pass

                return None

            current = current.get(part)

        return current




