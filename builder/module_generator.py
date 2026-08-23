import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from pathlib import Path
from datetime import datetime

class ModuleGenerator:

    def __init__(self):

        self.template = """#!/usr/bin/env python3
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

            name="{MODULE_NAME}",

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
"""

    # ------------------------------------------------------------

    def create(self, filename):

        file = Path(filename)

        if file.exists():

            print("[EXISTE]", file.name)

            return

        codigo = self.template.replace(

            "{MODULE_NAME}",

            file.stem

        )

        file.write_text(

            codigo,

            encoding="utf-8"

        )

        print("[CRIADO]", file.name)

    # ------------------------------------------------------------

    def create_examples(self):

        exemplos = [

            "017_NOTIFICATION_CENTER.py",

            "018_EMAIL_ENGINE.py",

            "019_SMS_ENGINE.py"

        ]

        print()

        print("="*70)

        print("MODULE GENERATOR")

        print("="*70)

        print()

        for modulo in exemplos:

            self.create(modulo)

        print()

        print("GERAÃ‡ÃƒO FINALIZADA.")

        print()



