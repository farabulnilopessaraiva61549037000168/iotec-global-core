import os
import glob

print("=" * 65)
print("   IOTEC PLATFORM - INVENTÁRIO DO ACERVO (PASTA DOWNLOADS)")
print("=" * 65)

user_profile = os.environ.get("USERPROFILE")
downloads_dir = os.path.join(user_profile, "Downloads")

print(f"\n🔍 Buscando arquivos de interface em: {downloads_dir}\n")

if not os.path.exists(downloads_dir):
    print("⚠️ Pasta Downloads não encontrada.")
else:
    extensions = ['*.html', '*.htm', '*.js', '*.css', '*.json', '*.zip']
    files_found = []

    for ext in extensions:
        files_found.extend(glob.glob(os.path.join(downloads_dir, ext)))
        # Busca em até 1 nível de subpasta em Downloads
        files_found.extend(glob.glob(os.path.join(downloads_dir, "*", ext)))

    files_found = list(set(files_found))

    if not files_found:
        print("⚠️ Nenhum arquivo HTML/JS/CSS/JSON encontrado na pasta Downloads.")
    else:
        print(f"✅ Encontrados {len(files_found)} arquivos relevantes em Downloads:\n")
        for filepath in sorted(files_found):
            filename = os.path.basename(filepath)
            size_kb = os.path.getsize(filepath) / 1024
            
            purpose = "Sem cabeçalho identificado"
            if not filename.endswith('.zip'):
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read(1024)
                        if "<title>" in content.lower():
                            start = content.lower().find("<title>") + 7
                            end = content.lower().find("</title>")
                            if end > start:
                                purpose = f"Título HTML: '{content[start:end].strip()}'"
                        elif "function" in content or "const" in content:
                            purpose = "Script JavaScript"
                except Exception:
                    purpose = "Erro na leitura"
            else:
                purpose = "Arquivo de Arquivo/Backup (ZIP)"

            print(f"📄 [{filename}] ({size_kb:.1f} KB)")
            print(f"   └─ Propósito: {purpose}")
            print("-" * 65)

print("\n>>> Fim da varredura em Downloads.")
