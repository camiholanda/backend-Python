user = str(input("Informe usuário: "))
passw = int(input("Informe senha: "))

if user == 'admin' and passw == 1234:
    print("Login válido")
else:
    print("Login inválido")
