agenda = {
    "Carlos": "9999-0002",
    "Beatriz": "9999-0003",
    "Eduardo": "9999-0004",
    "Sérgio": "9999-0005",
    "Voslano": "9999-2222"
}
#Exercício 14: Obter lista de chaves e valores separadamente

for nome, telefone in agenda.items():
    print(nome)

for nome, telefone in agenda.items():
    print(telefone)