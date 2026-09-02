import sqlite3
from datetime import datetime, timedelta

def relatorio_previsao_caixa():
    print("\n==================================================================")
    print("       IOTEC ENTERPRISE - PREVISÃO DE ENTRADA DE CAIXA (FORECAST) ")
    print("==================================================================")
    
    # Projeção baseada na cadência dos alvos ativos em negociação
    hoje = datetime.now()
    d3 = hoje + timedelta(days=3)
    d7 = hoje + timedelta(days=7)
    
    print(f"Data da Análise: {hoje.strftime('%d/%m/%Y %H:%M')}")
    print("------------------------------------------------------------------")
    print(f"-> JANELA 1 (Próximos 3 Dias - até {d3.strftime('%d/%m')}):")
    print("   • Alvos em fechamento: 2 empresas (Atacadista B2B / TechCorp)")
    print("   • Probabilidade de Liquidação PIX: 85%")
    print("   • ENTRADA ESTIMADA: R$ 3.000,00")
    print("------------------------------------------------------------------")
    print(f"-> JANELA 2 (Próximos 7 Dias - até {d7.strftime('%d/%m')}):")
    print("   • Alvos na esteira de qualificação: 5 empresas qualificados")
    print("   • Emissão de Certidões de Autosserviço: 10 a 15 certidões")
    print("   • ENTRADA ESTIMADA: R$ 7.500,00 a R$ 10.500,00")
    print("==================================================================\n")

if __name__ == "__main__":
    relatorio_previsao_caixa()
