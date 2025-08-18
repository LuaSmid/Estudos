#Exercício 13: Acrescentar elemento (append) - Peça ao usuário um nome. Se ele ainda não estiver na lista, adicione-o.
#Minha_Lista = ["Ana", "Carlos", "Beatriz", "Eduardo", "Sérgio"]
#Luana 11251103287
#UMC - 25/04/2025

Minha_Lista = ["Ana", "Carlos", "Beatriz", "Eduardo", "Sérgio"]
print(f"Minha lista: {Minha_Lista}")
nome = input("Digite um nome: ")
if nome not in Minha_Lista:
    Minha_Lista.append(nome)
    print(f"Nome '{nome}' adicionado à lista.")
else:
    print(f"Nome '{nome}' já está na lista.")
#O resultado é:
#Minha lista: ['Ana', 'Carlos', 'Beatriz', 'Eduardo', 'Sérgio']
#Digite um nome: Ana
#Nome 'Ana' já está na lista.
#Ou:
#Digite um nome: Voslano
#Nome 'Voslano' adicionado à lista.
#A função append() é utilizada para adicionar um novo elemento ao final da lista.
