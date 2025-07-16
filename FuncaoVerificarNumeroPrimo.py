def verificar_NumPrimo(n):
    import math
    if n % 2 == 0 and math.isqrt(n):
        return "Número primo."
    else:
       return "Não é número primo."
n = int(input("Número: "))      
print(verificar_NumPrimo(n))


















