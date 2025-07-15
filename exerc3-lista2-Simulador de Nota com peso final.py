#Simulador de Nota com peso final

import statistics

n1 = float(input("n1:"))
n2 = float(input("n2:"))
n3 = float(input("n3:"))
n1Final = n1 * 0.2
n2Final = n2 * 0.3
n3Final = n3 * 0.5
media = [n1Final, n2Final, n3Final]
mediaFinal = statistics.mean(media)
if media >= 6.0:
    print("Aprovado.")
else:
    print("Reprovado")

