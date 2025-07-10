from datetime import datetime

# Entrada do nome
nome = input("Digite seu nome: ")

# Tentativa de leitura e validação da data
while True:
    data_str = input("Digite sua data de nascimento (DD/MM/AAAA): ")
    try:
        data_nascimento = datetime.strptime(data_str, "%d/%m/%Y")
        break  # Data válida, sai do loop
    except ValueError:
        print("Data inválida. Por favor, use o formato DD/MM/AAAA.")

# Obter o nome do dia da semana em português
dias_semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]
dia_semana = dias_semana[data_nascimento.weekday()]  # weekday() retorna 0 (segunda) até 6 (domingo)

# Mensagem personalizada
print(f"Olá, {nome}! Você nasceu em uma {dia_semana}!")
