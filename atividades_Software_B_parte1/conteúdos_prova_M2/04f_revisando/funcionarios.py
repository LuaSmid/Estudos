import os

funcionarios = [
    [1, "Ana", "Analista de Sistema", 75000.0],
    [2, "Bruno", "Programador", 85000.0],
    [3, "Carlos", "DBA", 55000.0],
    [4, "Daniel", "Analista de Sistema", 65000.0],
    [5, "Eduarda", "Programador", 70000.0],
    [6, "Felipe", "DBA", 80000.0],
    [7, "Gabriela", "Analista de Sistema", 90000.0],
    [8, "Henrique", "Programador", 60000.0],
    [9, "Isabela", "DBA", 58000.0]
    ]

while True:
    print("="*40)
    print("      FUNCIONÁRIOS")
    print("="*40)
    opt = input('''
    [1] Relatório formatado
    [2] Média salarial
    [3] Maior salário
    [4] Menor salário
    [5] Sair
           
    Escolha uma opção:
''')  

    if opt == '1':
        os.system('cls')
        print(f"{'ID':<3} {'Nome':<10} {'Cargo':<20} {'Salário':>10}")
        print('-' * 45)
        for f in funcionarios:
            print(f"{f[0]:<3} {f[1]:<10} {f[2]:<20} R$ {f[3]:>8.2f}")     
            input("Pressione Enter para continuar")
            os.system('cls')
            break

    elif opt == '2':
        os.system('cls')
        media = (75000.0 + 85000.0 + 55000.0 + 65000.0 + 70000.0 +  80000.0 +  90000.0 + 60000.0 + 58000.0)/9
        print(f"A média de salários é: {media:.2f}")    
        break

    elif opt == '3':
        os.system('cls')
        maior = max(funcionarios, key=lambda f: f[3])
        print(f"Maior salário: {maior[1]} ({maior[2]}) - R$ {maior[3]:.2f}")

    elif opt == '4':
        os.system('cls')
        menor = min(funcionarios, key=lambda f: f[3])
        print(f"Menor salário: {menor[1]} ({menor[2]}) - R$ {menor[3]:.2f}")

    elif opt == '5':
        break

    else:
        print("Opção inválida. Tente novamente.")


