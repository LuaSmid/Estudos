import os
from rich.console import Console
from rich.table import Table

clientes = [
    [1,  12345678000101, "Tech Solutions Ltda", 11987654321],
    [2, 98765432000199, "Comercial Silva ME", 11991234567],
    [3, 11222333000100, "Alimentos Boa Mesa SA", 21987654321],
    [4, 55667788000155, "Construtora Ideal Ltda", 31999887766]
    ]

while True:
    print("="*40)
    print("      CONTROLE DE FUNCIONÁRIOS")
    print("="*40)
    opt = input('''
    [1] Relatório formatado
    [2] Incluir cliente
    [3] Alterar cliente
    [4] Sair
                ''')
    
    if opt == '1':
        os.system('cls')
        #Criação da tabela
        tabela = Table(title = "Clientes")

        #Criação de colunas
        tabela.add_column("ID", style="cyan", justify="center")
        tabela.add_column("CGC", style="magenta")
        tabela.add_column("Razão Social", style="yellow")
        tabela.add_column("Celular", style="green")

        # Adicionar linhas com os dados dos produtos
        for cliente in clientes:
            tabela.add_row(
                str(cliente[0]),
                str(cliente[1]),
                str(cliente[2]),
                str(cliente[3])
            )

        # Mostrar no terminal
        console = Console()
        console.print(tabela)
        input("Pressione Enter para continuar")
        os.system('cls')

    elif opt == '2':
        os.system('cls')
        novo_id = int(input("Insira um id para incluir um novo cliente: "))
        if any(cliente[0] == novo_id for cliente in clientes):
            print("Cliente já está na lista")
        else:
            novo_cgc = int(input("Insira o CGC do cliente: "))
            nova_razao = input("Insira a Razão Social do cliente: ")
            novo_celular = int(input("Insira o celular do cliente: "))
            clientes.append([novo_id, novo_cgc, nova_razao, novo_celular])
            print("Cliente incluído com sucesso!")
        input("Pressione Enter para continuar")
        os.system('cls')

    elif opt == '3':
        os.system('cls')
        alterar_id = int(input("Insira o id do cliente: "))
        for i, cliente in enumerate(clientes):
            if cliente[0] == alterar_id:
                novo_id = int(input("Insira o id do cliente: "))
                novo_cgc = int(input("Insira o CGC do cliente: "))
                nova_razao = input("Insira a Razão Social do cliente: ")
                novo_celular = int(input("Insira o celular do cliente: "))
                clientes[i] = [novo_id, novo_cgc, nova_razao, novo_celular]
                print("Cliente alterado")
                break
        else:
            print("Id não existe!")
        input("Pressione Enter para continuar")
        os.system('cls')
    
    elif opt == '4':
        break
    else:
        os.system('cls') 
        print("Opção inválida. Tente novamente.")




