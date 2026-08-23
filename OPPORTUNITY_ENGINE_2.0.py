import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
==============================================================

IOTEC OPPORTUNITY ENGINE 2.0

GLOBAL COMMERCIAL INTELLIGENCE

==============================================================

MISSÃƒÆ'O

Centralizar todas as oportunidades comerciais da IOTEC.

Receber oportunidades oriundas de:

Ã¢â‚¬Â¢ Site
Ã¢â‚¬Â¢ Landing Pages
Ã¢â‚¬Â¢ IA
Ã¢â‚¬Â¢ Chat
Ã¢â‚¬Â¢ FormulÃƒÂ¡rios
Ã¢â‚¬Â¢ CRM
Ã¢â‚¬Â¢ LinkedIn
Ã¢â‚¬Â¢ Google
Ã¢â‚¬Â¢ Facebook
Ã¢â‚¬Â¢ Instagram
Ã¢â‚¬Â¢ LicitaÃƒÂ§ÃƒÂµes
Ã¢â‚¬Â¢ Editais
Ã¢â‚¬Â¢ NotÃƒÂ­cias
Ã¢â‚¬Â¢ Operadores Humanos

OBJETIVO

Responder continuamente:

Ã¢â‚¬Â¢ Quem precisa dos nossos produtos?
Ã¢â‚¬Â¢ Qual produto oferecer?
Ã¢â‚¬Â¢ Quanto vale a oportunidade?
Ã¢â‚¬Â¢ Qual a probabilidade de fechar?
Ã¢â‚¬Â¢ Qual campanha pertence?
Ã¢â‚¬Â¢ Quem serÃƒÂ¡ responsÃƒÂ¡vel?
Ã¢â‚¬Â¢ Quanto isso representa para o mapa de metas?

==============================================================
"""

import sqlite3
import os

from datetime import datetime
from dataclasses import dataclass

DB = r"C:\IOTEC\IOTEC_OPPORTUNITY.db"

conn = sqlite3.connect(DB, timeout=30)

conn.row_factory = sqlite3.Row

cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")



