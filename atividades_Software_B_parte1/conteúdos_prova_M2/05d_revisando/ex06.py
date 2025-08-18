agenda = {
 "Ana": "9999-0001",
 "Carlos": "9999-0002",
 "Beatriz": "9999-0003",
 "Eduardo": "9999-0004",
 "Sérgio": "9999-0005"
}

# Exercício 6: Percorrer com for e items()
print("Contatos da agenda:")
for nome, telefone in agenda.items():
    print(f"{nome}: {telefone}") 