import os, subprocess, sys

def achar_e_iniciar():
    print('=== BUSCANDO MÓDULO DO WHATSAPP / WPPCONNECT ===\n')
    for root, dirs, files in os.walk(r'C:\IOTEC'):
        if 'node_modules' in root and root.count(os.sep) > 4:
            continue
        for f in files:
            f_lower = f.lower()
            if ('wpp' in f_lower or 'whatsapp' in f_lower or 'bot' in f_lower) and f_lower.endswith('.js'):
                caminho_completo = os.path.join(root, f)
                print(f'-> Encontrado: {caminho_completo}')
                
                # Testa ler o arquivo para ver se tem inicialização do WPPConnect
                try:
                    with open(caminho_completo, 'r', encoding='utf-8', errors='ignore') as file:
                        conteudo = file.read()
                        if 'wppconnect' in conteudo.lower() or 'venom' in conteudo.lower() or 'create' in conteudo.lower():
                            print(f'\n🚀 Iniciando o serviço interativo: {caminho_completo}\n')
                            os.chdir(root)
                            subprocess.run(['node', f], check=True)
                            return
                except Exception as e:
                    pass

    print('❌ Nenhum script interativo do WhatsApp foi encontrado diretamente.')

achar_e_iniciar()
