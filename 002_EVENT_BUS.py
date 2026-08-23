# ==============================================================================
# 002_EVENT_BUS.py
# IOTEC OMEGA X
# GLOBAL EVENT BUS
# ==============================================================================

from __future__ import annotations

import uuid
import time
import threading
import traceback
from dataclasses import dataclass, field
from datetime import datetime
from collections import defaultdict
from queue import Queue, Empty
from typing import Callable, Dict, List, Any


# ==============================================================================
# EVENT
# ==============================================================================

@dataclass
class Event:

    id: str

    topic: str

    source: str

    action: str

    timestamp: str

    payload: dict = field(default_factory=dict)


# ==============================================================================
# EVENT BUS
# ==============================================================================

class EventBus:

    def __init__(self):

        self.queue = Queue()

        self.subscribers: Dict[str, List[Callable]] = defaultdict(list)

        self.running = False

        self.thread = None

        self.statistics = {

            "published": 0,

            "processed": 0,

            "failed": 0,

            "topics": 0,

            "listeners": 0

        }

    # -------------------------------------------------------------------------

    def start(self):

        if self.running:

            return

        self.running = True

        self.thread = threading.Thread(

            target=self.__worker,

            daemon=True

        )

        self.thread.start()

        print("[EVENT BUS] ONLINE")

    # -------------------------------------------------------------------------

    def stop(self):

        self.running = False

        print("[EVENT BUS] OFFLINE")

    # -------------------------------------------------------------------------

    def subscribe(

        self,

        topic: str,

        callback: Callable

    ):

        self.subscribers[topic].append(callback)

        self.statistics["topics"] = len(self.subscribers)

        self.statistics["listeners"] = sum(

            len(x)

            for x in self.subscribers.values()

        )

    # -------------------------------------------------------------------------

    def unsubscribe(

        self,

        topic,

        callback

    ):

        if topic not in self.subscribers:

            return

        if callback in self.subscribers[topic]:

            self.subscribers[topic].remove(callback)

    # -------------------------------------------------------------------------

    def publish(

        self,

        topic,

        source,

        action,

        payload=None

    ):

        if payload is None:

            payload = {}

        event = Event(

            id=str(uuid.uuid4()),

            topic=topic,

            source=source,

            action=action,

            timestamp=str(datetime.now()),

            payload=payload

        )

        self.queue.put(event)

        self.statistics["published"] += 1

    # -------------------------------------------------------------------------

    def __worker(self):

        while self.running:

            try:

                event = self.queue.get(timeout=1)

            except Empty:

                continue

            listeners = self.subscribers.get(event.topic, [])

            for callback in listeners:

                try:

                    callback(event)

                except Exception:

                    self.statistics["failed"] += 1

                    traceback.print_exc()

            self.statistics["processed"] += 1

    # -------------------------------------------------------------------------

    def dashboard(self):

        print()

        print("=" * 70)

        print("GLOBAL EVENT BUS")

        print("=" * 70)

        print("STATUS..............", "ONLINE" if self.running else "OFFLINE")

        print("TOPICS..............", self.statistics["topics"])

        print("LISTENERS...........", self.statistics["listeners"])

        print("PUBLISHED...........", self.statistics["published"])

        print("PROCESSED...........", self.statistics["processed"])

        print("FAILED..............", self.statistics["failed"])

        print("QUEUE...............", self.queue.qsize())

        print("=" * 70)


# ==============================================================================
# TEST
# ==============================================================================

if __name__ == "__main__":

    bus = EventBus()

    def mission_listener(event):

        print()

        print("MISSION EVENT")

        print(event.action)

        print(event.payload)

    def commercial_listener(event):

        print()

        print("COMMERCIAL EVENT")

        print(event.payload)

    bus.subscribe(

        "MISSION",

        mission_listener

    )

    bus.subscribe(

        "COMMERCIAL",

        commercial_listener

    )

    bus.start()

    bus.publish(

        "MISSION",

        "CORE",

        "MISSION_CREATED",

        {

            "mission":"MISSION_001",

            "objective":"Acquire Contracts"

        }

    )

    bus.publish(

        "COMMERCIAL",

        "CRM",

        "NEW_LEAD",

        {

            "company":"ABC Engenharia",

            "city":"Fortaleza"

        }

    )

    while True:

        bus.dashboard()

        time.sleep(5)

