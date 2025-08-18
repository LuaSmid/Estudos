#Exercício 16: Criar um dicionário a partir de duas listas

nomes = ["Carlos","Beatriz", "Eduardo", "Sérgio", "Voslano"]
telefones = [ "9999-0002", "9999-0003", "9999-0004", "9999-0005", "9999-2222"]

agenda = dict(zip(nomes, telefones))
print(agenda)