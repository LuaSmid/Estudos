#Exercício 12: Alteração de elemento - Se o nome da posição 0 for "Ana", substitua por "Anastácia".
#Minha_Lista = ["Ana", "Carlos", "Beatriz", "Eduardo", "Sérgio"]
#Luana 11251103287
#UMC - 25/04/2025

Minha_Lista = ["Ana", "Carlos", "Beatriz", "Eduardo", "Sérgio"]
print(f"Antes da alteração: {Minha_Lista}")
if Minha_Lista[0] == "Ana":
    Minha_Lista[0] = "Anastácia"
print(f"Depois da alteração: {Minha_Lista}")
#O resultado é: Antes da alteração: ['Ana', 'Carlos', 'Beatriz', 'Eduardo', 'Sérgio']
#Depois da alteração: ['Anastácia', 'Carlos', 'Beatriz', 'Eduardo', 'Sérgio']
