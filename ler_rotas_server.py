import os

caminhos = [r'C:\IOTEC\server.js', r'C:\IOTEC\REAL_SYSTEM\server.js']

for caminho in caminhos:
    if os.path.exists(caminho):
        print(f'=== ARQUIVO: {caminho} ===\n')
        with open(caminho, 'r', encoding='utf-8', errors='ignore') as f:
            linhas = f.readlines()
            for idx, line in enumerate(linhas):
                if any(k in line for k in ['.post(', '.get(', 'app.use', 'port', 'send', 'message', 'session']):
                    print(f'Linha {idx+1}: {line.strip()}')
        print('\n' + '='*40 + '\n')
