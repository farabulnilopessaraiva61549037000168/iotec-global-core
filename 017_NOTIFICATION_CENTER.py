import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass
from datetime import datetime
import logging
import uuid

LOGGER = logging.getLogger(__name__)

@dataclass
class ModuleInfo:

    id: str
    name: str
    created_at: str


class Module:

    def __init__(self):

        self.info = ModuleInfo(

            id=str(uuid.uuid4()),

            name="017_NOTIFICATION_CENTER",

            created_at=str(datetime.now())

        )

    # --------------------------------------------------

    def execute(self):

        LOGGER.info("%s ONLINE", self.info.name)

        print()

        print("="*70)

        print(self.info.name)

        print("="*70)

        print("ID.......:", self.info.id)

        print("CRIADO...:", self.info.created_at)

        print("STATUS...: ONLINE")

        print()

if __name__=="__main__":

    Module().execute()




