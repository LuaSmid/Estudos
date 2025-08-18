# Empresa UMC
# Data 06/03/2025
# Programador Eduarda e Luana
# Calculo de salario do joão após contas
import os
import math

titulo='''
███████╗ █████╗ ██╗      █████╗ ██████╗ ██╗ ██████╗ 
██╔════╝██╔══██╗██║     ██╔══██╗██╔══██╗██║██╔═══██╗
███████╗███████║██║     ███████║██████╔╝██║██║   ██║
╚════██║██╔══██║██║     ██╔══██║██╔══██╗██║██║   ██║
███████║██║  ██║███████╗██║  ██║██║  ██║██║╚██████╔╝
╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝ ╚═════╝                                                  
'''
#Entrada
salario=float(input("Insira o salário: "))
conta1=float(input("Insira o valor da conta 1: "))
conta2=float(input("Insira o valor da conta 2:"))
#Processamento
contasTotal=((conta1*0.2)+conta1)+((conta2*0.2)+conta2)
#Saída
print(contasTotal)
print(("-")*50)