# String é uma lista
var ='Paralele!pip9do'
for i,dado in enumerate(var):
    if dado in ["!","#","1","2","3","4","5","6","7","8","9","0"]:
        print(f"Nome invalido, posição {i}, caracter {dado}")