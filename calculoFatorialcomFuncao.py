def numero(n):
    nFat = 1
    for i in range(n, 1, -1):
        nFat *= i
    return nFat

n = int(input("Informe um numero para calcular seu fatorial: "))
fatorial = numero(n)
print("Fatorial = ", fatorial)














