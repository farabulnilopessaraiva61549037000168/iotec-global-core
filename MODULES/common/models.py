import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from __future__ import annotations

from dataclasses import dataclass, field

from typing import Any, Dict





@dataclass

class CommandEnvelope:
    pass

    target_nucleus: str

    objective: str

    risk: float

    confidence_inputs: Dict[str, float]

    metadata: Dict[str, Any] = field(default_factory=dict)



    def score(self) -> float:
        pass

        values = []

        for _, value in self.confidence_inputs.items():
            pass

            try:
                pass

                values.append(float(value))

            except Exception:
                pass

                values.append(0.0)

        if not values:
            pass

            return 0.0

        return max(0.0, min(1.0, sum(values) / len(values)))




