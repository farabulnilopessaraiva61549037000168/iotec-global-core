# ==============================================================================
# IOTEC ENTERPRISE - ATENDIMENTO CONSULTIVO HUMANIZADO (MOTOR CEREBRAL)
# CNPJ: 61.549.037/0001-68
# ==============================================================================

import sqlite3
import time
import random
import logging

logging.basicConfig(level=logging.INFO, format='[AGENTE CAMILA] %(asctime)s - %(message)s')

class AgenteHumanizadoIOTEC:
    def __init__(self):
        self.db_path = r"C:\IOTEC\iotec_human_brain.db"
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS matriz_atendimento (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            etapa TEXT,
            intencao_cliente TEXT,
            gatilhos_reconhecimento TEXT,
            resposta_humanizada TEXT,
            acao_sistema TEXT,
            delay_segundos INTEGER
        )
        ''')
        
        cursor.execute("SELECT COUNT(*) FROM matriz_atendimento")
        if cursor.fetchone()[0] == 0:
            cenarios = [
                (
                    "ABORDAGEM_INICIAL", "PRIMEIRO_CONTATO",
                    "ola, bom dia, boa tarde, quem e, do que se trata",
                    "Olá! Aqui é a Camila, da IOTEC. Estou entrando em contato direto com o setor financeiro de vocês. Mapeamos um gargalo comum na emissão e liquidação de boletos na rotina da empresa e preparamos uma estrutura prática de conciliação via PIX automático para zerar essa taxa de inadimplência. Com quem eu conseguiria validar 2 minutinhos sobre isso por aqui?",
                    "AGUARDAR_RESPOSTA", 45
                ),
                (
                    "QUALIFICACAO", "DUVIDA_FUNCIONAMENTO",
                    "como funciona, qual a proposta, o que voces fazem, me explica, me manda material",
                    "Perfeito! Em resumo: nossa infraestrutura se conecta ao seu sistema de vendas ou faturamento e automatiza todo o ciclo. O cliente recebe o PIX dinâmico com baixa instantânea e emissão de nota sem precisar de intervenção manual da sua equipe. Isso reduz em até 70% o tempo gasto com cobranças manuais. Vocês usam algum ERP ou emissor próprio hoje?",
                    "REGISTRAR_INTERESSE", 60
                ),
                (
                    "OBJECAO_PRECO", "PERGUNTA_VALOR",
                    "quanto custa, qual o valor, e caro, tabela de preços, valores",
                    "Trabalhamos com um modelo muito enxuto para garantir retorno rápido. O investimento da licença corporativa é fixo em R$ 1.500/mês, sem taxas escondidas ou percentuais sobre o seu faturamento. Na prática, a economia em taxas de boletos e horas de equipe paga a licença logo na primeira semana. Consigo liberar o teste da estrutura para vocês ainda hoje.",
                    "ENVIAR_PREPROPOSTA", 50
                ),
                (
                    "OBJECAO_SEGURANCA", "CONFIRMACAO_CNPJ",
                    "tem cnpj, e seguro, qual a garantia, como contrato, empresa real",
                    "Com certeza, total transparência! Nossa operação é registrada sob o CNPJ 61.549.037/0001-68 (IOTEC Enterprise). Todo o fluxo de pagamentos é processado via gateway homologado com liquidação direta na conta da sua empresa, com contrato formal e nota fiscal inclusa.",
                    "ENVIAR_DADOS_INSTITUCIONAIS", 40
                ),
                (
                    "FECHAMENTO", "ACEITE_PROPOSTA",
                    "quero fechar, como pago, manda o link, manda o contrato, vamos fechar, aceito",
                    "Excelente decisão! Geramos o seu termo de adesão com a ativação da licença. Você pode conferir os detalhes e liberar a entrada da sua empresa por este link seguro com chave PIX oficial do Asaas: https://iotec-global-core.onrender.com/checkout/ativa-empresa. Assim que o PIX for confirmedo, nossa engenharia inicia a liberação no mesmo instante!",
                    "GERAR_CHECKOUT_ASAAS", 35
                )
            ]
            cursor.executemany('''
            INSERT INTO matriz_atendimento 
            (etapa, intencao_cliente, gatilhos_reconhecimento, resposta_humanizada, acao_sistema, delay_segundos)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', cenarios)
            conn.commit()
        conn.close()

    def processar_mensagem_cliente(self, mensagem_texto, nome_empresa="Empresa"):
        msg_clean = mensagem_texto.lower().strip()
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT intencao_cliente, gatilhos_reconhecimento, resposta_humanizada, delay_segundos, acao_sistema FROM matriz_atendimento")
        regras = cursor.fetchall()
        conn.close()

        resposta_escolhida = None
        delay_aplicado = 5
        acao = "RESPOSTA_PADRAO"

        for intencao, gatilhos, resposta, delay, acao_sys in regras:
            lista_gatilhos = [g.strip() for g in gatilhos.split(",")]
            if any(gatilho in msg_clean for gatilho in lista_gatilhos):
                resposta_escolhida = resposta
                delay_aplicado = delay + random.randint(-5, 10)
                acao = acao_sys
                break

        if not resposta_escolhida:
            resposta_escolhida = f"Entendo perfeitamente a necessidade da {nome_empresa}. Deixe-me confirmar esse detalhe específico com o nosso arquiteto de soluções para te responder com exatidão em instantes."
            delay_aplicado = 15

        return {
            "resposta": resposta_escolhida,
            "delay_segundos": max(3, delay_aplicado),
            "acao": acao
        }

if __name__ == "__main__":
    agente = AgenteHumanizadoIOTEC()
    print("\n--- TESTE DE SIMULAÇÃO DE RESPOSTAS HUMANIZADAS ---\n")
    
    testes = [
        "Olá, quem é você e do que se trata?",
        "Como funciona essa cobrança de PIX de vocês?",
        "Quanto custa para implementar isso na minha empresa?",
        "Vocês têm CNPJ e empresa registrada?",
        "Gostei, como faço para fechar o contrato agora?"
    ]

    for t in testes:
        print(f"[CLIENTE]: {t}")
        res = agente.processar_mensagem_cliente(t, "Atacadista B2B")
        print(f"[STATUS]: Simulando tempo de digitação humana ({res['delay_segundos']}s)...")
        print(f"[AGENTE CAMILA]: {res['resposta']}\n" + "-"*60)
