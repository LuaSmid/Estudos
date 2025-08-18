# Programador
# Menu
Pecas=[
    [1,"filtros",30],
    [2,"Pastilha nr 30",40],
    [3,"Correia",150]
]

import os

while True:

    os.system("cls")

    opt=input('''
    [1] Inclusão
    [2] Total
    [3] Pequisa por Descriçaõ ou Valor
    [4] Relatorio
    [5] Fim do Programa
   
    ''')

    if opt=="1":
        pos=int(input("Insira a posicção para a inserção: "))
        id=int(input("Insira o id do produto: "))
        desc=input("Insira a descrição do produto: ")
        val=float(input("Insira o preço do produto: "))
        Pecas.insert(pos,[id,desc,val])
        input ("Pressione enter para voltar ao menu")

    elif opt=="2":
        soma = 0
        for i in Pecas:
            soma = soma +i[2]
        print ("O valor da soma é :", soma)
        input ("Pressione enter para voltar ao menu")

    elif opt=="3":
        val=input("Entre com parte da descriçaõ ou o valor: ")
        for i in Pecas:
            if val in i[1] or val in str(i[2]):
                print (i)
        input ("Pressione enter para voltar ao menu")

    elif opt=="4":
        for i in Pecas:
            print (i)
        input ("Pressione enter para voltar ao menu")

    elif opt=="5":
        input ("Pressione enter para sair do programa")
        break

    else:
        print ("opção de menu invalida")
        input ("Pressione enter para voltar ao menu")
print ("Fim do Programa")