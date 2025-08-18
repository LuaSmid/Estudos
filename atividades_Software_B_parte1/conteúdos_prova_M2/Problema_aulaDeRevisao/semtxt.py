# Revisão de Python - Estruturas de Dados 
# Listas, Tuplas e Dicionários

pecas = [
    [1, 'filtro', 30]
    [2, 'pastilha', 40]
    [3, 'correia', 50]
]

while True:
    opt = input('''
        [1] Adicionar Peças
        [2] Somar valor total das peças
        [3] Pesquisa parcial de peças
        [4] Listar Peças
        [5] Excluir Peças
        [6] Sair
        Escolha uma opção: ''')

    if opt == '1':
        codigo = int(input("Digite o código da peça: "))
        nome = input("Digite o nome da peça: ")
        preco = float(input("Digite o preço da peça: "))
        pos = int(input(f"Digite a posição para inserir (0 a {len(pecas)}): "))
        if 0 <= pos <= len(pecas):
            pecas.insert(pos, [codigo, nome, preco])
            print("Peça adicionada com sucesso!")
        else:
            print("Posição inválida!")

    elif opt == '2':
        total = sum(peca[2] for peca in pecas)
        print(f"Valor total das peças: R$ {total:.2f}")

    elif opt == '3':
        termo = input("Digite o termo para pesquisa: ").lower()
        resultados = [peca for peca in pecas if termo in peca[1].lower()]
        if resultados:
            for peca in resultados:
                print(f"Código: {peca[0]}, Nome: {peca[1]}, Preço: R$ {peca[2]:.2f}")
        else:
            print("Nenhuma peça encontrada.")

    elif opt == '4':
        if pecas:
            for peca in pecas:
                print(f"Código: {peca[0]}, Nome: {peca[1]}, Preço: R$ {peca[2]:.2f}")
        else:
            print("Nenhuma peça cadastrada.")

    elif opt == '5':
        codigo = int(input("Digite o código da peça a ser excluída: "))
        pecas = [peca for peca in pecas if peca[0] != codigo]
        print("Peça excluída com sucesso!")

    elif opt == '6':
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")