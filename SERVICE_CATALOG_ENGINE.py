from dataclasses import dataclass
from typing import List


@dataclass
class ServiceCatalog:

    code: str
    name: str
    category: str
    active: bool = True


class ServiceCatalogEngine:

    def __init__(self):

        self.catalog: List[ServiceCatalog] = []

    def register(self, code, name, category):

        self.catalog.append(

            ServiceCatalog(

                code=code,

                name=name,

                category=category

            )

        )

    def total(self):

        return len(self.catalog)

    def categories(self):

        return sorted(

            {

                item.category

                for item in self.catalog

            }

        )

    def find(self, category):

        return [

            item

            for item in self.catalog

            if item.category == category

        ]


if __name__ == "__main__":

    engine = ServiceCatalogEngine()

    print("=" * 70)
    print("SERVICE CATALOG ENGINE")
    print("=" * 70)

    print("SERVICES   :", engine.total())
    print("CATEGORIES :", len(engine.categories()))

