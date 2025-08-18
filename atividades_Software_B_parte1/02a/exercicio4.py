# Empresa UMC
# Data 27/02/2025
# Programador Eduarda e Luana
# Calculo de Lucro e Estoque

import os

while True:
    try:
        V = float(input("Insira o valor da venda: "))
        os.system('cls')

        C = float(input("Insira o custo: "))
        os.system('cls')

    except ValueError:
        print("Valor inválido, tente novamente")
        opt=input("Pressione c para continuar ou qualquer outra tecla para sair: ").lower()
        if opt == 'c':
            os.system('cls')
        else:
            break
    else:
        L= V-C
        ML= (L*C)/100
        print("O valor do lucro é: ", L)
        print("A margem de lucro é: ", ML)
        opt=input("Pressione c para continuar ou qualquer outra tecla para sair: ").lower()
        if opt == 'c':
            os.system('cls')
        else:
            break