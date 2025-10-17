class Funcionario:
    def __init__(self, nome = None, salario = 1500, cargo = "assistente"):
        nome = input("Informe seu nome:")
        self.nome = nome
        self.salario = salario
        self.salario = float(input("Informe seu salario:"))
        while self.salario  < 1320:
            print("O salario n pode ser menor que 1320")
            self.salario = float(input("Informe seu salario:"))
        self.cargo = cargo
        
    def reajustar_sal(self):
        percentual = float(input("Digite o percentual p/ aumento: "))
        novosal = (self.salario/100) * percentual
        self.salario = self.salario + novosal

    def ver_detalhes(self):
        print(f"Nome:{self.nome} - Salario: {self.salario} - Cargo: {self.cargo}")
    
n1 = Funcionario()
n1.reajustar_sal()
n1.ver_detalhes()




