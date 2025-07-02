#coments

n1 = float(input("Primeiro número:"))
n2 = float(input("Segundo número:"))
n3 = float(input("Terceiro número:"))
media = (n1 + n2+ n3) // 3

if media >= 7:
    print("Muito bem! A media =", media)
elif media >=5 and media < 7:
    print("Você pode mehorar. A media =", media)
else:
    print("Estude mais. A media =", media)
    