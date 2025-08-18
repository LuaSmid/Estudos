#Exercício 15: Inserir elemento (insert) - Insira o nome “Mário” antes do último elemento da lista.
#Minha_Lista = ["Ana", "Carlos", "Beatriz", "Eduardo", "Sérgio"]
#Luana 11251103287
#UMC - 25/04/2025

Minha_Lista = ["Ana", "Carlos", "Beatriz", "Eduardo", "Sérgio"]
print(f"Antes da inserção: {Minha_Lista}")
Minha_Lista.insert(-1, "Mário")
print(f"Depois da inserção: {Minha_Lista}")
#O resultado é: Antes da inserção: ['Ana', 'Carlos', 'Beatriz', 'Eduardo', 'Sérgio']
#Depois da inserção: ['Ana', 'Carlos', 'Beatriz', 'Eduardo', 'Mário', 'Sérgio']
#O nome "Mário" foi inserido antes do último elemento da lista Minha_Lista.
#A inserção foi feita no índice -1, que corresponde à penúltima posição da lista.
