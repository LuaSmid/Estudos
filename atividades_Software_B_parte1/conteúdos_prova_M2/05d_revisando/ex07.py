agenda = {
 "Ana": "9999-0001",
 "Carlos": "9999-0002",
 "Beatriz": "9999-0003",
 "Eduardo": "9999-0004",
 "Sérgio": "9999-0005"
}

#Exercício 7: Verificar se chave começa com letra específica
print('Contatos que começam com "E":')
for nome, telefone in agenda.items():
    if nome.startswith("E"):
        print(f"{nome}: {telefone}")
    