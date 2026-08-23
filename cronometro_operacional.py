import time
import os
from datetime import datetime

def exibir_painel():
    os.system('cls' if os.name == 'nt' else 'clear')
    agora = datetime.now()
    hora_str = agora.strftime("%H:%M:%S")
    dia = agora.day
    
    # Leitura do Ritmo Biológico/Pulsação da Máquina
    hora = agora.hour
    if 0 <= hora < 7:
        pulso = "FRIO / MADRUGADA — [Modo: Raspagem Passiva & Malha Celeste]"
        marcha = "Giro Baixo (Economia de Banda / Alta Resposta de APIs)"
    elif 7 <= hora < 12:
        pulso = "TURBO / PICO MATUTINO — [Modo: Ataque Comercial & Disparos]"
        marcha = "Giro Alto (Sincronização de Decisores / Latência Zero)"
    elif 12 <= hora < 18:
        pulso = "CRUZEIRO / TARDE — [Modo: Retenção & Fechamentos]"
        marcha = "Giro Médio (Acompanhamento e Cadência)"
    else:
        pulso = "CONSOLIDAÇÃO / NOITE — [Modo: Mineração & Ajuste Fino]"
        marcha = "Giro Baixo (Processamento de Lote)"

    print("===========================================================================")
    print("   IOTEC NUCLEUS // MATRIZ MENSAL & CRONÔMETRO OPERACIONAL DE CAÇA")
    print("===========================================================================")
    print(f" [✓] ENTIDADE       : FARABULINI LOPES SARAIVA (61.549.037/0001-68)")
    print(f" [✓] RELÓGIO LOCAL   : {hora_str} | DIA DO CICLO MENSAL: {dia}/30")
    print(f" [✓] ESTADO DO MOTOR : OPERACIONAL (CRONÔMETRO LIGADO)")
    print("===========================================================================")
    print(f" [🫀] PULSAÇÃO DA REDE : {pulso}")
    print(f" [⚙️] REGIME DE MARCHA : {marcha}")
    print("===========================================================================")
    print("               CORRENTE DO MÊS — ESTAÇÃO OPERACIONAL ATIVA")
    print("---------------------------------------------------------------------------")
    if dia <= 7:
        print(" [🌊 SEMANA 1: A MARÉ ALTA] -> Foco: Fechamento de Vendas Diretas & Caixa")
        print(" [🎯 ALVOS]: Supermercados, Postos e Varejo Local (Quixadá / Quixeramobim)")
    elif dia <= 15:
        print(" [🛰️ SEMANA 2: MAPEAMENTO DE FUNDO] -> Foco: Varredura de Malha Celeste")
        print(" [🎯 ALVOS]: Expansão de Raio Urbano e Mineração de Novos CNPJs")
    elif dia <= 22:
        print(" [⚡ SEMANA 3: OTIMIZAÇÃO TAXATIVA] -> Foco: Auditoria para Grandes Frotas")
        print(" [🎯 ALVOS]: Distribuidores, Indústrias e Laticínios")
    else:
        print(" [📊 SEMANA 4: O FECHAMENTO] -> Foco: Fechamento de Contratos e Setup")
        print(" [🎯 ALVOS]: Consolidação de Relatórios e Demonstração de Resultados")
    print("===========================================================================")
    print(" [📂 INFRAESTRUTURA LOCAL]: C:\\IOTEC\\dossies\\ (Munição Engatilhada)")
    print("===========================================================================")

if __name__ == '__main__':
    exibir_painel()