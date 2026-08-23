# ==============================================================================
# 018_EXECUTION_ENGINE.py
# IOTEC - EXECUTION ENGINE
# HistÃ³rico completo das execuÃ§Ãµes
# ==============================================================================

import json
import uuid
from pathlib import Path
from datetime import datetime

DATABASE = Path("database/executions")
DATABASE.mkdir(parents=True, exist_ok=True)

ARQUIVO = DATABASE / "executions.json"


class ExecutionEngine:

    def __init__(self):

        self.execucoes = {}

        self.carregar()

        print("\nEXECUTION ENGINE ONLINE\n")

    def agora(self):
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def carregar(self):

        if ARQUIVO.exists():

            with open(ARQUIVO,"r",encoding="utf-8") as f:
                self.execucoes=json.load(f)

    def salvar(self):

        with open(ARQUIVO,"w",encoding="utf-8") as f:

            json.dump(
                self.execucoes,
                f,
                indent=4,
                ensure_ascii=False
            )

    def iniciar(

        self,

        investigation_id,

        process_id,

        modulo

    ):

        uid="EXEC-"+uuid.uuid4().hex[:8].upper()

        self.execucoes[uid]={

            "id":uid,

            "investigation":investigation_id,

            "process":process_id,

            "module":modulo,

            "inicio":self.agora(),

            "fim":None,

            "status":"EXECUTANDO",

            "arquivos":0,

            "eventos":0,

            "resultado":"",

            "cpu":None,

            "memoria":None,

            "duracao":None

        }

        self.salvar()

        print("="*60)
        print("EXECUÃ‡ÃƒO INICIADA")
        print("="*60)
        print(uid)

        return uid

    def registrar_eventos(self,uid,total):

        self.execucoes[uid]["eventos"]=total

        self.salvar()

    def registrar_arquivos(self,uid,total):

        self.execucoes[uid]["arquivos"]=total

        self.salvar()

    def finalizar(

        self,

        uid,

        resultado,

        cpu=None,

        memoria=None

    ):

        execucao=self.execucoes[uid]

        inicio=datetime.strptime(
            execucao["inicio"],
            "%d/%m/%Y %H:%M:%S"
        )

        fim=datetime.now()

        execucao["fim"]=fim.strftime("%d/%m/%Y %H:%M:%S")

        execucao["duracao"]=str(fim-inicio)

        execucao["status"]="FINALIZADA"

        execucao["resultado"]=resultado

        execucao["cpu"]=cpu

        execucao["memoria"]=memoria

        self.salvar()

        print(f"[FINALIZADA] {uid}")

    def dashboard(self):

        print("\n"+"="*70)

        print("EXECUÃ‡Ã•ES")

        print("="*70)

        for e in self.execucoes.values():

            print(e["id"])

            print("InvestigaÃ§Ã£o :",e["investigation"])

            print("Processo.....:",e["process"])

            print("MÃ³dulo.......:",e["module"])

            print("Status.......:",e["status"])

            print("Arquivos.....:",e["arquivos"])

            print("Eventos......:",e["eventos"])

            print("DuraÃ§Ã£o......:",e["duracao"])

            print("-"*70)


if __name__=="__main__":

    engine=ExecutionEngine()

    execucao=engine.iniciar(

        investigation_id="INV-000001",

        process_id="PROC-000001",

        modulo="DNA_AUDITOR"

    )

    engine.registrar_eventos(execucao,1543)

    engine.registrar_arquivos(execucao,742118)

    engine.finalizar(

        execucao,

        resultado="Gargalos encontrados.",

        cpu="38%",

        memoria="2.1 GB"

    )

    engine.dashboard()

