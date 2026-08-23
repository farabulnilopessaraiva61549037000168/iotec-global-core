import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def main():
    pass

    artemis_scan()

    generate_proposal(

        cliente="MUNICIPIO_EXEMPLO",

        problema="CONTINUIDADE_OPERACIONAL",

        pessoas_afetadas=25000,

        prejuizo_estimado=5000000,

        criticidade=8

    )

if __name__ == "__main__":
    main()




