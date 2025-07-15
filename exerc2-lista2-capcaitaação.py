# Conversor de moedas

# Solicita um valor em reais
realValor = float(input("Informe um valor R$: "))

# Define a taxa de conversão
taxaD = 1.15
taxaIene = 1.05

# Converte para dólar e iene
dolar = realValor / taxaD
iene = realValor / taxaIene

# Exibe os valores convertidos
print(f"Valor convertido em dólar: {dolar:.2f}")
print(f"Valor convertido em iene: {iene:.2f}")

