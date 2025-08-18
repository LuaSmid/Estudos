# Empresa UMC
# Data 06/03/2025
# Programador Eduarda e Luana
# Calculo de segundos em minutos
pesoRacao=int(input("Insira o peso do saco de ração em kg: "))
quantDia=float(input("Insira a quantidade de ração por dia em g: "))
racaoG=pesoRacao*1000
racao_total_dia= quantDia*2
racao_5_dias=racao_total_dia*5
restante = (racaoG-racao_5_dias)/1000
print ("A ração de", pesoRacao, "kg terá ", restante,"kg após 5 dias.")