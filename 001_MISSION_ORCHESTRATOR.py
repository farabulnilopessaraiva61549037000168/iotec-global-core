"""
===============================================================================
001_MISSION_ORCHESTRATOR.py
Orquestrador Central de MissÃµes da IOTEC
===============================================================================
"""

from datetime import datetime
from enum import Enum
import uuid


# =============================================================================
# STATUS DA MISSÃƒO
# =============================================================================

class MissionStatus(Enum):

    WAITING = "WAITING"

    PLANNING = "PLANNING"

    EXECUTING = "EXECUTING"

    PAUSED = "PAUSED"

    FINISHED = "FINISHED"

    FAILED = "FAILED"


# =============================================================================
# PRIORIDADES
# =============================================================================

class MissionPriority(Enum):

    LOW = 1

    NORMAL = 2

    HIGH = 3

    CRITICAL = 4


# =============================================================================
# MISSÃƒO
# =============================================================================

class Mission:

    def __init__(self,
                 title,
                 description,
                 priority=MissionPriority.NORMAL):

        self.id = str(uuid.uuid4())[:8]

        self.title = title

        self.description = description

        self.priority = priority

        self.status = MissionStatus.WAITING

        self.created_at = datetime.now()

    def info(self):

        return {

            "id": self.id,

            "title": self.title,

            "status": self.status.value,

            "priority": self.priority.name

        }


# =============================================================================
# ORQUESTRADOR
# =============================================================================

class MissionOrchestrator:

    def __init__(self):

        self.queue = []

        self.history = []

    # -------------------------------------------------------------------------

    def add_mission(self,
                    title,
                    description,
                    priority=MissionPriority.NORMAL):

        mission = Mission(title,
                          description,
                          priority)

        self.queue.append(mission)

        self.queue.sort(
            key=lambda x: x.priority.value,
            reverse=True
        )

        print(f"[MISSION CREATED] {mission.id} - {mission.title}")

        return mission

    # -------------------------------------------------------------------------

    def next_mission(self):

        if len(self.queue) == 0:

            return None

        mission = self.queue.pop(0)

        mission.status = MissionStatus.PLANNING

        return mission

    # -------------------------------------------------------------------------

    def execute(self, mission):

        print()

        print("=" * 60)

        print("EXECUTANDO MISSÃƒO")

        print("=" * 60)

        print(f"ID...........: {mission.id}")

        print(f"TÃTULO.......: {mission.title}")

        print(f"PRIORIDADE...: {mission.priority.name}")

        print()

        mission.status = MissionStatus.EXECUTING

        #
        # Aqui futuramente serÃ¡ criada automaticamente
        # uma Task Force especializada.
        #

        mission.status = MissionStatus.FINISHED

        self.history.append(mission)

        print()

        print("[MISSION COMPLETED]")

        print()

    # -------------------------------------------------------------------------

    def pending(self):

        return len(self.queue)

    # -------------------------------------------------------------------------

    def report(self):

        print()

        print("=" * 60)

        print("MISSION REPORT")

        print("=" * 60)

        print(f"Pendentes : {len(self.queue)}")

        print(f"ConcluÃ­das: {len(self.history)}")

        print()


# =============================================================================
# TESTE
# =============================================================================

if __name__ == "__main__":

    orchestrator = MissionOrchestrator()

    orchestrator.add_mission(

        "Construir Painel Comercial",

        "Criar painel para monitorar vendas.",

        MissionPriority.HIGH

    )

    orchestrator.add_mission(

        "Atualizar Banco",

        "Executar migraÃ§Ã£o.",

        MissionPriority.NORMAL

    )

    while orchestrator.pending():

        mission = orchestrator.next_mission()

        orchestrator.execute(mission)

    orchestrator.report()

