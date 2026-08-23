import os
import re

print("=" * 70)
print("      🔓 IOTEC - ABRINDO A CAIXA DE PANDORA DO NÚCLEO")
print("      Mapeamento de Módulos para Polos Estratégicos e Corredores")
print("=" * 70)

diretorio_base = r"C:\IOTEC"

# Foco em grande escala: logística, frota, eixos industriais, prefeituras de polos
palavras_chave = ["cgm", "cigm", "logistica", "carga", "frota", "industria", "corredor", "prefeito", "governor", "empresa"]

tesouros_encontrados = []

for raiz, pastas, arquivos in os.walk(diretorio_base):
    for arq in arquivos:
        if arq.endswith(".py"):
            caminho = os.path.join(raiz, arq)
            try:
                with open(caminho, "r", encoding="utf-8", errors="ignore") as f:
                    conteudo = f.read()
                
                encontrados = [p for p in palavras_chave if re.search(r'\b' + p + r'\b', conteudo, re.IGNORECASE)]
                if encontrados:
                    tamanho_kb = round(os.path.getsize(caminho) / 1024, 1)
                    tesouros_encontrados.append({
                        "arquivo": arq,
                        "caminho": caminho,
                        "tamanho": f"{tamanho_kb} KB",
                        "foco": list(set(encontrados))
                    })
            except Exception:
                pass

# Ordena pelos maiores arquivos (que costumam conter sistemas mais completos)
tesouros_encontrados.sort(key=lambda x: float(x["tamanho"].replace(" KB", "")), reverse=True)

print(f"⚡ Módulos pesados de alta escala localizados no núcleo: {len(tesouros_encontrados)}\n")
for item in tesouros_encontrados[:10]: # Mostra os 10 principais
    print(f"📦 Módulo: {item['arquivo']} ({item['tamanho']})")
    print(f"   • Pilares Detectados: {', '.join(item['foco'])}")
    print(f"   • Caminho: {item['caminho']}\n")

print("=" * 70)