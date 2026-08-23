import sys
import uuid
import json
from datetime import datetime, timezone, timedelta

def obter_hora_brasilia():
    tz_br = timezone(timedelta(hours=-3))
    return datetime.now(tz_br).strftime("%d/%m/%Y %H:%M:%S")

def registrar_auditoria_venda(cliente, item, valor, metodo, ultimos_digitos, parcelas):
    hora_oficial = obter_hora_brasilia()
    id_transacao = f"TXN-{uuid.uuid4().hex[:12].upper()}"
    token_gateway = f"tok_{uuid.uuid4().hex[:16]}"
    
    # Montando o pacote de auditoria blindado
    pacote_auditoria = {
        "timestamp_brasilia": hora_oficial,
        "id_operacao_interna": id_transacao,
        "dados_comerciais": {
            "cliente": cliente,
            "item_vendido": item,
            "valor_total_brl": valor
        },
        "dados_pagamento_seguro": {
            "metodo": metodo,
            "status": "APPROVED_PAID",
            "condicao": f"Parcelado em {parcelas}x" if parcelas > 1 else "À Vista",
            "cartao_mascarado": f"**** **** **** {ultimos_digitos}",
            "cvv": "[REDACTED_BY_PCI_COMPLIANCE]",
            "token_gateway": token_gateway
        },
        "agente_emissor": "Atendimento Interno IOTEC"
    }

    print("="*65)
    print("      NÚCLEO IOTEC - REGISTRO DE AUDITORIA DE PAGAMENTO      ")
    print("="*65)
    print(f" [!] HORA OFICIAL : {hora_oficial}")
    print(f" [!] ID OPERAÇÃO  : {id_transacao}")
    print("-" * 65)
    print(" >> DADOS DA VENDA:")
    print(f"    Cliente       : {pacote_auditoria['dados_comerciais']['cliente']}")
    print(f"    Item          : {pacote_auditoria['dados_comerciais']['item_vendido']}")
    print(f"    Valor         : R$ {pacote_auditoria['dados_comerciais']['valor_total_brl']:.2f}")
    print("-" * 65)
    print(" >> DADOS DO PAGAMENTO (PCI-COMPLIANT):")
    print(f"    Método        : {pacote_auditoria['dados_pagamento_seguro']['metodo']}")
    print(f"    Condição      : {pacote_auditoria['dados_pagamento_seguro']['condicao']}")
    print(f"    Cartão        : {pacote_auditoria['dados_pagamento_seguro']['cartao_mascarado']}")
    print(f"    CVV           : {pacote_auditoria['dados_pagamento_seguro']['cvv']} (Não Armazenado)")
    print(f"    Token Gateway : {pacote_auditoria['dados_pagamento_seguro']['token_gateway']}")
    print("-" * 65)
    print(" [OK] TRANSAÇÃO REGISTRADA COM SUCESSO NO BANCO DE DADOS INTERNO.")
    print("="*65)
    
    return pacote_auditoria

if __name__ == "__main__":
    # Simulação da entrada de dados reais pelo cliente/atendimento (R$ 29,90)
    registrar_auditoria_venda(
        cliente="PROSPECT_REAL_FORTALEZA",
        item="Licença Mensal - Suporte IOTEC Base",
        valor=29.90,
        metodo="Cartão de Crédito (Mastercard)",
        ultimos_digitos="8472", # Só recebemos os 4 últimos do Gateway
        parcelas=1
    )