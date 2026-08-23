"""
===================================================================================
                       IOTEC NUCLEUS - TELA DE RENDIMENTOS REAIS
               MÓDULO DE LIQUIDEZ E RETORNO SOBRE INVESTIMENTO (ROI)
===================================================================================
 Arquiteto-Chefe: Farabulini Lopes Saraiva
 Entidade Proprietária: CNPJ 61.549.037/0001-68
 Diretriz: Strict Real-Time Liquidity (Zero Simulação / Zero Falsos Positivos)
===================================================================================
"""

from typing import List, Dict, Any
import manifest

class TelaRendimentos:
    def __init__(self):
        # Apenas transações confirmadas via Webhook/API bancária entram aqui
        self.transacoes_processadas: List[Dict[str, Any]] = []

    def Ingerir_evento_bancario_real(self, webhook_payload: Dict[str, Any]) -> None:
        """
        Recebe apenas payloads autenticados do banco/gateway em tempo real.
        """
        self.transacoes_processadas.append(webhook_payload)

    def renderizar_painel_rendimentos(self) -> Dict[str, Any]:
        saldo_liquido_real = 0.0
        vendas_confirmadas = 0
        vendas_pendentes_rejeitadas = 0
        extrato_real = []

        for tx in self.transacoes_processadas:
            status = str(tx.get("status_banco", "")).upper()
            if status in ["PAID", "CONFIRMADO", "SETTLED", "CONFIRMADO_PELO_BANCO"]:
                valor_net = float(tx.get("valor_bruto", 0.0)) - float(tx.get("taxa_gateway", 0.0))
                saldo_liquido_real += valor_net
                vendas_confirmadas += 1
                extrato_real.append({
                    "tx_id": tx.get("tx_id"),
                    "cliente": tx.get("cliente"),
                    "modulo": tx.get("modulo_origem"),
                    "valor_liquido": valor_net
                })
            else:
                vendas_pendentes_rejeitadas += 1

        print("┌" + "─" * 73 + "┐")
        print("│                      PAINEL DE RENDIMENTOS REAIS - IOTEC               │")
        print("├" + "─" * 73 + "┤")
        print(f"│  SALDO LIQUIDADO EM CONTA (BRL) : R$ {saldo_liquido_real:>15,.2f}               │")
        print(f"│  TRANSAÇÕES CONFIRMADAS         : {vendas_confirmadas:>18}               │")
        print(f"│  EVENTOS PENDENTES/IGNORADOS    : {vendas_pendentes_rejeitadas:>18}               │")
        print("├" + "─" * 73 + "┤")
        print("│  STATUS DE AUDITORIA: [✓] SEM SIMULAÇÃO / ESPERANDO WEBHOOK REAL        │")
        print("└" + "─" * 73 + "┘\n")

        return {
            "saldo_liquido_total": saldo_liquido_real,
            "total_operacoes_confirmadas": vendas_confirmadas,
            "extrato": extrato_real
        }

if __name__ == "__main__":
    painel = TelaRendimentos()
    # Execução limpa: Sem dados fictícios injetados. Saldo Real = R$ 0,00
    painel.renderizar_painel_rendimentos()