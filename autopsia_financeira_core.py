import os
import re

print("=" * 65)
print("      🔍 IOTEC - MINERAÇÃO DE INTEGRAÇÕES FINANCEIRAS NO CORE")
print("=" * 65)

diretorio_base = r"C:\IOTEC"
termos_busca = ["picpay", "paypal", "mercadopago", "checkout", "token", "client_id", "secret", "pix", "payment"]

encontrados = []

for raiz, pastas, arquivos in os.walk(diretorio_base):
    for arq in arquivos:
        if arq.endswith((".py", ".env", ".json", ".txt", ".ini")):
            caminho_completo = os.path.join(raiz, arq)
            try:
                with open(caminho_completo, "r", encoding="utf-8", errors="ignore") as f:
                    conteudo = f.read()
                    
                matches = []
                for termo in termos_busca:
                    if re.search(r'\b' + termo + r'\b', conteudo, re.IGNORECASE):
                        matches.append(termo)
                
                if matches:
                    encontrados.append({
                        "arquivo": arq,
                        "caminho": caminho_completo,
                        "termos": list(set(matches))
                    })
            except Exception as e:
                pass

if encontrados:
    print(f"✅ Encontrados {len(encontrados)} arquivos com rastros de pagamento/integração:\n")
    for item in encontrados:
        print(f"📄 Arquivo: {item['arquivo']}")
        print(f"   • Caminho: {item['caminho']}")
        print(f"   • Termos Identificados: {', '.join(item['termos'])}\n")
else:
    print("⚠️ Nenhum código antigo de pagamento foi localizado na pasta base.")

print("=" * 65)