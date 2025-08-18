#Exercício 5: Inserir elemento (insert) - Insira "Sicrano 2" logo após "Beatriz".  
#Minha_Lista = ["Ana", "Carlos", "Beatriz", "Eduardo", "Sérgio"]
#Luana 11251103287
#UMC - 25/04/2025

Minha_Lista = ["Ana", "Carlos", "Beatriz", "Eduardo", "Sérgio"]
print(f"Antes da inserção: {Minha_Lista}")
id = Minha_Lista.index("Beatriz")
Minha_Lista.insert(id + 1, "Sicrano 2")
print(f"Depois da inserção: {Minha_Lista}")
#O resultado é: Antes da inserção: ['Ana', 'Carlos', 'Beatriz', 'Eduardo', 'Sérgio']
#Depois da inserção: ['Ana', 'Carlos', 'Beatriz', 'Sicrano 2', 'Eduardo', 'Sérgio']
#O nome "Sicrano 2" foi inserido na lista Minha_Lista logo após "Beatriz".
#A inserção foi feita no índice 3, que corresponde à quarta posição da lista.
#A lista agora contém 6 elementos, com "Sicrano 2" sendo o quarto elemento.
#A função insert() é utilizada para adicionar um novo elemento em uma posição específica da lista.

