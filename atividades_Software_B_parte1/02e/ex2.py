# UMC
# Eduarda e Luana
# 18/03
# Números pares e ímpares

import os

def limpar_tela():
    os.system('cls')
    print(tituloo)

tituloo = '''
                                             _                           
    ____  ____ ______   ____  __  __   (_)___ ___  ____  ____ ______
   / __ \/ __ `/ ___/  / __ \/ / / /  / / __ `__ \/ __ \/ __ `/ ___/
  / /_/ / /_/ / /     / /_/ / /_/ /  / / / / / / / /_/ / /_/ / /    
 / .___/\__,_/_/      \____/\__,_/  /_/_/ /_/ /_/ .___/\__,_/_/     
/_/                                            /_/                                                                                                                                                                                                                             
'''
print(tituloo)

while True:
    try:
        numero = int(input("Insira um número: "))
        limpar_tela()

        if numero % 2 == 0:
            print(f"O número {numero} é par")
        else:
            print(f"O número {numero} é ímpar")
    except ValueError:
        print("Valor inválido. Por favor, insira um número inteiro.")
    
    opt = input("Pressione c para continuar ou s para finalizar: ").lower()
    limpar_tela()

    if opt == "s":
        print("Você saiu do programa")
        break

             
               



     

