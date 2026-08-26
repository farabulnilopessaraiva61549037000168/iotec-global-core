import sqlite3

DB_PATH = "C:\\IOTEC\\iotec.db"

class CallCenterVirtualIOTEC:
    def __init__(self):
        self.inicializar_banco_e_credenciais()
        self.inicializar_posicoes_atendimento()

    def inicializar_banco_e_credenciais(self):
        """ Garante a gravação permanente do CNPJ e dados institucionais no iotec.db """
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS credenciais_empresa (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                razao_social TEXT,
                cnpj TEXT UNIQUE,
                email_corporativo TEXT,
                whatsapp_sac TEXT,
                diretor_responsavel TEXT
            )
        ''')

        cursor.execute('''
            INSERT INTO credenciais_empresa (razao_social, cnpj, email_corporativo, whatsapp_sac, diretor_responsavel)
            VALUES ('Farabulini Lopes Saraiva', '61.549.037/0001-68', 'IOTEC.BL@proton.me', 'EMBUTIDO_NUCLEO_IOTEC', 'Farabulini Lopes Saraiva')
            ON CONFLICT(cnpj) DO UPDATE SET
                razao_social=excluded.razao_social,
                email_corporativo=excluded.email_corporativo,
                diretor_responsavel=excluded.diretor_responsavel
        ''')

        conn.commit()
        conn.close()

    def inicializar_posicoes_atendimento(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS callcenter_posicoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cnae_alvo TEXT UNIQUE,
                operador_nome TEXT,
                assunto_especifico TEXT,
                diagnostico_problema TEXT,
                solucao_tecnica TEXT,
                oferta_produto TEXT
            )
        ''')

        operadores = [
            (
                '6499-9/99', 
                'Operador Especialista em Fintechs & Core Bancário',
                'Proteção de Gateway e Estabilidade de Latência',
                'picos de ataques de bots e sobrecarga de memória RAM em servidores de validação de PIX/API',
                'IOTEC Quantum Shield — Módulo de Filtragem de Borda B2B',
                'R$ 5.000,00/mês'
            ),
            (
                '5211-7/01', 
                'Operador Especialista em Logística Portuária & Carga',
                'Gargalos na Integração de Manifestos e Robocalls no SAC',
                'bloqueios de linhas PABX no centro de distribuição e travamento de sistemas de manifesto de carga',
                'IOTEC Logística Shield — Interceptador PABX & CleanRAM',
                'R$ 3.500,00/mês'
            ),
            (
                '8610-1/00', 
                'Operador Especialista em Infraestrutura Hospitalar',
                'Descongestionamento de Linhas Telefônicas de Emergência',
                'congestionamento de centrais de atendimento médico por disparos massivos de telemarketing e bots',
                'IOTEC Health Gatekeeper — Blindagem PABX Hospitalar',
                'R$ 4.000,00/mês'
            ),
            (
                '1012-1/01', 
                'Operador Especialista em Agroindústria e Frigoríficos',
                'Estabilidade de Telemetria e Pedidos de Carga',
                'interrupções na troca de dados entre balanças industriais e o ERP central por acúmulo de logs mortos',
                'IOTEC AgroCore Telemetria & Expurgador de RAM',
                'R$ 2.500,00/mês'
            )
        ]

        for cnae, op_nome, assunto, diag, sol, oferta in operadores:
            cursor.execute('''
                INSERT INTO callcenter_posicoes 
                (cnae_alvo, operador_nome, assunto_especifico, diagnostico_problema, solucao_tecnica, oferta_produto)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(cnae_alvo) DO UPDATE SET
                    operador_nome=excluded.operador_nome,
                    assunto_especifico=excluded.assunto_especifico,
                    diagnostico_problema=excluded.diagnostico_problema,
                    solucao_tecnica=excluded.solucao_tecnica,
                    oferta_produto=excluded.oferta_produto
            ''', (cnae, op_nome, assunto, diag, sol, oferta))

        conn.commit()
        conn.close()

    def processar_atendimento_personalizado(self, empresa_alvo, cnae_alvo):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Busca credenciais oficiais gravadas
        cursor.execute("SELECT razao_social, cnpj, email_corporativo, diretor_responsavel FROM credenciais_empresa WHERE id = 1")
        razao, cnpj, email, diretor = cursor.fetchone()

        # Busca dados da posição do Call Center
        cursor.execute("SELECT operador_nome, assunto_especifico, diagnostico_problema, solucao_tecnica, oferta_produto FROM callcenter_posicoes WHERE cnae_alvo = ?", (cnae_alvo,))
        dados = cursor.fetchone()
        conn.close()

        if not dados:
            print(f" [!] Posição de atendimento para CNAE {cnae_alvo} em alocação...")
            return

        op_nome, assunto, diag, sol, oferta = dados

        mensagem = f"""
===============================================================================
📞 [POSIÇÃO VIRTUAL] {op_nome.upper()}
===============================================================================
EMISSOR OFICIAL: {razao} | CNPJ: {cnpj}
DE: {diretor} <{email}>
PARA: Diretoria de TI / Infraestrutura de {empresa_alvo}
ASSUNTO: Diagnóstico de Infraestrutura: {assunto}

Prezada equipe de Engenharia da {empresa_alvo},

Analisando os requisitos operacionais específicos da sua unidade (CNAE {cnae_alvo}), nossa mesa de acompanhamento técnico identificou que o setor enfrenta {diag}.

Para essa demanda específica, desenvolvemos o {sol}. Esta solução atua diretamente nas dependências de rede e centrais da sua empresa, neutralizando a causa raiz sem afetar os sistemas em produção.

Especificações de Credenciamento e Contato Institucional:
• Razão Social Credenciada: {razao}
• CNPJ Oficial: {cnpj}
• Solução Dedicada: {sol} ({oferta})
• E-mail Corporativo: {email}
• Atendimento SAC / WhatsApp: Suporte humano ativo em tela para validação e licença.

Caso a diretoria deseje analisar o relatório de desempenho do módulo, estamos à disposição para liberar uma licença de teste supervisionada.

Atenciosamente,

{diretor}
Diretor de Infraestrutura & Operações
{razao} | IOTEC Tecnologia
===============================================================================
"""
        print(mensagem)

if __name__ == "__main__":
    cc = CallCenterVirtualIOTEC()
    cc.processar_atendimento_personalizado("BANCO DO BRASIL SA", "6499-9/99")
    cc.processar_atendimento_personalizado("COMPLEXO HOSPITALAR CENTRAL", "8610-1/00")
