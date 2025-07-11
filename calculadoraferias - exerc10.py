
sal = float(input("Informe o salário: "))
dias_ferias = int(input("Informe os dias de férias: "))

ferias = sal * (dias_ferias / 30)
terco = ferias / 3
valorF = ferias + terco

print(f"A receber: R$ {valorF:.2f}")
   
