import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
import tkinter as tk
from tkinter import ttk

CONTRACT_DB = r"C:\IOTEC\IOTEC_CONTRACTS.db"
OPPORTUNITY_DB = r"C:\IOTEC\IOTEC_OPPORTUNITY.db"

root = tk.Tk()

root.title("IOTEC EXECUTIVE WALL")

root.configure(bg="black")

root.state("zoomed")

title = tk.Label(
    root,
    text="IOTEC COMMAND CENTER",
    bg="black",
    fg="white",
    font=("Segoe UI", 30, "bold")
)

title.pack(pady=20)

revenue_label = tk.Label(
    root,
    text="",
    bg="black",
    fg="white",
    font=("Segoe UI", 42, "bold")
)

revenue_label.pack(pady=20)

pipeline_label = tk.Label(
    root,
    text="",
    bg="black",
    fg="white",
    font=("Segoe UI", 24)
)

pipeline_label.pack(pady=10)

status_label = tk.Label(
    root,
    text="",
    bg="black",
    fg="white",
    font=("Segoe UI", 18)
)

status_label.pack(pady=10)

def refresh():
    pass

    try:
        pass

        conn = sqlite3.connect(CONTRACT_DB)
        cur = conn.cursor()

        revenue = cur.execute("""

        SELECT
        COALESCE(SUM(contract_value),0)

        FROM contracts

        WHERE status='ATIVO'

        """).fetchone()[0]

        conn.close()

    except:
        pass

        revenue = 0

    try:
        pass

        conn = sqlite3.connect(OPPORTUNITY_DB)
        cur = conn.cursor()

        pipeline = cur.execute("""

        SELECT
        COALESCE(
        SUM(
        estimated_value * probability / 100.0
        ),
        0
        )

        FROM opportunities

        """).fetchone()[0]

        conn.close()

    except:
        pass

        pipeline = 0

    revenue_label.config(
        text=f"RECEITA REAL\nR$ {revenue:,.2f}"
    )

    pipeline_label.config(
        text=f"PIPELINE\nR$ {pipeline:,.2f}"
    )

    if revenue > 0:
        pass

        status_label.config(
            text="STATUS: MONETIZANDO"
        )

    else:
        pass

        status_label.config(
            text="STATUS: EM EXPANSAO"
        )

    root.after(
        10000,
        refresh
    )

refresh()

root.mainloop()


