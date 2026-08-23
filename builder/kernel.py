import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from datetime import datetime

class Kernel:

    def __init__(self):

        self.started = datetime.now()

    def status(self):

        print("[KERNEL] ONLINE")


