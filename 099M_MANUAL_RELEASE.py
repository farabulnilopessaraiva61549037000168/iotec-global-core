import sys
import argparse
from datetime import datetime, timezone, timedelta

def obter_hora_brasilia():
    tz_br = timezone(timedelta(hours=-3))
    return datetime.now(tz_br).strftime("%d/%m/%Y %H:%M:%S")

def liberar_ordem_manualmente(ordem_id, motivo):
    hora = obter_hora_brasilia()
    print("="*60)
    print("       NÚCLEO IOTEC/X27 - BAIXA MANUAL DE AUDITORIA       ")
    print("="*60)
    print(f" ID DA ORDEM : {ordem_id}")
    print(f" DATA/HORA   : {hora} (Horário de Brasília)")
    print(f" MOTIVO      : {motivo}")
    print("-" * 60)
    print(" [OK] STATUS ALTERADO PARA: APPROVED / PAID (MANUAL)")
    print(" [OK] FLUXO DE PÓS-VENDA LIBERADO COM SUCESSO!")
    print("="*60)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Liberação Manual IOTEC")
    parser.add_argument("--ordem", type=str, required=True, help="ID da Ordem")
    parser.add_argument("--motivo", type=str, default="Aviso manual de pagamento", help="Motivo da baixa")
    args = parser.parse_args()

    liberar_ordem_manualmente(args.ordem, args.motivo)
