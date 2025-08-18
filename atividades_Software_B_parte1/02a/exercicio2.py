# Empresa UMC
# Data 27/02/2025
# Programador Eduarda e Luana
# Conversão de moeda

import os 
def limpar_tela():
    os.system('cls')

while True: 
    try:
        X=float(input("Entre com o valor em reais: "))
        limpar_tela()

        C=float(input("Entre com o valor do dólar: "))
        limpar_tela()
    except ValueError:
        print("Valor inválido, tente novamente")
        opt=input("Pressione c para continuar ou qualquer outra tecla para sair: ").lower()
        if opt == 'c':
            limpar_tela()
        else:
            break
    else:    
        ValorD = X/C
        print (f"O valor em dólares é = {ValorD:.2f}R$")
        opt=input("Pressione c para continuar ou qualquer outra tecla para sair: ").lower()
        if opt == 'c':
            limpar_tela()
        else:
            break