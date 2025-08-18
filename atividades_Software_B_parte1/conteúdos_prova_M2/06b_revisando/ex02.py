'''2. Contador de Vogais 
Crie uma função `contar_vogais(texto)` que receba uma string e retorne a 
quantidade de vogais (a, e, i, o, u) presentes nela. '''

def contar_vogais(texto):
    vogais = 'aeiouAEIOU'
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador

texto = input("Informe um texto: ")
print(f"O texto contém {contar_vogais(texto)} vogais")