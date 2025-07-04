
age = int(input("Digite sua idade: "))

if age < 12:
    print("Criança")
elif age > 12 and age <= 17:
    print("Adolescente")
elif age >= 18 and age <= 59: 
     print("Adulto")
else:
    print("Idoso")

