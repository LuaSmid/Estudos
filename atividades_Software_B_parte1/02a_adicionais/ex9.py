# Empresa UMC
# Data 06/03/2025
# Programador Eduarda e Luana
# Calculo de quantidade minima de convites
import os
import math
titulo=''' 
████████╗███████╗ █████╗ ████████╗██████╗  ██████╗ 
╚══██╔══╝██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔═══██╗
   ██║   █████╗  ███████║   ██║   ██████╔╝██║   ██║
   ██║   ██╔══╝  ██╔══██║   ██║   ██╔══██╗██║   ██║
   ██║   ███████╗██║  ██║   ██║   ██║  ██║╚██████╔╝
   ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝                                                   
'''
#Entrada
c=float(input("Insira o custo de um espetaculo teatral: "))
p=float(input("Insira o custo do convite do espetaculo: "))
#Processamento
quantMinimaConvite=math.ceil(c/p)
#Saída
os.system("cls")
print(titulo)
print ("-"*50)
print("A quantidade mínima de convites é: ", math.ceil(c/p))
print ("-"*50)