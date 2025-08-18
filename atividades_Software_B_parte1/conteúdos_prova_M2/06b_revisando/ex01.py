'''1. Par ou Ímpar 
Crie uma função chamada `par_ou_impar(numero)` que receba um número 
inteiro e retorne a string "par" se o número for par ou "ímpar" se for ímpar'''

def par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

num = int(input("Informe um número: "))
print(par_ou_impar(num))

