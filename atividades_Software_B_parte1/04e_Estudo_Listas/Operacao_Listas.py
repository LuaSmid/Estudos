# Operações com Listas
# o operador lógico OR retorna o primeiro valor verdadeiro que ele encontra
import os
os.system("cls")
Minha_Lista=["Fulano da Silva","Eulano de Souza",
             "Tulano Junior","Sicrano da Silva", "Voslano Fulano Junior"]
#========================
#for i , dado in enumerate(Minha_Lista):
#    print (i,"\t",dado)
#=========================
#Nm=input("Entre com um nome a ser adicionado: ")
#Minha_Lista.append(Nm)
#print (Minha_Lista)
#=========================
id=int(input("Entre com o indice do Nome a ser alterado: "))
print (f"Dados a serem alterados: {id} {Minha_Lista[id]}")
##
Nm=input("Entre com a alteração do nome ou enter para manter: ") or Minha_Lista[id]
###
Minha_Lista[id]=Nm
print (Minha_Lista)

