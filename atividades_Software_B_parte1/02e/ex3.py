#UMC
#Eduarda e Luana 
#18/03
#Números repetidos

#Entrada
tituloo='''
                     _   _                 
 _ __ ___ _ __   ___| |_(_) ___ __ _  ___  
| '__/ _ \ '_ \ / _ \ __| |/ __/ _` |/ _ \ 
| | |  __/ |_) |  __/ |_| | (_| (_| | (_) |
|_|  \___| .__/ \___|\__|_|\___\__,_|\___/ 
         |_|                                                                                                                                                                                                                                                                                                     
'''
print(tituloo)

import os

def limpar_tela():
    os.system('cls')
    print(tituloo)

while True:
    try:
        n1=int(input("Insira o primeiro número: "))
        limpar_tela()

        n2=int(input("Insira o segundo número: "))
        limpar_tela()

        n3=int(input("Insira o terceiro número: "))
        limpar_tela()

        n4=int(input("Insira o quarto número: "))
        limpar_tela()
    except:
        print("Valor inválido")
        opt=input("Pressione c para continuar ou s para finalizar o programa: ")
        limpar_tela()
        if opt=="s" or opt=="S":
            break
    else:
        if n1 == n2:
            print(f"números repetidos: n1: {n1} e n2: {n2}")
            break
        if n1 == n3:
            print(f"números repetidos:  n1: {n1} e n3: {n3}")
            break
        if n1 == n4:
            print(f"números repetidos:  n1: {n1} e n4: {n4}")
            break
        if n2 == n3:
            print(f"números repetidos:  n2: {n2} e n3: {n3}")
            break
        if n2 == n4:
            print(f"números repetidos:  n2: {n2} e n4: {n4}")
            break 
        if n3 == n4:
            print(f"números repetidos:  n3: {n3} e n4: {n4}")
            break
        else:
            print("Nenhum número repetido.")
            break

#Processamento e decisão
#Saída
input("Fim do programa, pressione enter")
limpar_tela()