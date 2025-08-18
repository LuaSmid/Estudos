#Exercício 10: Enumerar elementos (enumerate) - Mostre todos os nomes da lista com sua respectiva posição. 
#Minha_Lista = ["Ana", "Carlos", "Beatriz", "Eduardo", "Sérgio"]
#Luana 11251103287
#UMC - 25/04/2025

Minha_Lista = ["Ana", "Carlos", "Beatriz", "Eduardo", "Sérgio"]
print(f"Minha lista: {Minha_Lista}")
for i, name in enumerate (Minha_Lista):
    print(f"Posição {i}: {name}")
#O resultado é:: Minha lista: ['Ana', 'Carlos', 'Beatriz', 'Eduardo', 'Sérgio']
#Posição 0: Ana
#Posição 1: Carlos
#Posição 2: Beatriz
#Posição 3: Eduardo
#Posição 4: Sérgio
#A função enumerate() é utilizada para obter tanto o índice quanto o valor de cada elemento da lista.
#Neste caso, a lista Minha_Lista contém 5 nomes, e o loop for percorre cada elemento, imprimindo sua posição e nome correspondente.
#O resultado mostra a posição (índice) de cada nome na lista, começando do índice 0.
#A função enumerate() é útil quando precisamos acessar tanto o índice quanto o valor dos elementos em uma lista.
#Ela retorna um objeto enumerado, que pode ser convertido em uma lista ou iterado diretamente em um loop for.
