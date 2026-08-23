import time
import logging
import importlib

logging.basicConfig(level=logging.INFO, format='[MAESTRO-IOTEC] %(message)s')

try:
    negociador = importlib.import_module('080_IOTEC_NEGOCIADOR')
except Exception as e:
    logging.error(f"Erro ao carregar o módulo Negociador: {e}")
    negociador = None

def executar_ciclo_vendas_automático():
    logging.info("--- INICIANDO CICLO AUTOMÁTICO DE PROSPECÇÃO E FECHAMENTO ---")
    
    # Exemplo de lead capturado pela esteira
    lead_simulado = {
        "id": "LEAD_NUVEM_001",
        "email": "cliente_potencial@empresa.com",
        "mensagem_recebida": "Quero comprar um pacote de revenda com desconto para minha empresa"
    }
    
    if negociador:
        logging.info(f"Processando lead [{lead_simulado['id']}] na Mesa de Negociação...")
        
        resultado = negociador.MesaDeNegociacao.processar_resposta_cliente(
            lead_id=lead_simulado["id"],
            mensagem_cliente=lead_simulado["mensagem_recebida"],
            email_cliente=lead_simulado["email"]
        )
        
        logging.info(f"Resposta Gerada: {resultado['resposta_agente']}")
        
        if resultado.get("pix_dados") and resultado["pix_dados"].get("status") == "sucesso":
            pix = resultado["pix_dados"]["pix_copia_cola"]
            logging.info(f"✅ Pix Gerado com Sucesso: {pix[:30]}...")
            logging.info("--> Oferta + Código Pix prontos para envio no atendimento ao cliente!")
        else:
            logging.warning("⚠️ Não foi possível gerar a chave Pix no ciclo atual.")

if __name__ == "__main__":
    logging.info("Orquestrador Maestro IOTEC Iniciado (Modo Nuvem/Ativo)...")
    
    # Executa uma rodada imediata e entra em loop contínuo
    executar_ciclo_vendas_automático()
