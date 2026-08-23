import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import time
import pandas as pd
import matplotlib.pyplot as plt


def menu_principal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("====================================")
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â· Bem-vindo, comandante!")
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¹ Aqui ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© o Optimus, sua IA residente!")
    print("====================================")
    print("1 - Ver Dados")
    print("2 - Criar GrÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡fico")
    print("3 - Fazer CÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lculo")
    print("4 - Encerrar")
    print("====================================")
    escolha = input("Digite sua escolha: ")
    return escolha


def ver_dados():
    dados = {
        'Produto': ['A', 'B', 'C', 'D'],
        'Vendas': [120, 340, 560, 230]
    }
    df = pd.DataFrame(dados)
    print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â Dados disponÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­veis:\n")
    print(df)
    input("\nPressione ENTER para voltar ao menu...")


def criar_grafico():
    produtos = ['A', 'B', 'C', 'D']
    vendas = [120, 340, 560, 230]

    plt.bar(produtos, vendas, color='cyan')
    plt.title('ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  Vendas por Produto')
    plt.xlabel('Produto')
    plt.ylabel('Vendas')
    plt.grid(axis='y')
    plt.show()


def fazer_calculo():
    print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  Calculadora Inteligente")
    num1 = float(input("Digite o primeiro nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºmero: "))
    operacao = input("Escolha a operaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o (+, -, *, /): ")
    num2 = float(input("Digite o segundo nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºmero: "))

    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Erro: DivisÃƒÆ'Ã†â€™o por zero!"
    else:
        resultado = "OperaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o invÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lida!"

    print(f"\nÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Resultado: {resultado}")
    input("\nPressione ENTER para voltar ao menu...")


# Loop principal
while True:
    opcao = menu_principal()

    if opcao == '1':
        ver_dados()
    elif opcao == '2':
        criar_grafico()
    elif opcao == '3':
        fazer_calculo()
    elif opcao == '4':
        print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â´ Encerrando o Optimus...")
        time.sleep(1)
        break
    else:
        print("OpÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o invÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lida, tente novamente.")
        time.sleep(1)


