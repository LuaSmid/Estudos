'''
3. Contar Ocorrências de Letra 
Crie uma função `contar_letra(texto, letra)` que receba uma string e uma letra, 
e retorne quantas vezes essa letra aparece na string. 
'''

def contar_letra(texto, letra):
    contador = 0
    for caractere in texto:
        if caractere == letra:
            contador += 1
    return contador

texto = input("Informe um texto: ")
letra = input("Informe a letra: ")
print(f"A letra: {letra} aparece {contar_letra(texto, letra)} vezes no texto")
