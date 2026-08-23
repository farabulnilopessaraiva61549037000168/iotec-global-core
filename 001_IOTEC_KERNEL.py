import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
===============================================================================
 IOTEC OPERATING SYSTEM
===============================================================================

MÃƒâ€œDULO:
001_IOTEC_KERNEL.py

VERSÃƒÆ'O:
1.0

MISSÃƒÆ'O

Este ÃƒÂ© o Sistema Operacional da IOTEC.

Nenhum motor conversa diretamente com outro.

Todos os motores conversam com o Kernel.

O Kernel administra:

Ã¢â‚¬Â¢ agentes
Ã¢â‚¬Â¢ setores
Ã¢â‚¬Â¢ eventos
Ã¢â‚¬Â¢ missÃƒÂµes
Ã¢â‚¬Â¢ decisÃƒÂµes
Ã¢â‚¬Â¢ prioridades
Ã¢â‚¬Â¢ indicadores
Ã¢â‚¬Â¢ logs

Toda a plataforma passa obrigatoriamente por aqui.

===============================================================================
"""

import sqlite3
import json
import os
from pathlib import Path
from datetime import datetime

# =============================================================================
# IDENTIDADE DO KERNEL
# =============================================================================

SYSTEM_NAME = "IOTEC OPERATING SYSTEM"

SYSTEM_VERSION = "1.0"

ROOT = Path(r"C:\IOTEC")

DATABASE = ROOT / "kernel.db"

CONFIG = ROOT / "kernel_config.json"

LOG_FOLDER = ROOT / "kernel_logs"

REPORT_FOLDER = ROOT / "kernel_reports"

LOG_FOLDER.mkdir(exist_ok=True)

REPORT_FOLDER.mkdir(exist_ok=True)

# =============================================================================
# KERNEL
# =============================================================================


class Kernel:

    def __init__(self):

        self.connection = sqlite3.connect(DATABASE)

        self.cursor = self.connection.cursor()

        self.initialize_database()

    # -------------------------------------------------------------------------

    def initialize_database(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS agents(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT,

            sector TEXT,

            status TEXT,

            last_seen TEXT,

            missions INTEGER,

            completed INTEGER

        )

        """)

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS events(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            agent TEXT,

            type TEXT,

            description TEXT,

            timestamp TEXT

        )

        """)

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS missions(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            title TEXT,

            sector TEXT,

            priority TEXT,

            impact TEXT,

            status TEXT,

            created TEXT

        )

        """)

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS decisions(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            title TEXT,

            reason TEXT,

            created TEXT

        )

        """)

        self.connection.commit()

    # -------------------------------------------------------------------------

    def now(self):

        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # -------------------------------------------------------------------------

    def register_agent(self, name, sector):

        self.cursor.execute("""

        INSERT INTO agents(

            name,

            sector,

            status,

            last_seen,

            missions,

            completed

        )

        VALUES(?,?,?,?,?,?)

        """,

        (

            name,

            sector,

            "ONLINE",

            self.now(),

            0,

            0

        )

        )

        self.connection.commit()

        print(f"[KERNEL] Agente registrado: {name}")

    # -------------------------------------------------------------------------

    def publish_event(

        self,

        agent,

        event_type,

        description

    ):

        self.cursor.execute("""

        INSERT INTO events(

            agent,

            type,

            description,

            timestamp

        )

        VALUES(?,?,?,?)

        """,

        (

            agent,

            event_type,

            description,

            self.now()

        )

        )

        self.connection.commit()

        print(f"[EVENTO] {description}")

    # -------------------------------------------------------------------------

    def create_mission(

        self,

        title,

        sector,

        priority,

        impact

    ):

        self.cursor.execute("""

        INSERT INTO missions(

            title,

            sector,

            priority,

            impact,

            status,

            created

        )

        VALUES(?,?,?,?,?,?)

        """,

        (

            title,

            sector,

            priority,

            impact,

            "ABERTA",

            self.now()

        )

        )

        self.connection.commit()

        print(f"[MISSÃƒÆ'O] {title}")

    # -------------------------------------------------------------------------

    def create_decision(

        self,

        title,

        reason

    ):

        self.cursor.execute("""

        INSERT INTO decisions(

            title,

            reason,

            created

        )

        VALUES(?,?,?)

        """,

        (

            title,

            reason,

            self.now()

        )

        )

        self.connection.commit()

        print(f"[DECISÃƒÆ'O] {title}")

# =============================================================================
# TESTE
# =============================================================================

if __name__ == "__main__":

    kernel = Kernel()

    kernel.register_agent(

        "KERNEL",

        "ADMINISTRAÃƒâ€¡ÃƒÆ'O"

    )

    kernel.publish_event(

        "KERNEL",

        "INICIALIZAÃƒâ€¡ÃƒÆ'O",

        "Sistema Operacional iniciado."

    )

    kernel.create_mission(

        "Construir Torre de Controle",

        "Infraestrutura",

        "ALTA",

        "Base do sistema operacional"

    )

    kernel.create_decision(

        "Inicializar Kernel",

        "Primeira execuÃƒÂ§ÃƒÂ£o do Sistema Operacional."

    )

    print()

    print("="*70)

    print("IOTEC OPERATING SYSTEM")

    print("Kernel iniciado com sucesso.")

    print("="*70)




# --- BLOCO ADICIONADO AUTOMATICAMENTE PARA MANTER O SERVIÇO ATIVO ---
import time
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
