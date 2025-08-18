import os
from rich.console import Console
from rich.table import Table

students = [
[101, "Ana Silva", "Sistemas de Informação", 1],
[102, "Bruno Souza", "Análise e Desenvolvimento de Sistemas", 2],
[103, "Carlos Pereira", "Engenharia de Software", 3],
[104, "Daniela Costa", "Sistemas de Informação", 4],
[105, "Eduardo Lima", "Análise e Desenvolvimento de Sistemas", 2],
[106, "Fernanda Alves", "Engenharia de Software", 1],
[107, "Gabriel Ferreira", "Sistemas de Informação", 3],
[108, "Helena Rodrigues", "Análise e Desenvolvimento de Sistemas", 4],
[109, "Igor Martins", "Engenharia de Software", 1],
[110, "Juliana Oliveira", "Sistemas de Informação", 1]
]

while True:
    print("="*40)
    print("      CONTROLE DE ESTUDANTES")
    print("="*40)
    opt = input('''
    [1]Relatório formatado
    [2]Pesquisar por curso
    [3]Pesquisar por semestre
    [4]Pesquisar por nome
    [5]Sair
                ''')
    
    if opt == '1':
        os.system('cls')

        # Criar a tabela
        tabela = Table(title="Estudantes")

        # Adicionar colunas
        tabela.add_column("RA", style="cyan", justify="center")
        tabela.add_column("Nome", style="magenta")
        tabela.add_column("Curso", style="yellow")
        tabela.add_column("Semestre", style="green")

        # Adicionar linhas com os dados dos produtos
        for student in students:
            tabela.add_row(
                str(student[0]),
                str(student[1]),
                str(student[2]),
                str(student[3])
            )

        # Mostrar no terminal
        console = Console()
        console.print(tabela)
        input("Pressione Enter para continuar")
        os.system('cls')
        

    elif opt == '2':
        os.system('cls')
        curso = input("Qual o curso do aluno: ").strip()
        encontrados = [
            aluno for aluno in students 
            if curso.lower() in aluno[2].lower()
            ]
        if encontrados:
                for aluno in encontrados:
                    print(f"RA: {aluno[0]}, Nome: {aluno[1]}, Curso: {aluno[2]}, Semestre: {aluno[3]}")
        else:
                print("Nenhum aluno encontrado para esse curso.")
        input("Pressione Enter para continuar")
        os.system('cls')

    elif opt == '3':
            os.system('cls')
            semestre = int(input("Qual o semestre do aluno: "))
            encontrados = [
                aluno for aluno in students 
            if aluno[3] == semestre
            ]
            if encontrados:
                for aluno in encontrados:
                    print(f"RA: {aluno[0]}, Nome: {aluno[1]}, Curso: {aluno[2]}, Semestre: {aluno[3]}")
            else:
                print("Nenhum aluno encontrado para esse semestre.")
            input("Pressione Enter para continuar")
            os.system('cls')
        
    elif opt == '4':
            os.system('cls')
            nome = input("Qual o nome do aluno: ").strip()
            encontrados = [
                aluno for aluno in students 
            if nome.lower() in aluno[1].lower()
            ]
            if encontrados:
                for aluno in encontrados:
                    print(f"RA: {aluno[0]}, Nome: {aluno[1]}, Curso: {aluno[2]}, Semestre: {aluno[3]}")
            else:
                print("Nenhum aluno encontrado.")
            input("Pressione Enter para continuar")
            os.system('cls')
        
    elif opt == '5':
         break
    
    else:
        os.system('cls') 
        print("Opção inválida. Tente novamente.")
        