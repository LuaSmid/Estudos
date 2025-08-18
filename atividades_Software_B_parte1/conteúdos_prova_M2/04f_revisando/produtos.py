import os
from tabulate import tabulate

categorias = {
    1: "Dispositivos Móveis",
    2: "Computadores e Acessórios",
    3: "Entretenimento e Áudio"
}

# [ID_Produto, Descrição, Categoria (int), Desc_Categ, Qtde_Estoque, Preço/Unidade]
produtos = [
    [101, "Smartphone Galaxy", 1, categorias[1], 10, 1500.00],
    [102, "Notebook Dell", 2, categorias[2], 5, 3500.00],
    [103, "Fone Bluetooth", 3, categorias[3], 20, 200.00]
]

while True:
    print("="*40)
    print("      CONTROLE DE ESTOQUE DE PRODUTOS")
    print("="*40)
    opt = input('''
[1] Relatório formatado
[2] Incluir produto
[3] Valor total do estoque por categoria
[4] Sair
Escolha uma opção: ''')

    if opt == '1':
        os.system('cls')
        headers = ["ID", "Descrição", "Categoria", "Qtde", "Preço/Unidade"]
        tabela = [
            [p[0], p[1], p[3], p[4], f"R$ {p[5]:.2f}"] for p in produtos
        ]
        print(tabulate(tabela, headers=headers, tablefmt="grid"))
        input("Pressione Enter para continuar")
        os.system('cls')

    elif opt == '2':
        os.system('cls')
        try:
            novo_id = int(input("ID do produto: "))
        except ValueError:
            print("ID inválido!")
            input("Pressione Enter para continuar")
            os.system('cls')
            continue
        if any(prod[0] == novo_id for prod in produtos):
            print("ID já cadastrado!")
            input("Pressione Enter para continuar")
            os.system('cls')
            continue
        descricao = input("Descrição: ")
        print("Categorias:")
        for k, v in categorias.items():
            print(f"[{k}] {v}")
        try:
            cat = int(input("Escolha a categoria (1-3): "))
            if cat not in categorias:
                raise ValueError
        except ValueError:
            print("Categoria inválida!")
            input("Pressione Enter para continuar")
            os.system('cls')
            continue
        try:
            qtde = int(input("Quantidade em estoque: "))
            preco = float(input("Preço por unidade: "))
        except ValueError:
            print("Quantidade ou preço inválido!")
            input("Pressione Enter para continuar")
            os.system('cls')
            continue
        produtos.append([novo_id, descricao, cat, categorias[cat], qtde, preco])
        print("Produto incluído com sucesso!")
        input("Pressione Enter para continuar")
        os.system('cls')

    elif opt == '3':
        os.system('cls')
        totais = {k: 0.0 for k in categorias}
        for p in produtos:
            totais[p[2]] += p[4] * p[5]
        headers = ["Categoria", "Valor Total"]
        tabela = [
            [categorias[k], f"R$ {totais[k]:.2f}"] for k in categorias
        ]
        print(tabulate(tabela, headers=headers, tablefmt="grid"))
        input("Pressione Enter para continuar")
        os.system('cls')

    elif opt == '4':
        break
    else:
        os.system('cls')
        print("Opção inválida. Tente novamente.")