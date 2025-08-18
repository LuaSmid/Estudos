# Empresa UMC
# Data 06/03/2025
# Programador Eduarda e Luana
# Calculo de segundos em minutos

import os

titulo='''

████████╗███████╗███╗   ███╗██████╗  ██████╗ 
╚══██╔══╝██╔════╝████╗ ████║██╔══██╗██╔═══██╗
   ██║   █████╗  ██╔████╔██║██████╔╝██║   ██║
   ██║   ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║   ██║
   ██║   ███████╗██║ ╚═╝ ██║██║     ╚██████╔╝
   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝      ╚═════╝ 
                                             
'''

#Entrada
ts=int(input("Insira o tempo em segundos: "))

#Processamento
minutos = ts//60
segundos = ts % 60

#Saída
os.system("cls")
print(titulo)
print ("-"*50)
print (ts, "segundos são ", minutos," minutos e ", segundos, "segundos.")
print ("-"*50)
input ("Pressione enter para finalizar")