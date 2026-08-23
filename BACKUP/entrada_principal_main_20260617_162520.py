import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from engine.simulador import rodar_simulacao

from config import MUNICIPIO



def main():
    pass

    print(f"\n=== IOTEC FISCAL COCKPIT ===")

    print(f"MunicÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­pio: {MUNICIPIO}\n")



    dados = {

        "professores": 100,

        "salario_atual": 2500,

        "piso": 3500,

        "aliquota_rpps": 0.14

    }



    resultado = rodar_simulacao(dados)



    print("\n--- RESULTADO ---")

    for k, v in resultado.items():
        pass

        print(f"{k}: {v}")



if __name__ == "__main__":
    pass

    main()




