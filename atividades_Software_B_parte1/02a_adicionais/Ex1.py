# Empresa UMC
# Data 27/02/2025
# Programador Eduarda e Luana
# Calculo de tempo de donwload

while True:
    try:
        b=float(input("Insira o tamanho do arquivo: "))
        bs=float(input("Insira a velocidade de conexão: "))
    except ValueError:
        print("Valor inválido. Tente novamente.")
    else:    
        Tempo=b/bs
        print ("O tempo necessário para o dowload do arquivo é: ", Tempo," segundos")