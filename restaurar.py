import os

caminho = r"C:\IOTEC\ecossistema.html"

if os.path.exists(caminho):
    # Lê o arquivo em bytes brutos
    with open(caminho, 'rb') as f:
        conteudo = f.read()

    # Transforma bytes para string sem quebrar em caracteres inválidos
    texto = conteudo.decode('utf-8', errors='ignore')

    # Passagens de limpeza para desfazer as múltiplas camadas de codificação PowerShell/ANSI
    for _ in range(3):
        try:
            texto = texto.encode('raw_unicode_escape').decode('utf-8')
        except (UnicodeEncodeError, UnicodeDecodeError):
            try:
                texto = texto.encode('latin1').decode('utf-8')
            except (UnicodeEncodeError, UnicodeDecodeError):
                pass

    # Garante a correção de sequências residuais específicas vistas na tela
    reparos = {
        'Â': '',
        'Ã¢€i': 'Â',
        'Ã¢€g': 'É',
        'Ã¢€o': 'Ó',
        'Ã¢€s': 'Ê',
        'Ã¢€': '',
        'Ãƒ': 'Á',
        'Âª': 'ª',
        'Âº': 'º',
        '': '',
    }
    for errado, certo in reparos.items():
        texto = texto.replace(errado, certo)

    # Reescreve o arquivo no formato UTF-8 limpo
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(texto)

    print(">>> RESTAURAÇÃO COMPLETA DE NÍVEL DE ENCODING EXECUTADA COM SUCESSO! <<<")
else:
    print("Arquivo não encontrado.")