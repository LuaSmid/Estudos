#Exercício 11: Acesso por índice e startswith - Verifique se o nome na quarta posição da lista começa com a letra 'E'. Mostre 'Sim' ou 'Não'. 
#Minha_Lista = ["Ana", "Carlos", "Beatriz", "Eduardo", "Sérgio"]
#Luana 11251103287
#UMC - 25/04/2025

Minha_Lista = ["Ana", "Carlos", "Beatriz", "Eduardo", "Sérgio"]
print("Acesso pelo índice positivo")
print(f"O quarto nome da lista é: {Minha_Lista[3]}")
print("Verificando se o nome começa com a letra 'E'")
if Minha_Lista[3].startswith("E"):
    print("Sim")
else:
    print("Não")
#O quarto nome da lista é Eduardo, que começa com a letra 'E'.  
#Portanto, o resultado é 'Sim'.
#O método startswith() verifica se a string começa com o prefixo especificado.
#Ele retorna True se a string começar com o prefixo e False caso contrário.
