
sal = float(input("Informe o salário: "))
dias_ferias = int(input("Informe os dias de férias: "))

numSorteio = random.randint(1, 10)

while True:
    numUser = int(input("Adivinhe o número sorteado: "))
    if numSorteio < numUser:
        print("Numero menor.")
    elif numSorteio > numUser:
        print("Numero maior.")
    else:
        print("Numero correto.")
        break

