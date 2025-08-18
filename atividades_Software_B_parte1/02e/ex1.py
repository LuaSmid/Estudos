# UMC
# Eduarda e Luana
# 18/03
# Divisão possível e impossível

import os

def limpar_tela():
    os.system('cls')
    print(tituloo)

tituloo = '''
██████╗ ██╗██╗   ██╗██╗███████╗ █████╗  ██████╗ 
██╔══██╗██║██║   ██║██║██╔════╝██╔══██╗██╔═══██╗
██║  ██║██║██║   ██║██║███████╗███████║██║   ██║
██║  ██║██║╚██╗ ██╔╝██║╚════██║██╔══██║██║   ██║
██████╔╝██║ ╚████╔╝ ██║███████║██║  ██║╚██████╔╝
╚═════╝ ╚═╝  ╚═══╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝                                                                                                                              
'''
print(tituloo)

while True:
    try:
        n1 = int(input("Insira o primeiro número: "))
        limpar_tela()

        n2 = int(input("Insira o segundo número: "))
        limpar_tela()
    except ValueError:
        print("Valor inválido")
        opt = input("Pressione c para tentar novamente ou s para finalizar: ").lower()
        limpar_tela()
        if opt == "s":
            print("Você saiu do programa")
            break
    else:
        if n2 == 0:
            print("A divisão é impossível")
        else:
            div = n1 / n2
            print(f"A sua divisão é igual a: {div}")
        
        opt = input("Pressione c para tentar novamente ou s para finalizar: ").lower()
        if opt == "s":
            print("Você saiu do programa")
            break
        elif opt == "c":
            limpar_tela()

 