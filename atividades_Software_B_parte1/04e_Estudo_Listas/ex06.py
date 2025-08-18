#Exercício 6: Remoção (del) - Remova o segundo nome da lista.  
#Minha_Lista = ["Ana", "Carlos", "Beatriz", "Eduardo", "Sérgio"]
#Luana 11251103287
#UMC - 25/04/2025

Minha_Lista = ["Ana", "Carlos", "Beatriz", "Eduardo", "Sérgio"]
print(f"Antes da remoção: {Minha_Lista}")
del Minha_Lista[1]
print(f"Depois da remoção: {Minha_Lista}")
#O resultado é: Antes da remoção: ['Ana', 'Carlos', 'Beatriz', 'Eduardo', 'Sérgio']
#Depois da remoção: ['Ana', 'Beatriz', 'Eduardo', 'Sérgio']
#A remoção foi feita no índice 1, que corresponde ao segundo elemento da lista.
#A função del é utilizada para remover um elemento de uma lista em uma posição específica.
#A função del não retorna nenhum valor, apenas remove o elemento da lista.
