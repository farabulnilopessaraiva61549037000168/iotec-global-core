#!/usr/bin/env python3
# ============================================================
# 001_IOTEC_ARCHITECTURE_AUDITOR.py
# OFFICIAL IOTEC ARCHITECTURE AUDITOR
# ============================================================

import os
import json
import hashlib
import sqlite3
from pathlib import Path
from collections import defaultdict
from datetime import datetime

ROOT = Path.cwd()

IGNORAR = {
    "__pycache__",
    ".git",
    ".idea",
    ".vscode",
    "node_modules",
    ".venv",
    "venv",
    "dist",
    "build"
}


class Auditor:

    def __init__(self, raiz):

        self.raiz = Path(raiz)

        self.py = []
        self.db = []
        self.jsons = []
        self.csv = []
        self.logs = []

        self.total_linhas = 0

        self.modulos = []
        self.bancos = []

        self.duplicados = defaultdict(list)

    # ------------------------------------------------------

    def ignorar(self, path):

        for parte in path.parts:
            if parte in IGNORAR:
                return True

        return False

    # ------------------------------------------------------

    def hash(self, arquivo):

        h = hashlib.sha256()

        with open(arquivo, "rb") as f:

            while True:

                bloco = f.read(65536)

                if not bloco:
                    break

                h.update(bloco)

        return h.hexdigest()

    # ------------------------------------------------------

    def descobrir(self):

        print("\nESCANEANDO ARQUITETURA...\n")

        for root, dirs, files in os.walk(self.raiz):

            dirs[:] = [d for d in dirs if d not in IGNORAR]

            for nome in files:

                caminho = Path(root) / nome

                ext = caminho.suffix.lower()

                try:

                    tamanho = caminho.stat().st_size

                except:

                    tamanho = 0

                if ext == ".py":

                    self.py.append(caminho)

                    try:

                        with open(
                            caminho,
                            encoding="utf8",
                            errors="ignore"
                        ) as f:

                            linhas = len(f.readlines())

                    except:

                        linhas = 0

                    self.total_linhas += linhas

                    self.modulos.append({

                        "arquivo": str(caminho.relative_to(self.raiz)),
                        "linhas": linhas,
                        "bytes": tamanho

                    })

                elif ext == ".db":

                    self.db.append(caminho)

                elif ext == ".json":

                    self.jsons.append(caminho)

                elif ext == ".csv":

                    self.csv.append(caminho)

                elif ext in (".log", ".txt"):

                    self.logs.append(caminho)

                try:

                    h = self.hash(caminho)

                    self.duplicados[h].append(str(caminho))

                except:

                    pass

    # ------------------------------------------------------

    def auditar_bancos(self):

        print("AUDITANDO DATABASES...\n")

        for banco in self.db:

            dados = {

                "arquivo": str(banco.relative_to(self.raiz)),
                "tabelas": []

            }

            try:

                conn = sqlite3.connect(banco)

                cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

                cur.execute(
                    "SELECT name FROM sqlite_master WHERE type='table';"
                )

                tabelas = cur.fetchall()

                for tabela in tabelas:

                    nome = tabela[0]

                    try:

                        cur.execute(f'SELECT COUNT(*) FROM "{nome}"')

                        total = cur.fetchone()[0]

                    except:

                        total = -1

                    dados["tabelas"].append({

                        "nome": nome,
                        "registros": total

                    })

                conn.close()

            except Exception as erro:

                dados["erro"] = str(erro)

            self.bancos.append(dados)

    # ------------------------------------------------------

    def relatorio_terminal(self):

        print("=" * 70)
        print("IOTEC OFFICIAL ARCHITECTURE AUDITOR")
        print("=" * 70)

        print()

        print("DATA")

        print(datetime.now())

        print()

        print("ARQUIVOS PYTHON........:", len(self.py))
        print("DATABASES..............:", len(self.db))
        print("JSON...................:", len(self.jsons))
        print("CSV....................:", len(self.csv))
        print("LOGS...................:", len(self.logs))

        print()

        print("LINHAS DE CÃ"DIGO.......:", self.total_linhas)

        print()

        print("=" * 70)

        print("DATABASES")

        print("=" * 70)

        for banco in self.bancos:

            print()

            print(banco["arquivo"])

            for tabela in banco.get("tabelas", []):

                print(
                    f'   {tabela["nome"]:<35} {tabela["registros"]}'
                )

        print()

        print("=" * 70)

        print("TOP 20 MAIORES MÃ"DULOS")

        print("=" * 70)

        maiores = sorted(

            self.modulos,

            key=lambda x: x["linhas"],

            reverse=True

        )

        for m in maiores[:20]:

            print(

                f'{m["linhas"]:6}  {m["arquivo"]}'

            )

        print()

        print("=" * 70)

        print("ARQUIVOS DUPLICADOS")

        print("=" * 70)

        qtd = 0

        for lista in self.duplicados.values():

            if len(lista) > 1:

                qtd += 1

                print()

                for item in lista:

                    print(item)

        print()

        print("GRUPOS DUPLICADOS:", qtd)

    # ------------------------------------------------------

    def salvar_json(self):

        estrutura = {

            "data": str(datetime.now()),

            "python":

                self.modulos,

            "databases":

                self.bancos,

            "total_python":

                len(self.py),

            "total_db":

                len(self.db),

            "linhas":

                self.total_linhas

        }

        with open(

            "IOTEC_ARCHITECTURE_REPORT.json",

            "w",

            encoding="utf8"

        ) as f:

            json.dump(

                estrutura,

                f,

                indent=4,

                ensure_ascii=False

            )

    # ------------------------------------------------------

    def executar(self):

        self.descobrir()

        self.auditar_bancos()

        self.relatorio_terminal()

        self.salvar_json()

        print()

        print("RELATÃ"RIO GERADO")

        print("IOTEC_ARCHITECTURE_REPORT.json")


if __name__ == "__main__":

    Auditor(ROOT).executar()

