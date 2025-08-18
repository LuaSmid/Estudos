# Empresa UMC
# Data 27/02/2025
# Programador Eduarda e Luana
# Calculo de aumento de estoque
import os

while True:
    try:
        N = float(input("Insira o estoque atual:"))
        os.system('cls')

        P = float(input("Insira a porcentagem de aumento:"))
        os.system('cls')
    except ValueError:
        print("Valor inválido, tente novamente")
        opt=input("Pressione c para continuar ou qualquer outra tecla para sair: ").lower()
        if opt == 'c':
            os.system('cls')
        else:
            break
    else:
        NovoEstoque = N + (N*P/100)
        print ("Este é o seu novo estoque: ",NovoEstoque)
        opt=input("Pressione c para continuar ou qualquer outra tecla para sair: ").lower()
        if opt == 'c':
            os.system('cls')
        else:
            break
