# Menu_questionary.py
# Exemplo simples com questionary
# pip install --user questionary
import questionary
import os
while True:
    os.system ("cls")
    escolha = questionary.select(
        "Escolha uma opção:",
        choices=[
            "1 - Escolha da opção 1",
            "2 - Escolha da opção 2",
            "3 - Escolha da opção 3",
            "4 - Fim do Programa"
        ]
    ).ask()
    os.system ("cls")
    if escolha.startswith("1"):
        print("Você escolheu a opção 1")
        input("Pressione Enter para voltar ao menu.")
    elif escolha.startswith("2"):
        print("Você escolheu a opção 2")
        input("Pressione Enter para voltar ao menu.")
    elif escolha.startswith("3"):
        print("Você escolheu a opção 3")
        input("Pressione Enter para voltar ao menu.")
    elif escolha.startswith("4"):
        input("Pressione Enter para sair do programa.")
        break
    else:
        print("Opção inválida.")
        input("Pressione Enter para continuar.")

print("Fim do Programa")
