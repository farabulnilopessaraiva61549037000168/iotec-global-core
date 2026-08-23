import subprocess
import sqlite3
import sys
from pathlib import Path

ROOT = Path(r"C:\IOTEC")
DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

print("="*70)
print("OMEGA AUTONOMOUS CORE")
print("="*70)

def executar(script):

    arq = ROOT / script

    if not arq.exists():
        print(f"[IGNORADO] {script}")
        return

    print()
    print("="*70)
    print(script)
    print("="*70)

    subprocess.run(
        [sys.executable, str(arq)]
    )

conn = sqlite3.connect(DB, timeout=30)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

# ------------------------------------------------------------------
# ETAPA 1
# PROPOSTAS
# ------------------------------------------------------------------

propostas = cur.execute("""

SELECT COUNT(*)

FROM pipeline

WHERE status='PROPOSTA_ENVIADA'

""").fetchone()[0]

if propostas:

    executar("AUTO_APPROVAL_ENGINE.py")

# ------------------------------------------------------------------
# ETAPA 2
# PAGAMENTOS
# ------------------------------------------------------------------

pagamentos = cur.execute("""

SELECT COUNT(*)

FROM pipeline

WHERE status='PAGAMENTO_PENDENTE'

""").fetchone()[0]

if pagamentos:

    executar("PAYMENT_ENGINE.py")

# ------------------------------------------------------------------
# ETAPA 3
# MONITOR PAYPAL
# ------------------------------------------------------------------

aguardando = cur.execute("""

SELECT COUNT(*)

FROM pipeline

WHERE payment_status='AGUARDANDO_PAGAMENTO'

""").fetchone()[0]

if aguardando:

    executar("PAYPAL_AUTOMATION_ENGINE.py")

# ------------------------------------------------------------------
# ETAPA 4
# SINCRONIZAÃ‡ÃƒO
# ------------------------------------------------------------------

executar("SYNC_MONETIZATION_TO_TOWER.py")

# ------------------------------------------------------------------
# ETAPA 5
# DASHBOARD
# ------------------------------------------------------------------

executar("FLOW_ANALYZER.py")

executar("PIPELINE_EXECUTION_AUDITOR.py")

print()
print("="*70)
print("AUTONOMOUS CYCLE FINALIZADO")
print("="*70)

conn.close()


