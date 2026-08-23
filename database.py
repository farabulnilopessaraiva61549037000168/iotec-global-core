import json
from pathlib import Path


ROOT = Path(r"C:\IOTEC")


DATABASES = {

    "companies": ROOT / "IOTEC_COMPANY_DATABASE.json",

    "crm": ROOT / "IOTEC_CRM_DATABASE.json",

    "pipeline": ROOT / "IOTEC_PIPELINE_DATABASE.json",

    "opportunities": ROOT / "IOTEC_OPPORTUNITY_DATABASE.json"

}


class JsonDatabase:

    def __init__(self, file):

        self.file = Path(file)

        self.file.parent.mkdir(parents=True, exist_ok=True)

        if not self.file.exists():

            with open(self.file, "w", encoding="utf-8") as f:

                json.dump([], f)

    # -----------------------------------------------------

    def load(self):

        try:

            with open(self.file, encoding="utf-8") as f:

                data = json.load(f)

            if isinstance(data, list):

                return data

            return []

        except:

            return []

    # -----------------------------------------------------

    def save(self, data):

        with open(self.file, "w", encoding="utf-8") as f:

            json.dump(

                data,

                f,

                indent=4,

                ensure_ascii=False

            )

    # -----------------------------------------------------

    def insert(self, record):

        data = self.load()

        data.append(record)

        self.save(data)

    # -----------------------------------------------------

    def update(self, key, value, new_record):

        data = self.load()

        updated = False

        for i, item in enumerate(data):

            if item.get(key) == value:

                data[i] = new_record

                updated = True

                break

        if updated:

            self.save(data)

        return updated

    # -----------------------------------------------------

    def exists(self, key, value):

        data = self.load()

        return any(

            x.get(key) == value

            for x in data

        )

    # -----------------------------------------------------

    def find(self, key, value):

        data = self.load()

        for item in data:

            if item.get(key) == value:

                return item

        return None

    # -----------------------------------------------------

    def count(self):

        return len(self.load())


CompanyDB = JsonDatabase(DATABASES["companies"])

CRMDB = JsonDatabase(DATABASES["crm"])

PipelineDB = JsonDatabase(DATABASES["pipeline"])

OpportunityDB = JsonDatabase(DATABASES["opportunities"])


if __name__ == "__main__":

    print("=" * 70)
    print("IOTEC ENTERPRISE DATABASE")
    print("=" * 70)
    print()

    print("Companies.....", CompanyDB.count())

    print("CRM...........", CRMDB.count())

    print("Pipeline......", PipelineDB.count())

    print("Opportunity...", OpportunityDB.count())

