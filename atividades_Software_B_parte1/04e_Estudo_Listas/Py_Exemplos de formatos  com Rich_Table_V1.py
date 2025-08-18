#Empresa
#Programador - Data xx/xx/xxxx
#Programa: Listas Simples
#==================================================
from rich.console import Console
from rich.table import Table
# Entrada
Minha_Lista = ["Fulano da Silva", "Eulano de Souza",
               "Tulano Junior", "Sicrano da Silva", "Voslano Fulano Junior"]
# Criar o Console
console = Console()
# Criar a Tabela com separação entre linhas
table = Table(
    title="Lista de Nomes",
    title_style="bold cyan",
    border_style="bright_blue",
    show_lines=True  # <- Isso desenha uma linha horizontal entre cada item
)
# Adicionar Coluna com estilo em negrito azul e centralização
table.add_column("Nome", style="green", justify="center",header_style="bold blue")
# Adicionar os Nomes como linhas
for nome in Minha_Lista:
    table.add_row(nome)
# Imprimir a Tabela
console.print(table)
