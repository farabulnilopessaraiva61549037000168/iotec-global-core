"""
===================================================================================
                       IOTEC NUCLEUS - GERADOR DE DOSSIÊ B2B (PDF)
===================================================================================
 Arquiteto-Chefe: Farabulini Lopes Saraiva
 Entidade Proprietária: CNPJ 61.549.037/0001-68
 WhatsApp Corporativo: (88) 99930-6416
===================================================================================
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
import manifest

class GeradorDossiePDF:
    def __init__(self, output_dir: str = r"C:\IOTEC\dossies"):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def gerar_pdf(self, dados_empresa: dict) -> str:
        razao = dados_empresa.get("razao_social", "EMPRESA ALVO")
        cnpj = dados_empresa.get("cnpj", "00.000.000/0000-00")
        cidade = dados_empresa.get("cidade", "N/A")
        uf = dados_empresa.get("uf", "N/A")
        atividade = dados_empresa.get("atividade", "N/A")

        nome_arquivo = f"Dossie_IOTEC_{cnpj.replace('/', '').replace('.', '').replace('-', '')}.pdf"
        caminho_completo = os.path.join(self.output_dir, nome_arquivo)

        doc = SimpleDocTemplate(
            caminho_completo,
            pagesize=letter,
            rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36
        )

        styles = getSampleStyleSheet()
        
        # Estilos Customizados IOTEC
        title_style = ParagraphStyle(
            'TitleStyle',
            parent=styles['Heading1'],
            fontName='Helvetica-Bold',
            fontSize=18,
            textColor=colors.HexColor("#1A2B4C"),
            spaceAfter=6
        )
        
        subtitle_style = ParagraphStyle(
            'SubTitleStyle',
            parent=styles['Normal'],
            fontName='Helvetica',
            fontSize=10,
            textColor=colors.HexColor("#4A5568"),
            spaceAfter=15
        )

        body_style = ParagraphStyle(
            'BodyStyle',
            parent=styles['Normal'],
            fontName='Helvetica',
            fontSize=10,
            leading=14,
            textColor=colors.HexColor("#2D3748")
        )

        story = []

        # Cabeçalho Institucional
        story.append(Paragraph("IOTEC NUCLEUS — CARTOGRAFIA ECONÔMICA", title_style))
        story.append(Paragraph(f"Dossiê de Otimização Financeira & Liquidez | Entidade: {manifest.EMPRESA_TITULAR} (CNPJ: {manifest.CNPJ_TITULAR})", subtitle_style))
        story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1A2B4C"), spaceAfter=15))

        # Tabela de Dados da Empresa Prospectada
        dados_tabela = [
            [Paragraph("<b>Razão Social:</b>", body_style), Paragraph(razao, body_style)],
            [Paragraph("<b>CNPJ Alvo:</b>", body_style), Paragraph(cnpj, body_style)],
            [Paragraph("<b>Localização:</b>", body_style), Paragraph(f"{cidade}/{uf}", body_style)],
            [Paragraph("<b>Atividade Principal:</b>", body_style), Paragraph(atividade, body_style)],
        ]

        tabela_empresa = Table(dados_tabela, colWidths=[130, 400])
        tabela_empresa.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F7FAFC")),
            ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#E2E8F0")),
            ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#EDF2F7")),
            ('PADDING', (0,0), (-1,-1), 6),
        ]))

        story.append(tabela_empresa)
        story.append(Spacer(1, 15))

        # Corpo do Diagnóstico
        story.append(Paragraph("<b>1. RESUMO EXECUTIVO DE AUDITORIA</b>", ParagraphStyle('H2', parent=title_style, fontSize=12)))
        p1 = (
            f"O presente dossiê tem por finalidade apresentar à diretoria da <b>{razao}</b> "
            "uma análise preliminar de artérias econômicas e potenciais pontos de recuperação de liquidez. "
            "A metodologia IOTEC atua sob o princípio rígido de <b>Veracidade Financeira (Zero Simulação)</b>, "
            "assegurando auditoria direta em conciliações reais."
        )
        story.append(Paragraph(p1, body_style))
        story.append(Spacer(1, 10))

        story.append(Paragraph("<b>2. CANAL DE CONTATO E DIREÇÃO</b>", ParagraphStyle('H2', parent=title_style, fontSize=12)))
        p2 = (
            f"<b>Arquiteto Responsável:</b> {manifest.EMPRESA_TITULAR}<br/>"
            f"<b>CNPJ Corporativo:</b> {manifest.CNPJ_TITULAR}<br/>"
            f"<b>Canal Oficial WhatsApp:</b> {manifest.WHATSAPP_CORPORATIVO}<br/>"
            f"<b>E-mail Oficial:</b> {manifest.EMAIL_CORPORATIVO}"
        )
        story.append(Paragraph(p2, body_style))
        story.append(Spacer(1, 20))

        story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#CBD5E0"), spaceAfter=10))
        story.append(Paragraph("<i>Documento Gerado Automatizado via IOTEC Nucleus Localhost — Sem Dados Fictícios.</i>", ParagraphStyle('Foot', parent=subtitle_style, fontSize=8)))

        doc.build(story)
        print(f"[✓] DOSSIÊ PDF GERADO COM SUCESSO: {caminho_completo}")
        return caminho_completo

if __name__ == "__main__":
    gerador = GeradorDossiePDF()
    exemplo_dados = {
        "razao_social": "EMPRESA DE TESTE REGIONAL LTDA",
        "cnpj": "61.549.037/0001-68",
        "cidade": "Ibicuitinga",
        "uf": "CE",
        "atividade": "Comércio e Serviços de Logística"
    }
    gerador.gerar_pdf(exemplo_dados)