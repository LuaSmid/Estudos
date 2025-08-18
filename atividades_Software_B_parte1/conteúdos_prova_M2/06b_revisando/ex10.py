'''10. Soma por Categoria 
Crie uma função `soma_por_categoria(lista, categoria)` que receba uma lista 
de listas com peças automotivas no formato [id, nome_produto, valor, 
categoria] e retorne a soma dos valores dos produtos dessa categoria. Caso a 
categoria não exista, a função deve informar isso.'''

pecas = [ 
[1, "Filtro de óleo", 35.90, "Motor"], 
[2, "Pastilha de freio", 120.00, "Freio"], 
[3, "Óleo de motor", 89.90, "Motor"], 
[4, "Filtro de ar", 45.00, "Motor"], 
[5, "Correia dentada", 150.00, "Motor"] 
] 

def soma_por_categoria(pecas, categoria):
    total = sum(peca[2] for peca in pecas if categoria.lower() == peca[3].lower())
    if total > 0:
        return f"Valor total das peças: R$ {total:.2f}"
    else:
        return "Categoria inexistente!"

categoria = input("Informe a categoria que deseja somar valores: ")
print(soma_por_categoria(pecas, categoria))


