import statistics
lista = []
media = 0
for i in range(4):
    lista.append(int(input("Informe sua nota")))
    media = statistics.mean(lista)
print("Media = ", media)

if media >= 6:
    print("Aluno aprovado.")