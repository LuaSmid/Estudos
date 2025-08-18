#Empresa
#Programador - Data xx/xx/xxxx
#Programa: Listas Simples
#==================================================
from tabulate import tabulate

# Entrada
Minha_Lista = ["Fulano da Silva", "Eulano de Souza", "Tulano Junior", "Sicrano da Silva", "Voslano Fulano Junior"]

# Processamento
dados = [[nome] for nome in Minha_Lista]
cabecalho = ["Lista de Nomes"]

# Saída
linha = "-" * 50
print(linha)
print(tabulate(dados, headers=cabecalho, tablefmt="grid"))
print(linha)
