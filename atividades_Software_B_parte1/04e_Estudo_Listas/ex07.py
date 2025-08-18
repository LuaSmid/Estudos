#Exercício 7: Ordenar (sorted) - Mostre os nomes em ordem decrescente.  
#Minha_Lista = ["Ana", "Carlos", "Beatriz", "Eduardo", "Sérgio"]
#Luana 11251103287
#UMC - 25/04/2025

Minha_Lista = ["Ana", "Carlos", "Beatriz", "Eduardo", "Sérgio"]
print(f"Minha lista: {Minha_Lista}")

print(f"Minha lista em ordem decrescente: {sorted(Minha_Lista, reverse=True)}")
#O resultado é: Minha lista: ['Ana', 'Carlos', 'Beatriz', 'Eduardo', 'Sérgio']
#Minha lista em ordem decrescente: ['Sérgio', 'Eduardo', 'Carlos', 'Beatriz', 'Ana']
#A lista Minha_Lista foi ordenada em ordem decrescente, do maior para o menor.
#A função sorted() é utilizada para ordenar os elementos de uma lista.
#O parâmetro reverse=True indica que a ordenação deve ser feita em ordem decrescente.
#A função sorted() retorna uma nova lista com os elementos ordenados, sem modificar a lista original.

