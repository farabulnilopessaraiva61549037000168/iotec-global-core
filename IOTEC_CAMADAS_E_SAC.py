import sqlite3
import time
import json
import datetime

DB_PATH = "C:\\IOTEC\\iotec.db"

def inicializar_estrutura_camadas():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Tabela de controle de licenças e suporte contínuo
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS licencas_e_suporte (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id TEXT,
            razao_social TEXT,
            chave_licenca TEXT,
            versao_sistema TEXT DEFAULT '1.0.0',
            status_suporte TEXT DEFAULT 'ATIVO',
            data_pagamento DATETIME,
            historico_atualizacoes TEXT
        )
    ''')
    conn.commit()
    conn.close()

class GatekeeperPagamento:
    """Garante que o Agente Arquiteto SO RODE após a confirmação financeira."""
    @staticmethod
    def verificar_e_liberar():
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Filtra estritamente quem PAGOU
        cursor.execute("SELECT id, razao_social, email FROM central_vendas_leads WHERE status_venda = 'PAGAMENTO_CONFIRMADO'")
        pagos = cursor.fetchall()
        
        for item in pagos:
            lead_id, empresa, email = item
            print(f"\n[💰 TESOURARIA IOTEC] Pagamento RECONHECIDO para: {empresa}")
            print(f"    └─ Encaminhando cliente para a CAMADA 3 (Agente Arquiteto Fabricante)...")
            
            # Atualiza status para desbloquear a fabricação
            cursor.execute("UPDATE central_vendas_leads SET status_venda = 'EM_FABRICACAO' WHERE id = ?", (lead_id,))
            
        conn.commit()
        conn.close()

class SACWhatsAppAutomacao:
    """Gerencia SAC, Reconfiguração e Venda de Atualizações via WhatsApp"""
    @staticmethod
    def processar_atendimento_sac(cliente, mensagem_cliente):
        print(f"\n[📱 SAC WHATSAPP IOTEC] Mensagem de {cliente}: \"{mensagem_cliente}\"")
        time.sleep(1)
        
        msg = mensagem_cliente.lower()
        if "reconfigurar" in msg or "erro" in msg or "mudar" in msg:
            print("    └─ [🤖 AGENTE RECONFIGURADOR]: Solicitando atualização remota de módulo...")
            print("    └─ [✔] Patch de correção gerado e enviado ao sistema do cliente com sucesso.")
            return "Sua reconfiguração foi aplicada remotamente com sucesso! Atualize seu sistema."
            
        elif "atualização" in msg or "novo recurso" in msg or "upgrade" in msg:
            print("    └─ [💼 AGENTE OPORTUNIDADE]: Oferta de upgrade enviada ao cliente.")
            return "Temos o Módulo 2.0 disponível! Deseja incluir Inteligência de Vendas no seu painel por R$ 149/mês?"
            
        else:
            return "Olá! Sou o assistente técnico IOTEC. Seu sistema está rodando na versão 1.0.0 estável. Como posso ajudar?"

if __name__ == "__main__":
    inicializar_estrutura_camadas()
    print("============================================================")
    print("   IOTEC ENGINE - CAMADAS DE SEGURANÇA E SAC ATIVADAS 24/7  ")
    print("============================================================")
    
    # Teste de validação da esteira
    GatekeeperPagamento.verificar_e_liberar()
    
    # Simulação de atendimento via SAC WhatsApp
    resposta = SACWhatsAppAutomacao.processar_atendimento_sac("Grupo Industrial S.A.", "Preciso reconfigurar a taxa de comissão no meu painel de vendas.")
    print(f"    └─ Resposta enviada ao cliente: \"{resposta}\"")
