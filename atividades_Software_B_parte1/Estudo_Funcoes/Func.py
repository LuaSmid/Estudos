# Definição Função
def MEDIA (L1): # o parametro é uma lista
    soma = 0
    for i in L1:
        soma = soma + i
    Var_Media=soma/len(L1)
    return (soma,len(L1),Var_Media)


print ("Será executado no código principal")
print ("Nome do módulo é",__name__)
if __name__ == "__main__":
    print ("Não será executado no código principal")