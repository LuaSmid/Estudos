import os

while True:
    try:
        nome=input("Nome: ")
        os.system('cls')
        salario=float(input("Salário: "))
        os.system('cls')
    except ValueError:
        print("Valor inválido")
        opt=input("Pressione c para tentar novamente ou s para sair").lower()
        if opt == 'c':
            os.system('cls')
        else:
            break
    else:
        if salario < 2.500:
            reajuste=(salario*0.15)
            print("O reajuste do seu salário foi: ", reajuste)
        else:
            salario >= 2.500
            reajuste=(salario*0.10)
            print("O reajustedo seu salário foi: ", reajuste)
            opt=input("Pressione c para tentar novamente ou s para sair").lower()
            if opt == 'c':
                os.system('cls')
            else:
                break



            
