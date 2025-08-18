'''4. Verificar Tipo Numérico 
Crie uma função `verificar_tipo(valor)` que receba um valor e retorne se ele é 
do tipo `int`, `float` ou outro
'''
def verificar_tipo(valor):
    if isinstance(valor, int):
        return "Seu número é um valor inteiro!"
    elif isinstance(valor, float):
        return "Seu número é um valor float!"
    elif isinstance(valor, str):
        return "Seu número é um valor string!"
    else:
        return "Seu número é um valor diferente de int, float e str!"

while True:
    entrada = input("Informe um valor: ")
    try:
        valor = int(entrada)
    except ValueError:
        try:
            valor = float(entrada)
        except ValueError:
            valor = entrada

    print(verificar_tipo(valor))

