import os
import re

print("=" * 70)
print("      🔍 IOTEC - AUDITORIA DE INTEGRAÇÕES FINANCEIRAS (PAYPAL / PICPAY)")
print("=" * 70)

diretorio_base = r"C:\IOTEC"
termos = ["paypal", "picpay", "client_id", "client_secret", "payment", "checkout", "sdk"]

encontrados = []

for raiz, pastas, arquivos in os.walk(diretorio_base):
    for arq in arquivos:
        if arq.endswith((".py", ".env", ".json", ".ini", ".txt")):
            caminho_completo = os.path.join(raiz, arq)
            try:
                with open(caminho_completo, "r", encoding="utf-8", errors="ignore") as f:
                    conteudo = f.read()
                    
                matches = [t for t in termos if re.search(r'\b' + t + r'\b', conteudo, re.IGNORECASE)]
                if matches:
                    encontrados.append({
                        "arquivo": arq,
                        "caminho": caminho_completo,
                        "termos": list(set(matches))
                    })
            except Exception:
                pass

if encontrados:
    print(f"✅ Encontrados {len(encontrados)} arquivos com rastros de integração:\n")
    for item in encontrados:
        print(f"📄 Arquivo: {item['arquivo']}")
        print(f"   • Caminho: {item['caminho']}")
        print(f"   • Termos: {', '.join(item['termos'])}\n")
else:
    print("⚠️ Nenhum arquivo contendo termos de pagamento foi localizado.")

print("=" * 70)