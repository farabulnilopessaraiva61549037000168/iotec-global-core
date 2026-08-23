import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import logging
from pathlib import Path

class BuilderLogger:

    def __init__(self):

        Path("logs").mkdir(exist_ok=True)

        self.logger = logging.getLogger("IOTEC")

        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:

            handler = logging.FileHandler(

                "logs/build.log",

                encoding="utf-8"

            )

            formatter = logging.Formatter(

                "%(asctime)s | %(levelname)s | %(message)s"

            )

            handler.setFormatter(formatter)

            self.logger.addHandler(handler)

    # ----------------------------------------------------

    def info(self,message):

        self.logger.info(message)

        print("[INFO]",message)

    # ----------------------------------------------------

    def warning(self,message):

        self.logger.warning(message)

        print("[WARNING]",message)

    # ----------------------------------------------------

    def error(self,message):

        self.logger.error(message)

        print("[ERROR]",message)


