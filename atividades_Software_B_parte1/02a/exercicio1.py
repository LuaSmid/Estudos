# Empresa UMC
# Data 27/02/2025
# Programador Eduarda e Luana
#  Calculo do Desconto

import os 
def limpar_tela():
    os.system('cls')

while True:
    try:
        V=float(input("entre com o valor do produto: "))
        limpar_tela()

        P=float(input("Entre com a '%' de desconto, ex: 30% , digite 30: "))
        limpar_tela()
    except ValueError:
        print("Valor inválido")
        opt = input("Pressione c para tentar novamente ou s para finalizar: ").lower()
        limpar_tela()
        if opt == "s":
            print("Você saiu do programa")
            break
    else:
            D=(V*P)/100
            Vf=V-D
            print ("O valor do produto é = ",V,"O valor do desconto é = ",D,"Preço Final = ",Vf)
            opt = input("Pressione c para tentar novamente ou s para finalizar: ").lower()
            if opt == "s":
                print("Você saiu do programa")
                break
            elif opt == "c":
                limpar_tela()