

num = [1, 2, 3, 4, 5, 6, 7,8 ,9, 10]
for items in range(0, 10):
      print(num[items])

nUser = int(input("Informe um número para criação de tabuada: "))

for items in range(0, 10):
    result =  nUser * num[items]
    print(" ", nUser, " x ", num[items], " = ", result)

  