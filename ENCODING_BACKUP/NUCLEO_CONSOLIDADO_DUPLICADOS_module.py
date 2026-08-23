import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import uuid
from datetime import datetime


class Module:
    pass

    def __init__(
        self,
        name,
        category,
        priority=1,
        description=""
    ):

        self.id = (
            f"MOD-{uuid.uuid4().hex[:8].upper()}"
        )

        self.name = name
        self.category = category
        self.priority = priority
        self.description = description

        self.status = "ACTIVE"

        self.created_at = datetime.now()

    def execute(self):
        pass

        print(f"\n[EXECUTION] {self.name}")

        print(f"ID: {self.id}")

        print(f"CATEGORY: {self.category}")

        print(f"STATUS: {self.status}")

        print(f"TIME: {datetime.now()}")


