from datetime import datetime

def obter_data_nascimento():
  """
  Solicita ao usuário a data de nascimento e a retorna como um objeto datetime.
  """
  while True:
    data_str = input("Digite sua data de nascimento (DD/MM/AAAA): ")
    try:
      # Tenta converter a string para um objeto datetime usando o formato especificado
      data_nascimento = datetime.strptime(data_str, "%d/%m/%Y")
      return data_nascimento
    except ValueError:
      # Se a conversão falhar (formato inválido), informa o usuário e tenta novamente
      print("Formato de data inválido. Use DD/MM/AAAA.")

# Obtém a data de nascimento do usuário
data_nascimento = obter_data_nascimento()

# Imprime a data de nascimento formatada ou faz algo com ela
print(f"Data de nascimento: {data_nascimento.strftime('%d/%m/%Y')}")