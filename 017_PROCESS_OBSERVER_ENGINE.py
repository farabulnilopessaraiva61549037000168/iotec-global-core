# ==============================================================================
# 017_PROCESS_OBSERVER_ENGINE.py
# IOTEC - PROCESS OBSERVER ENGINE
# Observa e registra processos em execuÃ§Ã£o
# ==============================================================================

import json
import uuid
import os
from pathlib import Path
from datetime import datetime


DATABASE = Path("database/processes")
DATABASE.mkdir(parents=True, exist_ok=True)

ARQUIVO = DATABASE / "processes.json"


class ProcessObserver:

    def __init__(self):

        self.processos = {}

        self.carregar()

        print("\nPROCESS OBSERVER ENGINE ONLINE\n")


    def agora(self):

        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


    def salvar(self):

        with open(ARQUIVO, "w", encoding="utf-8") as f:

            json.dump(
                self.processos,
                f,
                indent=4,
                ensure_ascii=False
            )


    def carregar(self):

        if ARQUIVO.exists():

            with open(ARQUIVO, "r", encoding="utf-8") as f:

                self.processos = json.load(f)


    def iniciar(self, nome, tipo="GERAL", pid=None):

        uid = uuid.uuid4().hex[:8].upper()

        self.processos[uid] = {

            "id": uid,

            "nome": nome,

            "tipo": tipo,

            "pid": pid if pid else os.getpid(),

            "inicio": self.agora(),

            "fim": None,

            "status": "EXECUTANDO",

            "erro": None
        }

        self.salvar()

        print("=" * 60)
        print("PROCESSO INICIADO")
        print("=" * 60)
        print("ID........", uid)
        print("NOME......", nome)
        print("PID.......", self.processos[uid]["pid"])
        print()

        return uid


    def finalizar(self, uid):

        if uid not in self.processos:
            return

        self.processos[uid]["fim"] = self.agora()
        self.processos[uid]["status"] = "FINALIZADO"

        self.salvar()

        print(f"[FINALIZADO] {uid}")


    def erro(self, uid, mensagem):

        if uid not in self.processos:
            return

        self.processos[uid]["fim"] = self.agora()
        self.processos[uid]["status"] = "ERRO"
        self.processos[uid]["erro"] = mensagem

        self.salvar()

        print(f"[ERRO] {uid}")


    def listar(self):

        print("\n" + "=" * 70)
        print("PROCESSOS OBSERVADOS")
        print("=" * 70)

        for p in self.processos.values():

            print(f"[{p['id']}]")

            print("Nome......:", p["nome"])

            print("Tipo......:", p["tipo"])

            print("PID.......:", p["pid"])

            print("Status....:", p["status"])

            print("InÃ­cio....:", p["inicio"])

            print("Fim.......:", p["fim"])

            if p["erro"]:
                print("Erro......:", p["erro"])

            print("-" * 70)


# ==============================================================================
# TESTE
# ==============================================================================

if __name__ == "__main__":

    observer = ProcessObserver()

    proc = observer.iniciar(

        nome="DNA_AUDITOR",

        tipo="AUDITORIA"

    )

    observer.finalizar(proc)

    observer.listar()

