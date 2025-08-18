agenda = {
    "Carlos": "9999-0002",
    "Beatriz": "9999-0003",
    "Eduardo": "9999-0004",
    "Sérgio": "9999-0005",
    "Voslano": "9999-2222"
}

#Exercício 17: Contar quantos nomes possuem mais de 6 letras

for nome, telefone in agenda.items():
    if len(nome) > 6:
        print(nome)
    