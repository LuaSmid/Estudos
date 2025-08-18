'''8. Encontrar Repetidos 
Crie uma função `nomes_repetidos(lista_nomes)` que receba uma lista de 
nomes e retorne uma nova lista contendo apenas os nomes que aparecem 
mais de uma vez. '''

def nomes_repetidos(lista_nomes):
    repetidos = []
    for nome in set(lista_nomes):
        if lista_nomes.count(nome) > 1:
            repetidos.append(nome)
    return repetidos

lista_nomes = [
    'luana',
    'pedro',
    'julia',
    'luana',
    'pedro',
    'felipe',
    'felipe'
]

print(nomes_repetidos(lista_nomes))

