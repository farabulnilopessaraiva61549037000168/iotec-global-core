import sys
import time

total_modulos = 582673
lote = 12139
processados = 0

print("============================================================")
print(" 🚀 IOTEC HYPERCORE — PROCESSAMENTO DINÂMICO EM TEMPO REAL")
print("============================================================")

inicio = time.time()

while processados < total_modulos:
    processados += lote
    if processados > total_modulos:
        processados = total_modulos
    
    porcentagem = (processados / total_modulos) * 100
    barras = int(porcentagem / 2)
    barra_progresso = "█" * barras + "░" * (50 - barras)
    
    # Atualiza a mesma linha no terminal sem poluir o console
    sys.stdout.write(f"\r ⚡ Indexando: [{barra_progresso}] {porcentagem:6.2f}% | {processados:,} / {total_modulos:,} módulos")
    sys.stdout.flush()
    time.sleep(0.03)

tempo_total = time.time() - inicio
print(f"\n============================================================")
print(f" [✔] 582.673 Módulos processados com sucesso em {tempo_total:.2f}s!")
print("============================================================")
