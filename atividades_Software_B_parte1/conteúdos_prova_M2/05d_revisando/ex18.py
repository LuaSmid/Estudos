agenda = {
    "Carlos": "9999-0002",
    "Beatriz": "9999-0003",
    "Eduardo": "9999-0004",
    "Sérgio": "9999-0005",
    "Voslano": "9999-2222"
}
#Exercício 18: Filtrar dicionário
terminacoes = ("0001", "0003", "0005")

filtrados = {
    nome: telefone
    for nome, telefone in agenda.items()
    if telefone.endswith(terminacoes)
}

print("Contatos filtrados:")
for nome, telefone in filtrados.items():
    print(f"{nome}: {telefone}")