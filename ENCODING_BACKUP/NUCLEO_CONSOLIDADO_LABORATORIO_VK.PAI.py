import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

   Iniciar_Sistema()
Carregar_Entrada("/Sistema_VK_PAI/Entrada")

Para cada Arquivo em Entrada:
    Se Arquivo == Script:
        Validar_Permissao()
        Se OK:
            Executar(Arquivo)
        Senao:
            Solicitar_Permissao()

    Se Arquivo == Documento:
        Indexar(Arquivo)

    Se Arquivo == Mapa_Mental:
        Converter_Para_Processo()

Gerar_Relatorio()
Enviar_Status_Para_PAI()

Se Fluxo_Ativo:
    Ativar_Geracao_De_Receita()



