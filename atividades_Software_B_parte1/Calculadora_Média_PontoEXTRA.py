# UMC
# Luana Felix 11251103287 e Eduarda Beatriz 11251104036
# 10/04
# Atividade extra

import os

cor = '\033[1;32m'  
fim_cor = '\033[0m'
vermelho = '\033[31m'
verde = '\033[32m'

# Título do aplicativo
titulo = '''
_  _ ____ ___  _ ____    _  _ ____ ___ ____ ____ 
|\/| |___ |  \ | |__|    |\ | |  |  |  |__| [__  
|  | |___ |__/ | |  |    | \| |__|  |  |  | ___] 
                                                                                                                                                                             
'''

def limpar_tela():
    os.system('cls')  
    print(f"{cor}{titulo}{fim_cor}")

limpar_tela()

while True:
    try:
        m1 = float(input("Entre com a primeira nota: "))
        limpar_tela()
                
        m2 = float(input("Entre com a segunda nota: "))
        limpar_tela()
    except ValueError:
        print("Valor inválido")
        opt = input("Pressione c para tentar novamente ou s para finalizar: ").lower()
        limpar_tela()
        if opt == "s":
            print("Você saiu do programa")
            break
    else:
        ms = (m1 + 2 * m2) / 3
        if ms < 3:
            print(f"{vermelho}Você foi reprovado! Média: {ms:.1f}{fim_cor}")
            
        elif ms >= 3 and ms < 5:
            print(f"{vermelho}Você está de recuperação! Média: {ms:.1f}{fim_cor}")
          
        else:
            print(f"{verde}Você foi aprovado! Média: {ms:.1f}{fim_cor}")
        
        opt = input("Pressione c para tentar novamente ou s para finalizar: ").lower()
        limpar_tela()
        if opt == "s":
            print("Você saiu do programa")
            break