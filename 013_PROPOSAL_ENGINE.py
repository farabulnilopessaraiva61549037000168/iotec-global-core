# ==============================================================================
# 013_PROPOSAL_ENGINE.py
# ==============================================================================
# Gera propostas comerciais em PDF
# Requer: pip install fpdf2
# ==============================================================================

from fpdf import FPDF
from datetime import datetime
import os

PASTA = "database/proposals"

os.makedirs(PASTA, exist_ok=True)


class ProposalEngine:

    def __init__(self):

        print("PROPOSAL ENGINE ONLINE")

    def gerar(self, oportunidade):

        numero = datetime.now().strftime("%Y%m%d%H%M%S")

        pdf = FPDF()

        pdf.add_page()

        pdf.set_font("Helvetica", "B", 18)

        pdf.cell(0, 12, "PROPOSTA COMERCIAL", ln=True)

        pdf.set_font("Helvetica", "", 12)

        pdf.cell(0, 10, f"Numero: {numero}", ln=True)

        pdf.cell(0, 10, f"Data: {datetime.now().strftime('%d/%m/%Y')}", ln=True)

        pdf.ln(5)

        pdf.set_font("Helvetica", "B", 14)

        pdf.cell(0, 10, "CLIENTE", ln=True)

        pdf.set_font("Helvetica", "", 12)

        pdf.cell(0, 8, f"Nome: {oportunidade.cliente}", ln=True)

        pdf.cell(0, 8, f"Empresa: {oportunidade.empresa}", ln=True)

        pdf.cell(0, 8, f"Valor: R$ {oportunidade.valor:,.2f}", ln=True)

        pdf.ln(5)

        pdf.set_font("Helvetica", "B", 14)

        pdf.cell(0, 10, "ESCOPO", ln=True)

        pdf.set_font("Helvetica", "", 12)

        pdf.multi_cell(
            0,
            8,
            "Prestacao de servicos especializados de auditoria, "
            "analise e implantacao de solucoes digitais."
        )

        pdf.ln(5)

        pdf.set_font("Helvetica", "B", 14)

        pdf.cell(0, 10, "PRAZO", ln=True)

        pdf.set_font("Helvetica", "", 12)

        pdf.cell(0, 8, "30 dias", ln=True)

        pdf.ln(5)

        pdf.set_font("Helvetica", "B", 14)

        pdf.cell(0, 10, "STATUS", ln=True)

        pdf.set_font("Helvetica", "", 12)

        pdf.cell(0, 8, "AGUARDANDO ACEITE", ln=True)

        arquivo = os.path.join(
            PASTA,
            f"PROPOSTA_{numero}.pdf"
        )

        pdf.output(arquivo)

        print()

        print("PROPOSTA GERADA")

        print(arquivo)

        return arquivo


# ==============================================================================
# TESTE
# ==============================================================================

if __name__ == "__main__":

    from importlib import import_module

    crm_mod = import_module("012_CRM_ENGINE")

    lead_mod = import_module("011_LEAD_ENGINE")

    lead_engine = lead_mod.LeadEngine()

    crm = crm_mod.CRMEngine()

    lead = lead_engine.novo_lead(

        nome="ABC Engenharia",

        empresa="ABC Engenharia",

        email="contato@abc.com",

        telefone="859999999",

        cidade="Fortaleza",

        interesse="Auditoria Digital",

        valor=18000

    )

    oportunidade = crm.criar_oportunidade(lead)

    crm.mover(oportunidade.id, "PROPOSTA")

    proposal = ProposalEngine()

    proposal.gerar(oportunidade)

