class Circulo:
    def area(self, raio):
       return raio * raio * 3,14
    
circulo = Circulo()
print(circulo.area(4))
circulo2 = Circulo()
print(circulo.area(2))

class Quadrado:
    def area(self):
        return self.lado*self.lado
q = Quadrado()
q.lado = 2
print(q.area)
    
