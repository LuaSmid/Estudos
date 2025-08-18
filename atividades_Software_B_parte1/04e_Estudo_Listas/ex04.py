#Exercício 4: Índice de elemento (index) - Descubra em que posição está o nome "Sérgio". 
#Minha_Lista = ["Ana", "Carlos", "Beatriz", "Eduardo", "Sérgio"]
#Luana 11251103287
#UMC - 25/04/2025

Minha_Lista = ["Ana", "Carlos", "Beatriz", "Eduardo", "Sérgio"]
print(f"Minha lista: {Minha_Lista}")
print(Minha_Lista.index('Sérgio'))

#O nome "Sérgio" está na posição 4 da lista, pois a contagem começa em 0.
#Portanto, o índice 4 corresponde ao quinto elemento da lista.
#O resultado é: 4
#O método index() retorna o índice do primeiro elemento encontrado na lista que corresponde ao valor especificado.
#Se o valor não estiver presente na lista, o método index() gerará um erro ValueError.