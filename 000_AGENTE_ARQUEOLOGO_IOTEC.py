import os
import glob
from datetime import datetime

DIRETORIO_ALVO = r"C:\IOTEC"

def relatorio_conversacional():
    print("=" * 75)
    print(" 🧭 AGENTE ARQUEÓLOGO IOTEC - RELATÓRIO DE EXPEDIÇÃO & MENSURAÇÃO")
    print("=" * 75)
    print(" [!] 'Comandante, os mergulhadores voltaram do porão com os artefatos!'\n")
    
    arquivos_python = glob.glob(os.path.join(DIRETORIO_ALVO, "*.py"))
    
    if not arquivos_python:
        print(" [!] Nenhum módulo encontrado no diretório. O porão está vazio ou não mapeado.")
        return

    artefatos = []
    
    for arq in arquivos_python:
        nome_arquivo = os.path.basename(arq)
        tamanho = os.path.getsize(arq)
        mtime = datetime.fromtimestamp(os.path.getmtime(arq)).strftime("%d/%m/%Y %H:%M")
        
        # Leitura rápida do 'coração' do artefato (análise de laboratório)
        with open(arq, 'r', encoding='utf-8', errors='ignore') as f:
            conteudo = f.read()
            
        funcao = "Módulo de Infraestrutura Generico"
        ticket_estimado = "R$ 500,00"
        potencial_global = "Baixo"
        
        if "PAYMENT" in nome_arquivo.upper() or "PAYPAL" in conteudo.upper():
            funcao = "Motor de Gateway de Pagamentos / Checkout"
            ticket_estimado = "R$ 2.990,00 / $ 500.00"
            potencial_global = "ALTÍSSIMO (E-commerce / B2B)"
        elif "AUDIT" in nome_arquivo.upper() or "LEDGER" in conteudo.upper():
            funcao = "Cofre de Auditoria Financial / Compliance PCI"
            ticket_estimado = "R$ 5.000,00 / $ 1,000.00"
            potencial_global = "ALTO (Empresas Corporativas)"
        elif "WEB" in nome_arquivo.upper() or "PAINEL" in nome_arquivo.upper():
            funcao = "Central de Observabilidade / Dashboard Web"
            ticket_estimado = "R$ 1.500,00 / $ 300.00"
            potencial_global = "MÉDIO (Controle de Gestão)"
            
        artefatos.append({
            "nome": nome_arquivo,
            "tamanho": f"{tamanho / 1024:.1f} KB",
            "modificacao": mtime,
            "funcao": funcao,
            "valoraçao": ticket_estimado,
            "potencial": potencial_global
        })

    print(f" 🔎 Foram resgatados {len(artefatos)} artefatos tecnológicos nas profundezas de {DIRETORIO_ALVO}:\n")
    
    for i, art in enumerate(artefatos, 1):
        print(f" 📦 ARTEFATO #{i}: [{art['nome']}]")
        print(f"    • Tamanho no disco  : {art['tamanho']} (Última mexida: {art['modificacao']})")
        print(f"    • Análise do Lab    : {art['funcao']}")
        print(f"    • Estimativa Comercial: {art['valoraçao']}")
        print(f"    • Potencial Global  : {art['potencial']}")
        print(" " + "-"*65)

    print("\n [💬 DIAGNÓSTICO DO AGENTE ARQUEÓLOGO]:")
    print(" 'Comandante, essas engrenagens não são sucata. Temos motores de pagamento,")
    print("  sistemas de auditoria financeira e centrais de controle prontas.")
    print("  Podemos empacotar o Módulo de Auditoria + Checkout hoje mesmo e vender")
    print("  para empresas que precisam de laudo de conformidade técnica!'")
    print("=" * 75)

if __name__ == "__main__":
    relatorio_conversacional()
