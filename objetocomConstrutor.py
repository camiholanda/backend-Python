class Circulo:
    def __init__(self, raio = 10):
        self.raio = raio
    def area(self):
       return 3.14*self.raio*self.raio
    
class Quadrado:
    def __init__(self, lado = 4):
        self.lado = lado
    def area(self):
        return self.lado*self.lado

circulo = Circulo()
print("Área do círculo:", circulo.area())

q = Quadrado()
print("Área do quadrado:", q.area())