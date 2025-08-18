Lista = [1,2,3,4,5,6,7,8,9,300.89]
Dict = {
    "Luana": 12345,
    "Pedro": 54321
}

LD = [
     {"Luana": 12345,},
     {"Pedro": 54321}
]

soma = round(sum(Lista), 2)
máx = max(Lista)
mín = min(Lista)
print(f"{máx}, {mín}, {soma}")

divisao = máx / mín
divisao_arredondada = round(divisao, 2)
print(f"Divisão do maior pelo menor (arredondada): {divisao_arredondada}")

Dict.update({"Jessie": 65432})
print(Dict)

for contato in LD:
    if "Luana" in contato:
        print(contato["Luana"])
        print(LD)

Dict.update({"Luana": 3975})
print(Dict)

máx = max(Lista)
mini = min(Lista)
soma = round(sum(Lista), 2)