# Revisão de Python - Estruturas de Dados 
# Listas, Tuplas e Dicionários

import os

pecas = []

# Carrega os dados do arquivo ao iniciar o programa
if os.path.exists("dados.txt"):
    with open("dados.txt", "r") as RD:
        for linha in RD:
            partes = linha.strip().split(",")
            if len(partes) == 3:
                codigo = int(partes[0])
                nome = partes[1]
                preco = float(partes[2])
                pecas.append([codigo, nome, preco])

while True:
    opt = input('''
        [1] Adicionar Peças
        [2] Somar valor total das peças
        [3] Pesquisa parcial de peças
        [4] Listar Peças
        [5] Excluir Peças
        [6] Sair do Programa
        Digite a opção desejada:
    ''')

    if opt == '1':
        NovoReg = input('Deseja adicionar uma nova peça? (S/N): ').upper()
        os.system('cls')
        if NovoReg == 'S':
            codigo = int(input('Digite o código da peça: '))
            os.system('cls')
            nome = input('Digite o nome da peça: ')
            os.system('cls')
            preco = float(input('Digite o preço da peça: '))
            os.system('cls')
            Posicao = int(input('Digite a posição onde deseja inserir a peça: '))
            if 0 <= Posicao <= len(pecas):
                pecas.insert(Posicao, [codigo, nome, preco])
                print('Peça adicionada com sucesso!')
            else:
                print('Posição inválida. Peça não adicionada.')
            with open("dados.txt", "w") as RD:
                for i in pecas:
                    RD.write(f"{i[0]},{i[1]},{i[2]}\n")
        else:
            print('Nenhuma peça foi adicionada.')
        input("Pressione Enter para continuar")
        os.system('cls')

    elif opt == '2':
        os.system('cls')
        total = 0
        for peca in pecas:
            total += peca[2]
        print(f'O valor total das peças é: R$ {total:.2f}')
        input("Pressione Enter para continuar")
        os.system('cls')

    elif opt == '3':
        os.system('cls')
        while True:
            encontrados = []
            Nome = input("Entre com o nome a ser pesquisado ou FIM: ")
            if Nome.upper() == "FIM":
                input("Pressione Enter para encerrar a pesquisa")
                break
            else:
                for i in pecas:
                    if Nome.lower() in i[1].lower():
                        encontrados.append(i)
                if not encontrados:
                    print("Nome Não Encontrado")
                else:
                    for i in encontrados:
                        print(i)
            input("Pressione Enter para continuar")
            os.system('cls')

    elif opt == '4':
        os.system('cls')
        print("Lista de Peças:")
        for i in pecas:
            print(i)
        input("Pressione Enter para continuar")
        os.system('cls')

    elif opt == '5':
        os.system('cls')
        print("Lista de Peças:")
        for i, peca in enumerate(pecas):
            print(f"{i}: {peca}")
        try:
            id = int(input("Entre com o índice da peça a ser EXCLUÍDA: "))
            if 0 <= id < len(pecas):
                print(f"Dados a serem EXCLUÍDOS: {id} {pecas[id]}")
                del pecas[id]
                with open("dados.txt", "w") as RD:
                    for i in pecas:
                        RD.write(f"{i[0]},{i[1]},{i[2]}\n")
                print("Peça excluída com sucesso!")
            else:
                print("Índice não consta na lista")
        except ValueError:
            print("Índice inválido.")
        input("Pressione Enter para continuar")
        os.system('cls')

    elif opt == '6':
        os.system('cls')
        print('Saindo do programa...')
        break

    else:
        print("Opção inválida. Tente novamente.")
        input("Pressione Enter para continuar")
        os.system('cls')









