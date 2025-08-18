#Empresa
#Programador - Data xx/xx/xxxx
#Programa: Listas Simples
#==================================================
from tabulate import tabulate

Minha_Lista = ["Fulano da Silva", "Eulano de Souza", "Tulano Junior",
                "Sicrano da Silva", "Voslano Fulano Junior"]
dados = [[nome] for nome in Minha_Lista]
cabecalho = ["Lista de Nomes"]

formatos = ["grid", "fancy_grid", "pipe", "simple_grid", "double_grid", "rounded_grid"]

linha = "-" * 50
for fmt in formatos:
    print(linha)
    print(f"Formato: {fmt}")
    print(tabulate(dados, headers=cabecalho, tablefmt=fmt))
    print(linha)
