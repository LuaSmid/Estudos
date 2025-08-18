# Empresa UMC
# Data 27/02/2025
# Programador Eduarda e Luana
# Cálculo de Estoque

import os

while True:
    try:
        N = float(input("Entre com a quantidade de unidades do produto:"))
        os.system('cls')

        R = float(input("Insira o valor unitário:"))
        os.system('cls')
 
    except ValueError:
        print("Valor inválido, tente novamente")
        opt=input("Pressione c para continuar ou qualquer outra tecla para sair: ").lower()
        if opt == 'c':
            os.system('cls')
        else:
            break
    else:
        TotalEstoque = N * R 
        print ("O valor total do seu estoque é:", TotalEstoque)
        opt=input("Pressione c para continuar ou qualquer outra tecla para sair: ").lower()
        if opt == 'c':
            os.system('cls')
        else:
            break