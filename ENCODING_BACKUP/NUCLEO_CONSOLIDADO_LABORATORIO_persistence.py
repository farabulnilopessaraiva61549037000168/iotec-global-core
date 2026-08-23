import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json


class PersistenceEngine:
    pass

    def __init__(
        self,
        registry
    ):

        self.registry = registry

        self.database = (
            "data/iotec_registry.json"
        )

    def save(self):
        pass

        data = []

        for mod in self.registry.modules.values():
            pass

            data.append({

                "id": mod.id,

                "name": mod.name,

                "category": mod.category,

                "priority": mod.priority,

                "status": mod.status,

                "description": mod.description
            })

        with open(
            self.database,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

        print("\n[PERSISTENCE]")

        print(
            "MODULE DATABASE SAVED"
        )


