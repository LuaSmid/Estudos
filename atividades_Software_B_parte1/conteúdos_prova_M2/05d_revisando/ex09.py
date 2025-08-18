agenda = {
    "Ana": "9999-0001",
    "Carlos": "9999-0002",
    "Beatriz": "9999-0003",
    "Eduardo": "9999-0004",
    "Sérgio": "9999-0005"
}
#Exercício 9: Inclusão condicional

while True:
    nomenew = input("Insira um novo nome (ou pressione Enter para sair): ")
    if nomenew == "":
        break
    if nomenew in agenda:
        print("Nome já existe no dicionário!")
    else:
        telefonenew = input("Insira um novo telefone: ")
        agenda[nomenew] = telefonenew
        print(agenda)
