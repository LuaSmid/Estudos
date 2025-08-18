agenda = {
    "Carlos": "9999-0002",
    "Beatriz": "9999-0003",
    "Eduardo": "9999-0004",
    "Sérgio": "9999-0005",
    "Voslano": "9999-2222"
}

# Exercício 11: Acesso seguro com get()
telefone = agenda.get("João", "Contato 'João' não encontrado na agenda.")

print(telefone)
