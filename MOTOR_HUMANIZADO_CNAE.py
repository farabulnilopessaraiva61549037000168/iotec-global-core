import sqlite3
import datetime

DB_PATH = "C:\\IOTEC\\iotec.db"

class MotorHumanizadoOficial:
    def __init__(self):
        self.inicializar_tabelas_oficiais()

    def inicializar_tabelas_oficiais(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS dados_institucionais (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                razao_social TEXT,
                cnpj TEXT,
                email_corporativo TEXT,
                whatsapp_sac TEXT
            )
        ''')

        cursor.execute('''
            INSERT OR REPLACE INTO dados_institucionais (id, razao_social, cnpj, email_corporativo, whatsapp_sac)
            VALUES (1, 'Farabulini Lopes Saraiva', '61.549.037/0001-68', 'IOTEC.BL@proton.me', 'EMBUTIDO_NUCLEO_IOTEC')
        ''')

        conn.commit()
        conn.close()

    def gerar_proposta_oficial(self, razao_social_cliente, cnae_codigo):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("SELECT setor_nome, ticket_medio_mrr, dor_principal FROM cnaes_alto_ticket WHERE codigo_cnae = ?", (cnae_codigo,))
        dados_cnae = cursor.fetchone()
        conn.close()

        if not dados_cnae:
            setor_nome, ticket, dor = "Atividade Industrial", 1200.00, "Instabilidade de infraestrutura e spam"
        else:
            setor_nome, ticket, dor = dados_cnae

        texto_email = f"""
Olá, equipe de Engenharia e TI da {razao_social_cliente}.

Me chamo Farabulini Lopes Saraiva, Diretor de Infraestrutura e Operações na IOTEC Tecnologia.

Analisando o perfil operacional e os requisitos técnicos de empresas do segmento de {setor_nome} (CNAE {cnae_codigo}), identificamos o impacto constante causado por {dor.lower()}.

Desenvolvemos o IOTEC Shield como uma camada corporativa de alto rendimento que atua diretamente nos seus servidores, e-mails e centrais PABX, eliminando ruídos digitais e liberando recursos de hardware sem interromper sua operação.

Nossos dados institucionais e canais oficiais para alinhamento técnico:
• Razão Social: Farabulini Lopes Saraiva (CNPJ: 61.549.037/0001-68)
• Contato Direto: IOTEC.BL@proton.me
• Atendimento / SAC Técnico via WhatsApp: Atendimento imediato em tela para validação de licença.

Caso faça sentido para a diretoria, posso disponibilizar uma licença de teste supervisionada pelo nosso time.

Atenciosamente,

Farabulini Lopes Saraiva
Diretor de Infraestrutura & Operações
Farabulini Lopes Saraiva | IOTEC Tecnologia
E-mail: IOTEC.BL@proton.me | iotec-shield.render.com
        """

        print("============================================================")
        print(f" ✉️ MENSAGEM OFICIAL HUMANIZADA -> {razao_social_cliente}")
        print("============================================================")
        print(f" ├─ Emissor: Farabulini Lopes Saraiva (CNPJ: 61.549.037/0001-68)")
        print(f" ├─ E-mail Oficial: IOTEC.BL@proton.me")
        print(f" ├─ CNAE Alvo: {cnae_codigo} ({setor_nome})")
        print(f" ├─ Ticket de Referência: R$ {ticket:,.2f}/mês")
        print(" └─ Corpo da Mensagem:")
        print(texto_email)
        print("============================================================\n")

if __name__ == "__main__":
    engine = MotorHumanizadoOficial()
    engine.gerar_proposta_oficial("BANCO DO BRASIL SA", "6499-9/99")
    engine.gerar_proposta_oficial("SENDAS DISTRIBUIDORA S/A", "5211-7/01")
