from datetime import datetime
import zoneinfo

def exibir_salas_globais():
    brt = datetime.now(zoneinfo.ZoneInfo("America/Fortaleza")).strftime("%Y-%m-%d %H:%M:%S")
    cest = datetime.now(zoneinfo.ZoneInfo("Europe/Berlin")).strftime("%Y-%m-%d %H:%M:%S")
    aest = datetime.now(zoneinfo.ZoneInfo("Australia/Sydney")).strftime("%Y-%m-%d %H:%M:%S")

    print("\n=======================================================")
    print("      USINA GLOBAL IOTEC - SALAS DE OPERAÇÃO (24/7)    ")
    print("=======================================================")
    print(f" Brasil (BRT)    : {brt} [Turno Noite / Fechamento]")
    print(f" Alemanha (CEST) : {cest} [Turno Madrugada / Abertura]")
    print(f" Austrália (AEST): {aest} [Turno Meio-Dia / Pico Ativo]")
    print("=======================================================\n")

if __name__ == "__main__":
    exibir_salas_globais()
