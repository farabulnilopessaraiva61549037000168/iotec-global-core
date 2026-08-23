from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class RevenueDatabase:

    table: str

    records: Dict[str, Any]


class RevenueDatabaseEngine:

    def __init__(self):

        self.tables: Dict[str, RevenueDatabase] = {}

    def create_table(self, table):

        if table not in self.tables:

            self.tables[table] = RevenueDatabase(

                table=table,

                records={}

            )

    def insert(self, table, key, value):

        self.create_table(table)

        self.tables[table].records[key] = value

    def get(self, table, key):

        if table not in self.tables:

            return None

        return self.tables[table].records.get(key)

    def table_count(self):

        return len(self.tables)

    def record_count(self):

        total = 0

        for table in self.tables.values():

            total += len(table.records)

        return total


if __name__ == "__main__":

    db = RevenueDatabaseEngine()

    print("=" * 70)

    print("REVENUE DATABASE ENGINE")

    print("=" * 70)

    print("TABLES   :", db.table_count())

    print("RECORDS  :", db.record_count())

