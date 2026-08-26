import sqlite3

DB_PATH = "C:\\IOTEC\\iotec.db"

class MotorIntegradoGlobal:
    def __init__(self):
        self.inicializar_banco()

    def inicializar_banco(self):
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

    def processar_proposta_com_escavacao(self, empresa_alvo, cnae_alvo):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # 1. Puxa credenciais
        cursor.execute("SELECT razao_social, cnpj, email_corporativo, diretor_responsavel FROM credenciais_empresa WHERE id = 1")
        razao, cnpj, email, diretor = cursor.fetchone()

        # 2. Puxa operador do Call Center
        cursor.execute("SELECT operador_nome, assunto_especifico, diagnostico_problema, solucao_tecnica, oferta_produto FROM callcenter_posicoes WHERE cnae_alvo = ?", (cnae_alvo,))
        dados_op = cursor.fetchone()

        # 3. Escava 3 módulos das camadas profundas menos expostas
        cursor.execute('''
            SELECT modulo_hash, camada_nucleo 
            FROM controle_exposicao_modulos 
            ORDER BY quantidade_exposicoes ASC, RANDOM() 
            LIMIT 3
        ''')
        modulos_profundos = cursor.fetchall()

        # Atualiza contagem de exposição para girar o acervo
        for m_hash, _ in modulos_profundos:
            cursor.execute("UPDATE controle_exposicao_modulos SET quantidade_exposicoes = quantidade_exposicoes + 1 WHERE modulo_hash = ?", (m_hash,))

        conn.commit()
        conn.close()

        if not dados_op:
            print(f" [!] CNAE {cnae_alvo} sem operador alocado.")
            return

        op_nome, assunto, diag, sol, oferta = dados_op

        # Formatação do bloco de módulos do núcleo
        bloco_modulos = "\n".join([f"   ├─ [{camada}] Módulo: {m_hash}" for m_hash, camada in modulos_profundos])

        mensagem = f"""
===============================================================================
📞 [POSIÇÃO VIRTUAL + ESCAVAÇÃO NÚCLEO] {op_nome.upper()}
===============================================================================
EMISSOR OFICIAL: {razao} | CNPJ: {cnpj}
DE: {diretor} <{email}>
PARA: Diretoria de TI / Infraestrutura de {empresa_alvo}
ASSUNTO: Diagnóstico de Infraestrutura: {assunto}

Prezada equipe de Engenharia da {empresa_alvo},

Analisando os requisitos operacionais específicos da sua unidade (CNAE {cnae_alvo}), nossa mesa de acompanhamento técnico identificou que o setor enfrenta {diag}.

Para essa demanda específica, montamos uma arquitetura combinada que atua diretamente nas dependências de rede da sua empresa, composta pela solução principal e 3 módulos do núcleo avançado:

• Solução Base: {sol}
• Arquitetura Resgatada do Núcleo Profundo (Otimização Específica):
{bloco_modulos}

Especificações de Credenciamento e Contato Institucional:
• Razão Social Credenciada: {razao}
• CNPJ Oficial: {cnpj}
• Licenciamento e Suporte: {oferta}
• E-mail Corporativo: {email}
• Atendimento SAC / WhatsApp: Suporte humano ativo em tela para validação e licença.

Caso a diretoria deseje analisar o relatório de desempenho dessa compilação, estamos à disposição para liberar uma licença de teste supervisionada.

Atenciosamente,

{diretor}
Diretor de Infraestrutura & Operações
{razao} | IOTEC Tecnologia
===============================================================================
"""
        print(mensagem)

if __name__ == "__main__":
    motor = MotorIntegradoGlobal()
    motor.processar_proposta_com_escavacao("BANCO DO BRASIL SA", "6499-9/99")
    motor.processar_proposta_com_escavacao("SENDAS DISTRIBUIDORA S/A", "5211-7/01")
