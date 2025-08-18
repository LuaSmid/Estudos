'''9. Consulta Parcial de Produto 
Dada uma lista de listas com peças automotivas no formato [id, nome_produto, 
valor], crie uma função `buscar_produto(lista, termo)` que retorne todos os 
produtos cujo nome contenha o termo buscado (parcialmente). '''

pecas = [ 
[1, "Filtro de óleo", 35.90], 
[2, "Pastilha de freio", 120.00], 
[3, "Óleo de motor", 89.90], 
[4, "Filtro de ar", 45.00], 
[5, "Correia dentada", 150.00] 
]

def buscar_produto(pecas, termo):
    encontrados = []
    for peca in pecas:
        if termo.lower() in peca[1].lower():
            encontrados.append(peca)
    return encontrados

termo = input("Informe um termo para buscar um produto: ")
resultados = buscar_produto(pecas, termo)
if resultados:
    for peca in resultados:
        print(peca)
else:
    print("Peça não encontrada")
