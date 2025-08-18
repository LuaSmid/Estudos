# Programador
# Menu
import os
Minha_Lista=["Fulano da Silva","Eulano de Souza",
             "Tulano Junior","Sicrano da Silva", "Voslano Fulano Junior"]
#==========
while True:
    os.system("cls")
    opt=input('''
    [1] Relatório Geral
    [2] Inclusão
    [3] Alteração
    [4] Exclusão
    [5] Fim do Programa
    
    ''')
    if opt=="1":
        for i , dado in enumerate(Minha_Lista):
            print (i,"\t",dado)
        input ("Pressione enter para voltar ao menu")
    elif opt=="2":
        Nm=input("Entre com um nome a ser adicionado: ")
        Minha_Lista.append(Nm)
        input ("Pressione enter para voltar ao menu")
    elif opt=="3":
        id=int(input("Entre com o indice do Nome a ser alterado: "))
        if id <= len(Minha_Lista)-1:
            print (f"Dados a serem alterados: {id} {Minha_Lista[id]}")
            Nm=input("Entre com a alteração do nome ou enter para manter: ") or Minha_Lista[id]
            Minha_Lista[id]=Nm
        else:
            print ("Indice não consta na lista")
        input ("Pressione enter para voltar ao menu")
        
    elif opt=="4":
        id=int(input("Entre com o indice do Nome a ser EXCLUIDO: "))
        if id <= len(Minha_Lista)-1:
            print (f"Dados a serem EXCLUIDOS: {id} {Minha_Lista[id]}")
            del Minha_Lista[id]
        else:
            print ("Indice não consta na lista")
        input ("Pressione enter para voltar ao menu")
    elif opt=="5":
        input ("Pressione enter para sair do programa")
        break
    else:
        print ("opção de menu invalida")
        input ("Pressione enter para voltar ao menu")
print ("Fim do Programa")

    
