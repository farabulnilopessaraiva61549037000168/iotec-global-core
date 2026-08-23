import os
import glob

print("=" * 60)
print("   IOTEC PLATFORM - INVENTÁRIO DO PATRIMÔNIO DE CÓDIGO (HTML/JS)")
print("=" * 60)

base_dir = r"C:\IOTEC"
extensions = ['*.html', '*.htm', '*.js', '*.css']
files_found = []

for ext in extensions:
    files_found.extend(glob.glob(os.path.join(base_dir, ext)))

if not files_found:
    print("\n⚠️ Nenhum arquivo HTML/JS extra encontrado diretamente na raiz de C:\\IOTEC.")
    print("Se o acervo estiver em uma pasta específica ou em outro diretório, podemos ajustar o caminho.")
else:
    print(f"\nEncontrados {len(files_found)} arquivos no acervo:\n")
    for filepath in files_found:
        filename = os.path.basename(filepath)
        size_kb = os.path.getsize(filepath) / 1024
        
        # Leitura das primeiras linhas para identificar a proposta do arquivo
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                header = [f.readline().strip() for _ in range(3)]
                header_text = ' | '.join([h for h in header if h])[:80]
        except Exception:
            header_text = "Não foi possível ler o cabeçalho"
            
        print(f"📄 [{filename}] ({size_kb:.1f} KB)")
        print(f"   └─ Prévia: {header_text}")
        print("-" * 60)

print("\n>>> Fim do mapeamento do acervo.")
