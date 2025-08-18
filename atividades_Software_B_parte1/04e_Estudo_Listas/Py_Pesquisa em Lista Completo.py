#Empresa
#Programador - Data xx/xx/xxxx
#Programa: Listas Simples
#==================================================
import os
Minha_Lista=["Fulano da Silva","Eulano de Souza","Tulano Junior","Sicrano da Silva", "Voslano Fulano Junior"]
while True:
    Match=[] # precisa ser esvaziada antes de ser usada novamente
    os.system("cls")
    Nome=input("Entre com o nome a ser pesquisado ou FIM: ")
    if Nome.upper() == "FIM": # Checa solicitação de saída 
        input ("Precione Enter para encerar o programa")
        break
    else:
        for i in Minha_Lista: # varre a lista e variavel "i" recebe os valores  
            if Nome in i: # pesquisa aproximada
                 Match.append(i)
        if len(Match) == 0:
            print ("Nome Não Encontrado")
        else:
            for i in Match:
                print (i)
        input ("Pressione Enter para Continuar")
print ("Fim do Programa")

#O código é um programa simples em Python que permite ao usuário pesquisar nomes em uma lista pré-definida.
#Ele utiliza um loop while para permitir que o usuário faça várias pesquisas até decidir sair digitando "FIM".
#Dentro do loop, o programa solicita ao usuário que insira um nome e verifica se ele está presente na lista.
#Se o nome for encontrado, ele é adicionado a uma lista chamada "Match", que armazena todos os nomes correspondentes.
#Se a lista "Match" estiver vazia após a pesquisa, o programa informa que o nome não foi encontrado.
#Caso contrário, ele imprime todos os nomes correspondentes encontrados na lista.
#Após cada pesquisa, o programa aguarda que o usuário pressione Enter para continuar, permitindo que ele faça novas pesquisas.
#O programa termina quando o usuário digita "FIM", momento em que uma mensagem de fim de programa é exibida.
#O código utiliza a biblioteca "os" para limpar a tela do console a cada iteração do loop, proporcionando uma interface mais limpa para o usuário.
#O código é um exemplo simples de como trabalhar com listas, loops e condicionais em Python, além de demonstrar a interação básica com o usuário por meio de entradas e saídas no console.



