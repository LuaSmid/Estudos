# Programador
# Menu
import os
while True:
    os.system("clear")
    opt=input('''
    [1] Escolha da opção 1
    [2] Escolha da opção 2
    [3] Escolha da opção 3
    [4] Fim do Programa
    
    ''')
    if opt=="1":
        print ("Você escolheu a opção 1")
        input ("Pressione enter para voltar ao menu")
    elif opt=="2":
        print ("Você escolheu a opção 2")
        input ("Pressione enter para voltar ao menu")
    elif opt=="3":
        print ("Você escolheu a opção 3")
        input ("Pressione enter para voltar ao menu")
    elif opt=="4":
        input ("Pressione enter para sair do programa")
        break
    else:
        print ("opção de menu invalida")
        input ("Pressione enter para voltar ao menu")
print ("Fim do Programa")

    
