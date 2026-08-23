# ==============================================================================
# 012_CRM_ENGINE.py
# ==============================================================================
# CRM PIPELINE ENGINE
# CompatÃ­vel com 011_LEAD_ENGINE.py
# ==============================================================================

from dataclasses import dataclass, asdict
from datetime import datetime
import json
import os
import uuid

DATABASE = "database/crm"

os.makedirs(DATABASE, exist_ok=True)


# ==============================================================================
# OPORTUNIDADE
# ==============================================================================

@dataclass
class Opportunity:

    id: str

    lead_id: str

    cliente: str

    empresa: str

    etapa: str

    valor: float

    probabilidade: int

    responsavel: str

    ultima_acao: str

    proxima_acao: str

    criado: str

    atualizado: str


# ==============================================================================
# CRM
# ==============================================================================

class CRMEngine:

    def __init__(self):

        self.pipeline = {}

        print("CRM ENGINE ONLINE")

    # -------------------------------------------------------------------------

    def criar_oportunidade(self, lead):

        agora = datetime.now().isoformat()

        oportunidade = Opportunity(

            id=str(uuid.uuid4())[:8],

            lead_id=lead.id,

            cliente=lead.nome,

            empresa=lead.empresa,

            etapa="NOVO",

            valor=lead.valor_estimado,

            probabilidade=10,

            responsavel="IOTEC IA",

            ultima_acao="Lead recebido",

            proxima_acao="Entrar em contato",

            criado=agora,

            atualizado=agora

        )

        self.pipeline[oportunidade.id] = oportunidade

        self.salvar(oportunidade)

        print(f"CRM -> {oportunidade.cliente}")

        return oportunidade

    # -------------------------------------------------------------------------

    def mover(self, oportunidade_id, etapa):

        if oportunidade_id not in self.pipeline:

            return

        op = self.pipeline[oportunidade_id]

        op.etapa = etapa

        op.atualizado = datetime.now().isoformat()

        op.ultima_acao = f"Movido para {etapa}"

        probabilidades = {

            "NOVO":10,

            "CONTATO":20,

            "DIAGNOSTICO":40,

            "PROPOSTA":60,

            "NEGOCIACAO":80,

            "FECHADO":100

        }

        op.probabilidade = probabilidades.get(etapa,0)

        self.salvar(op)

    # -------------------------------------------------------------------------

    def salvar(self, oportunidade):

        arquivo = os.path.join(

            DATABASE,

            f"{oportunidade.id}.json"

        )

        with open(

            arquivo,

            "w",

            encoding="utf8"

        ) as f:

            json.dump(

                asdict(oportunidade),

                f,

                indent=4,

                ensure_ascii=False

            )

    # -------------------------------------------------------------------------

    def dashboard(self):

        print()

        print("="*70)

        print("CRM PIPELINE")

        print("="*70)

        total = 0

        fechado = 0

        etapas = {}

        for op in self.pipeline.values():

            total += op.valor

            etapas[op.etapa] = etapas.get(op.etapa,0)+1

            if op.etapa == "FECHADO":

                fechado += op.valor

        for etapa, quantidade in etapas.items():

            print(f"{etapa:20} {quantidade}")

        print()

        print(f"PIPELINE.............. R$ {total:,.2f}")

        print(f"FECHADO............... R$ {fechado:,.2f}")

        print("="*70)

        print()

        for op in self.pipeline.values():

            print(

                f"{op.cliente:30}"

                f"{op.etapa:15}"

                f"{op.probabilidade:4}%"

                f" R$ {op.valor:,.2f}"

            )


# ==============================================================================
# TESTE
# ==============================================================================

if __name__ == "__main__":

    from importlib import import_module

    lead_module = import_module("011_LEAD_ENGINE")

    engine = lead_module.LeadEngine()

    crm = CRMEngine()

    lead = engine.novo_lead(

        nome="Empresa XPTO",

        empresa="XPTO LTDA",

        email="contato@xpto.com",

        telefone="(85)99999-0000",

        cidade="Fortaleza",

        interesse="Auditoria Digital",

        valor=15000

    )

    oportunidade = crm.criar_oportunidade(lead)

    crm.mover(oportunidade.id,"CONTATO")

    crm.dashboard()

