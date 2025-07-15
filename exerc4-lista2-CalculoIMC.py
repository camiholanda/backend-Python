#Diagnóstico IMC

import math
peso = float(input("Peso:"))
alt = float(input("Altura:"))
alt_qd = pow(alt, 2)
imc = peso / alt_qd
print(f"IMC = {imc:.2f}")

