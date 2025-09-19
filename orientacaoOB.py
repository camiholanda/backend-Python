class Ponto:
    def mover(self, x: float, y: float):
        self.x = x
        self.y = y

    def restaurar(self):
        self.mover(0, 0)
    
p = Ponto()
p.x = 2
p.y = 4

p.mover(1, 3)
print(p.x)
print(p.y) 

p.restaurar()
print(p.x)
print(p.y) 








