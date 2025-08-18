#Exercício 14: Índice de elemento (index) - Mostre a posição do nome “Beatriz”. Se não estiver presente, mostre uma mensagem adequada.
#Minha_Lista = ["Ana", "Carlos", "Beatriz", "Eduardo", "Sérgio"]
#Luana 11251103287
#UMC - 25/04/2025
Minha_Lista = ["Ana", "Carlos", "Beatriz", "Eduardo", "Sérgio"]
print(f"Minha lista: {Minha_Lista}")
try:
    posicao = Minha_Lista.index("Beatriz")
    print(f"O nome Beatriz está na posição: {posicao}")
except ValueError:
    print("O nome Beatriz não está presente na lista.")
#O resultado é: O nome Beatriz está na posição: 2
#O nome "Beatriz" está na posição 2 da lista, pois a contagem começa em 0.
#Portanto, o índice 2 corresponde ao terceiro elemento da lista.
#O método index() retorna o índice do primeiro elemento encontrado na lista que corresponde ao valor especificado.


#OU:

#Minha_Lista = ["Ana", "Carlos", "Beatriz", "Eduardo", "Sérgio"] 
#if "Beatriz" in Minha_Lista: 
#print("Posição:", Minha_Lista.index("Beatriz")) 
#else: 
#print("Beatriz não está na lista.") 