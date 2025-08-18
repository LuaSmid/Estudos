#Exercício 16: Tamanho da lista (len) - Mostre se o tamanho da lista é par ou ímpar. 
#Minha_Lista = ["Ana", "Carlos", "Beatriz", "Eduardo", "Sérgio"]
#Luana 11251103287
#UMC - 25/04/2025

Minha_Lista = ["Ana", "Carlos", "Beatriz", "Eduardo", "Sérgio"]
print(f"Minha lista: {Minha_Lista}")
print(f"A quantidade de nomes na lista é: {len(Minha_Lista)}")
#Verifica se o tamanho da lista é par ou ímpar
if len(Minha_Lista) % 2 == 0:
    print("O tamanho da lista é par.")
else:
    print("O tamanho da lista é ímpar.")
#O resultado é: Minha lista: ['Ana', 'Carlos', 'Beatriz', 'Eduardo', 'Sérgio']  
#A quantidade de nomes na lista é: 5
#O tamanho da lista é ímpar.
#A função len() é utilizada para obter o tamanho da lista, ou seja, a quantidade de elementos que ela contém.
#Neste caso, a lista Minha_Lista contém 5 nomes, portanto o resultado é 5.
