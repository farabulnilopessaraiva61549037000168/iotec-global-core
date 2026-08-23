import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import sqlite3
from datetime import datetime

ROOT = r"C:\IOTEC"

PALAVRAS_TESTE = [
    "TEST",
    "TESTE",
    "EXEMPLO",
    "MODELO",
    "DEMO",
    "LOCAL_TEST",
    "CLIENTE_EXEMPLO",
    "EMPRESA_EXEMPLO",
    "PREFEITURA MODELO",
    "ESCOLA ALFA",
    "CLINICA VIDA",
    "MARIA JULIA"
]

print("=" * 70)
print("X27 REALITY AUDITOR")
print("=" * 70)
print()
print("DATA:", datetime.now())
print()

reais = []
testes = []

for arquivo in os.listdir(ROOT):

    if not arquivo.endswith(".db"):
        continue

    banco = os.path.join(ROOT, arquivo)

    try:

        conn = sqlite3.connect(banco)
        cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

        cur.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        )

        tabelas = cur.fetchall()

        for tabela in tabelas:

            nome_tabela = tabela[0]

            try:

                cur.execute(
                    f"SELECT * FROM {nome_tabela}"
                )

                registros = cur.fetchall()

                for registro in registros:

                    texto = str(registro).upper()

                    eh_teste = False

                    for palavra in PALAVRAS_TESTE:

                        if palavra in texto:
                            eh_teste = True
                            break

                    if eh_teste:
                        testes.append(
                            (
                                banco,
                                nome_tabela,
                                registro
                            )
                        )
                    else:
                        reais.append(
                            (
                                banco,
                                nome_tabela,
                                registro
                            )
                        )

            except:
                pass

        conn.close()

    except:
        pass

print("=" * 70)
print("RESUMO")
print("=" * 70)

print("REGISTROS REAIS :", len(reais))
print("REGISTROS TESTE :", len(testes))

print()

print("=" * 70)
print("AMOSTRA TESTES")
print("=" * 70)

for item in testes[:20]:

    print()
    print(item[0])
    print(item[1])
    print(item[2])

print()

print("=" * 70)
print("AMOSTRA REAIS")
print("=" * 70)

for item in reais[:20]:

    print()
    print(item[0])
    print(item[1])
    print(item[2])

print()

print("=" * 70)
print("CONCLUSAO")
print("=" * 70)

if len(reais) == 0:
    print("NAO FORAM IDENTIFICADOS CLIENTES REAIS")
    print("NUCLEO OPERA PRINCIPALMENTE COM DADOS DE TESTE")

elif len(reais) < len(testes):
    print("PREDOMINANCIA DE DADOS DE TESTE")
    print("RECOMENDADO CAPTAR CLIENTES REAIS")

else:
    print("EXISTEM REGISTROS REAIS RELEVANTES")
    print("INICIAR AUDITORIA COMERCIAL")

print()
print("AUDITORIA FINALIZADA")



