class Produto:
    def __init__(self, nome = None, preco = 10.0, qtd = 0):
        nome = input("Nome do produto:")
        self.nome = nome
        preco = float(input("Preço:"))
        self.preco = preco
        qtd = int(input("Quantidade:"))
        self.qtd = qtd

    def estoque_total(self):
        valorTotal = self.preco * self.qtd
        print("Valor do estoque total:", valorTotal)
        
    def repor(self):
        qtd = int(input("Informe quantos produtos deseja adicionar:"))
        self.qtd = qtd + self.qtd
        print("Valor + reposicao:", self.qtd)
         
    def vender(self):
            qtd = int(input("Informe quantos produtos deseja vender:"))
            self.qtd = self.qtd - qtd
            if self.qtd != 0:
                print("Valor + venda:", self.qtd)
            else:
                print("Adicione mais produtos!")
            if qtd > 10:
                print("Disponível desconto de 10%")
    def visualizar(self):
        print(f"Produto:{self.nome} -- Preço:{self.preco} -- Quantidade:{self.qtd}")
    
        
p = Produto()
p.estoque_total()
p.repor()
p.vender()
p.visualizar()






