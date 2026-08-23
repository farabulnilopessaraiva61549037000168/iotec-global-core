import logging
import importlib
from flask import Flask, request, jsonify

logging.basicConfig(level=logging.INFO, format='[MESA-NEGOCIACAO-IOTEC] %(message)s')

try:
    payments = importlib.import_module('070_IOTEC_PAYMENTS')
except Exception as e:
    logging.warning(f"Aviso: Módulo de pagamento não carregado no start: {e}")
    payments = None

class MesaDeNegociacao:
    """
    Agente Negociador B2B responsável por conduzir contrapropostas,
    aplicar descontos de tabela e fechar vendas em lote.
    """
    TABELA_PRECOS = {
        "individual": {"valor": 49.90, "desc": "Licença Individual IOTEC"},
        "pacote_5": {"valor": 199.00, "desc": "Pacote Revenda 5 Licenças IOTEC"},
        "pacote_20": {"valor": 599.00, "desc": "Pacote Franquia 20 Licenças IOTEC"}
    }

    @staticmethod
    def processar_resposta_cliente(lead_id, mensagem_cliente, email_cliente):
        msg = mensagem_cliente.lower().strip()
        logging.info(f"Analisando intenção do Lead [{lead_id}]: '{mensagem_cliente}'")

        # Regra 1: Intenção de compra direta ou revenda
        if "revenda" in msg or "pacote" in msg or "lote" in msg or "mais licenças" in msg:
            oferta = MesaDeNegociacao.TABELA_PRECOS["pacote_5"]
            resposta_texto = (
                f"Entendido! Para revendedores e parceiros B2B, temos o Pacote com 5 licenças por "
                f"R$ {oferta['valor']:.2f}. "
                f"Vou gerar a sua chave Pix para liberação imediata das licenças."
            )
        elif "desconto" in msg or "caro" in msg or "proposta" in msg:
            # Desconto negociado (10% na individual)
            valor_com_desconto = round(49.90 * 0.90, 2)
            oferta = {"valor": valor_com_desconto, "desc": "Licença IOTEC (Oferta Especial Negociada)"}
            resposta_texto = (
                f"Entendemos perfeitamente. Aprovamos um desconto especial na Mesa de Negociação IOTEC: "
                f"de R$ 49,90 por R$ {valor_com_desconto:.2f}. "
                f"Segue a chave Pix para concluir o fechamento."
            )
        else:
            oferta = MesaDeNegociacao.TABELA_PRECOS["individual"]
            resposta_texto = (
                f"Excelente! A Licença Individual IOTEC está saindo por R$ {oferta['valor']:.2f}. "
                f"Abaixo está a sua chave Pix."
            )

        # Gerar a cobrança no gateway
        pix_result = None
        if payments:
            pix_result = payments.criar_cobranca_pix(
                valor=oferta["valor"],
                descricao=oferta["desc"],
                email_cliente=email_cliente
            )

        return {
            "status": "negociado",
            "resposta_agente": resposta_texto,
            "oferta": oferta,
            "pix_dados": pix_result
        }

if __name__ == "__main__":
    logging.info("Módulo de Mesa de Negociação IOTEC inicializado com sucesso.")
    
    # Teste de simulação de negociação
    resultado_teste = MesaDeNegociacao.processar_resposta_cliente(
        lead_id="LEAD_TESTE_001",
        mensagem_cliente="Quero um pacote de revenda para meus clientes",
        email_cliente="revendedor@cliente.com"
    )
    print("\n--- SIMULAÇÃO DE NEGOCIAÇÃO REALIZADA ---")
    print(f"Resposta Agente: {resultado_teste['resposta_agente']}")
    print(f"Pix Gerado: {resultado_teste['pix_dados']}")
