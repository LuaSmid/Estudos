# Carga de rquivo TXT para Dicionario
L1=[] # Lista vazia
D1={} # Dicionario Vazio
with open("dados.txt","r") as RD: # r , modo de leitura
    for i in RD:
        L1.append(i.rstrip().split(","))
for i in L1:
    D1[i[0]]=[i[1],float(i[2])]
#print (L1)
#print (D1)
# Exclusão de item no dicionário
mat=input("Entre com a matricula a ser excluida: ")
del D1[mat]
print (D1)
input (" enter para continuar")
# Recriando o TXT a partir do dicionário
with open ("dados.txt", 'w') as RD: # w, modo escrita - apaga os registros
    for chave,dados in D1.items(): # Rescreve todo repositorio de dados TXT a partir do Dicionário
        RD.write (f"{chave},{dados[0]},{dados[1]}\n")

