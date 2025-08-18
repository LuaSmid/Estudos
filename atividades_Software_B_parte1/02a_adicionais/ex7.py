# Empresa UMC
# Data 06/03/2025
# Programador Eduarda e Luana
# Calculo de salário a receber
import os
titulo='''
███████╗ █████╗ ██╗      █████╗ ██████╗ ██╗ ██████╗ 
██╔════╝██╔══██╗██║     ██╔══██╗██╔══██╗██║██╔═══██╗
███████╗███████║██║     ███████║██████╔╝██║██║   ██║
╚════██║██╔══██║██║     ██╔══██║██╔══██╗██║██║   ██║
███████║██║  ██║███████╗██║  ██║██║  ██║██║╚██████╔╝
╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝ ╚═════╝ 
'''                                                 
#Entrada
horasTrab=int(input("Insira as horas trabalhadas: "))
salarioMin=float(input("Insira o salário mínimo: "))

#Processamento
valorHoraTrab=salarioMin/2
salarioBrut=horasTrab*valorHoraTrab
imposto=salarioBrut*0.03
salarioReceb= salarioBrut - imposto

#Saída
os.system("cls")
print(titulo)
print("-"*50)
print ("Horas trabalhadas: ", horasTrab)
print ("Salário Mínimo: ", salarioMin)
print ("Valor da hora trabalhada: ", valorHoraTrab)
print ("Salário Bruto: ", salarioBrut)
print ("Imposto: ", imposto)
print ("Salário a receber: ", salarioReceb)
print("-"*50)