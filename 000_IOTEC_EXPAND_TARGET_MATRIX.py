import sqlite3
import logging

logging.basicConfig(level=logging.INFO, format='[EXPANSAO IOTEC] %(asctime)s - %(message)s')

def expand_studied_targets():
    conn = sqlite3.connect("C:\\IOTEC\\iotec_kernel.db")
    cursor = conn.cursor()
    
    # Matriz de alvos B2B previamente estudados e qualificados
    novos_alvos = [
        ("33.456.789/0001-12", "Logística Express & Cargas S/A", "LOGISTICA", 92, "Custos altos e lentidão no recebimento de fretes fracionados.", "APROVADO_PARA_DISPARO"),
        ("44.567.890/0001-23", "Indústria de Plásticos Triângulo LTDA", "INDUSTRIA", 90, "Retenção de caixa em faturamentos faturados para 30/60/90 dias.", "APROVADO_PARA_DISPARO"),
        ("55.678.901/0001-34", "Rede de Clínicas & Saúde Integrada", "SAUDE", 94, "Glosa de convênios e falta de emissão e cobrança Pix recorrente.", "APROVADO_PARA_DISPARO"),
        ("66.789.012/0001-45", "Supermercados & Atacado Regional", "VAREJO_E_DISTRIBUICAO", 96, "Inadimplência alta no fiado/faturado direto de grandes clientes.", "APROVADO_PARA_DISPARO"),
        ("77.890.123/0001-56", "CloudTech Software & Nuvem LTDA", "SERVICOS_E_TI", 89, "Inadimplência de mensalidades SaaS por falta de cobrança Pix ativa.", "APROVADO_PARA_DISPARO")
    ]
    
    for emp in novos_alvos:
        try:
            cursor.execute('''
                INSERT OR REPLACE INTO empresas_qualificadas 
                (cnpj, razao_social, setor, score_potencial, gargalo_principal, status_qualificacao) 
                VALUES (?, ?, ?, ?, ?, ?)
            ''', emp)
            logging.info(f"[ALVO PROGRAMADO CARREGADO]: {emp[1]} | Setor: {emp[2]} | Score: {emp[3]}/100")
        except Exception as e:
            logging.error(f"Erro ao inserir alvo: {e}")
            
    conn.commit()
    conn.close()

if __name__ == "__main__":
    expand_studied_targets()
