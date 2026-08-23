import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
painel_replicador_ia.py

import os import shutil import uuid from datetime import datetime

DiretÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rios-base do sistema BASE

BASE_SITE_PATH = "./complexo_base" REPLICAS_DIR = "./replicas"

Teclado Mutante Jaguar body { margin: 0; background-color: #f9f9f9; font-family: 'Segoe UI', sans-serif; display: flex; flex-direction: column; height: 100vh; } header { background-color: #fff; border-bottom: 1px solid #ccc; padding: 1rem; text-align: center; font-weight: bold; } #teclado { flex: 1; display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 12px; padding: 1rem; transition: all 0.3s ease-in-out; } .tecla { background: #fff; border: 1px solid #ddd; padding: 1.5rem; border-radius: 12px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); cursor: pointer; text-align: center; transition: transform 0.2s; } .tecla:hover { transform: scale(1.05); box-shadow: 0 4px 10px rgba(0,0,0,0.1); } #botaoTopo { position: fixed; top: 10px; right: 10px; background: #444; color: white; border: none; padding: 0.5rem 1rem; border-radius: 8px; cursor: pointer; } .descanso { animation: pulse 4s



