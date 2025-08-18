l1 = ["Ana", "Carlos", "Beatriz", "Eduardo",
"Sérgio"]

try:
    id = l1.index("Beatriz")
    print(f"O id do nome Beatriz é: {id}")
except ValueError:
    print("Nome não está presente")
