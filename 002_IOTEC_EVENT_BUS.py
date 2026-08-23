import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
===============================================================================
IOTEC OPERATING SYSTEM
===============================================================================

MÃƒâ€œDULO:
002_IOTEC_EVENT_BUS.py

MISSÃƒÆ'O

Barramento oficial de comunicaÃƒÂ§ÃƒÂ£o da plataforma.

Todos os mÃƒÂ³dulos enviam eventos para este barramento.

O Event Bus grava no Kernel e distribui as mensagens
para a Torre de Controle.

===============================================================================
"""

import sqlite3
from pathlib import Path
from datetime import datetime

ROOT = Path(r"C:\IOTEC")

DATABASE = ROOT / "kernel.db"


class EventBus:

    def __init__(self):

        self.conn = sqlite3.connect(DATABASE)

        self.cursor = self.conn.cursor()

    # ================================================================

    def now(self):

        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # ================================================================

    def publish(

        self,

        agente,

        setor,

        categoria,

        titulo,

        descricao,

        impacto="NORMAL",

        prioridade="NORMAL"

    ):

        self.cursor.execute("""

        INSERT INTO events(

            agent,

            type,

            description,

            timestamp

        )

        VALUES(?,?,?,?)

        """,

        (

            agente,

            categoria,

            f"{titulo} | {descricao}",

            self.now()

        )

        )

        self.conn.commit()

        print()

        print("="*70)

        print("NOVO EVENTO")

        print("="*70)

        print("Agente      :",agente)

        print("Setor       :",setor)

        print("Categoria   :",categoria)

        print("TÃƒÂ­tulo      :",titulo)

        print("DescriÃƒÂ§ÃƒÂ£o   :",descricao)

        print("Impacto     :",impacto)

        print("Prioridade  :",prioridade)

        print("HorÃƒÂ¡rio     :",self.now())

        print()

    # ================================================================

    def mission(

        self,

        titulo,

        setor,

        impacto,

        prioridade,

        responsavel

    ):

        self.cursor.execute("""

        INSERT INTO missions(

            title,

            sector,

            priority,

            impact,

            status,

            created

        )

        VALUES(?,?,?,?,?,?)

        """,

        (

            titulo,

            setor,

            prioridade,

            impacto,

            "ABERTA",

            self.now()

        )

        )

        self.conn.commit()

        print()

        print("="*70)

        print("MISSÃƒÆ'O CRIADA")

        print("="*70)

        print("TÃƒÂ­tulo      :",titulo)

        print("ResponsÃƒÂ¡vel :",responsavel)

        print("Setor       :",setor)

        print("Prioridade  :",prioridade)

        print("Impacto     :",impacto)

        print()

    # ================================================================

    def executive_message(

        self,

        titulo,

        contexto,

        acao

    ):

        print()

        print("="*70)

        print("REVISTA EXECUTIVA")

        print("="*70)

        print()

        print("ASSUNTO")

        print(titulo)

        print()

        print("O QUE ACONTECEU")

        print(contexto)

        print()

        print("AÃƒâ€¡ÃƒÆ'O RECOMENDADA")

        print(acao)

        print()


# =====================================================================

if __name__ == "__main__":

    bus = EventBus()

    bus.publish(

        agente="PAYMENT_ENGINE",

        setor="Financeiro",

        categoria="ALERTA",

        titulo="Pagamento interrompido",

        descricao="Webhook nÃƒÂ£o respondeu.",

        impacto="CRÃƒÂTICO",

        prioridade="ALTA"

    )

    bus.mission(

        titulo="Corrigir Webhook PayPal",

        setor="Financeiro",

        impacto="Libera vendas",

        prioridade="CRÃƒÂTICA",

        responsavel="Agente Financeiro"

    )

    bus.executive_message(

        titulo="Fluxo Comercial Interrompido",

        contexto="""
O nÃƒÂºcleo identificou que o fluxo de pagamento foi interrompido.
Os mÃƒÂ³dulos financeiros existem, porÃƒÂ©m a confirmaÃƒÂ§ÃƒÂ£o automÃƒÂ¡tica
do pagamento nÃƒÂ£o foi localizada.

Enquanto este problema permanecer, nenhuma venda poderÃƒÂ¡ ser
concluÃƒÂ­da automaticamente.
""",

        acao="""
1. Abrir PAYMENT_ENGINE.py

2. Verificar webhook.

3. Executar teste.

4. Validar retorno.

5. Confirmar missÃƒÂ£o.
"""

    )




# --- BLOCO ADICIONADO AUTOMATICAMENTE PARA MANTER O SERVIÇO ATIVO ---
import time
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
