import datetime

ano = int(input("Informeo ano de nascimento: "))
idade = ano - datetime.datetime.now().year

if idade < 18:
    print("Pessoa maior de idade")
else:
    print("Pesssoa menor de idade")
