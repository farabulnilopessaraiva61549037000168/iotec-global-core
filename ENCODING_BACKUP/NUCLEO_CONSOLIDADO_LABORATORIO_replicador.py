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

Mascote IA Tsunama (simulaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o simples)

class Tsunama: def init(self, nome="Tsunama"): self.nome = nome self.cor = "translÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcida" self.halo = True

def saudar(self): return f"OlÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡, humano ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â! Eu sou {self.nome}, sua guia lesma espiritual minimalista. Vamos replicar com sabedoria." def relatar(self, mensagem): return f"{self.nome} diz: '{mensagem}'"

FunÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o principal de replicaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o

def replicar_complexo(nome_local, linguagem="pt", tema_cor="branco"): tsunama = Tsunama() print(tsunama.saudar())

nova_id = uuid.uuid4().hex[:8] destino = os.path.join(REPLICAS_DIR, f"{nome_local}_{nova_id}") try: shutil.copytree(BASE_SITE_PATH, destino) configurar_painel(destino, linguagem, tema_cor) print(tsunama.relatar(f"Complexo replicado em '{destino}' com linguagem '{linguagem}' e tema '{tema_cor}'.")) return destino except Exception as e: print(tsunama.relatar(f"Erro na replicaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o: {str(e)}")) return None

ConfiguraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o pÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³s-cÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³pia (ex: idioma e cor visual)

def configurar_painel(caminho, linguagem, tema): config_path = os.path.join(caminho, "config.txt") with open(config_path, "w") as f: f.write(f"linguagem={linguagem}\n")






