#UMC
#Eduarda e Luana 
#18/03
#Números consecutivos e em ordem crescente

#Entrada
import os

def limpar_tela():
    os.system('cls')
    print(tituloo)


tituloo='''
┌─┐┌─┐┌┐┌┌─┐┌─┐┌─┐┬ ┬┌┬┐┬┬  ┬┌─┐┌─┐
│  │ ││││└─┐├┤ │  │ │ │ │└┐┌┘│ │└─┐
└─┘└─┘┘└┘└─┘└─┘└─┘└─┘ ┴ ┴ └┘ └─┘└─┘                                                                                                                                                                                                                                                                                                                                                                                                       
'''
print(tituloo)
while True:
    try:
        n1=int(input("Insira o primeiro número: "))
        limpar_tela()

        n2=int(input("Insira o segundo número: "))
        limpar_tela()

        n3=int(input("Insira o terceiro número: "))
        limpar_tela()
    except:
        print("Valor inválido")
        opt=input("Pressione c para tentar novamente ou s para finalizar: ")
        limpar_tela()
        if opt=="s" or opt =="S":
            break
    else:
        limpar_tela()
        if n1 < n2 and n2 < n3 and n1 < n3 :
            print(f"números consecutivos e em ordem: n1 = {n1} , n2 = {n2} e n3 = {n3}")
            break
        else:
            print(f"Números não consecutivos e aleatórios n1 = {n1} , n2 = {n2} e n3 = {n3}")
            break



#Processamento

#Saída
input("Fim do programa, pressione enter")
limpar_tela()