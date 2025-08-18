l1 = ["Ana", "Carlos", "Beatriz", "Eduardo",
"Sérgio"]

nome = input("Digite um nome: ")

if nome not in l1:
    l1.append(nome)
    print(l1)
else:
    print("Este nome já está na lista")