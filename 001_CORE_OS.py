# ==============================================================================
# 001_CORE_OS.py
# IOTEC OMEGA X
# CORE OPERATING SYSTEM
# Parte 01
# ==============================================================================

from __future__ import annotations

import os
import sys
import json
import uuid
import queue
import time
import logging
import threading
import datetime

from pathlib import Path
from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional

# ==============================================================================
# VERSION
# ==============================================================================

CORE_NAME = "IOTEC CORE OS"

CORE_VERSION = "1.0.0"

BOOT_TIME = datetime.datetime.now()

# ==============================================================================
# PATHS
# ==============================================================================

ROOT = Path(__file__).parent

DATA = ROOT / "DATA"

LOGS = ROOT / "LOGS"

CONFIG = ROOT / "CONFIG"

CACHE = ROOT / "CACHE"

MISSIONS = ROOT / "MISSIONS"

EVENTS = ROOT / "EVENTS"

CAPABILITIES = ROOT / "CAPABILITIES"

TEMP = ROOT / "TEMP"

for folder in [
    DATA,
    LOGS,
    CONFIG,
    CACHE,
    MISSIONS,
    EVENTS,
    CAPABILITIES,
    TEMP,
]:
    folder.mkdir(exist_ok=True)

# ==============================================================================
# LOGGER
# ==============================================================================

logging.basicConfig(

    level=logging.INFO,

    format="%(asctime)s | %(levelname)s | %(message)s",

    handlers=[

        logging.FileHandler(LOGS / "core.log", encoding="utf8"),

        logging.StreamHandler()

    ]

)

LOGGER = logging.getLogger("CORE")

# ==============================================================================
# EVENT
# ==============================================================================

@dataclass
class Event:

    id: str

    timestamp: str

    category: str

    source: str

    action: str

    payload: dict = field(default_factory=dict)

# ==============================================================================
# MISSION
# ==============================================================================

@dataclass
class Mission:

    id: str

    name: str

    objective: str

    created: str

    status: str = "WAITING"

    priority: int = 5

    owner: str = "SYSTEM"

    metadata: dict = field(default_factory=dict)

# ==============================================================================
# CAPABILITY
# ==============================================================================

@dataclass
class Capability:

    id: str

    name: str

    category: str

    description: str

    enabled: bool = True

# ==============================================================================
# CORE
# ==============================================================================

class CoreOS:

    def __init__(self):

        self.running = False

        self.modules = {}

        self.capabilities = {}

        self.events = queue.Queue()

        self.missions = {}

        self.configuration = {}

        self.statistics = {

            "missions":0,

            "events":0,

            "modules":0,

            "capabilities":0

        }

        LOGGER.info("CORE CREATED")

    # -------------------------------------------------------------------------

    def boot(self):

        LOGGER.info("="*60)

        LOGGER.info(CORE_NAME)

        LOGGER.info(CORE_VERSION)

        LOGGER.info("BOOTING...")

        LOGGER.info("="*60)

        self.running=True

        self.load_configuration()

        self.load_capabilities()

        self.start_event_loop()

        LOGGER.info("CORE ONLINE")

    # -------------------------------------------------------------------------

    def shutdown(self):

        LOGGER.info("SHUTDOWN")

        self.running=False

    # -------------------------------------------------------------------------

    def register_module(self,name,module):

        self.modules[name]=module

        self.statistics["modules"]=len(self.modules)

        LOGGER.info(f"MODULE REGISTERED -> {name}")

    # -------------------------------------------------------------------------

    def register_capability(self,capability:Capability):

        self.capabilities[capability.id]=capability

        self.statistics["capabilities"]=len(self.capabilities)

        LOGGER.info(f"CAPABILITY -> {capability.name}")

    # -------------------------------------------------------------------------

    def create_mission(self,name,objective):

        mission=Mission(

            id=str(uuid.uuid4()),

            name=name,

            objective=objective,

            created=str(datetime.datetime.now())

        )

        self.missions[mission.id]=mission

        self.statistics["missions"]=len(self.missions)

        LOGGER.info(f"MISSION CREATED -> {mission.name}")

        return mission

    # -------------------------------------------------------------------------

    def publish_event(

        self,

        category,

        source,

        action,

        payload=None

    ):

        if payload is None:

            payload={}

        event=Event(

            id=str(uuid.uuid4()),

            timestamp=str(datetime.datetime.now()),

            category=category,

            source=source,

            action=action,

            payload=payload

        )

        self.events.put(event)

        self.statistics["events"]+=1

    # -------------------------------------------------------------------------

    def event_worker(self):

        while self.running:

            try:

                event=self.events.get(timeout=1)

                LOGGER.info(

                    f"[EVENT] "

                    f"{event.category} "

                    f"{event.source} "

                    f"{event.action}"

                )

            except:

                pass

    # -------------------------------------------------------------------------

    def start_event_loop(self):

        threading.Thread(

            target=self.event_worker,

            daemon=True

        ).start()

    # -------------------------------------------------------------------------

    def load_configuration(self):

        LOGGER.info("CONFIGURATION LOADED")

    # -------------------------------------------------------------------------

    def load_capabilities(self):

        LOGGER.info("CAPABILITIES LOADED")

    # -------------------------------------------------------------------------

    def dashboard(self):

        print()

        print("="*70)

        print("IOTEC CORE")

        print("="*70)

        print("Running :",self.running)

        print("Modules :",len(self.modules))

        print("Capabilities :",len(self.capabilities))

        print("Missions :",len(self.missions))

        print("Events :",self.statistics["events"])

        print("="*70)

# ==============================================================================
# BOOT
# ==============================================================================

if __name__=="__main__":

    core=CoreOS()

    core.boot()

    core.register_capability(

        Capability(

            id="COMMERCIAL",

            name="Commercial Engine",

            category="Business",

            description="Commercial Operations"

        )

    )

    mission=core.create_mission(

        "MISSION 001",

        "Acquire new contracts"

    )

    core.publish_event(

        "MISSION",

        "CORE",

        "CREATED",

        {

            "mission":mission.id

        }

    )

    while True:

        core.dashboard()

        time.sleep(5)

