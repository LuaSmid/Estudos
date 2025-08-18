#UMC
#Eduarda e Luana 
#18/03
#Direito a desconto

#Entrada
tituloo='''
┌┬┐┌─┐┌─┐┌─┐┌─┐┌┐┌┌┬┐┌─┐
 ││├┤ └─┐│  │ ││││ │ │ │
─┴┘└─┘└─┘└─┘└─┘┘└┘ ┴ └─┘                                                                                                                                                                                                                                                                                                                                                                                                       
'''
print(tituloo)

import os

def limpar_tela():
    os.system('cls')
    print(tituloo)


#Processamento
while True:
    try:
        idade=int(input("Insira a idade: "))
        limpar_tela()
    except:
        print("Valor inválido.")
        opt=input("Pressione C para entrar novamente ou S para finalizar: ")
        if opt=="S" or opt=="s":
            break
    else:
        limpar_tela()
        if idade < 16 or idade >= 60 :
            print(f"Você tem direito a desconto, idade = {idade}")
            break
        else:
            print(f"Você não tem direito a desconto, idade = {idade}")
            break
#Saída
input("Fim do programa, pressione enter")
limpar_tela()